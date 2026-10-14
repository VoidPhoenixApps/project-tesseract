# Toolhead motion and printing Z: urgent exploration backlog

**Captured:** 2026-10-14, from maintainer brainstorming. **Priority:** Explore ASAP, in parallel with existing bed-docking analysis. **Status:** Unreviewed concepts and questions only; no architecture selected, no design validated, no physical tests authorized.

This is a durable starting point for a focused mechanical/controls trade study, **not a new approved requirement or design decision**. The authoritative [requirements](../requirements.md), [architecture](../architecture.md), and [roadmap](../roadmap.md) take precedence. The initial physical milestone remains a bounded **two-bed docking, registration and cross-seam printing rig**; this exploration must not displace that prerequisite. The [Phase 1 study](../phase1/README.md) and its evidence should be consulted rather than treated as already solved.

## Why explore these together

Independent operation of four nominal 180 × 180 mm beds raises coupled questions about independently movable toolheads, relative Z motion, and joined-bed printing. Comparing XY motion and Z motion separately risks selecting a system that cannot support all required modes. The objective is to find plausible **integrated XY/Z architectures** that work with four retained individual sheets and automatic horizontal reconfiguration at a **common fixed-height plane during reconfiguration**.

The requirement for a common plane during reconfiguration **does not mandate stationary beds during printing**; the printing Z mechanism is explicitly undecided. Do not reinterpret this note as permission to move beds vertically to *perform horizontal reconfiguration*. Clear and appropriately position modules before rearrangement; protect running prints.

## Requirements and design boundaries to preserve

- **Separated:** four independent nominal 180 × 180 mm jobs, potentially at different Z progress simultaneously.
- **Row/column pairs:** two independent nominal 360 × 180 mm or 180 × 360 mm jobs.
- **Mixed:** one paired region plus two single-bed regions, potentially three concurrent jobs.
- **Fully joined:** one nominal 360 × 360 mm print region across **four still-installed sheets**. Real usable print area and seam transit remain unproven.
- Maintain automatic horizontal rearrangement at the required common fixed-height reconfiguration datum; no sheet swaps or manual mode conversion.
- Preserve active jobs, exclude occupied modules from unsafe repositioning, account for part heights, parked heads, nozzle/heater envelopes, and thermal/cable/pinch constraints.
- Prefer a mechanically distinctive, printable/reinforced-frame-first architecture; every printable part must fit an ordinary Ender 3. Distinct validated imperial/metric structural-stock interfaces and later 2020 adaptation remain mandatory targets.
- Removable, tool-free enclosure panels must not compromise motion, access, or required configurations. No active chamber heating is approved.
- **Four cooperative heads on one large object remain a separate unproven stretch goal.** Baseline joined-region coverage must not silently depend on cooperative path partitioning. At least one full-area head is a *candidate*, not a selected requirement.

## Toolhead XY candidates raised in discussion

| ID | Exploratory architecture | Opportunity | Key risks / unresolved question |
| --- | --- | --- | --- |
| XY-A | Four independent XY gantries / local head systems | Straightforward conceptual job independence | Frame bulk, mutual interference, parked-head clearance, reach beyond local quadrants |
| XY-B | Common motion framework/rails but four **genuinely independently driven XY heads** | Shared structural elements, potentially compact and distinctive | Shared-axis coupling, path crossing, carriage collision, truly independent two-axis travel and timing |
| XY-C | Four local independent heads **plus a separate full-region head** | Separates independent jobs from joined-print coverage | Fifth head, extra gantry/drive, mass, parked equipment, enclosure clearance and cost |
| XY-D | Shared/reconfigurable gantry, modular carriages or overlapping-reach heads | Potential material/space savings | How to retain concurrency and credible full-region access; toolchanging alone is not concurrent independent XY motion |

No CoreXY, IDEX, multi-gantry, robot-arm or rail layout is selected. Explore full nozzle reachable sets, not nominal bed rectangles. Show parked inactive heads and failure states.

## Printing Z candidates raised in discussion

| ID | Exploratory architecture | Potential benefit | Hard question |
| --- | --- | --- | --- |
| Z-A | **Gantry/head-side Z:** bed build planes stationary during printing; independent vertically moving head systems | Keeps docked bed elevations stable; four heads might progress at different layer heights | Four independent Z travels and structural stiffness; how full joined region is accessed |
| Z-B | **Independent bed Z:** fixed-height head motion support; each bed rides its own Z lift | Head-side packaging simplified; separated jobs can progress asynchronously | At seams, independently lifted beds must stay aligned while printing a joined part |
| Z-C | **Dual Z by mode:** independent bed Z for separate jobs, while locked beds stay fixed and a Z-moving gantry prints the combined region | Avoids independently lifting joined beds in large mode | Duplicate Z systems, reliable mode handoff, intermediate paired/mixed modes, gantry locking during separate jobs |
| Z-D | **Hybrid common gantry plus individual short-stroke head Z** | Possible mixed degrees of freedom | Head adjustment stroke may be inadequate for jobs at widely differing layer heights |
| Z-E | **Reconfigurable/coupled bed Z:** beds have individual Z drives when apart; docking also connects or coordinates their Z movement as a group | One consistent bed-Z printing architecture with groups of 1, 2, or 4 beds; may avoid moving the complete gantry in Z | Mechanical coupling accuracy, overconstraint, transmission/load sharing, hot seam behavior, drive faults and automatic engagement |

**Late addition and important candidate: Z-E.** The maintainer proposed that when bed modules dock, their Z drives could automatically join so the bed group moves reliably as one. This might replace the proposed dual-Z gantry scheme if the joined Z group proves adequately rigid, aligned, driven and safe. Do not confuse a *bed position lock*, a *load-bearing joint*, and an *actuator/drive coupling*: these are different functions and may need different mechanisms.

### Z-E coupling mechanisms to compare, not select

1. **Positive mechanical drive connection** between leadscrews / transmissions at docking (keyed shafts, couplers, clutches or gearing). Compare motor ownership, torque, phase, backlash, homing and engagement tolerances.
2. **Coordinated independent drives** with position sensing and fault checking. Electronic command synchronization by itself is not mechanical coupling or a guarantee against skew or stall.
3. **Mechanical linking of load-bearing Z carriages/platforms**, potentially with one engaged drive or multiple properly coordinated drives. Check guide overconstraint, force sharing, binding and thermal expansion.
4. **Hybrid mechanical tie plus measured synchronization.** Evaluate whether a modest mechanical linkage plus independent monitored drives offers fail-safe advantages over either alone.

**Critical failure cases:** a drive skips/stalls, one coupling fails to engage, one unlocks under load, loss of motor holding torque/power, uneven bed thermal growth, accumulated play, a Z carriage binds, or the joined platform twists. Define what halts movement and heating and how a safe restart/rehome works. A common motor is a possibility, **not** evidence that one motor can safely lift four heated beds, parts, guides and carriages.

### Required mode-by-mode Z behavior for study

| Mode | What must be independently possible | Candidate grouped-Z interpretation |
| --- | --- | --- |
| Four singles | Four jobs at unrelated heights/progress | Four separate Z groups |
| Two row or column pairs | Each pair prints its own seam-spanning object, possibly at a different height from the other pair | Two separately driven linked Z pairs |
| Pair plus two singles | One paired job plus two unrelated jobs | Three Z groups: 2 + 1 + 1 |
| Four joined | A large print crosses both seams | One synchronized 4-bed Z group **or** fixed joined beds plus gantry/head Z |

These are behavioral thought experiments, not proof that Z mechanisms can physically couple in both row and column directions. Geometry must be checked for every arrangement and travel state; real motion envelopes must respect each printed object's height.

## Additional maintainer concepts — 2026-10-14 (later discussion)

These ideas extend, but **do not select**, candidate Z-E and the independent-head XY study. Preserve the specific proposals for comparison, including their unresolved mechanics. No material, motor, pulley, servo, clutch, fixture or datum geometry is approved.

### Z-F — Belt-switched lift and secondary joined-bed frame

**Maintainer proposal:** Give each bed a belted independent Z drive. When beds join, servos and pulleys would redirect or switch belt drive from the individual bed lifts to a **secondary joined-bed lifting frame**. The secondary frame would have a rigid central **cross / “T” indexing fixture** against which the beds register; the coupled frame would then lift the selected joined-bed group as a common structure.

**Functional hypothesis:** During independent printing, each bed has its own printing Z. For joined-region printing, a mechanically referenced secondary frame carries the joined beds and provides one group Z motion, potentially eliminating an entire independently Z-moving toolhead gantry. A separate joined-frame Z motor or shared-drive arrangement is possible but not selected. The cross fixture might serve as a common *cold-side indexing datum* and part of the load path.

**Distinguish these choices before designing:**

- **Literal belt-path selection:** A servo-driven idler/pulley selector moves or redirects a belt between the individual and shared lift paths. Check maintained tension, tooth engagement/phase, tracking, backlash, edge loading and whether changeover would be safe only when stopped and unloaded.
- **Torque-path selection:** A servo actuates a positive clutch, dog engagement or other mechanical selector while timing belts stay on their own correctly tensioned pulley runs. This is a proposed alternative to evaluate, **not** a substitution for the maintainer's belt-switching concept.
- **Load transfer and restraint:** Both drive-selection variants separately need verified support, clamping/retention, guided Z travel, appropriate counterbalance/braking or passive fall prevention, positive engagement sensing, and a defined stop/recovery response. A positioning servo must not be treated as the sole load-bearing safety element.
- **Indexing versus rigidity:** A rigid central cross can provide a repeatable reference *if* its exact constraint set, capture/release travel, preload, stiffness, tolerances and thermal behavior work. Rigidity by itself **does not guarantee identical registration**. Check exactly constrained cold-carrier contacts, three noncollinear height supports or their appropriate equivalent, and thermal relief between reference frame and heated beds. Avoid four-way conflicting hard datums, parasitic load into plate edges, and locking out the inward-corner thermal strategy studied in [Phase 1B](../phase1b/README.md).
- **Cross-shape ambiguity:** Record whether “T” means a top-view orthogonal **cross** for all four inward corners, a literal three-arm T, or a sectional spine. The final indexing geometry is deliberately unresolved. It must not obstruct print seams, nozzle paths, horizontal approach/release, or bed heater cabling.
- **Partial-mode problem:** A permanently unified four-bed secondary lift does not by itself give two independently moving Z pairs or one Z pair plus two independent singles. Investigate selectively coupled/reconfigurable secondary sections, more than one shared lift group, or independent lifts remaining active in partial modes. Include row *and* column pair orientations, not only one.
- **Safe transition:** At the required common fixed-height **horizontal-reconfiguration datum**, with all affected beds empty and motion protected: align and support; seat verified locators; engage and *sense* the belt/drive selection; safely transfer load; isolate the unused motion path; move only after all verified states agree. Determine which order actually avoids binding, falls, missed belt teeth or unintended motion. No vertical lifting/lowering *as the rearrangement method* is authorized.
- **Faults to study:** power loss in mid-shift; selector half-engaged or false-positive; unexpected drive torque; timing-belt tooth skip/slack/breakage; a bed failing to seat or load-share; one Z support skew; heat-warped cross; frame growth; loss of a brake; and recovery from mixed/paired modes without disturbing active objects.

**Specific early artifacts:** (a) belt-and-clutch power-flow diagrams for independent, paired, mixed and joined modes; (b) indexing and load-path free-body sketches; (c) fault-tree showing which independent supports remain carrying weight during each mode transition; (d) packaging/stroke study of shared frame, horizontal dock and toolhead clearance; (e) relative Z seam-step and angular error budget with explicit measurement plan. All numerical tolerance or strength limits await review, not intuition.

### XY-E — Mirrored or oppositely oriented common toolheads

**Maintainer proposal:** Use the *same basic toolhead*, arranged as mirrored/opposing units, to minimize clearance required between heads and around central bed seams.

**Alternative ways to realize the intent:** (1) rotate/reorient an identical mechanically symmetric head and its accessory positions; (2) use common functional parts with interchangeable left/right ducts or brackets; (3) true left/right mirror builds if warranted. Compare common-BOM/service advantages against different printed parts or asymmetric cooling/filament routing. No claim of printable reach without swept-envelope analysis.

**Specific checks:**

- Compare nozzle-to-edge distances, full 3D body/fan/drive/connector envelopes, cooling and heat paths, service access, cable/bowden bend radii, parking and vertical strokes for all four positions.
- Explicitly evaluate collisions between **simultaneously moving heads**, hotends, probes, heaters and *completed objects*, including unequal Z/layer progress, near seams and when only some heads are active.
- For mirrored layouts, check opposite cooling asymmetry, extruder drive behavior, belt attachments, endstop/probe offsets, toolchange calibration, handed components, parts interchangeability and mirrored carriage dynamics.
- Determine whether identical heads rotated 180 degrees produce the desired offset without introducing opposite-rotation axis, cable or cooling conflicts. Show a dimensioned/nozzle-centered clearance table rather than relying on a visual impression.
- Keep full-region printing independent of the still-unproven four-head cooperative stretch goal: describe where inactive heads can park while a selected head traverses docked seams.

**Suggested comparison:** two-to-four simple nozzle-centered CAD envelope blocks (not finished toolheads), first in identical orientations, then alternated/mirrored, using common measured/reference dimensions. Log the minimum collision-free center distance and actual reachable seam envelope for each mode. Any clearance benefit is a hypothesis until computed and tested.

### Integration priority

Add **Z-F** to the mode/kinematic matrix beside **Z-C dual-Z** and **Z-E coupled bed Z**, and **XY-E** to all head-layout comparisons. Before selecting a mechanical architecture, focus on the compatibility of XY-E + Z-F with both orthogonal pair arrangements, mixed groups, full four-bed join and a safe all-empty docking/changeover sequence. Preserve the simpler Z-E and Z-A alternatives as controls rather than assuming the extra switching frame earns its complexity.

## Priority research questions (start here)

1. **Kinematics and reach:** Sketch four quadrants and all mandatory layouts. For XY-A through XY-D, show actual independent XY reachable sets, parking zones, collision/nozzle envelopes and at least one credible joined-print path without depending on cooperative heads.
2. **Z group transitions:** How do four Z lifts return to the common horizontal-reconfiguration datum, align, dock, engage/disengage drives and verify both position and coupling? Does coupling work for horizontal *and* vertical pairs as well as all four?
3. **Degrees of freedom:** Can joined platforms move vertically without overconstraining horizontal docking/thermal-expansion interfaces? Which constraints locate sheets, transmit Z loads, and allow controlled thermal motion?
4. **Drive safety:** Compare four independent motors synchronized in software, mechanically coupled shafts, carriage links, shared drives, and dual-Z handoff. Analyze missed steps, stalls, lost power, false sensors, failed coupling, E-stop and supervised recovery.
5. **Load/stiffness:** Quantify mass and center of gravity of bed modules, sheets, prints and Z stages, plus lift torque, deflection, pitch/roll, resonances, seam step, repeatability and thermal drift. Establish assumptions, units and parameter ranges before limits.
6. **Motion and packaging:** Account for independent lifts, horizontal bed travel, Z stroke/build height, guides, parked gantries, cable chains/heater flex, belts/screws, frame reinforcements, tool-free enclosure panels and maintenance access.
7. **Control/firmware feasibility:** Define machine states for singles/pairs/mixed/joined, drive ownership, independently scheduled layer heights, coupled-group coordinate frames, verification signals, planner rejection rules, homing, fault handling and restart. Do not claim Klipper or an existing slicer natively solves this.
8. **Complexity comparison:** Estimate motor/driver count, transmission/coupler count, sensors, printed and purchased components, cost, service burden and incremental failure modes. Avoid selecting a clever mechanism based on elegance alone.
9. **Comparison baseline:** Explicitly test whether a simple shared full-area head with other local heads, or a fully independent head-Z design, beats coupled bed-Z on proof burden, accessibility and reliability.

## Suggested first deliverables (desktop study only)

- **D1: Mode/kinematic matrix** for XY-A–E × Z-A–F, flagging incompatible pairings and mandatory modes that each cannot support.
- **D2: Two or three candidate concept sketches** with coordinate datums, Z travel/parking envelopes and a step-by-step coupling or belt-selector state sequence, including a potential cross indexing fixture; label all diagrams unvalidated.
- **D3: Coupled/switchable-Z failure-mode and constraints table** separating sheet alignment, load transfer, belt/drive selection, thermal relief and detection.
- **D4: Preliminary parameterized calculations** for lift loads, torque, skew-induced seam step, structural deflection and coupling error with sourceable assumptions and no fabricated tolerance.
- **D5: Decision matrix and open questions** ranking candidates for subsequent review; retain eliminated ideas and documented reasons.
- **D6: Proposed optional two-bed Z-coupling bench study**, only **after** the existing cold docking/seam work is scoped and with reviewed hazards, measurement uncertainty, acceptance/abort criteria, repeatability and supervision. This is not permission to build or energize anything.

## Evaluation and governance

Evaluate every candidate against: mandatory arrangements; true independent concurrency; full-region reach; layer-height independence; seam registration during hot Z travel; mechanical simplicity; printability; structural and thermal behavior; motor fault tolerance; wiring/enclosure; reproducibility; cost/serviceability; and whether risks can be tested with a bounded two-bed rig.

**Decision gate:** do not promote an idea to architecture or requirements until alternatives are compared, assumptions and quantitative acceptance criteria are independently reviewed, and appropriate physical evidence is collected. Documentation, calculations, animations and CAD are *not* validation. Hardware experiments need a reviewed procedure with measurable pass/fail criteria, hazards, abort conditions, supervised runs and preserved raw data. Any significant architecture selection needs risk-appropriate independent review.

**Community angle:** invite evidence-based critiques and alternative motion/coupling proposals through GitHub Discussions and the project Discord. Promote useful conclusions to GitHub review records; neither chat nor Discord votes settle engineering feasibility.

**Next resumption point:** Begin with **D1 (XY-A–E / Z-A–F compatibility across every required bed arrangement)**, then compare **Z-E coupled bed lifts, Z-C dual-Z and Z-F belt-switched secondary joined frame**, while testing XY-E mirrored/common-toolhead clearance against other head packaging. Keep the two-bed docking proof in its current engineering sequence.
