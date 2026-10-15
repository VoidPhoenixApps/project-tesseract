# D3 — provenance, verification and review record

**2026-10-14 America/Chicago. Research only.** [Report](d3-engineering-study.md).
No detailed CAD, fabrication files, purchases, hardware operation, physical tests,
firmware/controller changes, license selection or supporting-repository modifications.

## Baseline and authority

- Checkout began clean on D2, origin `https://github.com/VoidPhoenixApps/project-tesseract.git`.
  Fetch confirmed main `952c2202bc001d1aff38fa7bce9a0b86410695d6` and D2
  `5957b80a5478e1cc669cbd7f81d71a5934326d63`; current main instruction/requirements
  documents match the checkout. Read AGENTS, README, requirements, architecture,
  roadmap, contribution rules, research-first plan and reporting rules.
- Live #25 and #26 were both open Draft with no GitHub review records; their checked-in
  desk-review records describe bounded research approval, not human architecture approval.
  D1 head `25eb8a745cf8c4ddc54d64a65159e26f756bbc93`, base main; D2 base D1 branch.
  Created `codex/research-d3-bed-coupling` from that exact D2 head, targeting
  `codex/research-d2-reach-collision`. Parent PRs/history untouched.
- Read shared workflow skill and development, engineering, model-selection, knowledge,
  secrets and independent-review standards from sibling project-knowledge
  `147de4d979bba17120a4cc425983d590f85b6000`, confirmed GitHub main. No Tesseract
  CURRENT_STATE/project record found or invented. Current Home Infrastructure instructions
  read via GitHub; main `963185a4d528884473a28a87ef81ffb0d1e59dd4`.
  Cross-repository synchronization omitted because this task explicitly excludes changes.
- AgentMemory queried once; returned unrelated continuity, not used as evidence.
  No duplicate memory saved; durable research is owned here.
- Phase 1 docking, Phase 1B thermal/docking/results and Phase 1C fixture/review evidence
  inspected, including limits of runtime checks; D1/D2 reports, calculations, mode and
  review records consulted. All historical source, evidence and negative results retained.

## Changed-file inventory and deliverables

| File | Reason |
| --- | --- |
| [d3-engineering-study.md](d3-engineering-study.md) | Comparative mechanisms, central cross/T, D2 integration, rankings and three next analytical experiments |
| [d3-mode-constraints.md](d3-mode-constraints.md) | Eight mode P/L/T constraints, load/motion ownership, verified states and transition scope |
| [d3-selector-study.md](d3-selector-study.md) | Literal rerouting versus positive torque selection; continuous-path/phase/support questions |
| [d3-diagrams.md](d3-diagrams.md) | Original editable group, side, power, support and handoff schematics |
| [d3-failure-study.md](d3-failure-study.md) | Continuous support objective, intermediate transfer states, faults and safe-state/recovery obligations |
| [d3-calculations.md](d3-calculations.md) | Assumptions, equations, reactions, seam/thermal and fault sensitivity interpretation |
| [d3_analysis.py](d3_analysis.py) | Reproducible standard-library calculations reusing D1, D2 and Phase 1B |
| [d3-results.json](d3-results.json) | Deterministic generated numerical evidence, explicitly hypothetical |
| [test_d3_analysis.py](test_d3_analysis.py) | Equilibrium, energy, boundary, mode coverage, negative controls and reproduction tests |
| [d3-references.md](d3-references.md) | Primary-source evidence, limits, rights and consolidated future model dependencies |
| [d3-public-summary.md](d3-public-summary.md) | Public plain-English question, findings and remaining work |
| This record | Provenance, checks, independent review and handoff limits |

Requirements, architecture, roadmap and all D1/D2/Phase 1 files remain unchanged.
No final mechanism, stock, toolchain, electronics or license is selected. Four retained
sheets, all mode orientations, fixed-datum horizontal conversion, printable-first,
Ender 3 parts, both stock variants, later 2020, removable enclosure and reproducible
sources remain mandatory. Four-head cooperation is not assumed.

## Checks performed

- `python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v`:
  **40 passed** (6 unchanged D1, 20 unchanged D2, 14 D3).
- `python3 -B -m unittest discover -s docs/phase1b -p test_analysis.py -v`:
  **11 passed**, retaining historical thermal, rank and collision negative cases.
- `python3 -B -m unittest discover -s tests -v`: **63 passed** (33.578 s).
  Total **114 local software/analytical tests**, not physical tests.
- D3 tests check all eight group partitions and mass conservation; force/moment
  equilibrium and uplift; torque/work and catch energy; arm scaling; guide accommodation;
  intermediate belt-path length and virtual-work derivative; downstream backlash;
  pitch/roll endpoint budget; scalar group constraints; invalid inputs; historical
  thermal incompatibility; and byte-identical generated results.
- D3 stdout reproduced committed-intent JSON byte-for-byte. Both Python files parsed
  with Python 3.9 syntax rules. Nine Markdown files passed local links/anchors,
  balanced fences, consistent table-column counts, titles and terminal-newline checks.
  External primary references were opened as recorded in the ledger.
- Complete intended staged diff reviewed, including all new code, documents and JSON;
  explicit-path staging, working/staged whitespace checks and working/index equality
  checked. Only the twelve D3 files are added; parent research and requirements preserved.

Skipped: external Markdown renderer/linter (plain Markdown/text schematics checked
directly), new CAD runtime/export checks (no CAD changed), component fit/capacity and
all-state spatial trajectories (actual geometry unselected), hardware/thermal/motion
tests (outside authorization and prerequisites absent). No safety certification claimed.
Existing GitHub CI runs the 63-test repository suite; it does not run the research or
Phase 1B suites. Final CI outcome is recorded in the PR publication handoff.

## Independent desk review

A separate read-only AI reviewer inspected all twelve artifacts against the mission,
requirements, architecture, D1/D2, Phase 1B and shared review rubric. Result:
**APPROVE for bounded research publication**, zero Critical, Important or Minor findings.
No findings were suppressed and no mechanical revision was required.

The reviewer independently ran all 40 research tests, reproduced JSON byte-for-byte
from `/tmp`, and checked 1,000 deterministic randomized cases for tripod force/two-moment
equilibrium and arrest work-energy conservation. Derivations and numerical examples
were audited. Gates' independent-backup policy and Miki's tooth-form distinctions were
independently checked against primary PDFs; other external sources were not comprehensively
revalidated. The reviewer did not independently rerun the repository or Phase 1B suites.

Acceptance and architecture/requirements compliance: yes **for research scope**.
Implemented-model test confidence: High; overall review confidence: Medium.
Highest-risk unresolved area: continuous support and compatible guide/load transfer
at the fixed datum. This is an independent AI desk review, not qualified engineering
or safety certification. Human merge approval and qualified mechanical/electrical/controls
review before adoption or operation remain required. Publication/CI/Discord were outside
the read-only review; the final verification-record update reports actual author checks.

## Remaining evidence and durable knowledge

Strongest bed-side baseline for investigation is monitored independent lifts with
specified independent restraint; hybrid support deserves comparison if guides can be
made compatible. Positive selection is the simpler secondary-frame transmission
comparison; literal belt rerouting has the largest unresolved engagement/path burden.
Unified all-attached partial modes and unrelieved rigid-guide linking retain explicit
negative findings. No whole-machine winner is established because D2 geometry remains open.

Missing actual masses, stiffness, guides, thermal fields, sheet behavior, selector
geometry, restraints/sensors, working strokes and accepted tolerances prevent capacity,
seam-quality or safety claims. Qualified mechanical, electrical/thermal and controls/safety
review and human approval remain required before adoption or new CAD/physical work.
No manufacturer models were obtained; the consolidated ledger identifies later blockers.
The first physical proof remains separately reviewed two-bed docking and cross-seam printing.

After review, a separately authorized project-knowledge entry could link this package
and its unresolved status; no existing Tesseract CURRENT_STATE exists to update.
Neither supporting repository was modified. Final Draft PR, CI and Discord run/message
evidence belong in the publication handoff; publication does not complete an engineering gate.
