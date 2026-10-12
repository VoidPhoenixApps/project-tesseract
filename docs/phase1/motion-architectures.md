# Bed-motion architecture trade study

**Exploratory recommendations only.** Read [configuration feasibility](configuration-feasibility.md) for every candidate's top view, path and limitations. A nominal arrangement is not evidence of printability. All candidates must retain the four heated 180 × 180 mm modules and four sheets, common fixed-height conversion plane, printable-first development, Ender 3-sized printed parts and both reinforcement variants.

## Mechanism comparison

### A: independent XY carriers

Eight translations are the most direct way to give four bed centers independent X/Y coordinates with fixed orientation. Quadrant travel is only about 40 mm per axis in the example, so unrestricted whole-machine XY travel is unnecessary. Independent stages avoid moving a neighbor's carriage during a local conversion. Separate cold carrier datums can make the transport drive's step accuracy less consequential while leaving guidance straightness, Z drift and pitch/roll critical.

Nested stages carry the upper rail, drive and bed on the lower stage: bed → thermal mount → upper bearing → lower bearing → reinforced frame. This adds vertical stack, cantilever moment and compliance in series. A wide bearing separation is useful but competes with the 180 mm docked pitch. Two rails need mounting alignment; more bearings are not automatically better. The [THK mounting guidance](references.md) supports treating rail datums and parallelism as engineered assembly features rather than printed-hole accuracy.

Stationary shared guide foundations reduce frame duplication while preserving independent drives; they transmit disturbances through the common frame. A moving shared guide is a row mechanism with its coupling limitations. Compare screw/nut, belt, and remotely driven belts on required thrust, backlash, cable drag, heat and lock preload, not motor resolution alone. None is selected. A transport brake is not necessarily a precision locator or a safe lock under loss of power.

### B: nested rows/columns

Six translations reduce drives and allow reinforced crossbeams to support two beds. Bed → X bearings → moving row beam → row-end Y bearings → frame gives a longer load path and crossbeam torsion. Heating or moving one bed may change the other's surface. Wide beams and two-ended guidance can improve stiffness but multiply alignment demands and obstruct under-bed cable loops.

Compact rows support both pair orientations, but mixed vertical configurations need extra travel or local Y freedom. The documented 630 mm-wide stagger is a legitimate alternative, not equivalent to compact operation. Job scheduling must forbid moving a busy row; compensating bed coordinates while the support accelerates does not eliminate inertial disturbance. Differential Y trims restore independence in coordinates at roughly the original eight-axis count, plus longer load paths. Retain as a cost/packaging comparator, especially if later scheduling permits whole-row idle windows; do not weaken job protection to make it win.

### C: reconfigurable lattice

Telescopic beams, planar scissors, expandable rectangles and parallelograms give a distinctive mechanism with few drives. However, geometric coupling is exactly what obstructs mixed layouts. A two-pitch rectangle has two shape variables; different gaps on opposing edges require additional sliding or articulated joints and independent support. A one-input pantograph makes all gaps functions of one parameter and fails the two pair orientations as independent modes.

Selectable coupling can be useful **only** if each released platform remains supported, orientated, controlled and lockable. Clutches add lost-motion and uncertain state. Long telescopic overlap offers better axial support than thin scissor bars but may bind under racking. Scissor joints accumulate clearance and give pose-dependent stiffness; near a toggle, forces and sensitivity become unfavorable. Printed pin bosses and hot plastic joints are especially poor places to hide precision. A decoupled grounded lattice becomes a form of independent stage with more joints; investigate only if a measured packaging or load-path advantage emerges.

### D: linkage platforms and remote actuation

A single swing is cheap but a restricted circular locus cannot provide general X/Y positioning. Serial 2R arms add reach; orientation requires a follower or third controlled joint. Planar parallelograms preserve orientation only under their geometric assumptions; pin clearance and differential expansion add yaw error. Two serial parallelogram translations can provide two degrees of freedom without a motorized wrist, at the price of more joints and collision envelopes.

Five-bar parallel mechanisms can keep both motors on the frame and provide two load paths. They also have assembly modes and singularities; a controllable endpoint does not itself control bed yaw. Compare them against serial arms on Jacobian-conditioned stiffness, joint preload, elbow/follower clearance, vertical support and calibration. Remote cables or tendons reduce moving motor mass but introduce tension-only force limits, hysteresis and temperature sensitivity. A planar arm designed for horizontal force can still sag badly under bed weight and latch moments. Short metal pivots and reinforced links are plausible within a printed assembly, but unsupported printed arms are a poor precision datum near heaters.

### E: shared mover and other hybrids

E1 separates the number of supported degrees of freedom from the number of powered axes. Four passive XY carriers retain support and verified locks; one tug services them sequentially from below. This may lower motor/electronics count while adding a capture/release hazard and a common failure point. Loss of tug access must leave beds held, not floating. Do not unlock based solely on dog-command state. Its docking cartridges could be identical to A's, making a two-bed comparison relatively economical.

E2 orthogonal rail switching or horizontally transferred pallets can avoid full XY stages, but a carriage must cross rail intersections without dropping, lifting or losing pitch/roll constraint. Retractable rails must have verified load transfer before release. This is less mature than E1.

Other screened alternatives: (i) four planar magnetic/air-bearing movers need specialized stators or air supply and fail the low-cost printable-frame premise as a first experiment, although not a geometric impossibility; (ii) cable-only suspension has poor passive vertical/rotational restraint and hazardous loss-of-tension behavior; (iii) one rotating carousel or turntable couples all beds, rotates layouts and sweeps active objects; (iv) fixed beds with toolhead-only changes cannot deliver required bed reconfiguration. These are not shortlisted. Commercial component use is allowed; rejection is about fit to this investigation, not a blanket prohibition.

## Qualitative comparison matrix

Ratings express investigation burden under the stated concepts: L = lower, M = moderate, H = higher. For precision/stiffness/thermal potential, G = relatively favorable, M = mixed, W = weak. These are engineering judgments, **not measurements or weighted scores**. C1 and D costs have particularly low confidence because geometry is unfinished. Locks, homing and sensing are additional to listed motion axes.

| Criterion | A independent XY | B rows / trims | C decoupled lattice | D oriented arms / five-bar | E1 shared tug |
| --- | --- | --- | --- | --- | --- |
| All six layouts | Conditional path for all | Compact rows fail MV; wide/trims repair | Uniform forms fail; decoupled conditional | Added orientation/sweep design needed | Conditional serial path for all |
| Controlled motion | 8 translations | 6; ~8 with differential trims | ~8 independent coordinates plus couplers | 8 rotary + follower, or 12 with wrists | 2 tug axes + dog; locks on all beds |
| Precision/repeatability potential | G with cold frame datums | M: beam and local datum stack | W–M: joint stack and pose dependence | M at docking; W–M during transport | G at dock; transfer repeatability open |
| Structural stiffness potential | G with short supported paths | M: beam bending/torsion | W–M at extension | W serial; M parallel if well supported | As A carriers, plus tug reaction |
| Thermal stability potential | M: isolated mounts still essential | W–M: shared heated structure | W–M: many thermally active joints | W–M: long lever arms | M: same docking problem as A |
| Docking complexity | M | M–H for coupled rows | H: locate without fighting links | H: compliance/constraints handoff | H: capture, park and dock states |
| Heater cable management | M: four short XY loops | H: nested moving loops | H: changing link geometry | H: elbow rotation and full sweep | H: loops must leave tug routes clear |
| Collision risk burden | M | H: entire beam sweeps | H: scissors/pinch zones | H: arms and followers | H: dog and tug below other beds |
| Fault isolation/recovery | M: isolate one carrier | H: shared row affects two | H: coupled release/toggle | H: joint/assembly-mode ambiguity | H: shared tug failure, capture state |
| Printable-frame compatibility | G with manufactured guide datums | M: long stiff beams | M for body, W for precision joints | M with metal pivots, stiffness open | M: deep frame and transfer access |
| Imperial/metric compatibility | Separate frame sockets, common docks | Beam sections need separate stiffness checks | Joint/overlap geometry changes | Link section/pivot support changes | Common carrier datums, variant tug supports |
| Maintenance/repair burden | M: repeated accessible modules | M–H: row disassembly | H: many hidden pivots | H: preload and linkage calibration | H: locks/dog access under array |
| Manufacturing burden | M: repetitive mounts | M–H: straight beam references | H: accumulated joint tolerances | H: pivots, parallelism and yaw linkage | H: transfer and lock mechanisms |
| Relative cost/complexity | M–H drive count; baseline comparator | Potentially lower drive cost, added beam cost | H unless few joints prove adequate | H precision pivots; remote-drive trade | Unknown net saving: motors versus transfer |
| Mechanical distinctiveness | Moderate; frame can remain distinctive | Moderate | High | High | High |
| Two-bed proof suitability | Strong | Useful secondary comparator | Weak first choice | Secondary stiffness experiment | Useful after basic dock proof |

No total score is calculated: a mandatory-mode failure cannot be traded away for visual identity. A/B/E can share the same docking experiment, reducing sunk cost. If long-term hot-plate warping dominates all errors, transport rankings matter less than plate/mount redesign. If eight drive channels dominate verified cost, E1 deserves earlier investigation. If frame stiffness forces a very deep structure anyway, D's footprint penalty may lessen, but its joint compliance remains. If concurrent reconfiguration is operationally rare, B may improve in ranking; that observation does not authorize moving busy jobs.

## Ranked investigations and rejection criteria

1. **A1 + frame-referenced hybrid docking:** medium confidence as the most informative baseline; high confidence in independent coordinate reach. Stop if a practical bearing/lock/cable package cannot fit or hot seam evidence fails.
2. **E1 with the same carrier/dock:** low-to-medium confidence. Compare actual tug/lock cost and risk against saved motors only after dock stability works. Reject if access or loss-of-capture recovery requires lifting beds or disturbing a busy one.
3. **B1-wide and B2:** medium confidence in kinematic conclusions, low in cost advantage. Keep compact B1 documented as incomplete. Reject repairs whose workspace or support disturbance removes the expected benefit.
4. **D1/D2 with independent docking:** low confidence pending link sweep and load analysis. A cold one-platform stiffness/sweep mockup could reject these cheaply before heated fabrication.
5. **C1 selectively decoupled lattice:** low confidence; only advance with a concrete benefit and independently supported branches. Uniform C0 and simple D0 remain rejected as complete solutions, preserving their reasons rather than deleting them.

Two-bed tests cannot choose a four-bed architecture alone. Four-way constraint closure, cable access, head workspace, both stock variants, and active-job disturbance must subsequently be demonstrated. Review decisions are in the [risk register](risks-and-decisions.md).
