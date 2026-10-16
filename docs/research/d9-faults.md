# D9 — transfers and analytical fault challenges

[Contract](d9-contract.md) · [calculations](d9-calculations.md).
**Research falsification map, not an approved test or operating procedure.** No
probability, protective performance level, fault-force rating or safe limit is assigned.

## Affected groups and transition obligations

An affected bed is any bed whose group, pose, support path or reference changes,
including transitive structural/cable influence. Finished/cancelled objects remain
occupied. A change in group membership is a minimum affected set, never a complete
mechanical influence proof. [The model](d9_support.py) expands this set using supplied
influence edges; unknown physical influence prevents claiming an unaffected neighbor.

| Transition, both directions | Minimum affected beds | Neighbor obligations / exclusion witness |
| --- | --- | --- |
| S ↔ M12, M34, M13, M24 | Nominated pair | Other two retain P/L/R and actual pose throughout, with unchanged cables and bounded shared-frame disturbance. S→M12 with a shared 2–3 datum affects bed 3 too, even if bed 3 has zero commanded displacement |
| M12/M34 ↔ R | Other row | Existing row pair may continue only with independent support/reference and clear route; shared lifting platform invalidates that claim |
| M13/M24 ↔ C | Other column | Same obligation in orthogonal orientation; rotated bookkeeping does not establish rotated guide/cable feasibility |
| R ↔ C | All four | Every bed changes group. All must be clear; supported separation to singles may be a conceptual route, not a proven trajectory |
| Row mixed ↔ column mixed | Three beds in the union of the old/new pairs; fourth may be added by physical influence | For M12↔M13, beds 1/2/3 are affected; bed 4 stays outside membership closure only. Shared reference/support may still affect it; intermediate capture needs its own audit |
| Partial ↔ J | All four | Unified frame or joined group changes all support/influence domains. Retained finished objects block conversion |

All eight partitions and all 64 ordered mode pairs (including no-op) receive an
abstract membership-closure check. This is not proof of the 56 distinct physical
routes. Head park transfers also affect occupied volumes/supports and need clearance;
head movement into its supported park is not permission to move occupied beds.

## Constant-datum support handoff

This table applies to F/C J transfer and to any B station-guide transfer introduced
by horizontal conversion. E-sync that carries its entire lift horizontally may avoid
one handoff, but increases translating mass and swept volume. H still needs continuous
station/transport support through horizontal docking. All candidate transitions must
stay at the fixed reconfiguration datum; no vertical landing onto a tapered seat.

| State | P / T status | L and R owner | O / transition gate |
| --- | --- | --- | --- |
| 0 reserve and clear | Existing P/T; affected objects confirmed removed | Existing support and independent restraint, destination platform retained separately | Verify occupancy, influence domain and complete route; no blind homing of occupied modules |
| 1 approach at datum | Supported empty assembly returns to datum before horizontal conversion; T stopped/unloaded as appropriate | Existing L/R continuous over approach, not just at endpoints | Actual pose and retained energy known; destination compatibility established |
| 2 seat P / engage receiving L | Horizontal cold datum seating; selector torque inhibited | Old L remains capable; new support captured, not yet credited with load acceptance | Distinct P, positive engagement and downstream pose evidence; half-engaged means unknown |
| 3 compatible overlap | T isolated/aligned; specified follower freedoms released only while stability retained | Old/new supports coexist with controlled load sharing and R available | Measure reactions and settling; no incompatible hard-guide closure; new support demonstrates load acceptance before release |
| 4 transfer ownership | Selected full T path verified; unused torque isolated | Receiving L/R carries full specified force/moment; old path released only after state 3 evidence | Actual pose/load and restraint verified; release cannot be justified by command bits alone |
| 5 print eligibility | New P/T configuration, plane and thermal calibration | All loads, including unused platform and parked heads, remain supported/restrained | Fresh consistent downstream state and reviewed clearance; fault reset never automatically restarts |

Reverse transfer establishes local receiving supports and restraints **before** unloading
and releasing platform/tie joints. It does not reverse the actuator commands blindly.
Loaded teeth/catches may not release cleanly; stored strain can snap the assembly out of
position. If compatible load transfer requires deliberate vertical bed repositioning
during conversion, that implementation fails the fixed-height contract. Elastic settling
must be measured against future approved limits; D9 assigns no allowable datum drift.

The executable checker rejects unsupported states, missing R, incompatible overlap,
unobserved states, off-datum conversion, torque through partial selectors and releasing
old support without prior observed load-accepted overlap. Its booleans are hypothetical
evidence assertions, not implemented sensors. It samples declared states only; it cannot
prove continuity between them, discover an omitted load or prevent a real drop.

## Fault falsification ledger

In each row, retain physical loads and inhibit unsafe continuation in the full influence
domain. Mechanical coupling, shared frame/power or uncertain fault extent can require a
wider stop than the logical job. No fault response here is an executed injection.

| Initiator / counterexample | H versus B consequence | Evidence / proposed containment obligation | Classification and remaining limit |
| --- | --- | --- | --- |
| Power loss or stopped motor | H head/column can descend, including parked head; B bed or entire group can descend with hot object | Load-side passive retention or independently justified restraint; analyze undervoltage sequencing and heater/cooling disposition | Upstream torque alone fails stated fault; real restraint behavior unresolved |
| Belt tooth jump, broken belt/shaft, skipped steps | H nozzle error/drop; B relative bed step and joined-object load transfer | Observe actual downstream pose; R bypasses broken element; no continued motion of good axes against failed one | Motor encoder may remain correct while output fails; excludes encoder-only claim |
| Brake/catch disabled, detached or failed | One H column or B bed lacks credited backup; caught linked bed may twist partner | Map second path and anchors, detect unavailable restraint before admission, assess fault combinations and service support | Two named devices sharing a printed anchor are not independent; no universal single-fault guarantee |
| Stale sensor, replayed epoch or sensor disagreement | Hidden motion/half-engagement in either candidate | Downstream freshness, clock/epoch integrity, diversity and plausibility; unknown inhibits release/start and latches running fault | Software freshness tests cannot detect a sensor frozen with fresh timestamps; physical diagnostics missing |
| Partial selector or two drive owners | H optional transfer/park or F platform can lose torque or fight; B T-link can jump phase | Supports retained with torque inhibited until engagement/load/phase proven; no blind retry | Commanded selector position is not engagement or load capacity |
| Old support released before receiving support accepts load | Any support handoff can fall despite valid endpoint graphs | Continuous L/R, verified compatible overlap, load acceptance prior to release | Excludes the proposed sequence, not all handoffs; no actual transfer geometry |
| Redundant hard guides bind | H guide/root misalignment stores strain; B tied lifts fight across seam | Full six-DOF constraints, actual stiffness/preload/clearance and forces over stroke | D3 loop force is sensitivity, not actual bearing force; increasing motor force is not a remedy |
| Skew / asymmetric catch timing | H nozzle tilts/sweeps even if held vertically; B one bed arrests before neighbor, twisting seam and object | Pose/tilt and stop trajectories on both sides, moment-rated anchors, whole group fault envelope | R may prevent a fall but still destroy print or violate clearance; coupled dynamic response unknown |
| Off-center object / unilateral uplift | H extended arm loads root/feet; B COM leaves support polygon | Signed reaction/contact audit, hold-down and overturning evidence | Negative compression reaction excludes assumed maintained contact; actual load/geometry unmeasured |
| Filament drag, retained heater cable or strain-relief snag | H feed/harness adds torque through long column; B hot cable adds lift load and may conduct fault current | Measure force vs position/temperature, full loaded bend path, break/short behavior and independent electrical protection | Ignoring cable force or assigning omitted harness zero volume invalidates a claimed bound |
| Seam Z step/tilt with center probe unchanged | H stationary hot beds still bow; B adds output phase/skew and catching discontinuity | Both seam ends, interior shape and J center, actual sheet observations, uncertainty/covariance | One center observation cannot bound plane rotation or local sheet deformation |
| Common printed root/heat exposure or shared supply fails | H primary and catch anchors fail together; B several restraints/control observations lost at once | Dependency graph to foundation and energy sources; thermal creep and fault-load evidence | Synthetic common-root removal eliminates all credited paths; real independence remains unproved |
| Reset/service with retained object | H blind rehome strikes object; B return-to-datum moves occupied load | Deliberate supported recovery with actual object/pose knowledge; isolate stored energy for service | No automatic restart on restored power, cleared switch or panel replacement |

## Cross-system limits and next evidence

D8's B benefit assumes b_i=−h_g and retained finished depth. A failed lift violates
that coordinate relation and can raise a foreign object's relative intrusion or tilt
its edge. H must likewise include falling/tilting columns in parked and low-head
neighbor routes. D8's normal-motion boxes contain neither dynamic fault envelope.
D4's printed-root compliance, joint slip, thermal creep and foundation overturning
apply to normal and catch loads. Environmental panels cannot close missing structural
paths; panel absence alone is not a stop/interlock condition. Hazard-specific guards,
if justified, need separately allocated functions in both operating configurations.

Priority uncertainty is actual support/guide/retention geometry and measured stiffness,
not a larger simulation count. The [review packet](d9-review-packet.md) identifies the
smallest next comparison without authorizing construction or operation.
