# D2 — verification and review record

**Research evidence only, 2026-10-14 America/Chicago.** [Report](d2-engineering-study.md).
No physical verification, hardware operation, firmware changes, purchases, detailed CAD,
manufacturing files, architecture selection, licensing change or cross-repository edits.

## Provenance and workflow

- Original checkout clean on `codex/research-d1-compatibility-screen`; origin verified
  as `https://github.com/VoidPhoenixApps/project-tesseract.git`.
- Fetched main `952c2202bc001d1aff38fa7bce9a0b86410695d6`; read current CHATGPT_INSTRUCTIONS,
  AGENTS, README, requirements, architecture, roadmap, research-first plan, contribution
  and Discord reporting rules. Read the five requested D1 documents at
  `25eb8a745cf8c4ddc54d64a65159e26f756bbc93`.
- Live PR #25 open/draft, base main, head exactly that D1 commit. Created dedicated
  `codex/research-d2-reach-collision` from that head. D2 targets the D1 branch while D1
  remains unmerged. No modification or merge of PR #25; no reset, stash or cleanup.
- Shared workflow skill, engineering, independent review, development, knowledge,
  secrets and model-selection standards retrieved read-only from project-knowledge
  main `147de4d979bba17120a4cc425983d590f85b6000`. No Tesseract CURRENT_STATE found or invented.
- AgentMemory queried once; returned unrelated material, not used. No duplicate memory
  record saved. GitHub remains authoritative.

## Deliverable map and requirement preservation

| Artifact | Purpose / evidence |
| --- | --- |
| [Engineering report](d2-engineering-study.md) | XY-A through E, full structural alternatives, conventional comparisons, quantitative constraints, adversarial conditions and three next investigations |
| [Eight-mode matrix](d2-mode-coverage.md) | Groups, candidate head assignments, necessary paths, parking and unresolved conditions; injective reach matching prevents double-counting a head |
| [Mirrored study](d2-mirrored-study.md) | Exact fixed A/B/B/A transforms, equal-envelope comparison, seam saving/outer penalty and two-type evidence requirements |
| [Calculations](d2-calculations.md), [code](d2_geometry.py), [results](d2-results.json), [tests](test_d2_geometry.py) | Parameter classes, fixed-orientation 3D sweeps, continuous relative-motion collision kernel, 16 structural mode screens and sensitivity ranges |
| [Diagrams](d2-diagrams.md) | Editable text top/side views including full beams, bodies, descending columns, parks and local/cantilever alternatives |
| [Reference catalog](d2-references.md) | Primary evidence, traceable dimensions, retrieval limitations, exact candidate identities where known and future missing-model/rights dependencies |
| [Public summary](d2-public-summary.md) | Plain-language findings, limits and invitation for source-backed critique |
| This record | Provenance, tests, review and remaining evidence gates |

Requirements and D1 files remain unchanged. Four 180 mm nominal modules and retained
sheets, horizontal empty-bed fixed-datum reconfiguration, unrelated job progress and a
single J head path remain the targets. No nominal footprint is promoted to usable build
volume. Printable-first/Ender 3, both stock variants, later 2020, tool-free removable
enclosure in both states and editable reproducibility are preserved obligations, not
verified mechanical outputs from this study. Cooperative four-head printing is unused.

## Checks performed

- Research suite: `python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v`:
  **26 pass** (six unchanged D1, twenty D2).
- D2 tests cover fixed reflection/rotation, carriage/nozzle transforms, containment,
  continuous mid-path contact, moving/moving and moving/parked boxes, 3D height separation,
  tall completed objects and bed-Z translation, conservative-hull false positives,
  exact touching, all eight configurations, both paired directions, all mixed assignments,
  injective fifth-head limits, J parking/enclosure, stack column crossings, seam benefit
  and outer penalty, carrier reconfiguration mid-path collision, unsupported geometry,
  sensitivity, determinism, full moving beam versus object and head versus parked beam.
- Phase1B: `python3 -B -m unittest discover -s docs/phase1b -p test_analysis.py -v`:
  **11 pass**, including preserved negative thermal/constraint/transition evidence.
- Repository suite: `python3 -B -m unittest discover -s tests -v`: **63 pass**.
- Regenerated D2 JSON byte-identical to committed-intent output; both new Python files
  parse with Python3.9 syntax rules. Eight new Markdown documents checked for local
  targets/anchors, balanced fences, table column counts and terminal newlines.
- D1, requirements, architecture and roadmap unchanged against base. Full new-file
  review and whitespace checks include explicit staging before commit; no existing files edited.

These tests establish only the implemented analytical/software behavior. Missing real
geometry is explicitly U. No complete machine trajectory, all-mode transition planner,
actual cable sweep, verified service path, true physical clearance, dynamic behavior or
qualified safety review is claimed. Figures are editable text schematics; no CAD renderer
or external Markdown linter is required or invoked.

## Independent desk review

A separate read-only Astra Medium engineering reviewer inspected the actual package
against the user scope, requirements, D1 and shared review rubric and reran the then
19 D2 tests and JSON reproduction. Initial result: REQUEST CHANGES, zero Critical,
one Important, zero Minor. The reviewer independently found that park260 requires
carriage±280, outside the declared ±240 travel. The screen previously omitted parking
containment despite correctly flagging missing routes and enclosure conflicts.

Correction: report each parked head's required carriage coordinates and containment;
classify explicit parked reach failures REACH_REJECTED; preserve the negative parks;
add default-failure and exact boundary tests; regenerate JSON and update all affected
interpretations. The follow-up read-only review confirmed the fix, reran all26 research tests,
reproduced byte-identical JSON, checked staged whitespace and working/staged equality,
and returned **APPROVE for research documentation**, with zero Critical, Important or
Minor findings outstanding. Acceptance and requirements compliance: yes for bounded
research. Overall and test-coverage confidence: Medium. Other suites were not
independently rerun in that recheck.
External sources were not independently retrieved by the reviewer. This review is an AI desk review, not qualified mechanical/electrical
or controls/safety approval. Human approval is still required before merge, architecture
adoption or any subsequent CAD/hardware authorization.

## Remaining evidence and handoff

The key unresolved question is whether all structural members can coexist across the
required independent workspaces. Exact component envelopes, fixed supports, real axis
strokes, cable/filament routes, service corridors, maximum object heights, stopping and
position uncertainty, bed locks/support and enclosure geometry are missing. The
[reference catalog](d2-references.md) is the consolidated dependency request for later
CAD; it does not authorize downloads now.

No shared-repository edit is required to interpret these results. After review, a
separately authorized project-knowledge record could link to the Tesseract-owned research
and unresolved status without duplicating the package. Final draft PR, CI and milestone
reporting evidence belong in the PR handoff. Do not treat draft publication as engineering
approval or close the research-first pause on the strength of software tests.
