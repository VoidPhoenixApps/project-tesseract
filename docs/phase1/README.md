# Phase 1 — mechanical architecture trade study

**2026-10-12 · Proposal for review.** Analytical exploration only: no CAD, simulation, physical measurement, architecture approval, or engineering gate completion. The first physical proof remains two-bed docking and cross-seam printing. This study does not authorize fabrication, purchases, heaters, machine motion, firmware changes, or unattended operation.

## Reading order and authority

| Document | Owns |
| --- | --- |
| [Motion architectures](motion-architectures.md) | Mechanisms, load paths, comparative assessment and ranked investigations |
| [Configuration feasibility](configuration-feasibility.md) | Top views, coordinates, transition paths, clearance assumptions and concurrency limits |
| [Docking and registration](docking-registration.md) | Six-degree-of-freedom constraint allocation, thermal accommodation, locks and recovery |
| [Preliminary calculations](preliminary-calculations.md) | Inputs, equations, sensitivity, stock examples and reproducibility |
| [Risks and review decisions](risks-and-decisions.md) | Failure register, unresolved choices and requirement coverage |
| [Two-bed proof plan](two-bed-proof-plan.md) | Proposed experiments, metrology, candidate limits and safety prerequisites |
| [References](references.md) | Primary technical sources, provenance and evidence limits |
| [Verification record](verification.md) | Checks performed, independent desk-review scope and unavailable evidence |

The unchanged [requirements](../requirements.md) govern this work. The [architecture](../architecture.md) and [roadmap](../roadmap.md) retain their open decisions and gates. Analysis baseline: Project Tesseract GitHub `main` at `716834a501c3217f192417bac85600d6302c2316`, fetched and matched to a clean checkout on 2026-10-12. Shared standards and workflow were read from project-knowledge at `46ff107e35053b970915a3ca147f5513571f7be6`, matching its GitHub `main`; no Tesseract project record exists in that inspected checkout. Current Home Infrastructure instructions were consulted read-only. Neither supporting repository was changed. AgentMemory was unavailable.

## Principal findings

1. **Investigate independent quadrant XY carriers with frame-referenced docking first.** This is a comparison baseline, not a selected machine. Each empty bed can follow a short axis-aligned path without commanding a busy neighbor. Precision at temperature, frame disturbance and head clearance remain unproved.
2. **Separate transport, cold carrier registration and hot plate expansion.** Accurate docking of a carrier does not guarantee sheet seam height, edge position or adhesion. A precision latch cannot flatten a thermally warped sheet safely by assumption.
3. **Shared rows can reach paired modes cheaply but couple job availability.** A compact six-axis row mechanism cannot reproduce the canonical vertical-pair-plus-singles layout. Wider staggered parking can recover that mode at considerable travel and workspace cost. Independent Y trims recover the compact layout but approach XY-stage complexity.
4. **Uniform lattices and the screened outer-pivot swings fail mandatory layouts.** Additional selectively independent motion can repair them; the added joints, constraints and support paths then need evaluation as new mechanisms.
5. **A two-bed fixture should compare docking interfaces before committing to four-bed transport.** Begin with cold registration, then reviewed hot/differential tests, then supervised seam printing. Four-bed closure and concurrent-job vibration remain separate subsequent proofs.

Evidence confidence is high for the stated degree-of-freedom limitations and elementary calculations under their assumptions, medium for conditional transport plausibility, and low for achieved accuracy, reliability, cost and thermal print performance. No candidate has demonstrated all machine requirements physically.

## Review boundaries

Recommendations rank the next investigations. They do not select final motion, printing Z, toolheads, CAD, reinforcement, controllers, firmware, suppliers or license. Four-head cooperation on one object remains an unproven stretch goal. All nominal areas remain nominal; sheet margins, thermal gaps and head access determine eventual usable regions. Documentation checks and any independent desk review cannot approve physical operation.
