import importlib.util
import io
import json
import os
import tempfile
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch
from urllib import error

spec = importlib.util.spec_from_file_location("report", Path(__file__).parents[1] / "scripts/discord_report.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def dispatch():
    return {"repository": {"full_name": r.REPOSITORY}, "inputs": {
        "update_id": "reporting-smoke-test", "accomplished": "TEST ONLY: reporting software prepared.",
        "why": "Reproducible project updates.", "verification": "Mocked software checks only; no hardware test.",
        "unresolved": "Human review and merge remain pending.", "evidence": "software", "link": r.BASE}}


def merge():
    return {"repository": {"full_name": r.REPOSITORY}, "action": "closed", "pull_request": {
        "number": 12, "merged": True, "title": "Docking **proposal** @everyone <@123>",
        "base": {"ref": "main", "repo": {"full_name": r.REPOSITORY}}}}


class PayloadTests(unittest.TestCase):
    def build(self, event=None):
        return r.build_report("workflow_dispatch", event or dispatch(), "refs/heads/main")

    def test_development_contains_required_evidence_and_no_mentions(self):
        report = self.build()
        self.assertEqual(report["key"], "development:reporting-smoke-test")
        self.assertEqual(report["channel"], "development")
        for label in ("Accomplished", "Why it matters", "Verification", "Unresolved", "software", "TEST ONLY"):
            self.assertIn(label, report["payload"]["content"])
        self.assertEqual(report["payload"]["allowed_mentions"]["parse"], [])
        self.assertEqual(report["payload"]["flags"], 4)

    def test_merge_escapes_markdown_and_mentions_and_uses_canonical_link(self):
        report = r.build_report("pull_request_target", merge(), "refs/heads/main")
        self.assertEqual(report["channel"], "github")
        self.assertIn(r"\*\*proposal\*\*", report["payload"]["content"])
        self.assertNotIn("@everyone", report["payload"]["content"])
        self.assertIn(r.BASE + "/pull/12", report["payload"]["content"])
        self.assertIn("does not validate hardware", report["payload"]["content"])

    def test_nonmerged_wrong_base_and_wrong_repository_cannot_report(self):
        for mutate in (lambda e: e["pull_request"].update(merged=False),
                       lambda e: e["pull_request"]["base"].update(ref="feature"),
                       lambda e: e.update(action="opened")):
            event = merge(); mutate(event)
            self.assertIsNone(r.build_report("pull_request_target", event, "refs/heads/main"))
        event = dispatch(); event["repository"]["full_name"] = "attacker/fork"
        with self.assertRaises(r.ReportError): self.build(event)
        with self.assertRaises(r.ReportError): r.build_report("workflow_dispatch", dispatch(), "refs/heads/topic")

    def test_release_is_published_only_and_prerelease_is_labeled(self):
        event = {"repository": {"full_name": r.REPOSITORY}, "action": "published", "release": {
            "id": 9, "draft": False, "prerelease": True, "name": "Alpha", "html_url": r.BASE + "/releases/tag/v0.1"}}
        report = r.build_report("release", event, "refs/tags/v0.1")
        self.assertEqual(report["key"], "release:9")
        self.assertIn("Prerelease", report["payload"]["content"])
        event["release"]["draft"] = True
        self.assertIsNone(r.build_report("release", event, "refs/tags/v0.1"))

    def test_invalid_fields_rejected(self):
        for field, value in [("update_id", "Wrong Case"), ("update_id", "../evil"), ("evidence", "validated"),
                             ("why", ""), ("why", "x" * 301), ("why", 123),
                             ("link", "https://evil.example/"), ("link", r.BASE + "/../other"),
                             ("link", r.BASE + "/%2e%2e/other"), ("link", r.BASE + "?token=anything"),
                             ("verification", "github_pat_not-a-real-token")]:
            with self.subTest(field=field, value=value):
                event = dispatch(); event["inputs"][field] = value
                with self.assertRaises(r.ReportError): self.build(event)

    def test_total_utf16_budget_and_json_encoding(self):
        event = dispatch()
        for key in ["accomplished", "why", "verification", "unresolved"]:
            event["inputs"][key] = "😀" * 300
        with self.assertRaises(r.ReportError): self.build(event)
        event = dispatch(); event["inputs"]["why"] = 'Quotes " and newline\n$(touch /tmp/not-executed)'
        report = self.build(event)
        self.assertEqual(json.loads(json.dumps(report)), report)

    def test_untrusted_body_not_forwarded(self):
        event = merge(); event["pull_request"]["body"] = "sensitive body should never be sent"
        self.assertNotIn("sensitive body", str(r.build_report("pull_request_target", event, "refs/heads/main")))


class DeliveryTests(unittest.TestCase):
    # Construct a clearly synthetic endpoint; no live credentials or live requests.
    webhook = "https://discord.com/api/" + "webhooks/123/TEST_ONLY_NOT_A_REAL_CREDENTIAL"

    def test_post_requires_acknowledgement_and_wait_true(self):
        send = Mock(return_value={"id": "567"})
        self.assertEqual(r.post(self.webhook, {"content": "TEST"}, send), "567")
        send.assert_called_once_with(self.webhook + "?wait=true", payload={"content": "TEST"})
        for response in ({}, {"id": ""}, [], None):
            with self.assertRaises(r.ReportError): r.post(self.webhook, {}, Mock(return_value=response))

    def test_webhook_destination_validation(self):
        for url in [None, "http://discord.com/api/webhooks/1/a", self.webhook + "?x=1",
                    self.webhook.replace("discord.com", "discord.com.evil.example"),
                    self.webhook.replace("discord.com", "user:password@discord.com")]:
            send = Mock()
            with self.assertRaises(r.ReportError): r.post(url, {}, send)
            send.assert_not_called()

    def test_http_uses_json_timeout_and_redacts_errors_without_retry(self):
        opener = MagicMock()
        response = opener.open.return_value.__enter__.return_value
        response.read.return_value = b'{"id":"567"}'
        self.assertEqual(r.http_json(self.webhook, payload={"content": 'a"b'}, opener=opener), {"id": "567"})
        req = opener.open.call_args[0][0]
        self.assertEqual(json.loads(req.data), {"content": 'a"b'})
        self.assertEqual(opener.open.call_args[1]["timeout"], 20)
        for failure in [error.HTTPError(self.webhook, 429, "secret body", {}, None),
                        error.HTTPError(self.webhook, 500, "secret body", {}, None),
                        error.URLError(self.webhook), TimeoutError(self.webhook)]:
            opener = Mock(); opener.open.side_effect = failure
            with self.assertRaises(r.ReportError) as caught:
                r.http_json(self.webhook, payload={}, opener=opener)
            self.assertNotIn(self.webhook, str(caught.exception))
            self.assertNotIn("secret body", str(caught.exception))
            opener.open.assert_called_once()

    def test_redirects_never_follow(self):
        self.assertIsNone(r.NoRedirect().redirect_request(None, None, 302, "", {}, "https://evil.example"))

    def test_duplicate_history_reserves_failed_cancelled_and_successful_runs(self):
        for conclusion in ["success", "failure", "cancelled", None]:
            fetch = Mock(return_value={"workflow_runs": [{"id": 10, "display_title": "discord:development:abc", "conclusion": conclusion}]})
            self.assertTrue(r.already_attempted("development:abc", "11", "TEST", fetch))
        fetch = Mock(return_value={"workflow_runs": [{"id": 12, "display_title": "discord:development:abc"}]})
        self.assertFalse(r.already_attempted("development:abc", "11", "TEST", fetch))

    def test_history_pagination_and_fail_closed(self):
        fetch = Mock(side_effect=[{"workflow_runs": [{"id": 20, "display_title": "other"}] * 20},
                                  {"workflow_runs": [{"id": 1, "display_title": "discord:merge:12"}]}])
        self.assertTrue(r.already_attempted("merge:12", "11", "TEST", fetch))
        self.assertEqual(fetch.call_count, 2)
        with self.assertRaises(r.ReportError): r.already_attempted("x", "1", "", fetch)
        with self.assertRaises(r.ReportError): r.already_attempted("x", "1", "TEST", Mock(return_value={}))
        with self.assertRaises(r.ReportError):
            r.already_attempted("x", "1", "TEST", Mock(return_value={"workflow_runs": [{"id": 20}] * 20}))

    def test_realistic_history_page_fits_response_limit(self):
        # Full run objects include nested repository metadata (~14 KB each).
        page = {"workflow_runs": [{"id": 20, "display_title": "other", "metadata": "x" * 14000}] * 20}
        encoded = json.dumps(page).encode()
        self.assertLess(len(encoded), 1_000_000)
        opener = MagicMock()
        opener.open.return_value.__enter__.return_value.read.return_value = encoded
        self.assertEqual(len(r.http_json("https://api.github.com/", opener=opener)["workflow_runs"]), 20)
        fetch = Mock(return_value={"workflow_runs": []})
        r.already_attempted("merge:12", "11", "TEST", fetch)
        self.assertIn("per_page=20", fetch.call_args[0][0])

    def test_rerun_and_duplicate_do_not_post_and_failure_does_not_log_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "event.json"; path.write_text(json.dumps(dispatch()))
            env = {"GITHUB_EVENT_PATH": str(path), "GITHUB_EVENT_NAME": "workflow_dispatch", "GITHUB_REF": "refs/heads/main",
                   "GITHUB_RUN_ID": "11", "GITHUB_RUN_ATTEMPT": "2", "GH_TOKEN": "TEST"}
            with patch.dict(os.environ, env, clear=True), patch.object(sys, "argv", ["report"]), \
                    patch.object(r, "post") as post, patch.object(r, "already_attempted", return_value=True), \
                    redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as stderr:
                self.assertEqual(r.main(), 0); post.assert_not_called()
                os.environ["GITHUB_RUN_ATTEMPT"] = "1"
                self.assertEqual(r.main(), 0); post.assert_not_called()
                with patch.object(r, "already_attempted", side_effect=r.ReportError(self.webhook)):
                    self.assertEqual(r.main(), 1)
                self.assertNotIn(self.webhook, stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
