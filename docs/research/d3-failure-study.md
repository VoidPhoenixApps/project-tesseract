# D3 — load transfer, failures and proposed safe-state objectives

**Preliminary desk study, not a qualified hazard assessment, safety certification or
operating procedure.** [Mode obligations](d3-mode-constraints.md) apply in every row.
No numerical safety limits or reliability probabilities have been established.

## Support invariant and staged handoff

At every state each bed, disconnected platform and gravity-loaded head assembly needs
a defined support path capable of its forces/moments. Independent restraint must cover
failure of the switched/breakable transmission, not merely act on its input shaft.
This is a requirement to demonstrate, not a proven single-fault guarantee. Positive
hold-down may be needed when reactions become tensile. No controller command, stepper
holding torque, assumed screw self-locking or servo position substitutes for support.

| State | L support ownership | P/T and permitted conceptual change | Evidence required / failure disposition |
| --- | --- | --- | --- |
| 0 Printing/occupied | Existing local/group support, or previously qualified J platform | Existing motion owner; no reconfiguration | Actual plane/relative position, locks, occupied volumes and restraint monitored; group fault arrest as below |
| 1 Prepare affected group | Existing support retained; destination platform independently retained too | Verify affected modules clear; reconcile unaffected object/harness sweeps; empty modules may return to datum before horizontal conversion | No motion to recover datum with occupied affected modules; no inference of empty from a queue alone |
| 2 Retained at datum | Local support plus independent retention; compatible compliance where needed | Halt relative motion; unload relevant drive torque; horizontal translation stays at Z=0 | Actual output pose, gravity support, stored belt/shaft energy and isolation verified; stop if uncertain |
| 3 Dock P | Continuous horizontal transport/local support owns weight | Only assigned planar freedoms released; seat cold datums and verify P | Cross/locks must have horizontal capture/release at unchanged datum; no lifting onto tapered seats |
| 4 Engage new L | Old L still capable; new positive load joints engage without being forced to carry an unknown mismatch | Keep both supports, but do not impose conflicting rigid Z references | Direct lock state plus compatible reaction/preload/load evidence; switch signal alone cannot prove load acceptance |
| 5 Transfer load and select T | New L gradually accepts load while old support remains available as restraint | Compatible controlled load sharing at datum; unload selector interface, align, select, retain and verify T | Full geometry/stiffness sequence unresolved. Elastic settling must be budgeted; no vertical repositioning used as a docking technique. If constant-datum transfer cannot be achieved, reject concept |
| 6 Release old ownership | New L and independent restraint carry full specified gravity/moments | Old drive disconnected or follower role established; old guides released only in specified conflicting freedoms | Actual reactions, pose, restraint and T verified before release; remaining guidance must retain required stability |
| 7 Printing eligibility | Selected group path as mode matrix | Surface/thermal readiness and whole-machine clearance verified by later procedure | Not an automatic restart after fault. All acceptance/uncertainty/abort limits still require qualified review |

Decoupling reverses **ownership**, not blindly the command order: establish local
destination supports and restraints, demonstrate load acceptance, unload and release
secondary joints, then unlock P and retreat horizontally. Do not disengage loaded teeth
or withdraw a bearing support. Normal sensor evidence cannot yet supply numerical load
acceptance: load sensing, proof methods and their failure coverage remain open design work.
The unused frame must be secured clear of the full independent bed strokes in S/R/C/M.
No retracting it through neighboring occupied structures is assumed.

## Failure modes and response objectives

| Initiator / affected state | Mechanical consequence | Required observation or prevention to investigate | Proposed safe state and recovery boundary |
| --- | --- | --- | --- |
| Incomplete P/L engagement, states 3–6 | False ready; carrier shifts/tips when old support releases | Separate P seat, actual L retention and support/pose evidence; avoid common command-derived signals | Keep old support and gravity restraints; inhibit transfer; inspect debris/misalignment without force escalation |
| Wrong phase/partial T engagement | Tooth loading, torque loss or sudden seam displacement | Unloaded supported alignment, full-depth/retained position, output phase plausibility | No drive torque through partial engagement; retain loads, isolate interface, no blind retry |
| Lost steps, motor stall or belt tooth jump during grouped print | One bed deviates, tears adhered part, overloads guide/link | Downstream actual carrier pose and tilt; relative trajectory residuals with bounded latency | Coherent arrest of mechanically connected group, independent restraints; do not continue good axes into stalled one |
| Belt/shaft fracture | Local or common frame falls despite upstream motor brake | Restraint downstream/independent of failed element; inspection and fault-load analysis | Catch/hold within separately justified displacement and force envelope; inspect full load chain before any motion |
| Power loss during selector travel | Belt slack, neutral clutch or active lock release | Passive retained L and independent platform restraint across entire q, including intermediate states | No gravity release on power removal; heater energy isolation through separately reviewed protection; power return leaves restart inhibited |
| Sensor disagreement, stale data, loss of communications | Incorrect membership/pose or hidden half-engagement | Independent observations, freshness and plausibility; motor encoder alone misses downstream faults | Unknown is not engaged; hold supported state, stop required collision/load domain, reconcile physical state before recovery |
| Skew, guide bind, cross thermal distortion | Force loop, lift stall, stored strain releases abruptly | Plane observations, force/load estimates, released freedoms and stiffness/thermal model | Stop rather than increase force; never force loaded joint release; supervised supported recovery |
| Platform not isolated in partial modes | Unexpected cross-group Z constraint or impact | Detachment/park/clearance evidence including full guides, brakes and cables | Inhibit partial mode; do not drag isolated frame or pause unrelated jobs indefinitely as a workaround |
| Lock sensor true but contact unloaded/uplift | Plane loses support under eccentric part or clamp moment | Positive reaction/retention analysis; sensor cannot establish capacity | Retain hold-down/support independent of drive; revise support polygon or reviewed lock capability |
| Heater wiring snag, thermistor or heater fault | Tug changes seam/guide load; electrical/thermal hazard | Full XYZ/selector harness paths, strain relief, temperature/current ratings and fault detection | Reviewed hazardous-energy isolation while preserving mechanical restraint and justified cooling; no energization in this task |
| Active object on nominally unaffected bed | Mid-path collision or shared-frame deflection shifts a running print | Actual occupied/swept volumes, frame compliance and unchanged local support/reference | Reject transition if isolation cannot be proven. A fault may require wider stop; normal operation must still support independent progression |
| E-stop/service/restart | Motor power removal permits drop; stored gravity/tension remains | Independent retention, energy-specific isolation, positive service supports, restart state reconciliation | No automatic unlock/rehome/reheat; maintain support and prohibit service motion. Removable panels are not isolation devices |

Fault domain is at least the connected mechanical group; shared beams/frame/power can
require a wider stop. Preserving unaffected jobs is subordinate to actual fault safety,
but cannot be used to waive normal independent progress. Asymmetric catches can themselves
twist a rigidly linked pair; load sharing, arrest timing and linked-object damage need review.

## Quantitative implications and remaining gates

The [arrest model](d3-calculations.md) includes existing downward velocity, free-fall delay
and finite stopping stroke. Its energy-average force is a lower-order sizing input, not
peak force or a certified stop. Detection alone does not prevent displacement. A catch
that protects a person may still ruin a seam-spanning print; separate injury-prevention,
equipment-protection and print-quality limits are needed.

Before a physical procedure: qualified mechanical/controls/thermal-electrical review,
reviewed operating envelope, measured uncertainty, limits for pose/skew/lock engagement,
load/temperature/velocity, restraint capacity and stopping behavior, explicit abort
criteria, supervision and retained raw data. Review power-loss/fault recovery and service
states as well as normal printing. No physical procedure or safety integrity level is
approved here; the separately reviewed two-bed seam proof remains first.
