# Community preparation

**Owner-review package, 2026-10-12.** These are proposed community actions, not published issues, approved engineering decisions or completed Discord setup.

- [Eight issue drafts](issue-drafts.md), including beginner and specialist review boundaries.
- [Discussion, Discord and outreach drafts](message-drafts.md), each in a copyable block.
- [Contributor guide](../../CONTRIBUTING.md) for evidence and review standards.

## Verified starting point

Read-only GitHub inspection on 2026-10-12 found Discussions enabled, no existing Discussions, no open PRs, no issues, no topics, and existing `good first issue`, `help wanted` and `documentation` labels. Repository baseline: `7b734b0` (Phase 1 trade study, PR #7). Recheck live state before publishing or assigning work; engineering work can progress independently.

Shared workflow/engineering/knowledge/secrets/review standards were consulted at project-knowledge revision `46ff107e35053b970915a3ca147f5513571f7be6`, matching GitHub main. No Tesseract CURRENT_STATE record was present. Current Home Infrastructure instructions were consulted read-only. Neither source repository was changed; AgentMemory was unavailable.

The GitHub About description currently says “Open-source, reconfigurable multi-bed RepRap 3D printer,” which overstates the license status. Owner action: replace it with the following proposed description after review:

```text
Early feasibility research for a reconfigurable four-bed RepRap 3D printer. Printable-first; open-source intent, licensing undecided.
```

## GitHub owner actions

1. Review the About description above and proposed topics: `reprap`, `3d-printing`, `3d-printer`, `additive-manufacturing`, `mechanical-engineering`, `parametric-design`, `research`, `community`. Avoid an `open-source` topic until licensing is resolved.
2. Reuse existing `documentation`, `good first issue` and `help wanted` labels. Apply `good first issue` only to a bounded task with clear inputs, acceptance criteria and an available reviewer. Use `help wanted` for specialist tasks too; it does not imply beginner suitability. Optional new label: `engineering-review` for work requiring specialist assessment.
3. Triage the issue drafts against current engineering branches and PRs with their maintainers. Publish only one or two ready tasks initially; supply a reviewer and identify any overlapping investigation before inviting work. No issue has been created by this package.
4. Review and publish the two GitHub Discussion drafts, then pin them. Use an Announcements-style category for the welcome and an Ideas-style category for the first challenge, creating or choosing suitable categories as needed. No category or pin setting has been changed.
5. Review community moderation expectations and ownership before broad outreach. The contributor guide asks for respectful, evidence-based critique; it does not establish a staffed moderation program.

## Discord access

No public invitation was found in the inspected repository, About/homepage information or GitHub Discussions. No candidate invite was available to validate. Existing Discord channel URLs in [reporting documentation](../discord-reporting.md) are authenticated channel destinations, not public join links. README and CONTRIBUTING therefore point here instead of inventing an invitation.

Owner action: provide or create an intended public invitation, verify that it resolves to the correct Project Tesseract server, and test newcomer access and permissions with an ordinary account. Record the verification date and intended expiry policy, then add that verified invitation to README and CONTRIBUTING. Never substitute a webhook URL.

The reporting guide records Community activation/onboarding, role ordering and moderator 2FA setup as incomplete on 2026-10-11. These are historical records, not a fresh Discord UI audit; the owner should verify their current status. The GitHub-to-Discord reporting integration is documented as active. This package changes no workflows, permissions, webhooks, secrets or automation, and does not exercise message delivery.

Review the [Discord welcome and first challenge drafts](message-drafts.md) before publishing. No welcome, engineering prompt, milestone or outreach message is automatically posted by this task, following its explicit publication restriction.

## Scope and handoff

Engineering requirements, architecture, roadmap gates and Phase 1 studies are outside this change. Issue drafts extend source research and review; they neither commission a duplicate trade study nor select a mechanism, CAD tool, reinforcement stock or license. README and CONTRIBUTING could overlap later editorial changes; coordinate those two files before merge.

After approval/publication, any durable cross-project community ownership or access record should be linked from an appropriate, separately authorized project-knowledge record. No project record has been invented or updated here. Actual onboarding artifacts and evidence belong in this repository.
