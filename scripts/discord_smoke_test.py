#!/usr/bin/env python3
"""Supervised premerge transport check; normal updates must use Actions."""
import getpass
import sys

from discord_report import BASE, REPOSITORY, ReportError, build_report, post


def main():
    if not sys.stdin.isatty():
        print("Use an interactive terminal with hidden credential input.", file=sys.stderr)
        return 1
    event = {"repository": {"full_name": REPOSITORY}, "inputs": {
        "update_id": "reporting-premerge-transport-test",
        "accomplished": "TEST ONLY: checking the dedicated development webhook transport before PR merge.",
        "why": "Confirms Discord delivery without deploying the draft Actions workflow.",
        "verification": "Mocked reporting tests passed. This is a local transport test, not an Actions or hardware test.",
        "unresolved": "Human review, merge, and Actions dispatch/merge/release verification remain pending.",
        "evidence": "software", "link": BASE}}
    try:
        report = build_report("workflow_dispatch", event, "refs/heads/main")
        secret = getpass.getpass("Development webhook (hidden input; paste once): ")
        message_id = post(secret, report["payload"])
        secret = None
        print("Discord acknowledged test message " + message_id + ". Verify it in #development-updates.")
        return 0
    except (ReportError, OSError, ValueError):
        print("Test delivery uncertain or failed. Inspect Discord before retrying.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
