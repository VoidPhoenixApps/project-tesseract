# D3 — bed coupling and Z load-transfer investigation

**2026-10-14, America/Chicago. Comparative desk research; no architecture selection,
physical validation or permission for CAD/hardware work.** Built on D2 reviewed head
`5957b80a5478e1cc669cbd7f81d71a5934326d63` in [Draft #26](https://github.com/VoidPhoenixApps/project-tesseract/pull/26),
which depends on D1 [Draft #25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25).
The [requirements](../requirements.md) remain authoritative and unchanged.

**Finding:** Independent monitored bed lifts are the simplest bed-side comparison;
a mechanically compatible hybrid may improve joined support but adds force loops.
A unified secondary frame cannot independently advance two pairs or a pair and singles
while rigidly carrying them all. It can coexist with partial modes only when physically
isolated from those beds, supported itself, and clear of their entire travel. Dedicated
tensioned transmissions with positive selection remove the rerouting problem, but
neither selector interpretation establishes continuous support or successful engagement.

Read the [eight-mode constraint matrix](d3-mode-constraints.md),
[selector comparison](d3-selector-study.md), [editable load/power diagrams](d3-diagrams.md),
[calculations and seam budget](d3-calculations.md), [failure and transition study](d3-failure-study.md),
[evidence/model ledger](d3-references.md), [verification](d3-verification.md) and
[plain-English summary](d3-public-summary.md).

## Evidence hierarchy and preserved findings

- **Mandatory targets:** Four nominal 180 × 180 mm heated modules, four retained sheets,
  eight explicit arrangements, unrelated job progress, automatic horizontal conversion
  at the common fixed-height datum with affected modules clear. Nominal size is not
  printable area. Printable-first/Ender 3, distinct imperial/metric interfaces, later
  2020 edition, tool-free removable enclosure and reproducible editable sources persist.
- **Analytical evidence:** Phase 1B's [cold-carrier constraints](../phase1b/docking.md)
  and [thermal analysis](../phase1b/thermal.md) remain the source of the inward-corner
  investigation and failed center-anchor gap window. Phase 1's earlier suggestion of
  a corner-reference mode conflict was narrowed by Phase 1B: permanent quadrant
  assignment permits both seam directions in the ideal uniform-expansion model.
- **CAD/checker evidence:** [Phase 1C](../phase1c/README.md) retains its source,
  runtime failures/recovery and unfinished capture/retention/load engineering. Its
  successful bounded checks do not establish docking strength or hot registration.
- **Prior research:** [D1](d1-engineering-study.md) supplies relative-Z ownership,
  lift equations and rejected oversimplifications; [D2](d2-engineering-study.md)
  leaves whole-machine XY and structural clearance unresolved. This package does not
  promote D2's hypothetical dimensions to actual hardware envelopes.
- **Proposals/unknowns:** Every mechanism below, numerical sensitivity, restraint,
  sensor, usable stroke, tolerance and operating envelope remains unselected/unmeasured.
  Four-head cooperation remains a separate stretch goal; J assumes one full-region head.

## Mechanism comparison

In D1 notation, bed-side baselines develop Z-B/E; secondary platforms develop Z-F;
the last row develops Z-C. Each row still needs D2-compatible XY, passive gravity
retention, thermal relief and measured surface readiness. “Conditional” is a kinematic
research classification, not a feasibility pass.

| Candidate | Normal load and motion ownership | All eight modes? | Benefit versus simpler baseline | Burden / negative evidence / next discriminator |
| --- | --- | --- | --- | --- |
| Four independent Z lifts with measured group synchronization | Each carrier retains its own guided lift and gravity restraint; group trajectory shared but actual surfaces observed | Conditional: 4/2/3/1 independently progressing groups | No mechanical torque selector; support remains local through docking | At least plane/tilt observations per bed, downstream slip detection, coherent group stop and bounds on latency/skew. Equal step commands or motor encoders alone insufficient; test differential compliance and lost-drive displacement |
| Positive mechanical drive coupling | A selected master drive powers phased slave lift inputs; local supports carry weight, not the shaft alone | Conditional with selectable 12/34 and 13/24 links, all mixed placements and J | Reduces commanded phase disagreement and number of independent position loops per group | Equal shaft angle does not correct unequal lead/radius, compliance, backlash or guide mismatch. Release unused drives from position fighting; phase at datum and retain independent restraint downstream of breakable transmission |
| Structurally linked carriers, separate Z drives | Cold ties carry specified moments/load redistribution; separate actuators act on linked structure | Conditional, but unrelieved rigid-guide version rejected | Can suppress some differential displacement and share a failed lift's load if actually sized | Independent stiff position servos plus rigid link can fight. Needs compatible guide freedoms and force-sharing, joint stiffness, preload and overload limits; neither simple linking nor extra motor torque cures binding |
| Hybrid structural coupling and monitored drives | Group master defines pose; compliant/load-sharing followers with measured actual pose; cold support ties have explicit load roles | Conditional, leading coupled comparison | Separates support integrity from commanded alignment; can detect downstream faults | More sensors, calibrated compliance and failure cases; define which constraint owns every DOF. Not inherently safer until fault loads and restraint independence are demonstrated |
| Selectively coupled unified secondary platform | Partial modes use the first or hybrid row; J transfers all four carriers to a separately guided platform | Unified platform alone fails R/C/M; isolated platform plus retained group lifts is conditional | A common J structure may reduce relative local lift error | Added frame mass, torsion, unused-guide drag, isolated-frame parking, load handoff and selector. Literal belt rerouting remains unresolved; positive selection is a simpler transmission comparison, not a working mechanism |
| Sectional secondary platforms, explicit alternative | Separate sections support concurrent groups and couple in both orientations for J | Unresolved; four independently guided sections could express the partition | Potential group support without permanently tying all beds | Two fixed row sections fail column pairs unless they split/reconnect. Four sections trend toward the hybrid with extra joints. No sectional mechanism is assumed in the original proposal |
| Grouped bed Z plus independent gantry Z in J | Partial modes retain independently grouped bed lifts; empty J beds lock to stationary rated supports and gantry owns printing Z | Conditional; bed groups must remain available for R/C/M | Removes continuous joined-bed lift motion in J | Duplicated Z, datum calibration and safe handoff; cannot lock all partial-mode beds under one common gantry and retain unrelated heights. Additional gantry still has D2 obstructions |

Retain D1's **independent full-stroke head/gantry Z with stationary supported beds** as
the simpler *support ownership* control. D2 shows why it is not necessarily a simpler
whole printer: large moving bridges and descending columns may collide. No pricing
claim is possible without a BOM; compare bearings, brakes, guides, calibration, cables,
service joints and fault domains, not motor count alone.

## Central cross and T: separate three functions

1. **P — positional registration:** cold contacts locate X/Y/yaw. Phase 1B A retains
   guide yaw with one X and one Y stop; B deliberately floats X/Y/yaw and uses two
   separated X pads plus one Y pad. Three vertical supports own Z/roll/pitch. A cross
   can carry those datums, but adding its yaw constraint to already rigid guide yaw
   repeats the seven-equations/rank-six conflict. Keep hot plates relieved.
2. **L — gravity and moment support:** a cold cross needs an explicit support polygon,
   arm bending/torsion, retained contacts, positive load locks and a path to the main
   frame. A lateral locator or latch is not automatically a vertical support. A literal
   T has three arms, not four: the fourth carrier needs a separately demonstrated
   load path. Three collinear contacts cannot define a stable plane; three noncollinear
   supports still fail gravity-only equilibrium outside their polygon.
3. **T — torque transmission:** shafts/belts/gears/clutches carry torque. Their phase
   and stiffness graph is distinct from P and L. A three-edge torque tree joins four
   inputs without a fourth redundant phase closure; it does not prove six-DOF support.

Compare independent frame-referenced carriers (lowest coupling), a master/follower
locating tree with released slave freedoms, and a compliant cross sharing only specified
loads. A rigid cross attached to four fully guided carriers forms closed force loops.
Release the *conflicting* freedoms, retain required lateral stability and fall restraint,
and audit both rank and positive contact reactions. “Floating” cannot mean unsupported.
In partial modes a fixed common XY datum may be shared through independent sliding
interfaces; a common rigid Z tie cannot. A sectional cross is a new alternative.

The hot plate mounts and retained sheets remain separate layers. A cross cannot
eliminate sheet slip, local bow, temperature gradients or changing corner geometry.
No hot-edge clamp, bridge sheet, vertical landing or stronger latch is credited as a cure.

## Integration with D2 and the horizontal mechanism

| Interface | Required analysis / unresolved interference |
| --- | --- |
| Horizontal transport in S/R/C/M/J | Either complete Z guides travel with each XY carrier, or support hands off at datum. The first adds XY mass/envelope; the second adds precisely the support transition under study. No stationary rail may be pulled sideways by a dock. A lower shared tug competes with secondary-frame arms, belts and brake mounts |
| Both pair directions and mirrored mixed modes | Row-only shafts/sections do not solve column links. Releasing or reassigning a common member must not change the stiffness/load/reference of occupied unaffected beds; graph isolation alone is insufficient for a shared elastic frame |
| Perimeter cantilevers | Outer bed guides, lift motors and cable exits compete with D2 arm roots and retracted parks; bed lowering transforms attached objects but does not prove arm clearance. Additional full-stroke guides can block service/panel routes |
| Stacked bridges | Bed Z may reduce moving-head Z burden but cannot remove XY ordering or fixed descending-column obstacles. A secondary cross below beds does not solve those intersections |
| Common height and nozzle access | Horizontal conversion at Z=0 remains mandatory. Printing Z is separate. Empty affected modules may return to datum before conversion; no occupied bed moves merely to facilitate reconfiguration. Cross, locks and sensor flags must remain out of seam/nozzle/probe paths |
| Heater wiring | XYZ carrier motion and selector travel require actual flexible paths, temperature/current/bend ratings, strain relief and no belt/lock pinch. Secondary-frame parking cannot consume an assumed cable plane |
| Printed reinforcement | Cross/lift reactions reach printed joints, fasteners and reinforcement; creep at chamber temperature matters. No stock selected or rounded imperial/metric equivalence; each ready-to-print variant needs its own fit/stiffness proof and Ender 3 segmentation |
| Enclosure/service | Both enclosed and open configurations retain every mode. Tool-free removable panels must not carry assumed primary restraint or require mechanism disassembly. Provide access to inspect teeth, locks and independent service supports without entering stored-energy paths |

## Prioritized analytical experiments

1. **Group support and constraint audit:** instantiate P/L/T graphs for all eight
   modes and every handoff state for independent drives versus hybrid. Solve reactions
   with eccentric payloads, guide mismatch and one unavailable load path. Output the
   released freedoms, no-uplift/retention needs and fault loads. Discriminator: can
   support and required independence coexist without incompatible guide loops? Reject
   candidates needing occupied-neighbor displacement or an unsupported intermediate state.
2. **Continuous selector feasibility:** compare a defined finite-radius rerouting path
   against retained belts plus positive selection, using traceable pitch geometry only
   after component/source approval. Sweep full travel, wrap, length, tensioner reserve,
   tooth phase and selector force; include power loss at every state. Discriminator:
   whether rerouting supplies any benefit after its tension/engagement/support burdens.
   Endpoint equality alone fails the present counterexample. No detailed CAD is authorized.
3. **Seam and integration sensitivity:** use both seam orientations/endpoints and J center,
   load redistribution, support thermal paths and D2 full-structure envelopes. Keep measured
   bounds absent until supplied. Discriminator: whether any candidate can plausibly meet
   a separately justified first-layer/nozzle budget while retaining both pair directions,
   service routes and independent jobs. Unknown sheet behavior cannot be assigned zero.

These experiments narrow later CAD requests; they do not authorize them. Qualified
mechanical, thermal/electrical and controls/safety review must precede adoption or physical
work. The first physical proof remains separately reviewed two-bed docking, thermal
registration and cross-seam printing, with uncertainty, acceptance/abort limits and supervision.
