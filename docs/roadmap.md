# Project Tesseract roadmap

**Status:** Foundation documentation only. No engineering gate below has passed, and no CAD or prototype has been validated. Phases are a proposed sequence, not delivery dates or a commitment to unproven performance.

The [requirements](requirements.md) govern scope; [architecture](architecture.md) records alternatives and open decisions. Four-head cooperative printing is a separate stretch track. A failed gate leads to investigation and review, not an unsupported claim or silent removal of a requirement.

## Evidence required at every gate

Before testing, review the procedure and measurable pass/fail limits: units, operating conditions, samples/cycle counts, measurement method, instrument resolution/uncertainty, hazards, controls, and abort criteria. Numerical limits are not established by this foundation. They must be justified against first-layer, structural, thermal, motion, and safety needs before a test is labeled passing.

Record the design/source revision, stock standard, materials, hardware and software configuration, calibration, raw measurements, photos/logs where useful, observed failures, repeatability, and comparison with acceptance limits. Distinguish calculations, simulation, bench measurements, and integrated-machine results. State which configurations and temperatures were actually tested; do not generalize beyond them.

A passing result requires reviewable measurements and review against the agreed criteria. Failed and inconclusive tests remain part of the history. A changed load-bearing part, stock substitution, material, wiring arrangement, control behavior, or frame edition requires impact assessment and relevant revalidation.

## Phases and engineering gates

| Phase | Work and deliverables | Exit evidence |
| --- | --- | --- |
| 0 — Requirements foundation | Preserve the approved brief, classify targets/candidates/unknowns, establish contribution and safety rules | Reviewed foundation and requirement coverage; authority/link handoff to source repositories handled separately after review |
| 1 — Trade study and test planning | Compare bed docking, head reach, printable-frame load paths, reinforcement families, and kinematic constraints; define the Ender 3 envelope and staged test plan | Reviewed alternatives and risk register; measurable test criteria and safe prototype plan; no premature final-machine selection |
| 2 — First physical proof | Build a bounded **two-bed docking and cross-seam test rig** using retained individual sheets; choose only the reviewed components needed for the rig | Repeated dock/undock X/Y/Z registration, seam gap/step, thermal drift and first-layer measurements; a test object spanning the seam with reliable adhesion and safe nozzle transit |
| 3 — Printable-frame and four-bed development | Use the proof to revise concepts, develop native editable CAD and a staged BOM, build Ender 3-sized structural parts and both reinforcement options, expand bed travel | Measured structural performance and demonstrated separated, row-paired, column-paired, mixed, and joined layouts with locks, sensing, homing, safe wiring and no interference |
| 4 — Baseline print-system integration | Review electronics/firmware, integrate head motion, calibration and job-aware configuration for the required modes | Verified reachable print volumes, parking/collision envelopes, protected running jobs, job rejection, heater/stop/fault behavior and measured printing performance across required layouts |
| 5 — Reproducible printable-edition release | Complete both stock-standard packages, assembly/calibration/maintenance instructions, tested BOM alternatives and known limitations; resolve licensing through review | Independent builder reproduction using an ordinary Ender 3 and documented stock; all applicable gates passed for both variants, editable source/export reproducibility, and approved licensing before an open-source release claim |
| 6 — 2020 extrusion adaptation | Adapt the validated printable design, retaining common interfaces and costly components where practical | Revalidated frame/joints, safety and all core modes; documented upgrade path and reproducible build. No automatic equivalence claim |

Safety review is a prerequisite to each energized or moving experiment, beginning with the two-bed rig. Phase 4 integrates and broadens those checks; it does not defer them until then. Full-machine electronics, firmware details, suppliers and budget remain open until the relevant reviews. Rig choices must not silently become final-machine decisions.

## Required gate coverage

These seven gates preserve the approved brief's engineering obligations and apply to the relevant phases and editions.

1. **Bed seam proof:** Repeated X/Y/Z registration of two moving heated nominal 180 mm surfaces; measure thermal drift, seam gap and first-layer/adhesion performance, then print across the seam after repeated docking cycles. A small underside seam mark is acceptable; unreliable adhesion or unsafe nozzle transit is not.
2. **Bed mechanism:** Demonstrate all required arrangements and transitions without interference; verify constrained motion, positive locks and detection, homing, cable strain relief, heat-safe routing and flex behavior.
3. **Structural stiffness:** Calculate and measure deflection, torsion, vibration, creep, joint strength and dimensional drift. Validate both imperial and metric printable/reinforced variants and separately validate the extrusion edition. Include strength-critical substitutions.
4. **Head workspace:** Verify actual reachable volumes, parking, collision envelopes, service access, coordination and real-time requirements. Demonstrate concurrent independent jobs appropriate to each required arrangement; do not use nominal rectangles as proof of reach.
5. **Safety:** Demonstrate service-motion prevention, no automatic repositioning into objects, safe heater control, emergency-stop and stop-state behavior, failed-sensor/failed-lock interlocks, wiring thermal limits and fault recovery. Use supervised validation before any unattended operation claim.
6. **Software:** Prove configuration/scheduling uses real object footprints and actual machine state, protects running jobs, requires clear modules for rearrangement, and rejects unsafe/impossible jobs. Cooperative large-part printing requires its own evidence.
7. **Reproducibility:** Have another builder print the complete printable set on an ordinary Ender 3, source documented stock, assemble, calibrate and maintain a working machine. Supply native editable parametric source, derivative outputs and complete build information; record deviations and failures.

## Optional stretch track — cooperative printing

Only pursue four heads contributing to one large object as a separately reviewed experiment with path partitioning, synchronization, collision and failure-recovery evidence. It is unproven and must not hold the baseline hostage or be advertised as implemented. A single head covering the joined region remains a candidate strategy, subject to the same baseline requirements and review.

## Release and handoff discipline

Do not label a mechanism validated, a stock variant released, or the machine safe based only on CAD appearance, simulation, a single favorable trial, or green documentation checks. Publish operating limits and known failure modes with the evidence. Resolve licensing explicitly before presenting the repository as distributed under an open-source license.

After foundation review, update the original Home Infrastructure concept's authority/link statement and the narrowest appropriate project-knowledge entry in separate authorized work. Neither source repository is changed by this foundation PR.
