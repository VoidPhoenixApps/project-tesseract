# Discord development reporting

## Purpose and activation

GitHub remains authoritative for requirements, decisions, issues, source and evidence. Discord is a conversation and reporting surface. Reporting does not validate printer hardware or decide licensing.

This integration uses Python 3.9+ standard-library code and GitHub Actions, with two Discord incoming webhooks and no bot. The credentials are repository Actions secrets; Codex dispatches through its existing GitHub authorization and never needs their values.

**Reporting is active on `main` following [PR #3](https://github.com/VoidPhoenixApps/project-tesseract/pull/3).** Both the merged-PR notification and the explicitly dispatched development update have been verified in Discord. Published-release delivery remains unverified until a genuine release occurs; do not fabricate a release to test it.

## Activation evidence — 2026-10-11

The two dedicated channel-scoped webhooks and repository Actions secrets are configured. No bot was installed. All 15 mocked software tests passed, and independent security review approved the implementation before activation.

| Path | GitHub Actions evidence | Actual Discord verification |
| --- | --- | --- |
| Merged PR | [Successful run 38124114139](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38124114139) for PR #3 | Tesseract GitHub message in [#github-updates](https://discord.com/channels/1558743337735954512/1558745506421669888), report ID `merge:3`; confirmed by owner and inspected through Computer Use |
| Development dispatch | [Successful run 38124276930](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38124276930) on `main` | Tesseract Development message in [#development-updates](https://discord.com/channels/1558743337735954512/1558750555097145384), explicitly labeled `TEST ONLY`, report ID `development:reporting-activation-test`; inspected through Computer Use |
| Published release | Awaiting a genuine release | Not yet verified |

Before dispatch, retained reporting history contained only the merge notice and no activation-test run. Exactly one activation test was dispatched; do not send it again. The two original maintainer setup notes were edited in place to correct outdated unconnected/pending-merge claims while retaining their historical context. Both channel topics now reflect activation. Role preview verified that Community Member can read both channels but cannot send messages.

The earlier premerge transport test was blocked because Computer Use prohibited Terminal access. Postmerge Actions delivery verification supersedes that activation blocker; no local credential access is needed for ordinary reports. This verifies reporting software and delivery only, not printer hardware.

Separate Discord setup remains incomplete: Community activation awaits the owner's Community Guidelines agreement authorization, onboarding depends on that activation, role hierarchy reordering was not applied by the UI drag control, and moderator 2FA enforcement requires owner account 2FA. These do not block the verified reporting paths.

## Channels and secrets

| Destination | Discord webhook name | Repository Actions secret |
| --- | --- | --- |
| `#development-updates` | Tesseract Development | `DISCORD_DEVELOPMENT_WEBHOOK` |
| `#github-updates` | Tesseract GitHub | `DISCORD_GITHUB_WEBHOOK` |

Both channels inherit START HERE permissions: ordinary members can read but cannot send messages, create threads, post in threads, or use external apps to post. Maintainers can publish. Webhooks are individually scoped to their target channels. Do not give members or bots Administrator or Manage Webhooks. Keep webhook URLs out of files, screenshots, clipboard histories, logs, chat, command arguments and PR descriptions.

## Event and trust boundaries

- `workflow_dispatch` on `main`: an authorized Codex session submits a meaningful development milestone, approved decision, measured experiment, confirmed failure/blocker or significant task completion.
- `pull_request_target` with `closed`, targeting `main`, and `merged == true`: a short merge notice. Nonmerged closures are ignored; no push/commit notifications are sent.
- `release` with `published`: a release notice, including explicitly labeled prereleases. Draft/edit events do not publish.
- `reporting-tests.yml`: runs mocked tests on ordinary PRs and pushes to `main`, without webhook secrets.

The sender job uses only `contents: read` and `actions: read`. Checkout is pinned by full action SHA, reads `main` explicitly, and does not persist credentials. It never executes the PR head, merge ref, release tag, event payload or dispatched text as code. Event strings are read as JSON from `GITHUB_EVENT_PATH`, not interpolated into shell commands. No PR artifacts, caches, dependencies or build scripts are consumed in the secret-bearing job. Review workflow and sender changes carefully before merging. A merged malicious workflow could access repository secrets: repository writers and release publishers remain trusted, and only reviewed release refs should be published. Repository secrets are not protection against a malicious repository administrator.

Input text is required and bounded, Discord Markdown escaped, mentions disabled using `allowed_mentions`, and embeds suppressed. Text fields allow at most 300 characters (PR/release titles 256); the final message must fit 2,000 UTF-16 units. Evidence is one of `concept`, `simulation`, `software`, `physical-test`, or `project-admin`. Links are restricted to this repository on GitHub. PR/release bodies are never forwarded. Common credential patterns are rejected, but this is not a comprehensive data-loss-prevention system: author only public project information.

Webhook destinations must exactly match HTTPS `discord.com/api/webhooks/...`; redirects are rejected. Requests time out after 20 seconds, require a Discord acknowledgement via `wait=true`, never retry automatically, and never log remote bodies or secret-bearing exceptions.

## Duplicate suppression and delivery limits

Use a stable, lowercase milestone ID (3–64 letters, numbers and hyphens), such as `phase1-docking-trade-study`. Reuse that ID for the same milestone rather than inventing a new ID each session. Automatic keys are `merge:<PR number>` and `release:<release ID>`.

The run name records the non-secret report ID. Per-event concurrency serializes the same event/key; the sender checks all retained runs of this workflow and suppresses a key if any earlier run reserved it, even if that earlier run failed or was cancelled. Reruns (`GITHUB_RUN_ATTEMPT > 1`) are suppressed. A history API error or scan beyond 10,000 runs fails closed. Distinct milestone IDs do not share a global queue.

This is an **at-most-once attempt policy within retained Actions history**, not guaranteed exactly-once delivery. Deleted/expired workflow runs remove the duplicate record. Do not delete runs to force a retry. Review prior Discord messages and GitHub evidence when reporting old milestones beyond retention. GitHub may replace a pending concurrency run; a prior failed/cancelled attempt can therefore suppress delivery. Inspect before recovery.

A timeout, cancellation, 429 or server error may leave delivery uncertain; do not blindly rerun. Check Discord for the report ID first. If no message exists and the problem is fixed, deliberately dispatch a new ID ending in `-recovery-1`, explaining the recovery and linking the original evidence. Automatic merge/release failures can be summarized in a development recovery update; do not recreate a release or remerge a PR. If durable all-time deduplication or guaranteed delivery becomes necessary, review a transactional outbox design separately instead of overstating this lightweight approach.

## Setup and credential rotation

1. Inspect current integrations first. Reuse existing reporting channels; create only missing dedicated incoming webhooks. Preserve existing unrelated integrations, ownership and channel permissions.
2. Give each webhook the destination/name in the table. Store its URL directly in the corresponding GitHub **Settings → Secrets and variables → Actions → Repository secrets** field. Do not put it in variables or a command-line argument. Clear clipboard contents after the transfer.
3. Run mocked local tests, review the full diff and security boundaries, then obtain human approval to merge. Keep the PR Draft until ready.
4. After merge, dispatch one clearly labeled `TEST ONLY` development update and inspect its Actions run and the actual Discord message. Confirm the intended channel, no mentions and accurate evidence category. If a premerge smoke test already ran, label the postmerge test as Actions activation verification, not a new engineering milestone.
5. Verify the next genuine merged PR and published release. Do not claim those triggers verified merely because a manual message arrived.

For rotation, pause the reporting workflow, create a replacement channel-scoped webhook, replace the matching repository secret, perform one labeled test, and revoke the old webhook after confirming delivery. If exposed, revoke the old webhook immediately and investigate logs/history before restoring delivery. Do not copy a compromised value to a new secret. Resume the workflow after verification. Deleting a webhook revokes it; keep the channels and messages.

## Future Codex sessions

Read [AGENTS.md](../AGENTS.md) and the current GitHub state. At a meaningful milestone, prepare a public update containing accomplishment, significance, actual verification, unresolved work and a relevant GitHub link. Explicitly separate proposal, simulation, verified software and physically measured hardware. Check recent reporting runs/messages for an existing update; avoid duplicating the automatic merge notice.

After activation and authorization, ordinary public project reports do not require repeated user permission. Do not post confidential information or claim review/validation that has not occurred. A configured secret alone does not mean the workflow is active.

Use a local JSON file containing **only public report text** with these keys. The activation example below is historical and has already been delivered: do not dispatch it again. For future meaningful work, use its actual stable milestone ID and current evidence, then dispatch:

```json
{
  "update_id": "reporting-activation-test",
  "accomplished": "TEST ONLY: development reporting integration activated.",
  "why": "Checks the automated project update path.",
  "verification": "Reporting software tests passed; inspect this test delivery. No hardware validation.",
  "unresolved": "Published-release delivery awaits a genuine release; this existing activation ID must not be dispatched again.",
  "evidence": "software",
  "link": "https://github.com/VoidPhoenixApps/project-tesseract"
}
```

```sh
gh workflow run discord-reporting.yml --repo VoidPhoenixApps/project-tesseract --ref main --json < /path/to/public-update.json
gh run list --repo VoidPhoenixApps/project-tesseract --workflow discord-reporting.yml --limit 10
gh run view RUN_ID --repo VoidPhoenixApps/project-tesseract
```

Do not treat dispatch acceptance as delivery. Inspect the specific run and confirm the message in Discord; record the run/message link with the task evidence. If GitHub authentication, secrets or workflow activation are missing, report the exact blocker and preserve the prepared public update. Do not ask the user to paste secrets into chat.

## Local tests and troubleshooting

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Tests use mocked HTTP and synthetic endpoints; they never contact Discord. To inspect a message offline, supply a public GitHub-shaped event JSON file using `GITHUB_EVENT_PATH`, `GITHUB_EVENT_NAME=workflow_dispatch`, and `GITHUB_REF=refs/heads/main`, then run `python3 scripts/discord_report.py --preview`. No secrets are needed.

For a separately authorized premerge transport test, an operator can run `python3 scripts/discord_smoke_test.py` in an interactive terminal and paste the development webhook into its hidden prompt. It sends one fixed `TEST ONLY` message and prints only the acknowledgement ID. Clear the clipboard afterward. Do not retry until the target channel has been inspected. Computer Use may prohibit Terminal access; if so, leave this test pending for the owner or postmerge Actions verification.

| Symptom | Action |
| --- | --- |
| Workflow missing / dispatch 404 | Confirm the reviewed workflow has merged to default `main`, and GitHub authentication has repository access. |
| Job skipped | Check repository, event, merged status, dispatch ref and run attempt. |
| Duplicate suppressed | Inspect earlier runs and Discord for the same report ID. Do not automatically create a new ID. |
| Reporting failed safely | Check secret names, webhook destination, input lengths/evidence/link and Actions history access. Inspect Discord before recovery. |
| Discord 401/404 | Webhook may be revoked or invalid; rotate through the secure setup process. |
| Timeout / 429 / 5xx | Delivery may be ambiguous; inspect Discord before a deliberate recovery dispatch. |
| Message acknowledged but not seen | Check webhook channel mapping and member visibility; do not blindly retry. |

## References

- [GitHub workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [GitHub Actions workflow-run API](https://docs.github.com/en/rest/actions/workflow-runs)
- [Discord webhook execution](https://docs.discord.com/developers/resources/webhook#execute-webhook)

Project-knowledge has no Tesseract project record in the inspected checkout. After review/merge, a separately authorized knowledge update should record reporting ownership, the implementation-document link, activation/test evidence and remaining community-setup blockers. Do not duplicate credential values or this operational guide there.
