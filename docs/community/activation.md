# Community activation record — 2026-10-12

**Community and onboarding are active.** GitHub community content, pinned Discussions and the public Discord invitation are live. Moderator 2FA remains an owner-deferred follow-up; a real newcomer-account join has not been tested. This record concerns administration and documentation, not validated printer hardware.

Source baseline: current `main` at `6f65f13`, including onboarding PR #8, Phase 1B PR #9 and Fusion-first evaluation preference PR #10. Shared standards were consulted at project-knowledge `46ff107`, matching its current main; no Tesseract project record was invented. AgentMemory was unavailable. Home Infrastructure and project-knowledge were not modified. File changes use an isolated `codex/community-activation` worktree; the primary engineering checkout was preserved.

## Live administrative changes completed

| Surface | Actual result and evidence |
| --- | --- |
| GitHub About | Saved and reread: “Early feasibility research for a reconfigurable four-bed RepRap 3D printer. Printable-first; open-source intent, licensing undecided.” |
| Repository topics | Saved and reread: `reprap`, `3d-printing`, `3d-printer`, `additive-manufacturing`, `mechanical-engineering`, `parametric-design`, `research`, `community` |
| Beginner issues | [#13: navigation/glossary](https://github.com/VoidPhoenixApps/project-tesseract/issues/13) and [#14: conceptual layouts](https://github.com/VoidPhoenixApps/project-tesseract/issues/14), both labeled `documentation` and `good first issue`; the owner explicitly confirmed availability to review both. No contributor was assigned. Bodies and labels were reread after publication. |
| GitHub Discussions | [Welcome #11](https://github.com/VoidPhoenixApps/project-tesseract/discussions/11) in Announcements and [heated-bed challenge #12](https://github.com/VoidPhoenixApps/project-tesseract/discussions/12) in Ideas. Published from the prepared drafts with current Phase 1B context. Both were subsequently pinned through the signed-in GitHub UI; the Discussions landing page displayed both under Pinned Discussions. |
| Discord welcome | [Existing pinned message](https://discord.com/channels/1558743337735954512/1558745176116297829/1558746783910334466) edited in place, preserving its identity and adding direct requirements, contribution and Discussion links. The rendered message and edit acknowledgement were inspected. No duplicate welcome was posted. |
| Discord engineering prompt | [New message in #bed-docking](https://discord.com/channels/1558743337735954512/1558745615176040448/1559360581281120297), published once and pinned; the rendered message and pin notification were inspected. It links current Phase 1B, Discussion #12, requirements and CONTRIBUTING, and explicitly prohibits treating it as physical-test authorization. |
| Public invitation | [Join Project Tesseract](https://discord.gg/45NYXMxKHg), landing in `#welcome`: never expires, unlimited uses, no automatic role assignment, temporary membership off. Owner explicitly approved permanent public joining after automatic approval review required confirmation. The UI confirmed no expiration. |
| Development report | One `project-admin` milestone, `development:community-onboarding-launch`, dispatched after checking retained history for duplicates. [Actions run 38327236738](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38327236738) succeeded and the [actual Discord message](https://discord.com/channels/1558743337735954512/1558750555097145384/1559361648895201373) was inspected. It explicitly lists the remaining owner actions and links Draft PR #15. Do not dispatch this milestone again. |

The invitation was independently opened in a signed-out browser and displayed **Project Tesseract** with the account-creation/sign-in entry point. No account was created and no real newcomer joined. The invite is a public join link, not a webhook or privileged credential. Review it periodically and revoke/replace it through Server Settings → Invites if abused. Opening the invite dialog also produced a default 30-day link; that link was not distributed or placed in documentation. Review redundant invites in the owner's invite audit rather than assuming they were removed.

No channels, roles or bots were added. Community mode, onboarding and the explicitly owner-approved role order were changed. Role permission flags, role assignments, channel overrides, webhooks, secrets, workflows and owner-account authentication were preserved. No license or engineering architecture was selected. No Reddit, forum or external promotional posts were published.

## Access and safety observations

| Check | Observed result | Limit |
| --- | --- | --- |
| Community mode | Owner personally accepted the agreement and finished setup. UI confirmed Community Server, with `#rules`, private `#community-updates` for Community and safety notifications, and English. | Personal acceptance was performed by the owner, not the agent. |
| Activation prerequisites | Verified-email and scan-all-members media requirements already satisfied. | No protection was weakened. |
| Server onboarding | Saved and enabled: seven default channels, one optional multi-answer interest question, and a Server Guide with welcome and three tasks. Live guide and Channels & Roles were inspected. | Role/channel previews are not a real newcomer join. See configuration below. |
| Verification/filtering | Medium verification; filter media from all members; restrict member prune to admins enabled. Safety notifications target `#community-updates`. | UI settings only; no adversarial spam or media test. Discord warns assigned roles can bypass verification when onboarding is disabled. |
| AutoMod | Block Mention Spam, Block Suspected Spam Content and Block Commonly Flagged Words all enabled, each showing block-message action. | Rule thresholds/exemptions and real enforcement were not exhaustively tested. |
| Moderator 2FA | Require 2FA for moderator actions off; UI says the owner needs account 2FA to change it. | The owner explicitly chose to leave account setup and server enforcement as a follow-up. |
| Role hierarchy | Saved top-to-bottom order: Maintainer, Moderator, Contributor, Community Member, then @everyone. All four named roles showed zero members. | Owner explicitly approved the expanded moderation scope at action time. No permission flags or assignments changed. |
| Community Member role | No additional role grants enabled, including Administrator, Manage Roles, Manage Server and Manage Webhooks. | Effective access also inherits @everyone and channel overrides. |
| @everyone | View channels, message/history and normal discussion capabilities enabled; privileged management/administrator permissions were off. | Channel overrides still govern reporting and private channels. |
| Moderator role | Timeout Members, Manage Messages and Mute Members enabled; Administrator, Manage Roles, Manage Server, Manage Webhooks, Kick and Ban off. | Maintainer grants: Manage Channels, Manage Messages, Pin Messages and Manage Threads/Posts. Contributor had no additional grants. Neither had Administrator, Manage Roles or Manage Webhooks. Effective access still includes channel overrides. |
| Reporting channels | Discord **View Server As Role → Community Member**, then post-activation **@everyone**, could read `#github-updates` and `#development-updates`; both displayed “You do not have permission to send messages in this channel.” | Role preview, not a privileged-account posting test and not proof from an actual ordinary account. |
| Engineering discussion | Post-activation @everyone preview could see `#general` and `#bed-docking` with enabled message composers; private `#community-updates` was absent. | No real member post or thread/attachment test was performed. |
| Rules/welcome/channels | Existing respectful-conduct, anti-spam, privacy, evidence and safety rules; welcome/resources/announcements, community and engineering channels already present. | No need to duplicate channels or replace the existing rules. |
| Reporting delivery | Recent `merge:8`, `merge:9`, `merge:10` messages visible in `#github-updates`; corresponding Actions history successful. Prior engineering updates visible in `#development-updates`. | Published-release delivery still awaits a genuine release. No webhook values were inspected. |

The completion milestone `development:community-features-activated` was sent once after a duplicate-history check. [Actions run 38330071317](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38330071317) succeeded, and the [actual Discord message](https://discord.com/channels/1558743337735954512/1558750555097145384/1559370333985706050) was inspected after Community/onboarding changes. This confirms that development reporting still delivers without inspecting credentials.

## Saved onboarding configuration

- Default channels: `#welcome`, `#rules`, `#resources`, `#general`, `#ideas-and-suggestions`, `#questions-and-help`, `#bed-docking`. Discord showed seven total and four chattable, satisfying its displayed minimum of one chattable channel.
- Optional, multi-answer pre-join question: “What do you want to do in this community?” Four answers cover mechanical/docking, electronics/software, project updates, and sharing work/evidence/development tools. Only existing public channels are assigned; no roles are assigned. Discord confirmed all 16 public text channels were covered by defaults and answers. Private updates were not exposed.
- Server Guide welcome identifies early feasibility, no validated prototype, undecided licensing and GitHub authority. Three tasks link to the pinned welcome, an introduction/question in `#general`, and the pinned docking challenge. Discord also provides Read the rules.
- No reporting channel was converted into a resource page; feeds remain ordinary read-only channels. Existing resources remain available in the default list. No banner purchase, bot, new role or new channel was needed.

The first Server Guide save returned a generic “Errors: message” validation failure. A concise welcome entered again and three explicit tasks saved successfully; the live guide and enabled state supersede that failed attempt. Initial role dragging on the row did not change the order; using the actual drag grip worked, and Save Changes was acknowledged. No success was inferred from an attempted action alone.

## Remaining owner follow-ups and verification limits

1. **Moderator 2FA (explicitly deferred by owner):** enable owner-account 2FA privately, then enable Require 2FA for moderator actions in Safety Setup. Do not share authentication or recovery values with an agent.
2. **Moderation staffing:** all four custom roles had zero members. The owner remains responsible until trusted people are deliberately assigned; no unsolicited assignments were made.
3. **Independent newcomer test:** a willing ordinary account should use the public invitation and complete onboarding. Confirm welcome/rules/resources visibility, posting in `#general` and `#bed-docking`, inability to post/create threads/use external apps to post in reporting channels, and hidden private updates. Role preview verifies the displayed permissions but cannot establish real joining, verification delays, AutoMod enforcement or attachment/thread behavior.
4. **Draft PR review:** README and CONTRIBUTING invite/navigation changes remain in [Draft PR #15](https://github.com/VoidPhoenixApps/project-tesseract/pull/15), not main, until explicit human merge approval.

Historical blockers resolved during the continuation: owner Community agreement, actual onboarding configuration, signed-in GitHub pins, and approved role hierarchy. The original partial-activation report remains as dated history rather than being erased.

After independent newcomer testing and moderation ownership are settled, the owner can review the [outreach announcement](message-drafts.md#founding-contributors-outreach) for external promotion. Six issue drafts remain unassigned and unpublished; inspect ongoing engineering work before expanding the queue.

## Repository changes and verification boundaries

README and CONTRIBUTING gain the verified invitation and current participation links. Community records distinguish published items from remaining drafts and capture this audit. The reporting guide receives only a pointer to this newer community record. These source edits remain subject to a Draft PR and human approval; live administrative changes above have already occurred independently of the PR.

Engineering requirements, architecture, roadmap, CAD, Phase 1/1B studies and automation code remain outside scope. Documentation verification covers changed-file links/anchors, Markdown structure, requirement/license/status consistency, full diff and staged whitespace checks. The existing 15 mocked reporting tests check reporting software only. No physical, CAD-generation or actual newcomer-access test is implied.

All 15 reporting tests passed using bundled Python with `-X utf8 -m unittest discover -s tests -v`; 29 relative links/anchors across seven changed Markdown files and balanced fences passed. Full/new-file diff review and unstaged/staged whitespace checks passed. [Initial PR CI](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38327211440) also passed. The final reporting-evidence addition changes documentation only; its PR checks are tracked on [Draft PR #15](https://github.com/VoidPhoenixApps/project-tesseract/pull/15).

Any durable cross-project community ownership/access reference can be promoted separately after review; this task makes no source-repository knowledge update and creates no missing project record.

Continuation verification: all 29 relative links/anchors across the seven PR Markdown files and balanced fences passed again. Full continuation diff and whitespace checks passed. Existing reporting code is unchanged; the prior 15-test run remains applicable, and final PR CI is checked separately. No engineering or physical tests were run for this administrative/documentation continuation.
