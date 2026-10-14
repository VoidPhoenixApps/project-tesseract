# Research-first architecture phase — public plan

**Recorded:** 2026-10-14. **Maintainer direction:** Prioritize research and comparison of **all current Project Tesseract architecture concepts before undertaking further detailed CAD development**. This work is deferred until the maintainer has time. The community should be able to see the research, alternatives, evidence and reasoning, not just a finished CAD outcome.

**Status:** Planning direction, not completed research or an approved mechanism. Nothing here selects hardware, software, CAD, printer configuration, numerical acceptance limits, or a license. Existing Phase 1/1B/1C source, evidence and unfinished work must be retained; do not silently discard earlier CAD or rewrite its conclusions. No physical work is authorized by this plan.

## Why the order changes

Independent toolhead movement, Z ownership, coupled/selected lifts, bed docking and registration, frame compliance and safety are coupled decisions. More fixture or printer CAD now could prematurely embody one architecture and hide contradictions with the required separated, paired, mixed and fully joined configurations.

Use existing [requirements](requirements.md), [architecture](architecture.md), [roadmap](roadmap.md), [Phase 1](phase1/README.md), [Phase 1B](phase1b/README.md), [Phase 1C](phase1c/README.md) and [detailed toolhead/Z concept backlog](concepts/toolhead-z-motion-exploration.md) as the starting evidence. These records vary in evidence strength and do **not** establish a validated printer.

## Scope to research before new detailed CAD

| Track | Questions to answer and public output |
| --- | --- |
| Bed travel and mode changes | Compare independent XY carriers, row mechanisms and other viable transport paths; demonstrate feasible and infeasible arrangements/transition sequences for all five required layouts in conceptual kinematic diagrams |
| Registration, docking and seams | Study 6-DOF constraints, hot/cold references, thermal expansion, four-sheet seams, load transfer, horizontal-only docking and repeatability; preserve the quantitative negative results and assumptions from Phase 1/1B |
| Printing Z | Compare gantry/head Z, individual bed Z, dual-Z handoff, short-stroke hybrid head Z, automatically coupled bed Z and servo/belt-switched secondary lift; explain mode-specific actuation, positive support, homing, failure modes and intermediate pair/mixed modes |
| Toolhead XY and packaging | Compare independent gantries, shared motion rails with truly independent carriers, four local plus full-region head, modular systems and the precise mirrored A/B/B/A toolhead orientation; evaluate true nozzle reach, full swept collision envelopes, parked heads and unrelated Z progress |
| Structural systems | Compare printable-frame load paths, stiffness/creep/vibration, Ender 3 print envelope, actually sourceable imperial/metric reinforcement stock and later 2020 adaptation; avoid assuming dimensional interchangeability |
| Convertible enclosure | Study tool-free panel interfaces, frame/heat/motion clearances, removal/service paths, passive chamber environment, ventilation and thermal/electrical risks; no active chamber heating is approved |
| Motion electronics, firmware and scheduling | Assess independently scheduled jobs, coupled-group state transitions, sensors/locks, safe reconfiguration, heating/power, fail-safe behavior and controller feasibility without assuming an existing slicer or Klipper solves coordination |
| Reproducibility and manufacturability | Evaluate standard/obtainable components, serviceability, accurate sourcing, BOM complexity, editable parametric sources and a publicly reproducible CAD path without requiring paid/proprietary tools |

**Scope guard:** Four nominal 180 × 180 mm modules with retained individual build sheets, automatic horizontal rearrangement at a common fixed-height reconfiguration plane, all separated/paired/mixed/joined modes, printable-first and both reinforcement standards, later 2020 edition and removable enclosure remain approved targets. Four-head cooperation on one large object remains an **unproven separate stretch goal**, not a prerequisite for baseline joined-area coverage.

## Work sequence when research resumes

1. **Inventory and evidence map:** Link existing calculations, negative findings, concept notes and unresolved assumptions. Mark each item as requirement, hypothesis, analytical result, independent review or measured evidence. Do not redo work that is already reproducible unless checking a discrepancy.
2. **Public architecture matrix:** Make one traceable matrix crossing XY-A–E with Z-A–F against the five mandatory layout types. Separate mechanically impossible combinations from plausible-but-unproven ones. Identify active-object protection, collision and load-transfer constraints.
3. **Bounded research per candidate:** Use dated primary references, clear mechanisms, source/license information, parameterized estimates, loading/DOF diagrams and explicit uncertainty. Report both strong and weak arguments, not just a favored layout.
4. **Integrated comparisons:** Rank a small shortlist against all targets, safety/complexity/reproducibility and failure cases. Include simpler baselines. Record eliminated candidates, circumstances where rankings change, and serious dissent.
5. **Review before CAD continuation:** Request suitable independent mechanical/electrical/safety critique. Publish open questions and measurable test proposals. The maintainer reviews the trade study before authorizing further detailed architecture CAD. After review, resume **bounded** CAD needed to discriminate remaining candidates rather than committing to a full-machine model.
6. **Physical evidence remains subsequent:** The first physical proof is still the reviewed two-bed docking and cross-seam rig. Require reviewed hazards, explicit acceptance/abort criteria, measurement uncertainty, supervision and recorded failures before operating any prototype.

### What the public should see

Every completed research track should have a **readable public summary** in GitHub (with a stable link), plus its underlying source citations and reproducible calculations/figures where useful:

- Plain-English question, why it matters to builders and the required printing modes.
- Clear **labeled diagrams** (top/side views, mechanism and motion/clearance sketches), with editable source when created; conceptual art never presented as proof.
- Side-by-side alternatives showing advantages, liabilities, sourceable components, likely failure points and what remains unknown.
- Actual references, revisions/dates, assumptions, units, numerical sensitivity/ranges and code or formulas sufficient for reproduction.
- Decision and verification status: proposed, screened out with rationale, unresolved, independently reviewed or physically measured. Preserve failed or inconclusive approaches.
- An invitation to challenge assumptions or contribute better evidence through [GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions); keep reviewed conclusions in GitHub, using Discord for conversation and meaningful factual updates.

Do **not** describe publication, a PR, an animation or successful software checks as evidence that a mechanical design works. Publish milestones only when meaningful; the established Discord reporting workflow is not a mandate to announce every exploratory note.

## Exit condition for the research-first pause

New detailed printer/fixture CAD should resume only after a reviewed research package identifies:
- Requirements traceability for every mandatory mode and the current constraints/risks.
- A reasoned short list of *integrated* bed/head/Z/structure approaches, with showstoppers and uncertainties called out.
- Preliminary reproducible estimates for thermal drift, seam registration, lift loads, swept head coverage, collisions and safety-related faults appropriate to the proposed CAD scope.
- A prioritized list of narrow CAD experiments needed to resolve remaining uncertainty, plus the evidence each experiment must produce.

These are **planning/review criteria**, not assertions that research has been performed or physical engineering gates passed. The maintainer can authorize a specific exception, such as preserving, diagnosing or finishing an existing narrow CAD/evidence artifact, without treating it as approval for a new mechanical architecture.

**Resumption prompt:** Start at the existing concept backlog and Phase 1/1B/1C evidence. Produce the public mode × XY × Z compatibility matrix and an evidence inventory first. No new detailed CAD or hardware actions until the maintainer explicitly requests them.
