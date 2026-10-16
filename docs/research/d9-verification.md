# D9 — verification and handoff record

**2026-10-16 · Research only.** [Public study](d9-study.md).
Clean starting checkout was the D8 feature branch at `8ccb780`; existing alternate
Phase 1C worktree was preserved. Fetched origin, confirmed issue #43 and created
`codex/d9-z-support-falsification` directly from synchronized `origin/main`,
`bf8a55f40e2d6ff99069950e8ddc27874cf32e9d`. No stash/reset/clean or worktree removal.
Shared project-knowledge checkout matched live GitHub main at
`147de4d979bba17120a4cc425983d590f85b6000`; workflow skill, engineering, independent
review, knowledge, secrets and model standards read. No Tesseract CURRENT_STATE
exists there; none invented. Current Home Infrastructure instructions read via GitHub.
No supporting repository was edited or synchronized. AgentMemory queried once and
returned unrelated continuity; nothing used or saved.

## Changed-file inventory

| File | Reason |
| --- | --- |
| [d9-study.md](d9-study.md) | Readable conclusions, evidence classification, H/B comparison and requirement preservation |
| [d9-contract.md](d9-contract.md) | P/L/T/R/O separation, complete gravity inventory, eight owner partitions and F/C alternatives |
| [d9-faults.md](d9-faults.md) | Constant-datum transfers, occupied-neighbor closure, counterexamples and fault-containment obligations |
| [d9-diagrams.md](d9-diagrams.md) | Editable conceptual load paths, modes and handoff logic |
| [d9-calculations.md](d9-calculations.md) | D3 sensitivity reuse, inputs/units, signed contacts and exact mathematical limits |
| [d9-review-packet.md](d9-review-packet.md) | Qualified-review questions, future E2 scope, model/data requests and proposed abort gates |
| [d9_support.py](d9_support.py) | Abstract membership/support/observation/transfer checks and deterministic D3 sensitivities |
| [test_d9_support.py](test_d9_support.py) | Twelve focused positive, negative and boundary tests, including 24 intermediate-state mutations |
| [d9-results.json](d9-results.json) | Reproducible raw sensitivity and declared-graph counterexamples |
| [research-first-plan.md](../research-first-plan.md) | Narrow D9 navigation entry retaining the CAD pause |
| This file | Actual checks, review disposition, delivery evidence and limitations |

## Reproduce locally

Python 3.9+ standard library. No dependency installation, CAD runtime or hardware.
D8 full reproduction can take several minutes; it checks both generated files.

```sh
python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v
python3 -B -m unittest discover -s docs/phase1b -v
python3 -B -m unittest discover -s tests -v
python3 -B docs/research/d3_analysis.py > /tmp/tesseract-d9-d3.json
cmp docs/research/d3-results.json /tmp/tesseract-d9-d3.json
python3 -B docs/research/d7_matrix.py > /tmp/tesseract-d9-d7.md
cmp docs/research/d7-matrix.md /tmp/tesseract-d9-d7.md
python3 -B docs/research/d8_geometry.py --check
python3 -B docs/research/d9_support.py > /tmp/tesseract-d9-results.json
cmp docs/research/d9-results.json /tmp/tesseract-d9-results.json
python3 -B docs/phase1/screening_calculations.py
python3 -B scripts/check_fusion_smoke_test.py
python3 -B scripts/check_reference_parts.py --library '/Users/todd/Development Projects/tesseract-cad-library'
python3 -B scripts/reference_parts_triage.py --check-report
git diff --check
git diff --cached --check
```

## Verification results

- Research suite: **123 passed**, including 12 new D9 tests and inherited D3/D7/D8 tests.
  Phase 1B: **11 passed**. Repository suite: **84 passed**. Total: **218 software and
  analytical tests**, no physical tests.
- D3 JSON, D7 matrix and D9 JSON reproduced byte-identically. D8 full `--check`
  passed: generated JSON and Markdown match source (696 baseline / 1,728 sensitivity cases).
- Phase 1 screening and Fusion smoke source checker passed; no Fusion execution claim.
- Catalog validator: 45 candidates; one authorized existing local asset hash checked.
  Readiness report matched. No requested E2 model acquired or fabricated.
- Documentation validation initially found the not-yet-created verification record;
  record was then added and checks passed. Local Markdown paths, table columns,
  balanced fences, single H1 and terminal newlines checked. Python 3.9 grammar parsed;
  execution used Python 3.9.6. Diagrams manually checked against the contract, axes
  and mode tables; equations and rounded result tables checked against raw output.
  Complete intended diff including new files reviewed for requirement preservation,
  scope and secret exposure. Working and staged whitespace checks passed.

## Independent AI desk critique

Separate read-only reviewer inspected issue #43, actual new files, tests and prior
engineering evidence. Initial findings: **0 Critical, 0 Important, 1 Minor**. The
row-mixed ↔ column-mixed table incorrectly described all four beds as the minimum
affected set. Corrected to the three-bed membership union, with the fourth included
only by additional physical influence; added M12↔M13 → {1,2,3} to the regression.
Reviewer confirmed correction and all 12 D9 tests, reproduced the D9 JSON and checked
whitespace. Final disposition: **APPROVE for Draft research publication**, no
unresolved findings; architecture/requirement preservation Yes, test/overall confidence
Medium. No AI recommendation supplies qualified engineering signoff, a physical test
permit or human merge approval.

## Limits and remaining decisions

No detailed CAD, model retrieval, installation, purchasing, supplier contact, firmware
modification or hardware operation. Physical testing and actual fault injection were
not run because explicitly unauthorized and because reviewed hazards, limits, uncertainty,
containment, procedure and supervision do not exist. No CAD generation or physical fit
check is applicable to abstract original diagrams. Mermaid source is editable; browser
render validation is not claimed. No new stock choice or legal/license decision was made.

No final safety design, 56-route physical proof, continuous-support trajectory,
six-DOF constraint solution, actual load rating, peak catch-force bound, hot-seam proof
or complete D8 lift/harness envelope exists. Current source pages supply principles,
not exact device qualification or rights. Qualified mechanical and electrical/controls
review plus exact selected geometry/data remain prerequisites to bounded CAD adoption.
The first physical proof remains the separately reviewed two-bed docking/seam rig.

Requirements, architecture, roadmap, historical D1–D8/Phase 1/1B/1C artifacts and catalog
are unchanged. Proposed next work is the evidence-gated E2 specification, not machine
construction. After acceptance, a separately authorized project-knowledge navigation
entry may link D9 and its open gates; no existing Tesseract project record needs invented
state. Home Infrastructure has no changed device/configuration fact from this task.
Useful findings are recorded here, so no AgentMemory save is needed.

## Publication and Discord evidence

Draft PR and reporting evidence will be recorded after reviewed publication. No merge
authorized or performed.
