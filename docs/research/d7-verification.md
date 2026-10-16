# D7 — verification, review and delivery record

**2026-10-15, America/Chicago. Research only.**

## Source state and scope

Started clean on main at `8b2512035560350863a27fd7fb99af2366ffed2c`; fetch confirmed
0 ahead/0 behind origin/main. Branch `codex/d7-integrated-architecture`. Existing
Phase 1C worktree and unrelated branches preserved. Issue #39 read live. Shared
workflow/engineering/knowledge/secrets/model/independent-review standards read from
project-knowledge at `147de4d979bba17120a4cc425983d590f85b6000`, matching current GitHub
main; no Tesseract CURRENT_STATE exists there. Current Home Infrastructure instructions
read through GitHub; no household machine work performed. AgentMemory queried once,
returned unrelated context, not used. Neither source repository changed; no duplicate
research memory saved.

## Changed-file inventory

All new files are under `docs/research/`; `docs/research-first-plan.md` adds one navigation/status paragraph. Historical evidence and requirements are unchanged.

| File | Reason |
| --- | --- |
| `d7-integrated-study.md` | Public overview, three integrated research candidates plus explicit noncompliant control, dissent and CAD-resumption gate |
| `d7-evidence.md` | Baseline-pinned evidence classes, scope, negatives and corrected assumptions |
| `d7-compatibility.md` | Eight-mode head/Z/park ownership, named XY/Z variants, shared gates and exclusion rationale |
| `d7_matrix.py` | Reproducible conservative evidence classification; no physics/geometry solver |
| `d7-matrix.md` | Generated 1,536-cell comparison and subsystem profiles with E overlay contract |
| `test_d7_matrix.py` | Mode partitions cross-checked against D2, negative ownership regressions, grouped C/F correction and generated-report consistency |
| `d7-failure-chains.md` | Cross-system hazards, observable discrimination and proposed review obligations |
| `d7-diagrams.md` | Editable text top/side/support/parking diagrams, no invented dimensional CAD |
| `d7-experiments.md` | Prioritized future experiments, uncertainty/stop gates and consolidated geometry requirements |
| `d7-model-requests.md` | Stage D generated request packet retaining exact existing identities and rights limitations |
| `d7-verification.md` | This source/check/review/delivery record |
| `../research-first-plan.md` | Link the integrated package and narrowly supersede the research-not-started wording; retain CAD pause |

## Reproduction

Use existing Python 3.9+ standard library, from repository root; no installation needed.
These commands do not access hardware or retrieve models.

```sh
python3 -B docs/research/d7_matrix.py > /tmp/tesseract-d7-matrix.md
cmp docs/research/d7-matrix.md /tmp/tesseract-d7-matrix.md
python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v
python3 -B -m unittest discover -s docs/phase1b -v
python3 -B -m unittest discover -s tests -v
python3 -B docs/phase1/screening_calculations.py
python3 -B scripts/check_fusion_smoke_test.py
python3 -B scripts/check_reference_parts.py
python3 -B scripts/reference_parts_triage.py --check-report
git diff --check
git diff --cached --check
```

Regenerate only the matrix deliberately with `d7_matrix.py --write`. The model-request
appendix is Stage D's `--requests` output for the seven IDs listed in the experiment
file, with purpose `D7 future experiment dependencies; candidate references only, exact selections and revisions unresolved`
and blocked-work `Dependent E1/E2/E3/E5/E6 CAD remains gated; no retrieval authorized by D7`.
Exact reproduction is checked before delivery; no catalog changes are needed.

## Checks and limitations

- Research suite: **100 passed** (93 inherited plus seven D7).
- Phase 1B: **11 passed**; repository suite: **84 passed**; **195 tests total**.
- D1–D6 JSON, Phase 1B Markdown and D7 matrix reproduced byte-identically from `/tmp` using absolute script paths. D7 request appendix reproduced from Stage D tooling.
- Phase 1 screening calculations and Fusion smoke **source** checker passed; no Fusion execution claimed.
- Catalog validator passed for 45 records; existing authorized Feather bytes/license validated in the approved sibling library. Readiness report matched catalog. No additional assets retrieved.
- New Python source parsed with Python 3.9 grammar. D7 Markdown local links/anchors, table columns, fences, one H1 and final newline checked; conceptual diagrams inspected as text.
- Requirement file and all prior D1–D6/Phase artifacts unchanged. Full intended source/generated diff reviewed; working and staged whitespace checks performed before commit.

## Independent read-only review

A separate AI reviewer inspected all eleven D7 files, issue #39, requirements,
architecture/roadmap and relevant prior evidence. Initial findings: **0 Critical,
1 Important, 1 Minor**. The Important finding caught B1's concurrency exclusion
incorrectly carried into single-job J; J now remains unresolved pending whole-bridge
parking/path proof, with a regression. The Minor finding clarified B0 as four X
carriages on exactly one common Y beam and distinguished a two-beam alternative.
Both corrections are retained in source, generated matrix and this record.

Reviewer rechecked both fixes and independently ran all seven D7 tests: passed.
Final disposition: **APPROVE for Draft research publication; no remaining findings**.
Acceptance and architecture compliance Yes; test/overall confidence Medium;
authorization High; data integrity not applicable. Publication/reporting remained
primary-agent work. This is not qualified engineering review or human merge approval.
The highest residual risk is subsystem factorization: coordinate ownership does not
establish compatible geometry, thermal behavior, load paths or fault response.

## Verification limits
The D7 tests check the evidence ledger's structure and retained logical exclusions;
they do not independently establish the engineering judgments encoded in the profiles.
Cross-system review must still challenge the factorization. There is no full-machine
simulation, complete 56-transition proof, measured clearance or new physical result.

No CAD runtime, firmware build/execution, new renderer installation, component sourcing
transaction, hardware-in-loop, energized/moving experiment or safety certification was
performed: research-only scope, exact geometry/ratings and reviewed procedures absent.
Text diagrams are directly editable/readable; no external diagram renderer is required.
No external source availability/stock/price revalidation is claimed; D7 synthesizes
versioned prior research and the current catalog, retaining their source-access limits.

Required before CAD resumes: maintainer review plus independent qualified mechanical,
electrical/controls scrutiny, bounded experiment authorization, exact approved reference
geometry and public reproduction path. Physical work needs additional reviewed hazards,
acceptance/abort limits, uncertainty and supervision. No final design/license selected.

No cross-project durable decision has changed. After acceptance, separately authorized
project-knowledge work could link this D7 record and remaining gates; do not invent a
project CURRENT_STATE or claim that update occurred. Home Infrastructure needs no
engineering-copy update for this research publication.

## Publication and Discord report

Research commit `2fc9efe3910b4171c09434c2cd943cda02015dde` published in
[Draft PR #40](https://github.com/VoidPhoenixApps/project-tesseract/pull/40), targeting
main and linked to issue #39. The [initial CI run](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38852931958)
passed (repository suite and whitespace, not research-suite execution). Final delivery
record commits are documentation-only; final-head CI is checked separately at handoff.
No merge performed.

Inspected all 46 retained reporting runs; none had the D7 milestone ID. Dispatched
`d7-integrated-architecture-research` exactly once via `discord-reporting.yml --ref main`
with public fields and evidence category `concept`. [Run 38852952979](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38852952979)
succeeded and logged Discord acknowledgement for message `1560516100137951365`.
[Message location](https://discord.com/channels/1558743337735954512/1558750555097145384/1560516100137951365).

**Actual message-content inspection remains blocked:** the native Discord app returned
its existing view unchanged after server navigation, Raise and channel-switch attempts;
the browser fallback reached Discord login rather than the channel. No credentials
were read/requested and no retry/recovery/duplicate report was sent. Thus workflow
execution and Discord acknowledgement are verified, but channel-visible content is
not claimed verified. The public report says 195 software tests, inherited analytical
reproduction and resolved AI-review corrections; no physical validation or CAD permission.
