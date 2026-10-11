#!/usr/bin/env python3
"""Bounded, mention-free Discord reporting using the Python standard library."""
import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from urllib import error, parse, request

REPOSITORY = "VoidPhoenixApps/project-tesseract"
BASE = "https://github.com/" + REPOSITORY
WORKFLOW = "discord-reporting.yml"
LEVELS = {"concept", "simulation", "software", "physical-test", "project-admin"}


class ReportError(Exception):
    """Safe diagnostic: never include response bodies, input text or credentials."""


def text(value, limit=300):
    if not isinstance(value, str) or not value.strip():
        raise ReportError("A required text field is empty or invalid.")
    if len(value) > limit:
        raise ReportError("An input exceeds its documented length limit.")
    if re.search(r"(?i)(/api/(?:v\d+/)?webhooks/|gh[pousr]_|github_pat_)", value):
        raise ReportError("Possible credential detected in message input.")
    value = " ".join(value.split())
    value = "".join(c for c in value if not unicodedata.category(c).startswith("C"))
    value = re.sub(r"([\\`*_{}\[\]()<>#|~])", r"\\\1", value)
    return value.replace("@", "@\u200b")


def github_link(value):
    if not isinstance(value, str) or len(value) > 400:
        raise ReportError("Invalid GitHub link.")
    if not re.fullmatch(re.escape(BASE) + r"(?:/[A-Za-z0-9_.~/%+\-]+)*", value):
        raise ReportError("Links must point to this GitHub repository without query or fragment.")
    if any(part in {".", ".."} for part in parse.unquote(value).split("/")):
        raise ReportError("Invalid GitHub link path.")
    return value


def build_report(event_name, event, ref):
    if event.get("repository", {}).get("full_name") != REPOSITORY:
        raise ReportError("Unexpected repository.")
    if event_name == "workflow_dispatch":
        if ref != "refs/heads/main":
            raise ReportError("Development dispatches must use main.")
        inputs = event.get("inputs", {})
        update_id = inputs.get("update_id", "")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,63}", update_id):
            raise ReportError("update_id must be 3-64 lowercase letters, numbers or hyphens.")
        level = inputs.get("evidence", "")
        if level not in LEVELS:
            raise ReportError("Unknown evidence category.")
        content = "**Project Tesseract — development update**\n"
        content += "Evidence category: " + level + "\n"
        for key, label in [("accomplished", "Accomplished"), ("why", "Why it matters"),
                           ("verification", "Verification"), ("unresolved", "Unresolved")]:
            content += "**" + label + ":** " + text(inputs.get(key)) + "\n"
        content += "<" + github_link(inputs.get("link") or BASE) + ">"
        key, channel = "development:" + update_id, "development"
    elif event_name == "pull_request_target":
        pr = event.get("pull_request", {})
        if (event.get("action") != "closed" or pr.get("merged") is not True
                or pr.get("base", {}).get("ref") != "main"
                or pr.get("base", {}).get("repo", {}).get("full_name") != REPOSITORY):
            return None
        number = pr.get("number")
        if type(number) is not int or number <= 0:
            raise ReportError("Invalid pull request number.")
        key, channel = "merge:" + str(number), "github"
        content = ("**Pull request merged — #" + str(number) + "**\n" + text(pr.get("title"), 256)
                   + "\nMerged into main. Review and test evidence are recorded in the PR; "
                     "merge alone does not validate hardware.\n<" + BASE + "/pull/" + str(number) + ">")
    elif event_name == "release":
        release = event.get("release", {})
        if event.get("action") != "published" or release.get("draft") is not False:
            return None
        release_id = release.get("id")
        if type(release_id) is not int or release_id <= 0:
            raise ReportError("Invalid release ID.")
        key, channel = "release:" + str(release_id), "github"
        title = release.get("name") or release.get("tag_name")
        content = ("**" + ("Prerelease" if release.get("prerelease") else "Release")
                   + " published**\n" + text(title, 256)
                   + "\nSee release notes for scope, evidence and limitations. "
                     "Publication alone does not validate hardware.\n<"
                   + github_link(release.get("html_url")) + ">")
    else:
        raise ReportError("Unsupported event.")
    content += "\nReport ID: `" + key + "`"
    if len(content.encode("utf-16-le")) // 2 > 2000:
        raise ReportError("Message exceeds Discord's 2000-character limit.")
    return {"key": key, "channel": channel, "payload": {
        "content": content, "allowed_mentions": {"parse": [], "users": [], "roles": [], "replied_user": False},
        "flags": 4,  # SUPPRESS_EMBEDS: no unsolicited link previews.
    }}


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def http_json(url, *, token=None, payload=None, opener=None):
    headers = {"Accept": "application/json", "User-Agent": "Project-Tesseract-Reporter"}
    if token:
        headers.update({"Authorization": "Bearer " + token, "X-GitHub-Api-Version": "2022-11-28"})
    body = None
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = request.Request(url, data=body, headers=headers)
    opener = opener or request.build_opener(NoRedirect)
    try:
        with opener.open(req, timeout=20) as response:
            raw = response.read(1_000_001)
            if len(raw) > 1_000_000:
                raise ReportError("Response exceeded safety limit; inspect delivery before retrying.")
            return json.loads(raw) if raw else {}
    except error.HTTPError as exc:
        raise ReportError("Service returned HTTP " + str(exc.code) + "; inspect delivery before retrying.") from None
    except (error.URLError, TimeoutError, OSError, ValueError):
        raise ReportError("Request failed or returned invalid data; inspect delivery before retrying.") from None


def already_attempted(key, run_id, token, fetch=http_json):
    """Fail closed on history errors. Earlier runs reserve IDs even on failure."""
    if not token or not str(run_id).isdigit():
        raise ReportError("Actions history authentication or run ID is missing.")
    for page in range(1, 501):
        url = ("https://api.github.com/repos/" + REPOSITORY + "/actions/workflows/"
               + WORKFLOW + "/runs?per_page=20&page=" + str(page))
        data = fetch(url, token=token)
        runs = data.get("workflow_runs")
        if not isinstance(runs, list):
            raise ReportError("Cannot verify prior reporting runs.")
        for run in runs:
            if run.get("display_title") == "discord:" + key and int(run["id"]) < int(run_id):
                return True
        if len(runs) < 20:
            return False
    raise ReportError("History scan limit reached; refusing an unverified duplicate risk.")


def post(webhook, payload, send=http_json):
    if not isinstance(webhook, str) or not re.fullmatch(
            r"https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+", webhook):
        raise ReportError("Missing or invalid Discord webhook secret.")
    # wait=true gives a message acknowledgement. Never retry an uncertain POST.
    result = send(webhook + "?wait=true", payload=payload)
    if not isinstance(result, dict) or not str(result.get("id", "")).isdigit():
        raise ReportError("No message acknowledgement; inspect Discord before retrying.")
    return str(result["id"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", action="store_true", help="Validate without network or secrets")
    args = parser.parse_args()
    try:
        event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
        report = build_report(os.environ["GITHUB_EVENT_NAME"], event, os.environ.get("GITHUB_REF", ""))
        if report is None:
            print("Event does not require an announcement.")
            return 0
        if args.preview:
            print(json.dumps(report, ensure_ascii=True, indent=2))
            return 0
        if os.environ.get("GITHUB_RUN_ATTEMPT") != "1":
            print("Rerun suppressed: inspect original delivery; do not retry automatically.")
            return 0
        if already_attempted(report["key"], os.environ.get("GITHUB_RUN_ID", ""), os.environ.get("GH_TOKEN")):
            print("Duplicate report ID suppressed.")
            return 0
        name = "DISCORD_DEVELOPMENT_WEBHOOK" if report["channel"] == "development" else "DISCORD_GITHUB_WEBHOOK"
        message_id = post(os.environ.get(name), report["payload"])
        print("Discord acknowledged message " + message_id + ". Verify it in the intended channel.")
        return 0
    except (ReportError, KeyError, TypeError, ValueError, OSError):
        # Do not print arbitrary exception text: URLs, tokens and event content may appear there.
        print("Reporting failed safely. Check configuration and Discord delivery before a new dispatch.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
