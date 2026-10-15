# D5 — next investigations and unresolved decisions

[Study](d5-engineering-study.md) · [safety](d5-safety.md) · [dependencies](d5-references.md).
Priority is based on which uncertainty can invalidate an enclosure concept earliest.
Nothing below authorizes CAD continuation, fabrication, purchases or physical testing.
The first physical machine proof remains **two-bed docking and cross-seam printing**;
enclosure work must not replace it with an unreviewed four-bed build.

## Ordered evidence proposals

| Priority / question | Smallest useful next investigation | Required evidence and decision gate |
| --- | --- | --- |
| P0 hazard-specific risk allocation | Distinguish ordinary open-air printing, docking, panel conversion, actual guard access and maintenance; retain all eight operating modes | Document exposure, severity, likelihood and residual risk; justify protective functions for closing gaps, falling loads, electrical/heater faults and unexpected motion. No automatic panel interlock or blanket guarding requirement; preserve necessary protections |
| P0 complete envelope | After geometry authorization, compare lift-out and removable-hinge cassettes against one perimeter-root and one stacked-bridge candidate, plus D3 underbody lift paths | Exact approved component references; full normal/park/fault/service sweeps, uncertainty and occupied-job constraints. No “fits the box” result substitutes for D2's unresolved reach |
| P1 thermal operating requirements | Maintainer defines proposed materials/recipes, ambient and duty cases for review; estimate source power and a multi-node passive model | Temperature limits for every actual component, separate fault loads, heat-loss uncertainty and localized thermal map plan. Active heating/filtration/exhaust require separate decisions |
| P1 material and retention coupons, later only | Compare exact sheet grades, support/retainer/gasket stack and printed boss in both structural variants under reviewed loading | Force/displacement, engagement, edge damage, clamp relaxation and retained capture over hot/cold/dirty repeated cycles; no universal cycle count/force limit invented |
| P1 service mock-up, later only | Compare mass/grip/swing/extraction for each face including roof, storage and reverse insertion | Task completion without tools for conversion or dismantling primary systems; reach/visibility and supported final release; record failures and user variability |
| P2 thermal/frame integration, later only | Instrument corners, roof/base, printed roots, reinforcement, motors, wiring/connectors and protected electronics | Repeated heat/cool histories, gradients, retention force and relative head/bed datum drift; no uniform-air assumption or extrapolation from HDT |
| P2 fault and recovery evidence, later only | Qualified supervised protective-function tests on a bounded rig before integrated machinery | Failed/stuck sensors, missing latch, lost power, heater fault simulation, interruption/restart and stored energy; hazardous faults cannot be improvised on live printer |
| P3 reproducibility | Compare generated imperial/metric adapters and eventual2020 adaptation with a second builder | Exact stock/grade/tolerances, Ender print envelopes/process, separate named outputs/BOMs; no reaming, scaling or undocumented shims |

## What a future physical test authorization must contain

Before any test, specify design revision, exact materials/stock and aging state, sample
and cycle counts, load/temperature/environment history, fixtures and calibration,
supervision, PPE/guarding appropriate to reviewed hazards, safe procedure and isolation.
Set numerical acceptance and abort limits **before** operation. A useful proposal records:

- Retention: maximum service and credible fault load with justified margin; maximum
  release/installation force; minimum retained overlap; permitted permanent set and
  wear; measurement uncertainty and an appropriate guard band. Partial engagement must
  fail the acceptance check, not be counted as a successful cycle.
- Geometry: clearance budget containing fabrication/alignment/thermal/deflection and
  stop-state uncertainties; complete panel/hand reverse paths. Zero nominal overlap
  is not sufficient, and a fixed 2 mm software reserve is not the engineering budget.
- Temperature: component-specific continuous and transient limits, sensor uncertainty,
  spatial hot-spot coverage, stable-state criterion and cooldown conditions. Abort on
  unexpected rise, failed sensing, deformation, odor/smoke, loose retention or unsafe
  wiring; exact thresholds and response require qualified review.
- Frame/creep: allowable relative datum error allocated from seam/print needs, residual
  deformation and retained preload after specified duration/cycles; test both stock
  variants without panel stiffness credit.
- Safety: measured access/stop times, support preservation and inhibited unexpected
  restart; any uncontained fault, loss of support/protection or unexpected motion aborts.

Record raw data, uncertainty, failures, repeatability and review outcome. Plans with
unresolved thresholds are not ready to execute. These proposals intentionally do not
invent printer performance tolerances or describe unsafe hardware fault-injection steps.

## Maintainer decisions still open

1. Proposed operating recipes, ambient range, handling expectations and panel-change
   timing; whether changes wait for print completion/cooling. Automatic bed reconfiguration
   must remain possible with panels installed and affected beds clear.
2. Which architecture candidates deserve the next bounded geometry study; no final motion,
   frame or enclosure selected by D5. Any proposed protective barrier, sensor or interlock needs a documented hazard-specific risk basis; environmental-panel absence alone requires none.
3. Candidate exact material grades, sheet/cassette sizes and sourcing regions for quotes;
   relative importance of visibility, weight, scratches and replacement effort. No budget
   or procurement selected here.
4. Thermal/emissions control scope, including any future exhaust/filtration or active-heating
   proposal, with qualified review. No system is approved implicitly by the enclosure goal.
5. Approved model folder/catalog and exact-part rights before purchased-component CAD.
   Fusion remains a preference, not a selected/reproducible public toolchain.
6. Review ownership and quantitative acceptance budgets before trials. Licensing remains
   separate; no third-party model or material brochure establishes an open-source grant.

After accepted research/merge, separately authorized project-knowledge work could create
or link a concise Tesseract record to the owning research documents. No existing project
record was found; do not invent one as already present. Home Infrastructure already links
the design authority. Neither repository was modified; useful D5 facts are recorded here,
so no duplicate AgentMemory save is necessary.
