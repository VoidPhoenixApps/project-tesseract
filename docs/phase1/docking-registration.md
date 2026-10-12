# Docking and mechanical registration

**Candidate interfaces, not approved mechanisms.** Distinguish three datum systems: frame F, cold carrier K, and hot sheet surface S. Transport locates K approximately; a dock can refine K relative to F; a thermally accommodating mount relates S to K. Measuring K alone cannot establish a printable seam between two S surfaces.

## Six rigid-body degrees of freedom

Use `(Tx, Ty, Tz, Rx, Ry, Rz)` with Rx roll about X, Ry pitch about Y, Rz yaw about Z. For a frictionless point contact with normal n at location r, the small-displacement constraint is `n · (t + omega × r) = 0`. The six-column contact Jacobian must have the intended rank; six contacts all facing one direction do not fix six degrees of freedom. Friction is not a deterministic locator. These are first-order rigid-body constraints; plate bending adds deformation modes.

### Proposed allocation for a guide-retained planar dock

| Component | Intended independent constraints | What must remain free / caution |
| --- | --- | --- |
| Planar XY guidance and support | Tz, Rx, Ry and Rz | Tx, Ty free during transport; real bearings have finite compliance and redundant contacts |
| One X-normal hard stop | Tx | Do not add a second rigid yaw constraint against the guide |
| One Y-normal hard stop | Ty | Latch closes contact, does not independently define height |
| Horizontal compliant preload latch | Keeps stops seated | Must not add an inconsistent hard datum or deflect the plate |
| Three noncollinear hot-plate supports | Tz, Rx, Ry of plate relative to carrier | Separate thermal in-plane mount; no fourth rigid height adjuster |
| In-plane hot-plate anchor plus radial slot | Tx, Ty at one point and Rz at another | Allow growth along the slot; avoid forcing plate growth into cold frame |

The guide-retained design above **retains guide yaw accuracy**. If docking needs two X-normal contacts separated in Y to refine yaw, release yaw at the transport-to-carrier interface with a reviewed planar compliance/floating substage, or accept and quantify redundant elastic constraints. Do not claim exact constraint while a stiff guide and stiff dock both set yaw. Vertical supports remain continuously engaged; this study does not permit a vertical landing/reseating cycle.

An alternative horizontal 2+1 dock constrains Tx and Rz with two X-normal pads at different Y, and Ty with one Y-normal pad. It requires the carrier's transport connection to leave exactly those planar freedoms compliant during docking while retaining Tz, Rx, Ry. Such a planar flexure must have limited travel, verified out-of-plane stiffness and fatigue capacity. Coarse horizontal guidance handles the long stroke; the flexure only accommodates small registration mismatch.

## Interface comparison

| Concept | Constraint direction and release | Advantages | Principal failure / suitability |
| --- | --- | --- | --- |
| Frame stops + compliant latch | Planar stops as above; release preload and retreat along free X/Y | Short load loop, independent modules, portable across A/B/D/E | Guide-height errors remain; station calibration and frame drift matter |
| Side-entry six-contact coupling | Reorient cone/groove/flat or three grooves with horizontal approach; prove full-rank contacts and capture path | Can define all six carrier coordinates | Conflicts with vertically rigid guidance; seating geometry may demand prohibited Z movement; conditional research candidate |
| Horizontal tapered locator + relieved secondary | Taper may constrain directions transverse to insertion; secondary must release redundant direction | Large capture range, replaceable wear surfaces | Wedging can force Z/pitch, bind hot, or lift plate; not automatically compatible |
| Vertical round pin + diamond/slot | Pin gives planar Tx/Ty; relieved secondary controls yaw | Familiar 2+1 planar location principle | Ordinary insertion requires vertical motion, so reject direct lift-on arrangement for conversion |
| Horizontal retractable pin/slot | Pin axis horizontal; restrains transverse coordinates, axial stop supplies another | Can disengage without bed lifting | A horizontal round pin restrains Y/Z, not X/Y; must redesign constraint allocation, not rotate the drawing and reuse claims |
| Side-open V / two planar pads + end stop | V with normals wholly in XY sets two planar combinations; separated stop sets third | Horizontal entry possible; dirt can be accessible | A V sloped in Z creates vertical reactions; guide redundancy and mouth capture need analysis |
| Bed-to-bed edge datums | Relative edge location, usually partial planar constraints | Direct seam reference, short relative metrology path | Thermal coupling, cumulative errors, closed loop at J, force passed into hot plates |
| Wedges, toggles, cams, over-center latches | Preload/retention devices unless explicit locating faces added | Potential positive retention without continuous motor holding | Force multiplication, friction, wear, incomplete engagement, power-loss behavior; lock command is not lock evidence |
| Magnetic preload | Pulls toward contacts; no deterministic position by itself | Simple compliant preload | Gap/temperature-sensitive force, debris attraction; inadequate sole retention claim |

[Slocum](references.md) provides exact-constraint design principles, not proof of this horizontal implementation. [Carr Lane](references.md) explains relieved secondary pin location; its conventional pin products do not by themselves solve horizontal docking. A useful cartridge family would expose fixed carrier datums, approach directions, released freedoms, preload range, sensor surfaces and thermal boundary. It could be mounted on multiple transport systems without declaring them mechanically interchangeable.

## Horizontal approach and load path

Prefer a planar stop/latch experiment first: approach an X stop, then a Y stop while retaining vertical support; close compliant preload; verify state. Unload latch before retracting along the reverse directions. A second adjacent seam must not trap a pin, dovetail or wedge. For J, opposing corner capture pockets must remain open toward the allowed outward quadrant path. Side-entry six-DOF candidates must show a continuous horizontal capture trajectory at the existing height with finite assembly clearance; otherwise classify them as incompatible, not "self-aligning."

Latch forces should close through the cold carrier and frame, near the support plane and support polygon. Pulling on a hot plate edge makes it a spring and can change the very seam being registered. A downward clamp adds bending and guide redundancy; a wedge can amplify a modest motor force substantially. Design contact stress, preload variation and release force before sizing motors. Bearing/locator manufacturers' repeatability claims are not assembly repeatability. Dirt relief, wipers compatible with heater temperature, accessible replaceable hardened pads, drain/debris escape, lubrication compatibility and inspection intervals are required. Keep lubricant off sheets.

## Thermal expansion and four-bed closure

Four independently frame-located carriers are already fixed relative to the frame. Hard-locating all their adjoining edges again is redundant. In a square A-B-D-C-A, closure errors sum around the loop; forcing the final latch to close can bend carriers, spread the frame or preload bearings. Even a spanning tree of bed-to-bed locators is redundant if every bed remains fully fixed to the frame. A tree is only determinate after deliberately releasing corresponding freedoms at the frame interfaces.

Compare three strategies:

1. **Independent frame registration:** each bed locks to F; edges maintain measured clearance and carry no locating force. Seam error includes two station errors and thermal surface behavior, but there is no hard edge loop. Investigate first.
2. **Master bed plus locating tree:** one bed references F, others reference a noncyclic chain with explicitly floated freedoms. Avoid fourth-edge hard closure; a compliance-only retention feature may stabilize it. Disturbance and error can propagate through the tree; simultaneous active jobs complicate release.
3. **Compliant edge preload on frame-located carriers:** retain frame datums, add bounded elastic force near seams. Characterize stiffness/preload versus temperature and do not call it kinematic. Demonstrate it does not flatten or twist the sheets unpredictably.

Each plate's thermal anchor can be at its center (balanced growth, inward seam edges move) or near a chosen seam datum (less growth at that seam, more elsewhere). An inner-corner anchor helps a J central junction but may conflict with isolated/pair datum preferences and temperature gradients. Four separately expanding sheets still produce gaps and height differences; magnetic sheet slip, edge curl and corner chamfers can enlarge the central hole. Do not use a bridge sheet: the requirement retains four individual sheets in every mode. Central-cross coupons are a later four-bed test, not evidence obtainable from the two-bed rig alone.

## Sensing and fault recovery proposal

Use independent observations for carrier approach position, actual latch engagement, and registration/surface readiness. A motor encoder or home switch cannot prove a seated datum. Candidate sensing combines coarse homing with direct seated-contact/position observation and a lock-engaged sensor; plausibility checks detect contradictions. Sensor selection, redundancy and safety integrity are unresolved.

State sequence: `locked idle -> verify empty and path clear -> capture/support verified -> release -> transit -> coarse approach -> seat -> latch -> verify pose/lock -> surface readiness -> eligible to print`. Any contradiction leads to a latched fault and reviewed stop behavior. Loss of power should leave loads mechanically supported; brakes/latches must be analyzed for both locked and partially released states. Stop must not automatically drop the bed, release preload or restart motion. A failed dock is not recovered by increasing force or repeated blind homing. Isolate the region, preserve logs and require inspection/re-establishment of datum after the fault. The [proof plan](two-bed-proof-plan.md) specifies supervised fault tests, not an implemented safety controller.
