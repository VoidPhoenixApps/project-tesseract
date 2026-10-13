# A/B engineering desk comparison

**Cold concept only.** Dimensions are illustrative millimeters, not tolerances,
supplier specifications or authorized operating limits. Distinguish actual
modeled solids, hidden reservation solids, and unmodeled details below.

## Datum and load hierarchy

Frame F: +X right, +Y toward the rear, +Z upward. Sheet top is Z=0. Fixed bed
center is (100,120); moving dock center is (280+gap,120), default (280.5,120).
This positive-XY drawing origin is a translation of the Phase 1 coordinate
convention. It does not change the contact axes. The two beds represent the
upper-left/upper-right pair with inward corners at their lower seam ends.

```text
Top (docked):            +Y
                         ^
  fixed 180 square       |     moving 180 square
 +------------------+    |    +------------------+
 | 3 Z supports     | seam   | 3 Z supports      |
 |  carrier targets | .5 mm  | carrier targets   |
 +------------------+        +------------------+
                         X stops -> carrier left pads
                            Y stop below carrier front pad
                                  +X ->

Release: unload/retract preloads -> +Y 8 mm -> +X 40 mm.
Dock:    -X 40 mm -> -Y 8 mm; final compliance/capture remains unresolved.
All modeled surface tops stay at Z=0; no landing or lift operation.

Side, both beds:
  0       separate 1 mm sheet envelope
 -1       3 mm plate envelope
 -4       three separate 14 mm Z support envelopes
 -18      6 mm cold carrier; contacts Z=-22..-18
 -24      A rigid keys / B sliding shoes, 4 mm
 -28      common 4 mm mounting plate
 -32      ideal upper Y blocks, 4 mm
 -36      ideal Y rails, 4 mm
 -40      4 mm X bridge
 -44      ideal X blocks, 6 mm
 -50      ideal X rails, 10 mm
 -60      reference-base top; fixed bed has separate pedestals
 -68      base underside
```

These thin guide bands are **envelopes, not commercially available guides**.
Actual catalog fit may require a deeper fixed-height stack. The fixed bed's
carrier-to-base pedestals do not reproduce moving guide compliance; compare
moving A/B error relative to the same independently measured reference.

Gravity path: each sheet -> plate -> three height supports -> cold carrier ->
A rigid keys or B sliding shoes -> mount plate -> Y blocks/rails -> X bridge ->
X blocks/rails -> base. Fixed carrier instead uses three fixed pedestals.
Contact preload acts on the cold carrier, **not plate or sheet**. Station contact
towers return reactions to the reference base. Nominal preload and contact
planes coincide at Z=-20; finite support/CG moment arms still require analysis.

## Six-degree-of-freedom ownership

Rows are the seated, frictionless small-displacement idealization. Three
independent effective vertical rows eliminate Tz/Rx/Ry; the listed planar rows
are reduced at the carrier reference. Real finite pad patches do not implement
these ideal point-normal rows automatically.

| DOF | A: guide-retained yaw | B: floating 2+1 |
| --- | --- | --- |
| Tx | Single central X-normal contact | Two X-normal contacts collectively |
| Ty | Single central Y-normal contact | Single central Y-normal contact |
| Tz/Rx/Ry | Continuously supported guide stage, rigid coupling | Three noncollinear sliding shoes on supported stage |
| Rz | Guides through rigid coupling keys | Difference between X contacts, default 120 mm baseline |
| Drive behavior at seat | Both translations must yield/unload | Below float; must not bypass its planar compliance |
| Retention while traveling | Guide/bearing retention not detailed | Shoes support weight; hold-down/centering reserved only |

A's planar rows are X, Y and guide yaw. B's rows are
`[1,0,0,0,0,-60]`, `[1,0,0,0,0,60]`, `[0,1,0,0,0,0]`.
Both ideal systems have six independent rows/rank six. Remove an X pad from B
or collapse its baseline to zero: rank falls to five. Add guide yaw to B: seven
rows of rank six, making mismatch stress possible. Tests preserve all three
counterexamples. Full rank does not prove positive reactions, stiffness or capture.

**A risks:** guide yaw directly appears at the seam; a wide hard planar contact
can redundantly resist yaw. Three rigid keys are a coupling envelope, not a
defined bolted assembly. Do not add a second spaced X locator or a rigid drive
holding X/Y once the dock should own them.

**B risks:** float must allow X/Y/yaw while retaining out-of-plane stiffness.
Sliding shoes introduce stiction, wear and contamination. Guard contact while
seated defeats exact constraint; the weak-centering/hold-down reservation is not
a working mechanism. No positive retention under an overturning or separating
load is demonstrated. This is a fabrication/test blocker, not a detail to infer.

## Contacts, preload, adjustment and interchangeability

X reaction normals point +X; Y reaction normal points +Y. Reserved compliant
preload acts -X and -Y, with application centers at Y=120 and X=280.5 respectively.
Real actuators/latches must withdraw outside the sweep before release: their
hidden reservation solids are intentionally **excluded** from collision checks.
No spring rate, preload force or allowable motion speed has been selected.

With B's X-pad half-baseline a and yaw disturbance M, positive seating requires
`P > abs(M)/a` before additional separating forces and friction. Use consistent
units (N, N mm, mm). Do not reuse Phase 1B's example 50 N as a design load.
Planar support friction, cable drag and off-center Y preload consume this margin.

Each stationary wear/contact block is a distinct solid on a narrower tower stem.
Intended adjustment locations are behind X/Y contact blocks (normal translation),
the two B X blocks (differential yaw), below the three plate supports (height),
and at float neutral/limit positions. Adjustment screws, slots, locks, anti-creep
seats, pad crowns and tool sweeps are **not drawn**. They must be designed as
repeatable adjustments, not socket reaming or improvised builder shims. Thin
4 mm tower stems and overhanging contact pads need stiffness/fastener redesign.

The same lower mounting plate (default 172 x 172 x 4), four through bores on a
100 x 100 square, carrier outline, support plane and contact-height plane are
shared by A/B. B substitutes sliding shoes and four guard blocks for A's rigid
keys; A has one X pad where B has two. Station towers are independently replaced.
This is **datum/envelope interchangeability only**: the mounting bore diameter
5 mm is illustrative, no screw fit/grade is selected, and guide attachment,
dowels, retention, torque and tool access are absent. Do not bolt through B's
upper carrier in a way that locks its required planar freedoms.

## Horizontal path and what the checks establish

The nominal source checks cover both complete axis-aligned release segments
`(0,0)->(0,8)->(40,8)` and their reverse. Fixed and moving part pairs are checked
in relative coordinates, so co-moving touching support faces are not false
collisions. Positive-volume overlap fails; exact touching faces are allowed.
There is no positive general clearance allowance baked into this test.

At default dock: sheet gap 0.5; carrier-to-carrier gap 20.5; surface envelope width
360.5; upper carrier 160 square; mounting plate 172 square. Released: sheet gap
40.5 with an 8 mm Y stagger. Neither value is a thermal or printable-area claim.
Each X block stays on its illustrative rail with 10 mm end reserve at the stroke
endpoints; Y blocks similarly retain 10 mm. Bearings are boxes, not rated support.

The B guard estimate bounds corner movement conservatively by
`float_xy + 2*(carrier/sqrt(2))*sin(float_yaw_deg*pi/360)`.
Default demand is about **0.895 mm**, below the 1.5 mm guard gap by **0.605 mm**.
This establishes only a nominal envelope reserve; friction and elastic strain
are not represented. The CAD depicts **neutral yaw/float only**, not a flexure or
mechanism simulation. `float_*` inputs check capture allowances; they do not
animate carrier motion.

**Important failed assumption retained:** the analogous sheet bound is about
**0.944 mm**, greater than the 0.5 mm seam gap. Therefore arbitrary worst-case
float/yaw cannot approach the nominal seam safely. B needs an independently
reviewed pre-alignment/capture sequence, greater verified clearance or revised
geometry before operation. The straight, aligned source sweep is **not a capture
certificate**. Do not treat an empty collision list as closure of this risk.

The first draft also intersected the wider mounting plate with stop towers and
put B's front guard in the Y-contact region. Narrowed stems and an offset front
guard remove those *box-model* interferences. These revisions increase tower
stiffness and asymmetric-guard questions; no failed physical result was erased.

Unmodeled: bolts, pad crown, springs, retainers, drives, cables, indicators, plate
tabs, heaters, insulation, compliance, backlash, contact friction, angular capture,
toolheads, printed objects, guards and emergency-stop distance. Enlarged real
envelopes and failure positions must be checked later.

## Thermal reservations and metrology

Center option reserves a planar anchor at each plate center. Inset option reserves
anchors at the inward lower corners, 16 mm from both inward edges; this is a
packaging variable, not Phase 1B's 10 mm thermal recommendation being adopted.
A secondary reservation extends along +Y from each anchor for a radial relief
mechanism. The third Z support must permit in-plane growth. None of these boxes
is a working anchor, slot, thermal break, heater fastener or sheet locator.
Reservations are hidden by default and may overlap support solids by design.

Plate-height supports form a noncollinear triangle under the nominal center of
mass; actual mass, print/cable forces and plate bending are unknown. No fourth
hard height screw is implied. Separate sheets are not assumed to follow plate
thermal strain; their retention/slip remains unresolved. Cold geometry cannot
approve equal or differential heating.

Two exposed carrier probe targets on each bed's +Y edge allow separate carrier
translation/yaw observations. Use plate/sheet edges and top surfaces as distinct
references: never attribute sheet slip to the cold dock. A later instrument
layout must add a third noncollinear height target, rigid indicator stands,
probe direction/force, access with sheets installed, calibration and uncertainty.
Show/hide sheet/plate components for desk inspection; physical access is unproved.

## Printable-first and future four-bed scope

Candidate printed pieces are carriers, bridge, mount plate, pedestals, towers,
targets, A keys and B guards. Their axis-aligned individual bounds fit the
provisional 200 x 200 x 180 budget in the supported parameter domain (largest
default XY footprint 172 square). This ignores brim, orientation, supports,
shrinkage, fastening and thermal exposure; verify the actual Ender 3 usable
envelope before issuing any print files. Base, sheets/plates, rails/blocks,
contact pads and B sliding shoes are non-print-certified envelopes, not selected
stock. No structural suitability of a printed part is inferred from fit.

Two hidden `Reinforcement_interface_*_NO_STOCK_SELECTED` volumes reserve interface
space only. Future imperial and metric editions need supplier-dimensioned
profiles, tolerances, wall/grade, fits, named parameter sets, separately generated
parts/BOMs and stiffness validation. Do not convert a nominal inch diameter to a
rounded metric socket, scale meshes, or ask builders to edit CAD. No sockets or
2020 joints are generated here; those are explicit outstanding requirements.

The two-bed fixture may use simple XY transport, but the final machine must still
reach separated, row-paired, column-paired, both mixed orientations and joined
layouts at fixed height with four sheets. Phase 1's independent-quadrant XY
construction remains a **conditional route**, not a selected architecture.
This local stationary nest must not be copied into four obstructing endpoint
stops: retractable/selectable nests, mirrored lower/inward anchors, cable/head
sweeps and occupied-region isolation remain open. No fixed diagonal linkage,
shared row-only constraint, inter-bed load-sharing closure loop or vertical
reseating is adopted by this fixture.
