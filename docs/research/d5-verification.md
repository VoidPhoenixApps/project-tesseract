# D5 — verification and review record

**2026-10-15, America/Chicago.** Completed desk checks and independent read-only review
for preliminary research publication. No physical validation is implied.

## Source and scope

Clean D4 branch at `30367e326ae1eec1cfe62b7eb6c5eb1d30c9f7c5`; origin verified. Fetched
Tesseract only. Live D1–D4 remained open Draft PRs with matching heads. D5 targets D4.
All new files are under docs/research; [package index](d5-engineering-study.md#package)
lists each file and purpose. Requirements and parent research remain unchanged.

## Checks and independent review

- `python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v`: **68 passed**, including 13 new D5 tests and 55 inherited D1–D4 tests.
- `python3 -B -m unittest discover -s docs/phase1b -v`: **11 passed**.
- `python3 -B -m unittest discover -s tests -v`: **63 passed**. Reporting mocks and historical CAD/source checks are not physical evidence.
- **142 tests passed** total. D5 JSON generated from outside the repository was byte-identical; both new Python files parsed using Python 3.9 grammar.
- All 13 Markdown files checked for internal files/heading anchors, table column structure, balanced fences, one H1 and final newline. Editable diagrams inspected as text; no external Markdown renderer was run.
- Requirements/classification, cross-document consistency, eight explicit modes and both panel states reviewed. Full new-file diff and generated results reviewed. Explicit intended paths staged; working and staged `git diff --check` passed.
- Main requirements/architecture/roadmap/plan and parent D1–D4 evidence remain unchanged. Supporting project-knowledge working tree remains clean.

A separate read-only AI reviewer inspected all 16 new files, user acceptance criteria,
requirements/architecture, inherited constraints and the shared independent-review policy.
They independently ran all 68 research tests, checked the analytical equations and
spot-checked PALSUN, PERSPEXre, the AGC property proxy, 5754 aluminum and selected ISO
catalog identities. They did not independently reread every external reference or run
the Phase 1B/repository suites; those were executed by the author.

Disposition: **APPROVE for preliminary research publication**, with **0 Critical,
0 Important and 0 Minor findings**, conditional on completing this record (now completed).
Arithmetic/test and research-publication confidence high; no hardware/safeguarding
approval, physical prediction confidence or human merge authorization follows.
The reviewer identified open-air protection as the highest-risk unresolved area,
followed by local temperatures and real removal envelopes.

Source retrieval limitations remain explicit: Pilkington EXP11 unavailable, full normative
standards not acquired, exact glass ratings and lifetime material data absent. AGC PDF
text was available and independently checked; an optional page screenshot timed out.
No unavailable-source value was silently promoted to selected-part evidence.

## Limits and durable context

No CAD generation/fit, physical measurements, energized/moving tests, hardware fault
injection or professional certification: this task is research-only and exact geometry,
ratings and reviewed test procedures are missing. Source gaps and missing-model dependencies
are recorded in the [ledger](d5-references.md). No final material, mechanism, controller,
thermal target, active heater, filtration/exhaust or license selected. Supporting source
repositories unchanged; future separately authorized knowledge work is identified in
[next investigations](d5-next-investigations.md).
