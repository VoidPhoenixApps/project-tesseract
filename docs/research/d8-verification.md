# D8 — verification and handoff record

**2026-10-16; analytical research only.** [Study](d8-assembly-study.md).
Started with clean main equal to fetched origin/main at D7 merge
`7657641742bc7d612457dfbdf414c5413fc60e14`; branch
`codex/d8-assembly-reach-parking`. Shared standards checkout matched its GitHub main
at `147de4d979bba17120a4cc425983d590f85b6000` and was read without modification.
No source-repository synchronization or external repository writes were performed.

## Changed-file inventory

| File | Reason |
| --- | --- |
| [d8-assembly-study.md](d8-assembly-study.md) | Public findings, source/assumption policy, competing architectures and smallest proposed E1 experiment |
| [d8-motion-contract.md](d8-motion-contract.md) | Full assembly accounting, omissions, eight-mode ledger and R intermediate support contract |
| [d8-diagrams.md](d8-diagrams.md) | Editable top/side/mode/path sketches and pre-CAD decision tree |
| [d8_geometry.py](d8_geometry.py) | Bounded H/B/common/E continuous box experiments reusing D2; reproducible generation/check commands |
| [test_d8_geometry.py](test_d8_geometry.py) | Negative/boundary and transform regression tests |
| [d8-results.json](d8-results.json) | Generated raw cases, first collision intervals and sensitivity witnesses |
| [d8-results.md](d8-results.md) | Generated readable mode and sensitivity tables |
| [d8-model-requests.md](d8-model-requests.md) | Existing missing-model tool output for four candidate identities; no new catalog records or retrieval |
| [research-first-plan.md](../research-first-plan.md) | Narrow navigation pointer retaining CAD pause |
| This file | Actual verification, limitations, review disposition and publication evidence |

## Reproduce

Python 3.9+ standard library only, from repository root. No installation, network,
CAD application or hardware is required by these calculations/tests. Generation runs
thousands of continuous component-pair comparisons and can take a few minutes.

```sh
python3 -B docs/research/d8_geometry.py --check
python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v
python3 -B -m unittest discover -s docs/phase1b -v
python3 -B -m unittest discover -s tests -v
python3 -B docs/research/d2_geometry.py > /tmp/tesseract-d8-d2.json
cmp docs/research/d2-results.json /tmp/tesseract-d8-d2.json
python3 -B docs/research/d7_matrix.py > /tmp/tesseract-d8-d7.md
cmp docs/research/d7-matrix.md /tmp/tesseract-d8-d7.md
python3 -B docs/phase1/screening_calculations.py
python3 -B scripts/check_fusion_smoke_test.py
python3 -B scripts/check_reference_parts.py
python3 -B scripts/reference_parts_triage.py --check-report
git diff --check
git diff --cached --check
```

Use `d8_geometry.py --write` only when deliberately regenerating the two results.
The model request appendix reproduces with the existing helper's `--requests`, four
`--id` values in the study table, purpose
`D8 future E1 envelope discrimination; candidates only, exact selections unresolved`
and blocked-work `Future bounded E1 CAD; no download or CAD execution authorized`.
`--requests` cannot combine with `--library`; an initial rejected invocation was
corrected without a download. Local-library validation is a separate read-only check:

```sh
python3 -B scripts/check_reference_parts.py --library '/Users/todd/Development Projects/tesseract-cad-library'
```

## Verification results

- Research suite: **111 passed** (100 inherited, 11 D8); repository suite: **84 passed**;
  Phase 1B suite: **11 passed**. **206 software/analytical tests total**.
- D8 full `--check` passed: JSON and Markdown reproduce byte-identically from source.
  696 baseline and 1,728 sensitivity cases. Model-request appendix reproduced exactly.
- D2 JSON and D7 matrix reproduced byte-identically with the commands above.
- Phase 1 analytical script and Fusion smoke source checker passed. No CAD runtime claim.
- Catalog validator: 45 candidates; the one existing authorized local asset and license
  passed hash checks. Readiness report matched. Local library has no requested head/stage model.
- Markdown local links/anchors, tables, fenced blocks, one H1 per document and terminal
  newlines checked; Python source parsed with Python 3.9 grammar. Editable text diagrams
  inspected against code axes, bed numbering, dimensions and fixed-length rail behavior.
- Requirements, architecture, roadmap, prior D1–D7/Phase evidence and CAD/catalog artifacts
  remain unchanged. Full intended source/document diff reviewed; generated artifacts
  checked against source. Working and staged whitespace checks passed before commit.

### Independent AI review

The separate read-only reviewer inspected issue #41, applicable instructions, D2/D7,
new source/tests and documents. Initial findings: **0 Critical, 1 Important, 1 Minor**.
The Important finding identified synchronized departure without a single departing
owner while other jobs print; source now includes every owner's departure/return
with others retaining live print routes across all candidate/orientation/panel states.
The Minor finding corrected the original baseline count. A generated-coverage
regression now asserts the expanded case inventory. Reviewer independently ran D2
20/20, D7 7/7 and revised D8 10/10 before the final inventory test was added.

Final disposition: **APPROVE for Draft research publication**, with no unresolved
findings. Reviewer rechecked all 11 D8 tests, 696/1,728 case counts, generated Markdown
against JSON, vertical negative intervals, mixed schedules, narrative event counts
and the conservative interval-test acceleration. All passed. Architecture compliance Yes; test/overall
confidence Medium; authorization High; data integrity not applicable. No professional
engineering signoff, permission to execute E1, or human merge approval follows.

## Limits and remaining gates

No detailed printer/fixture CAD, new CAD tool, vendor model retrieval, purchases,
manufacturer contact, firmware change, physical experiment or machine operation.
Fusion smoke validation checks **source**, not a Fusion runtime or physical fit.
No real assembly collision certificate, all-path/all-height proof, 56 conversion
route proof, thermal/seam validation, positive gravity support or safety rating.
No external vendor availability/rights requalification is claimed. The existing
Feather asset has no role in head/stage geometry. Full harness/filament paths,
frame/under-bed details, service extraction and actual component revisions remain
unknown and cannot be assigned zero size. Counts are not risk or feasibility scores.

Independent qualified mechanical and electrical/controls review and maintainer
acceptance remain necessary before any bounded CAD authorization. Physical testing
requires a separately reviewed hazard assessment, procedure, measurable limits,
uncertainty, abort conditions and supervision. First physical proof remains two-bed
docking/cross-seam printing. Grouped-bed restraint and hot-seam problems remain open.
All approved requirements and prior evidence are preserved; no architecture or license
selected. After acceptance, a separately authorized project-knowledge link could
record D8 and its remaining gates; no Tesseract CURRENT_STATE was invented. No new
AgentMemory save is needed because useful task evidence is recorded here.

## Publication and Discord evidence

Research commit `313e16c49c6fdc1809874f301fec671f4f875e7f` published in
[Draft PR #42](https://github.com/VoidPhoenixApps/project-tesseract/pull/42), targeting
main and linked to issue #41. [Initial CI](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38855713903)
passed: repository tests and whitespace only; the 111 research tests were run locally.
This publication-record update changes documentation only; final-head CI is checked at
handoff. No merge performed; the PR remains Draft.

Inspected all 48 retained reporting runs before dispatch; no D8 milestone duplicate.
Sent `d8-full-assembly-reach-parking` exactly once via `discord-reporting.yml --ref main`
with public text and evidence category `concept`.
[Run 38855751919](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38855751919)
succeeded and acknowledged message `1560524240762052619`.
[Actual Discord message](https://discord.com/channels/1558743337735954512/1558750555097145384/1560524240762052619)
was then inspected through the native Discord UI in **Project Tesseract / development-updates**.
Verified the D8 accomplishment, significance, 206 tests, 696/1,728 cases, concept category,
remaining geometry/qualified-review/gravity/hot-seam gates, PR #42 link and stable report ID.
Workflow success, Discord acknowledgement and channel-visible message content were each
verified separately. No secret values were read/requested; no duplicate/recovery sent.
