# Precision docking interfaces

**Original conceptual analysis; no measured repeatability.** Frame F has X right, Y up in top view and Z upward; nominal sheet top Z=0. Carrier K and plate P have separate datum systems. Use DOFs `(Tx, Ty, Tz, Rx, Ry, Rz)`, angles in radians. Plate elasticity and guide deflection are additional modes, not extra rigid-body DOFs. [Slocum's exact-constraint principles](verification.md) inform the audit; the particular mechanisms below are proposals.

## Constraint audit

A frictionless contact at r with normal n supplies the row `[nx,ny,nz,(r cross n)x,(r cross n)y,(r cross n)z]`. Contact equations are local, seated, small-displacement constraints. Full matrix rank does not establish positive contact reactions, capture range, stiffness, friction-free seating or fatigue life. All unilateral contacts need a demonstrated preload solution; do not count friction as a precise locator.

For illustrative carrier contacts in mm, three continuous vertical constraints at `(-60,-60)`, `(60,-60)`, `(0,60)` give rows `[0,0,1,-60,60,0]`, `[0,0,1,-60,-60,0]`, `[0,0,1,60,0,0]`. These represent the *effective* Tz/Rx/Ry restraint of a supported stage, not a claim that recirculating guides contain only three contacts.

| Candidate | Tz, Rx, Ry | Tx | Ty | Rz | Compliance / redundancy |
| --- | --- | --- | --- | --- | --- |
| A: guide-retained yaw | Continuously supported XY guides | One X-normal stop | One Y-normal stop | Guides | Transport drives must unload or comply in X/Y; do not add separated second X stop |
| B: planar floating 2+1 | Supported floating substage, high out-of-plane stiffness | Two X-normal pads collectively | One Y-normal pad | Difference of X-pad positions | Substage must permit Tx,Ty,Rz over capture mismatch; stiff guide yaw must terminate below it |
| C: practical hybrid | A or B at F→K; three noncollinear plate-height supports at K→P | Cold dock as A/B; one plate anchor fixes local X/Y | Same | Dock as A/B; radial slot at second plate point controls plate yaw | All other plate supports release in-plane growth; sheet retention assessed separately |
| D: planar side-open V plus remote pad | Continuous support as B | Two XY-only V normals collectively | V normals collectively | One separated pad | Same planar float as B; no Z slope on V; sliding/friction and wedge release burden |
| E: master carrier plus relative locating tree | Each continuously supported; released planar freedoms explicitly assigned | Master at F; slaves relative to parent | Same | Same | No additional rigid frame planar stops on floated slaves and no closed fourth-edge locator |

C is an integration of a carrier dock and a thermally relieved plate, not a fourth way to obtain six carrier constraints. A and B also require thermal accommodation. E is credible but ranks below independent frame datums because load, drift and fault recovery propagate between regions.

### Annotated six-DOF diagrams

Original editable text diagrams; dimensions describe contact locations, not manufacturing drawings. Mirrored cartridges are needed in the other quadrants. Arrows describe preload directions into stops; their reactions point oppositely.

```text
A: TOP of cold K (guides underneath own Z, roll, pitch, yaw)
                        Y-stop normal Y
                       =========
                          ^ Py
                +------------------+
 X-stop |  <- Px |        K         |     X stop at y=0 -> Tx only
        |       +------------------+     Y stop at x=0 -> Ty only
                 guide yaw retained      retreat +X, then -Y here
 No hard second X stop. Drives yield X/Y once contact begins.

B: TOP, shown in local approach coordinates (X right, Y up)
 X-pad 1 | at y=+60  +------------------+
         |   <- Px  | planar float K   |   transport -> float -> K
 X-pad 2 | at y=-60  +------------------+   float yields X/Y/yaw
                     v Py                  keeps Z/roll/pitch stiff
                   Y-pad at x=0
 Retreat +Y then +X; all contact faces are vertical, open sided.
 No enclosing socket, taper in Z or vertical landing.

C: SIDE / load hierarchy
 separate sheet S ================================= Z target 0
 hot plate P     ----------- anchor + radial relief -----------
                           o      o      o  3 Z supports
 cold K          ===== replaceable A or B dock ===== <- latch
                 continuous supported XY stage
 frame F         ===== instrumented reference / frame coupon ===
 Gravity: S -> P -> supports -> K -> guides -> F.
 Latch: F -> compliant latch -> K -> planar contact -> F.
 Do not route the latch load through P or S.

D: TOP, two V normals lie ONLY in XY
           / contact n1
 approach >  carrier rounded button ---- remote flat pad
           \ contact n2                    controls yaw
 Open mouth permits horizontal reverse; friction can jam the V.
 Z/roll/pitch still owned by continuous support, not by the V.
```

B's planar rows with contact baselines ±60 mm are `[1,0,0,0,0,-60]`, `[1,0,0,0,0,60]`, `[0,1,0,0,0,0]`. Together with three independent vertical rows their rank is six. Removing either separated X row leaves yaw free; placing them at the same Y loses rank. A replaces these with one central X row, one central Y row and the guide yaw row `[0,0,0,0,0,1]`. Adding guide yaw to B yields seven equations of rank six: nonzero guide/dock mismatch creates elastic stress. The [checks](test_analysis.py) include these negative cases. D can use two nonparallel XY normals at its button plus a remote normal with a nonzero yaw lever arm; an in-line remote pad that supplies no independent moment fails the rank test.

## Entry, exit and force closure

**A:** Approach coarse X, reduce drive force against the X stop, then approach Y while sliding tangentially past X. This demands enough sliding length, clean vertical stop faces and bounded friction. Unload Y preload, retreat Y, unload X preload and retreat X as the pocket permits. Guide yaw misalignment cannot be corrected by the stop. Transport encoders establish coarse position only.

**B:** Travel on a continuously supported substage centered by weak planar springs or a bounded coupling. Within the capture range, seat the two X pads, then the Y pad, using separate compliant X/Y preload elements. Initial one-pad contact rotates K into the other; float travel must exceed combined station error, guide yaw times lever arm, thermal carrier drift and debris allowance. Stops limiting float travel must not engage during normal seating. A flexure is not truly zero-stiffness: its restoring wrench adds preload demand. Sliding planar support instead trades flexure strain for stiction, debris and wear. Both require measurement. Detach preload before backing away; automatic centering must not jerk a neighboring region.

**C:** Keep plate anchors and all three height supports engaged through conversion. A cold-carrier latch never transfers plate weight to another bed. Inset inward-corner plate reference plus a radial relieved secondary is the leading comparison against center anchoring; see [thermal analysis](thermal.md). Printed flexures near heaters are not presumed suitable. A parallel compliant stage needs an out-of-plane stiffness/fatigue drawing before detailed adoption.

**D:** A side-open V at one carrier button and a remote pad can give three planar constraints without vertical insertion. The preload wrench must put both V reactions and the remote reaction in compression. Avoid shallow self-locking wedges: release must work at worst friction/contamination and thermal state, not just nominal geometry. This alternative exchanges two independently visible pads for a harder-to-inspect mouth and remains secondary.

**E:** Reference one cold master carrier to F and float the slaves only in the planar DOFs assigned to relative contacts. The locating graph must be a tree and all contacts must release horizontally. A tree alone is not enough if slave frame stops remain active. Transitions involving a master carrying a job cannot release it or alter its load. Conditional layout reach does not justify a four-edge closure loop.

For B, with symmetric X pads ±a, pure X preload P and yaw disturbance M, reactions are `R1,2 = P/2 ± M/(2a)`; both stay seated only if `P > |M|/a`, plus other separating forces. At a=60 mm, P=50 N and M=1 N·m, reactions are 16.67/33.33 N. These are examples, not selected loads. A Y preload offset also contributes to M. A latch 40 mm below its reaction plane under 50 N introduces 2 N·m pitch/roll moment. Over a 120 mm support lever this changes support reactions by 16.67 N, potentially unloading a gravity-only support. Positive hold-down must retain support without hard-constraining thermal slip; quantify its stiffness and friction.

## Error, durability and observable state

| Issue | A | B / C with B | D / E |
| --- | --- | --- | --- |
| Guide yaw / parallelism | Appears at seam: error ≈ lever × yaw; 0.1° at 90 mm gives 0.157 mm | Float must absorb yaw; guide Z/tilt still transmitted | Same float burden; E adds parent pose errors |
| Pad error / wear | Single-stop displacement follows pad error | Differential X-pad error Δe yields yaw ≈ Δe/120; 0.02 mm gives 0.00955° | V contact wear shifts two coordinates; E accumulates along tree |
| Manufacturing variation | Adjustable cold datum blocks; machined datum inserts as needed | Independent pad setting plus float centering and travel; no tight printed holes as final reference | More contact-normal and parent-interface calibration |
| Gravity and stiffness | Guide ratings, base compliance, serial-stack moment loads | Additional soft modes/flexure parasitic Z; preload deflection | V does not support gravity; E support remains per bed |
| Contamination | Exposed pads inspectable, relief channels/wipers proposed | Two X seats must both be observed | V pockets trap debris; tree diagnosis more complex |
| Wear / fretting | Replaceable cold contacts, measured preload, clean sheet zone | Micro-slip from float springs and thermal drift | V sliding wear and inter-bed force cycling |
| Fault recovery | Isolate affected carrier; retained support, no force escalation | Float at travel stop or one-pad seating is a fault | Jammed V or master disturbance inhibits connected region |

Proposed observations: coarse position; separate X-seat observations (two for B), Y-seat observation; direct mechanical latch-engaged state; float travel margin for B; carrier pose and sheet surface readiness. Contact closure can still conceal dirt or elastic deflection, so sensor truth is not metrology. Require a state table covering contradictory/stale signals, power loss during partial latch, and restart inhibition. A motor command/current rise is not lock evidence. In every state gravity support remains intact; a stop must not cause automatic release or recovery motion. Exact sensors, control integrity and safe force/speed remain unresolved.

Do not shortlist a rotated cone/groove/flat coupling or horizontal taper solely because its seated rank is six. It must have a continuous fixed-Z capture path, load-bearing support during approach and a way to release conflicting guide constraints. Conventional vertical pins and vertical landing fail horizontal conversion; a horizontal round pin constrains transverse Y/Z, not planar X/Y. Preserve these exclusions from Phase 1 rather than silently changing insertion direction.
