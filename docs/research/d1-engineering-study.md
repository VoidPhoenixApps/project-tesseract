# D1 — first comparative mechanical investigation

**2026-10-14 · Research proposal, not an architecture decision or physical validation.**
This extends [Draft PR #25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25).
Read the [initial screen](d1-compatibility-initial-screen.md), with its explicit audit below,
then [calculations](d1-calculations.md), [conceptual diagrams](d1-diagrams.md),
[failure study](d1-failure-study.md), and [sources/verification](d1-verification.md).
The [requirements](../requirements.md) remain unchanged and authoritative.

## Public summary

The difficult question is not whether four beds can move. It is whether the machine
can print two different seam-spanning objects at different heights while keeping
each object's supporting beds aligned. A single joined lifting frame cannot do
that alone. Equally, four motors receiving the same commands do not prove that
four surfaces stayed level.

Independent head-side Z is the simplest comparison baseline because it leaves hot
seams stationary during printing. Selectively grouped bed lifts deserve further
study because they can represent every required grouping. The proposed secondary
frame deserves a bounded comparison, but moving a belt between lift paths adds a
separate support-and-engagement problem. Keeping belts tensioned and selecting a
torque path with a clutch is a distinct alternative, not proof that belt switching works.

There is also a correction to our first screen: dual-mode Z-C is not inherently
incapable of paired/mixed printing. It can retain bed lifts for those modes, **if**
it solves the same synchronization and support problems as grouped bed Z. That is
an additional mechanism requirement, not a demonstrated solution.

The next useful work is to challenge these assumptions, establish real head and
lift envelopes, and review error budgets. No final design, CAD platform, controller,
stock, license or physical test is approved. Community critique is welcome through
[GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions).

## Evidence and audit of the initial matrix

Baseline `main`: `952c2202bc001d1aff38fa7bce9a0b86410695d6`; the original D1
screen is retained in branch history. Phase 1B remains the owner of the thermal
negative result: fixed center anchors vary gap by 0.33984 mm over its temperature
range, wider than the proposed 0.20 mm window. Reproduction here agrees. That window
is **not an approved tolerance**. Phase 1C establishes bounded CAD/checker evidence,
including retained failures and recovery, not hot registration or active lift evidence.

| Initial claim | Audit / present interpretation |
| --- | --- |
| Z-A provides every mode | Only a relative-Z DOF result. Local-only XY still fails joined/pair coverage. Four long-travel gantries also need independently clear structures. |
| Z-C partial modes blocked | Correct for locked beds under one common gantry. Too broad if applied to every dual-Z implementation: grouped bed lifts may remain active in partial modes; see equation below. |
| Z-F partial modes blocked | Correct for beds rigidly attached to one unified frame. The original backlog already permits independent lifts remaining active in partial modes. Evaluate that variant explicitly, rather than treating the missing mechanism as an impossibility theorem. |
| XY-C fifth head solves large mode | Supplies a candidate single-head J route only. One fifth head cannot supply two simultaneous independent paired jobs by itself. |
| Mirrored heads improve clearance | Possible at inward corners, not universal across full travel. No selected head geometry exists; no actual clearance has been established. |

Let `h_i = z_nozzle_i - z_bed_i` denote relative job height, with fixed nozzle offsets
absorbed into calibration. For a common gantry `g` and downward bed travel `b_i`,
`h_i = g + b_i`. Independent bed coordinates therefore retain independent relative
heights even with one common gantry. A joined pair must have equal physical surface
height (including tilt/thermal error), not just equal commanded `b_i`. If the bed
lifts are locked, only `g` remains and all active jobs share one progression coordinate.
Z-C partial modes can use a stationary gantry and independent **groups** of bed lifts;
moving both simultaneously adds range allocation and fault complexity without resolving
seams. Do not move an occupied bed to the reconfiguration datum merely to recover range.

## All mandatory modes and candidate combinations

Coordinates/bed IDs follow [diagrams](d1-diagrams.md): 1 NW, 2 NE, 3 SW, 4 SE.
S, R, C, M and J are the original five families; M is expanded into both orientations
and their mirrored placements. Each group needs independently usable XY and relative Z.

| Mode | Explicit bed groups | Concurrent height coordinates | Required active nozzle paths |
| --- | --- | --- | --- |
| S | 1 / 2 / 3 / 4 | 4 | Four single-region paths |
| R | 12 / 34 | 2 | Two horizontal pair-spanning paths |
| C | 13 / 24 | 2 | Two vertical pair-spanning paths |
| M-horizontal | 12 / 3 / 4 or 34 / 1 / 2 | 3 | One horizontal pair and two singles |
| M-vertical | 13 / 2 / 4 or 24 / 1 / 3 | 3 | One vertical pair and two singles |
| J | 1234 | 1 | One full-region head; remaining heads/gantries park clear |

Classification: **CF** conceptually feasible at DOF level only; **C** conditionally
feasible with the stated added mechanisms; **U** unresolved because topology/range is
unspecified; **X** unsupported as presently proposed. None is a demonstrated capability.

The following are **integrated research candidates**. `A+` means an explicit proposed
extension of XY-A: four independent systems with overlapping reach sufficient to assign
two pair paths in either direction, three mixed paths, and one full-region path. It is
not a claim that the current local-head proposal already has that reach. All C cells
also require swept-volume proof; structural crossing may still eliminate A+.

| XY/Z combination | S | R | C | M-horizontal | M-vertical | J | Principal condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XY-A+ / Z-A baseline | C | C | C | C | C | C | Independent full Z travel; extended reach and parked structures clear of other jobs |
| XY-A+ / Z-E monitored independent group drives | C | C | C | C | C | C | Measured group height/tilt, protected support, disturbance detection, compatible guide constraints |
| XY-A+ / Z-F literal switch, unified secondary frame only | C | X | X | X | X | U | S individual lifts; J needs continuous support and tension/phase-preserving switch |
| XY-A+ / Z-F positive selector, unified frame only | C | X | X | X | X | C | J support handoff, rated positive engagement and retained drive path; still no partial groups |
| XY-A+ / Z-F positive selector plus E-like partial-mode lifts | C | C | C | C | C | C | Bed lifts retain monitored pairs/mixed; frame isolated in partial modes |
| XY-A+ / Z-F literal switch plus E-like partial-mode lifts | C | C | C | C | C | U | Same partial groups; J still needs continuous belt-path/tension and support proof |
| XY-C / Z-A with strictly quadrant-local four heads | C | X | X | C | C | C | Fifth covers one mixed pair or J; cannot cover two unrelated pairs simultaneously; fifth Z and parking also needed |
| XY-A+ / Z-C retaining grouped beds in partial modes | C | C | C | C | C | C | Adds E-like partial-mode obligations plus locked-bed/gantry handoff for J |
| XY-A+ / Z-D finite head trim only | U | U | U | U | U | C | Unrestricted unrelated heights unsupported whenever divergence exceeds usable trim stroke |

XY-C mixed feasibility assumes the fifth head can operate independently alongside
both local singles; its gantry could invalidate that assumption. Adding pair reach
to at least two local heads repairs R/C only with a new geometry proof. XY-B and XY-D
remain U across all Z combinations until independent XY paths and carriage ordering
are specified. A common Y beam constrains its carriages to common Y; adding independent
X motors does not provide arbitrary simultaneous XY jobs. A single active toolchanger
is X for concurrent S/R/C/M; retained as a J-only subsystem, not a complete baseline.
XY-E overlays every row, with the exact two-type relationship in the diagrams.

For **every C cell**, docking occurs horizontally at the common fixed datum with
only affected empty modules, continuous support, sensed position locks, known structural
joint state and separate drive ownership. Parking includes inactive gantries, not just
nozzles. A tall active or finished object stays an obstacle; unrelated jobs cannot be
made safe by silently moving their beds or pausing them indefinitely. A transition can
be rejected when active objects obstruct it. See the [failure table](d1-failure-study.md)
for common stop/recovery conditions and the diagrams for group/load ownership.

## Balanced Z comparison

| Concept | Load path and actuation | Advantages | Liabilities, thermal effects and cost/maintenance drivers | Decisive unknown |
| --- | --- | --- | --- | --- |
| Z-A independent head/gantry Z | Head/XY beam → independent vertical guides/drive → frame; bed carriers remain supported at print datum | Avoids lifting joined hot surfaces; naturally independent relative heights; no Z drive exchange at bed join | Four moving beam/head systems, long guides, cable travel, anti-fall provision; frame bending changes nozzle-to-bed distance; beam crossing and enclosure access; heaters on beds still need horizontal flex routing | Can full-stroke independent gantries cover both pairs and J without colliding? Head mass is not necessarily lower than bed mass |
| Z-B independent bed lifts | Sheet/plate → carrier → local lift guides/actuator → horizontal transport/frame | Similar head height; simple conceptual singles; modular service | Lift mass grows with parts; four heater harnesses flex in XYZ; unequal drive/guide compliance changes seam step; long vertical guides must travel or hand off horizontally | Joined printing needs a synchronization/support mechanism, becoming E-like; open-loop equal steps are insufficient |
| Z-C dual-mode bed/gantry Z | S/partial: local/group lifts; J: beds structurally locked, gantry lifts | Can keep joined beds stationary while retaining independent singles | Duplicated lift systems, locks and calibration; partial-mode repair retains E complexity; switching must not impose vertical docking or shift occupied jobs; thermal/load changes invalidate assumed offsets | Define both pair directions and three groups explicitly; prove stationary support of locked J and unused drives |
| Z-D common gantry + head trim | Common beam lift plus four compact head slides | Potentially compact fine trim; can absorb small calibration differences | Independent height divergence consumes trim, not just layer thickness; adds head mass/play and common-frame fault domain; trim wiring, calibration and travel stops | Full-job divergence/build-height envelope and overhead crossing; finite short stroke cannot support unrestricted independent job histories |
| Z-E selective group Z | Local carriers/guides; selectable drive or load links, monitored independent motors, or hybrid | Group partition matches 4/2/3/1 progress coordinates; one printing-Z strategy | Orthogonal docking transmission, overconstraint, uneven torque/load sharing, backlash, fail-safe support; hot plates require relief from cold links; sensors, shafts and service disconnects add cost | Which constraints are released when grouping, and how does one failed lift stop without twisting a joined print? |
| Z-F secondary frame | Independent belts for S; joined beds supported by a guided frame through selected power path | Common J structure can reduce differential local lift motion; cold cross may consolidate datum | Adds frame mass and lift guide structure below beds; selector service access and belt wear; cross expansion/torsion; partial modes still need E-like lifts or sectional frame; lowest apparent motor count may hide highest integration burden | Continuous support at changeover, both pair orientations, retained horizontal docking clearance and central cross constraint set |

Z-A is comparatively simpler **in Z ownership**, not a proven cheaper whole machine.
There is no priced BOM; compare total guides, motors, brakes, harnesses, calibration
and service operations, not motor count alone. Printable nodes must carry stiffness and
creep demands at actual enclosure temperature. Both stock variants and later 2020 edition
need their own interface/structural verification; this study selects no stock dimensions.

### Z-E mechanism discrimination

| Variant | Mechanism and useful property | Failure/complexity needing resolution |
| --- | --- | --- |
| Positive drive link | Shaft/gear/dog connection phases multiple lift inputs | Equal angle does not ensure equal displacement when leads/radii differ; shaft torsion, accumulated backlash, wrong phase and redundant powered motors can rack the group |
| Monitored independent drives | Separate motors follow group trajectory; sensors observe carrier height/tilt | Motor encoder cannot observe downstream belt slip or carrier compliance; latency and stopping skew require bounds; four loop commands alone are not detection |
| Structural carriage link | Load-bearing tie shares gravity load, ideally with compatible guide freedoms | Redundant guides form force loops; linkage must carry bending/torsion, not merely hold XY location; one drive may now bear all group mass |
| Hybrid | Mechanical support/tie with monitored drives | Can improve fault response but adds competing constraints; specify one position reference and compliant/load-sharing followers rather than forcing independent servos against a rigid tie |

A square network of four bed couplings contains a closed loop. A three-edge spanning
connection can connect all four without a redundant drive loop, but the omitted drive
edge is not permission to omit needed structural seam support. Drive and structural
constraint graphs must be reviewed separately; R uses edges 12/34, C uses 13/24.

### Z-F: preserve both proposed power paths

**Literal belt-path switching:** Moving idlers changes path length, wrap and belt
tracking during the entire shift. Two equal endpoint lengths do not imply constant
intermediate tension. A toothed belt is not a freely sliding chain derailleur: tooth
phase, tensioner capacity, minimum bend/engagement and flange access require explicit
geometry. Gates' design guidance establishes those checks, not a working switch [R4
in sources](d1-verification.md). A switch is U until a supported, stopped, unloaded
changeover and continuous path-length model exist. A single loss of tension cannot be
allowed to release a gravity load.

**Positive torque-path selector:** Belts remain on dedicated tensioned runs while a
mechanical dog/clutch selects the output. This avoids belt rerouting but still needs
shaft phase, complete engagement, torque capacity, bearing support, retention and
independent sensing. Tooth-clutch catalogs distinguish tooth shapes and engagement
positions [R5](d1-verification.md); a servo command is not engagement evidence. A
clutch is not automatically a brake. No catalog unit is selected or sized here.

The central cross is a proposed **cold-side** datum/load structure, not four rigid
hot-edge constraints. Three noncollinear Z supports can define a plane; many additional
height contacts require equalization/compliance or a reviewed stiffness model. An
orthogonal cross and a literal three-arm T are different unresolved topologies. Both
must stay below seam nozzle travel, allow horizontal release, and avoid the Phase 1B
thermal anchoring conflict. A sectional frame that joins in both orientations must
prove its own grouping and joint stiffness; it cannot be credited to the unified frame.

## Shortlist and subsequent investigations

Retain **(1) XY-A+ / Z-A**, **(2) XY-A+ / Z-E monitored groups with separately specified
support**, and **(3) XY-A+ / Z-F with positive selector and E-like partial modes** as
research comparisons. Keep literal belt switching beside candidate 3 as a separately
unresolved branch, not silently discarded. If A+ cannot package, revisit XY-B topology
or XY-C with added local pair reach before choosing any Z winner.

Provisionally reject as complete machines: strictly local XY-A; XY-C with only one
pair-capable head; shared single-active XY-D; Z-D restricted to trim when job divergence
exceeds stroke; Z-C with all beds locked in partial modes; Z-F unified frame as the only
partial-mode support. Each rejection identifies a missing function, not an immutable
judgment on a revised mechanism.

| Rank | Next bounded investigation (recommendation only) | Evidence required to discriminate |
| --- | --- | --- |
| 1 | Independent XY/Z reach and collision feasibility | Actual nozzle-centered head/gantry/cable/probe envelopes, axis ranges and parking; all eight explicit layout states; adversarial unequal object heights; both conventional and A/B orientations; reject intersecting swept sets before detailed CAD |
| 2 | Group-support and guide constraint graph | Separate position/structural/transmission graphs; reaction loads for eccentric parts, failed actuator, and each transfer state; prove no unsupported state or incompatible guide loop |
| 3 | Seam error budget across temperature/load | Relative Z, pitch/roll, layer/sheet stack, compliance and measurement uncertainty; retain Phase 1B negative case; derive acceptance/abort limits from printing requirements for review |
| 4 | Selector desk model | Literal path length/wrap/tension versus selector coordinate, and separate clutch phase/backlash/load isolation; compare complexity to direct grouped lifts |
| 5 | Narrow CAD envelopes after explicit approval | Validate selected reference-model identity/revision/rights, travel/parking and exact constraints; include Ender 3 part segmentation, both stock interfaces, enclosure removal/service routes |
| 6 | First physical proof, separately authorized later | Reviewed two-bed docking/seam procedure, measurement uncertainty, safe loads/temperatures, pass/abort limits, supervision and retained raw results |

No dates, prices or safety limits are invented. Outstanding work includes detailed
3D swept geometry, actuator/guide sizing, dynamic frame/plate models, thermal gradients,
wire life, fault response measurements, sensing architecture and qualified independent
mechanical/electrical review. This first pass supplies testable hypotheses, not the exit
approval for the research-first pause.
