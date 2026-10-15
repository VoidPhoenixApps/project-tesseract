# D6 — verification and review record

**2026-10-15, America/Chicago. Desktop research only.**

## Scope and source state

Clean D5 head `8c9321acedf9dda9b1cbbcba9f9bf3284a8b685d`; origin and open Draft
stack inspected. D6 branch targets D5. [Package inventory](d6-engineering-study.md#package-and-changed-file-inventory)
lists every new file and reason. Parent evidence, requirements and supporting repositories
remain unchanged. Source availability and exact firmware identities are recorded in the
[ledger](d6-references.md).

## Checks performed

- `python3 -B -m unittest discover -s docs/research -p 'test_d*.py'`: **93 passed**, including 25 D6 tests and 68 inherited tests.
- `python3 -B -m unittest discover -s docs/phase1b -v`: **11 passed**.
- `python3 -B -m unittest discover -s tests -v`: **63 passed**.
- **167 tests passed** total. Repository tests include reporting mocks and historical CAD/source checks; none validate printer hardware.
- Results regenerated from `/tmp` using the absolute script path were byte-identical. Both new Python files parse with Python 3.9 grammar. Standard library only.
- All ten Markdown files checked for local file/heading links, balanced fences, table columns, one H1 and final newline. Initial check caught two comparison rows missing a final column; fixed and rerun successfully.
- Requirement coverage/classification, eight modes, cross-document consistency, complete package source and generated numbers reviewed. Explicit intended paths only; working and staged `git diff --check` passed before commit.

Mermaid diagrams were reviewed as editable source; no external Markdown/Mermaid renderer
was run. No firmware runtime/build experiment, full G-code parser, hardware-in-loop test,
CAD fit/sweep, electrical test, physical measurement or safety certification was performed:
this task is desktop research, and selected geometry/parts, risk assessment and reviewed
physical procedures are absent. Model tests cover synthetic state invariants only.

## Independent read-only review

A separate AI reviewer inspected all D6 artifacts, task acceptance criteria,
requirements/architecture, inherited constraints and the shared review policy. They
ran the initial 24 D6 tests and byte-identical reproduction; primary-source spot checks
supported the qualified firmware claims. This was not an exhaustive firmware source
or standards audit, nor a qualified engineering review.

Initial disposition: **REQUEST CHANGES**, 0 Critical / 1 Important / 0 Minor. The
abstract transition checked its route against parks but omitted park-to-park,
park-to-obstacle and park-to-retained-job checks. A clear remote route could therefore
accept impossible parking evidence. The fix checks the whole idle park set against
those obstacles before mode/history mutation. Added three negative cases preserving
mode, history, job progress and reservations; the negative finding is retained here.

Independent re-review: **APPROVE for preliminary research publication as a Draft PR**;
all **25 D6 tests independently passed**, no open Critical/Important/Minor findings.
Acceptance yes for research deliverables (publication/reporting author-owned), architecture
compliance yes, test and overall confidence medium, security/data-integrity not applicable.
Highest remaining risks are actual geometry, grouped-Z fault handling and firmware
lifecycle integration. This disposition does not authorize merge or hardware work.

## Limits and durable context

No final architecture, component, electronics/firmware selection, operating limit,
protective circuit, CAD toolchain or license is adopted. Source/retrieval gaps are in
[the ledger](d6-references.md); next evidence and qualified reviews are in
[the study](d6-engineering-study.md#prioritized-decisions-and-experiments).
Source repositories remain unchanged. A later separately authorized knowledge entry
could link this research; no existing Tesseract CURRENT_STATE was found or invented.

## Publication and reporting

Published as stacked [Draft PR #30](https://github.com/VoidPhoenixApps/project-tesseract/pull/30)
from research commit `6a06e639ec137e2cd4d769f58ff8627ab9b5b65a`, targeting D5.
Parent PRs remained open Drafts at the recorded heads; no parent changed or merged.
Before dispatch, retained Actions history contained 31 reporting
runs and no D6 milestone. Discord's development-updates view was inspected and showed
D5's report with PR #29 and matching public content; no D6 report was present. This also
establishes later visibility of the D5 message whose original record left that check open;
the historical D5 file is preserved unchanged.

Dispatched `d6-controls-scheduling-study` exactly once through `discord-reporting.yml`
on main with public text and evidence category `concept`.
[Actions run 38688477155](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38688477155)
completed successfully and logged acknowledgement for message `1560166648638607371`.
The [acknowledged message](https://discord.com/channels/1558743337735954512/1558750555097145384/1560166648638607371)
was then confirmed in Discord's actual development-updates accessibility view: the
full D6 text, PR #30 link and `development:d6-controls-scheduling-study` ID matched.
Thus execution, acknowledgement and app-content inspection were checked separately.

Screenshot-level viewport verification remains incomplete: the first stale view showed
D5, native scrolling returned `noWindowsAvailable`, and raising the existing window
refreshed accessibility content to include D6. A screenshot still showed D5; another
scroll failed with the same error. No duplicate/recovery dispatch was made. This is
stronger evidence than acknowledgement alone but is not a claim of screenshot-visible
D6 content or ordinary-member access testing.

[PR CI run 38688437353](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38688437353)
passed at research commit `6a06e639ec137e2cd4d769f58ff8627ab9b5b65a`. Existing CI runs
repository reporting/CAD-source tests and whitespace checks; D6 research tests were
executed locally and independently, not silently attributed to CI.
