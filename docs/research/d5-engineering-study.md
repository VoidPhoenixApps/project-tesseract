# D5 — convertible enclosure feasibility

**2026-10-15, America/Chicago. Comparative desk research, not a selected or validated
enclosure.** No detailed CAD, fabrication, purchase, physical test, active chamber
heating, controller choice or license decision is authorized by this package.

**Finding:** Retain three conditional concepts for further study: supported lift-out
cassettes with positive hand retainers; removable hinged cassettes; and captured-edge
panels with hand-released end stops where extraction space exists. Compare transparent
polycarbonate, acrylic and tempered-glass inserts with opaque metal and hybrid panels.
No candidate yet demonstrates all-mode motion clearance, protective guarding, practical
handling or acceptable temperatures. Whole-machine feasibility remains unresolved.

## Package

| File | Owned question / reason for addition |
| --- | --- |
| [Public summary](d5-public-summary.md) | Plain-English findings and limits |
| [Materials](d5-materials.md) | Temperature, expansion, impact, fire evidence, sourcing and replacement |
| [Attachments](d5-attachments.md) | Hand operation, secure retention and failure comparisons |
| [Modes and clearances](d5-mode-clearance.md) | Eight arrangements, both panel states, frame variants and motion families |
| [Removal and service](d5-service.md) | Complete panel/hand paths and access obligations |
| [Thermal/environment](d5-thermal.md) | Passive heat balance, gradients, emissions and service consequences |
| [Safety register](d5-safety.md) | Fault states, safeguarding alternatives and future review gates |
| [Editable diagrams](d5-diagrams.md) | Original conceptual views; no vendor geometry |
| [Calculations](d5-calculations.md) | Equations, assumptions, units and interpretation |
| [Python](d5_analysis.py), [tests](test_d5_analysis.py), [results](d5-results.json) | Deterministic sensitivities, negative controls and reproduction |
| [Sources and dependencies](d5-references.md) | Primary-source ledger, applicability and missing-model list |
| [Next investigations](d5-next-investigations.md) | Priorities, evidence gates and maintainer decisions |
| [Verification](d5-verification.md) | Executed checks, independent review and publication evidence |

## Dependency and authority

The clean checkout and live GitHub inspection found this unmerged Draft stack:

| Track | PR | Reviewed research head / branch |
| --- | --- | --- |
| D1 | [#25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25) | `25eb8a745cf8c4ddc54d64a65159e26f756bbc93`, `codex/research-d1-compatibility-screen` |
| D2 | [#26](https://github.com/VoidPhoenixApps/project-tesseract/pull/26) | `5957b80a5478e1cc669cbd7f81d71a5934326d63`, `codex/research-d2-reach-collision` |
| D3 | [#27](https://github.com/VoidPhoenixApps/project-tesseract/pull/27) | `096ae806c08d437bf1c84c77d217cacdfd6f3231`, `codex/research-d3-bed-coupling` |
| D4 | [#28](https://github.com/VoidPhoenixApps/project-tesseract/pull/28) | `30367e326ae1eec1cfe62b7eb6c5eb1d30c9f7c5`, `codex/research-d4-structural-frame` |

D5 branches from D4's head as `codex/research-d5-convertible-enclosure` and targets
D4's branch, per the task-specific exception to the normal main-base workflow. Parent
PRs and evidence remain untouched. Prior AI desk review does not mean human adoption.
Fetched main `952c2202bc001d1aff38fa7bce9a0b86410695d6` supplies the unchanged AGENTS,
README, requirements, architecture, roadmap and contribution rules. The research plan
also remains unchanged. A future stack rebase/retarget requires renewed dependency review.

## Requirements traceability

| Classification | Obligation / D5 treatment |
| --- | --- |
| Mandatory | Four nominal 180 × 180 mm heated beds, four retained individual sheets, automatic horizontal configuration at a common fixed-height plane; all eight arrangements with independent jobs remain in the [matrix](d5-mode-clearance.md). Nominal joined dimensions do not promise usable area |
| Mandatory | Enclosed and open-air printing, genuinely hand-only panel installation/removal without dismantling primary systems; [attachments](d5-attachments.md) and [service](d5-service.md) assess both directions |
| Mandatory | Secure normal retention and repeated convenient conversion; separate weight support, outward retention, thermal relief, engagement verification and guarding |
| Mandatory | Cleaning, calibration, wiring inspection and component replacement access; no panel-as-brace or panel-as-gravity-restraint credit |
| Mandatory | Printable-first, ordinary Ender 3 part envelope, separate imperial/metric structural interfaces, later 2020 edition; same capabilities require distinct fit/thermal/clearance verification |
| Mandatory | Editable sources and public reproducibility without required paid/proprietary tooling; original Markdown diagrams and standard-library Python only |
| Preference | Readily obtainable materials/hardware; compare sourcing and replacement burdens without selecting suppliers |
| Proposed | Three enclosure concepts, floating followers, separate permanent protection and hypothetical sensitivity dimensions; no final architecture or material |
| Unknown | Temperature recipes, material grades/thicknesses, outer dimensions, ventilation, filtration, active heating, controller, operating limits, ratings and license |
| Stretch | Four-head cooperation on one object remains unproven and separate; baseline J examines one full-region head |

## Inherited evidence and negative findings

[D1](d1-engineering-study.md) distinguishes relative-Z ownership from whole-machine
feasibility. [D2](d2-mode-coverage.md) rejects the illustrative ±260 mm parks because
carriage travel is insufficient; widening an enclosure cannot repair that. Stacked
beams still have descending columns. No all-mode physical envelope is known.
[D3](d3-engineering-study.md) requires independent support and restraint of a secondary
lift even when parked; enclosing it does not create support or independent partial modes.
[D4](d4-enclosure.md) excludes removable panels from frame bracing and gravity support;
its [printed joints](d4-printable-joints.md) have no long-duration warm creep rating.

[Phase 1B](../phase1b/thermal.md) retains the failed center-anchor cold-gap interval
[0.43984, 0.30000] mm under its assumptions. A warmer or more uniform chamber does not
prove that result repaired; anchor, sheet and local-gradient evidence is still needed.
Existing Phase 1C CAD/checker evidence is preserved without extending it to hot hardware.

## Fair concept comparison and shortlist

| Concept | Why retain | What could rule it out / change ranking |
| --- | --- | --- |
| A: bottom-supported lift-out cassette, positive hand cams/quarter-turns; optional magnets only for location | Separates weight from closure, limits opening swing, replaceable flat insert; floating followers can accommodate growth | Overhead brace may block lift; bottom track can trap debris; awkward two-hand grip, thermal binding or hot handles could defeat convenience |
| B: framed panel on removable hinges with positive hand latch | Door stays supported for routine access; full removal can expose service corridor | Full swing and hinge-pin withdrawal collide with roots/filament; hot or heavy door creates drop/tip risk; hinge alignment and separate anti-lift retention needed |
| C: captured-edge sliding cassette with captive hand end stop | Edges distribute load, useful where there is no door swing | Requires roughly panel-length extraction corridor; dirty tracks and expansion can jam; removable structural rail would violate conversion requirement |

A and B merit the first geometric comparison; C remains credible for a face with proven
extraction space, not as a universal wall solution. This priority is an engineering
inference about failure discrimination, not a weighted winner. Hybrid transparent/opaque
construction may reduce window size and handling mass but adds joints and expansion
interfaces. Keep glass where scratch resistance justifies handling/edge-protection costs;
keep acrylic as a transparent comparison with explicit brittle-failure concerns.

Screen out **as sole claimed solutions**: friction/magnets alone for gravity or guarding;
printed snap clips with assumed lifetime; panels relied on for frame stiffness; fixed
roof/brace removal needed for conversion; permanently attached doors advertised as
removable; tool-drive quarter-turns; interlocks simply bypassed for open-air printing.
These negative findings do not reject every use of magnets, snaps, hinges or sensors.

Qualified mechanical, electrical/thermal and safeguarding review precedes adoption.
The first physical proof remains two-bed docking and cross-seam printing. D5 completes
research documentation only; it does not end the research-first pause by itself.
