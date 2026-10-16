# D9 — Z-motion support, load transfer and fault falsification

**2026-10-16 · Research only · [issue #43](https://github.com/VoidPhoenixApps/project-tesseract/issues/43).**
Neither moving heads nor moving beds has a demonstrated gravity-support solution.
D9 finds specific ways to reject incomplete proposals, and defines the evidence
needed to compare the remaining ones. It selects no machine architecture and does
not lift the research-first CAD pause.

Moving the heads in Z keeps the hot beds stationary during printing, simplifying
bed support and avoiding synchronized bed descent across a joined print. The cost
is four full-range head lifts, long moving columns and retained parked assemblies.
Moving bed groups down can keep object tops below the head travel plane, as D8's
ideal geometry illustrates. It adds moving hot loads, differential lift errors,
full-stroke heater harnesses and more complicated support through horizontal docking.
Neither advantage removes the other candidate's obligations by assumption.

## Read the package

| Artifact | Purpose |
| --- | --- |
| [Support and mode contract](d9-contract.md) | Separate P/L/T/R/O obligations, eight height-owner partitions and alternative load paths |
| [Transitions and fault challenges](d9-faults.md) | Support handoff, occupied-neighbor protection, failure counterexamples and scope of exclusions |
| [Editable diagrams](d9-diagrams.md) | Head/bed load paths, mode graphs and handoff logic; conceptual, without dimensions |
| [Calculations](d9-calculations.md) | Reused D3 signed reactions, moment/deflection, guide and arrest sensitivities; exact limits |
| [Source](d9_support.py), [tests](test_d9_support.py), [raw results](d9-results.json) | Reproducible abstract state/graph checks and numerical examples |
| [Engineering-review and E2 packet](d9-review-packet.md) | Smallest future comparison, exact geometry dependencies, measurements and authorization gates |
| [Verification](d9-verification.md) | Checks actually run, changed files, review disposition and publication evidence |

## Findings and exclusions

| Proposition challenged | D9 disposition | What could change it |
| --- | --- | --- |
| One permanently attached rigid bed platform can provide every mode with fixed-height heads | Excluded as stated: one bed-height coordinate cannot supply S/R/C/M unrelated job progress | Independent full-range head Z or independently separable platform sections changes the topology; requires new support analysis |
| Two permanent row platforms suffice for both pair orientations | Excluded for C and arrangements that split rows under bed-Z-only progress | Selectable support sections or independent lifts, with continuous restraint and constraint compatibility |
| Motor holding torque, a motor brake or an engaged transmission proves gravity retention | Counterexample: downstream belt/shaft failure bypasses an upstream brake | Identify a retained load-side path that survives the named failure and has verified capacity/anchor integrity |
| Stronger rigid ties always improve joined-bed precision | Counterexample: redundant guides turn mismatch into internal force; compression contact can unload | Measured compliance/contact behavior and explicitly released follower freedoms without loss of moment support |
| A valid before/after support graph proves a transfer | Excluded inference: an unsupported intermediate, half-engaged catch or incompatible overlap can exist | Continuous supported trajectory, load acceptance, observed restraint and maintained datum through transfer |
| Head-Z avoids bed-Z's fault problem and therefore is preferable | Unresolved: long columns, parked head loads, common roots and reach-dependent compliance may dominate | Same endpoint nozzle-to-sheet error and fault-displacement evidence for both candidates |
| D8's lowered object tops establish B clearance | Excluded inference: under-bed lifts/catches, heater loops and fault skew were absent | Exact full-stroke/fault envelopes reconciled with retained objects and both panel states |

These exclusions apply to stated topologies or inferences, not every possible H/B
implementation. A no-error result in the abstract checker means only that supplied
assertions are internally acceptable. It proves neither strength nor spatial stability.

## Reconciliation with earlier evidence

Baseline is D8 merge `bf8a55f40e2d6ff99069950e8ddc27874cf32e9d`; all prior evidence
remains unchanged. [D8](d8-assembly-study.md) evaluated 696 baseline and 1,728
sensitivity cases. All baseline cases violate the allocated boundary; selected H/E
paths have no object events, and B's ideal object tops stay low. Those conditional
results neither condemn all perimeter stages nor establish a feasible assembly.
D9 adds support obligations; it does not recompute D8 boxes with imaginary mechanisms.

[D3](d3-engineering-study.md) owns load/support equations and selector counterexamples;
[D4](d4-load-paths.md) adds printed-root compliance, unilateral-contact and shared-anchor
risks; [D6](d6-safety.md) separates operational stop, protective functions and service
isolation; [D7](d7-integrated-study.md) supplies the integrated shortlist and E2 question.
[Phase 1](../phase1/README.md) preserves independent horizontal-carrier comparisons.
[Phase 1B](../phase1b/thermal.md) retains the center-anchor thermal-gap contradiction:
its illustrative cold interval is empty over 20–100 °C. Inward reference reduces one
normal term, not bow, sheet slip or seam tilt. [Phase 1C](../phase1c/README.md) retains
bounded CAD/check evidence, including failures and restoration; it has no demonstrated
positive retention, loaded capture, hot seam or physical fit. D9 does not promote it
to a tested support design.

## Requirements and status

All [requirements](../requirements.md) remain unchanged: four nominal 180 × 180 mm
heated modules and four retained individual sheets; automatic horizontal conversion
at the common datum; four independent, both pair, all four mixed and joined modes;
printable-frame-first development; Ender 3-compatible parts; distinct ready-to-print
imperial/metric stock interfaces without scaling or builder rework; later 2020 edition;
tool-free removable environmental panels and full open/enclosed operation; editable
parametric sources and public reproduction without mandatory paid/proprietary tools.
No exact usable area, performance, stock, controller, CAD toolchain or license is selected.
Four-head cooperation remains a separate unproven stretch goal. Environmental panels
receive no load-restraint or primary-bracing credit and no blanket removal interlock.

The first physical proof remains the separately reviewed two-bed docking and cross-seam
printing rig. D9 proposes only future bounded comparisons, with qualified mechanical
and electrical/controls review before consequential adoption. No CAD, vendor model
retrieval, installation, purchases, manufacturer contact, firmware changes or hardware
operation occurs. AI critique and passing analytical tests are not engineering signoff.
Community challenges should cite assumptions and evidence in
[GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions).
