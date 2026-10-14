# Parameters, dependencies and generated components

The authoritative defaults and bounds are `PARAMETERS` in
[fixture_model.py](../../cad/fusion/TesseractDockingFixture/fixture_model.py).
Fusion names prepend `t1c_`. All inputs are mm except `float_yaw_deg`, a unitless
number interpreted as degrees for the analytical capture bound. Fusion API
coordinates are cm; the generator explicitly converts from mm. Bounds define
supported *concept geometry*, not safe operating ranges or tolerances.

| Input | Default | Supported range | Dependency / use |
| --- | --- | --- | --- |
| bed | 180 | exactly 180 | Both nominal plate/sheet envelopes, dock pitch |
| gap | 0.5 | 0.2–2 | Cold pitch; fixed center + bed + gap |
| carrier | 160 | 156–164 | Carrier, bridge, plate and guard outlines |
| stroke | 40 | 20–50 | X rails, base length, released X endpoint |
| release_y | 8 | 6–10 | Y rails, Y unseat endpoint |
| travel_x | 0 | 0–stroke | Moving X blocks and every upper component |
| travel_y | 0 | 0–release_y | Upper Y blocks, cartridge, moving bed |
| pad_baseline | 120 | 100–130 | B X contacts at ±half-baseline |
| float_xy | 0.5 | 0.2–0.8 | B translation allowance analysis only |
| float_yaw_deg | 0.2 | 0.05–0.3 | B yaw allowance analysis only; no CAD rotation |
| guard_gap | 1.5 | 1–2 | Neutral B guard/carrier spacing |
| support_span | 100 | 90–110 | Three shoes/keys and plate Z-support triangles |
| anchor_inset | 16 | 14–20 | Inset anchor reservation from inward edges |
| mount_pitch | 100 | 90–110 | Four common mounting bores on square pattern |
| mount_bore | 5 | 4–6 | Illustration only, not fastener fit selection |
| print_xy | 200 | 180–220 | Per-part XY bound screening, no geometry effect |
| print_z | 180 | 100–250 | Per-part Z bound screening, no geometry effect |

Derived parameters: `fixed_x=100`, `center_y=120`, `dock_x=fixed_x+bed+gap`,
`moving_x=dock_x+travel_x`, `moving_y=center_y+travel_y`,
`left=dock_x-carrier/2`, `bottom=center_y-carrier/2`,
`base_length=dock_x+carrier/2+stroke+30`, `base_width=240`,
`cartridge_side=carrier+12`. Default base is **430.5 x 240 x 8 mm**.
Do not override derived expressions or drag occurrences; CHECK rejects mismatched
bodies/poses. The body sketches use driving offset and size dimensions, offset
planes and extrusions. Each mount bore has its own sketch and through-cut, with
driving X=`t1c_moving_x ± t1c_mount_pitch/2`,
Y=`t1c_moving_y ± t1c_mount_pitch/2`, and diameter=`t1c_mount_bore`.
All four sketches use the plate's Z datum and the same global XY origin. The
plate uses the same moving center; changing carrier size changes edge margins,
not pitch. Separate sketches avoid cross-hole constraint coupling without fixing
the pattern at its initial coordinates. The user confirmed B,inset generation
and the default four-hole pattern. The previous 164 mm failure was a trapezoidal footprint caused by missing edge
constraints. After adding rectangle orientations, the maintainer's B,inset
160→164→160→156→164→156→160 mm CHECK sequence passed with all 59 footprints fully
constrained. See the [failure and runtime evidence record](verification.md).


All non-base sketch lower corners must remain in positive XY so driving distance
dimensions cannot change quadrant. Top Z=0 and the height bands are intentionally
fixed. To redesign the stack, change source and review load/support dependencies;
this version does not promise arbitrary parametric topology edits.

## Validation rules

- Reject unknown, nonnumeric, nonfinite and out-of-range input values.
- Permit only the immediately adjacent floating-point representation outside a
  nonzero declared bound, normalizing it to that bound before further checks.
  This covers the reproduced cm/mm conversion error; two outward steps are
  rejected. Zero and all in-range values remain exact. This is not a mechanical
  tolerance or permission to exceed the parameter domain.
- Reject travel beyond the selected strokes; X motion requires Y fully released.
- Reject guard clearance no greater than the translation-plus-yaw corner bound.
- Reject X-pad baseline without edge reserve, invalid/nonpositive boxes, negative
  sketch positions, bores crossing plate edges and candidate print-envelope excess.
- Reject positive-volume intersections among modeled solid boxes. Hidden
  reservation boxes are excluded. Intended face contacts are allowed.
- CHECK reads current input parameters, recomputes geometry, checks complete named
  component set, identity occurrence poses, one solid per component, analytical
  bounds within 0.001 mm and volume within max(0.001 mm³, 1 ppm).

These numerical comparison thresholds detect source/kernel disagreement, not
manufacturing tolerance. Fusion can accept an unsupported edit before CHECK;
there is **no event listener enforcing bounds continuously**. Run CHECK after
every change; undo failed changes. Expressions/topology not covered by these
checks require manual feature/history inspection.

## Inventory

Default A generates **51 components**, B **59**, with one body each. A has 43
visible solid components and 8 hidden reservation components; B has 50 visible
solid components and 9 hidden reservations. Center/inset selection changes
reservation locations and names, not count. All are independent components
using common global datums; no assembly motion joints are claimed.

| Group | Components / purpose |
| --- | --- |
| Reference | Laboratory base envelope, three fixed pedestals |
| Each bed | Separate retained sheet and plate envelopes, cold carrier, three plate Z supports, two carrier probe targets |
| X transport | Two fixed rail envelopes, four X blocks, bridge |
| Y transport | Two rails on bridge, four upper blocks |
| Shared interface | One mount plate with four through bores |
| A | Three rigid keys; one station X pad/tower and moving pad |
| B | Three sliding shoes; four float guards; two station X pads/towers and moving pads |
| Both | One station Y pad/tower and moving Y pad |
| Hidden reservations | Two anchors and two radial secondary regions; two retractable-preload regions; two reinforcement regions; B adds centering/hold-down region |

The names ending `ENVELOPE`, `RESERVED`, `RETRACT_BEFORE_RELEASE`, and
`NO_STOCK_SELECTED` are deliberate limitations. Turning on hidden reservations
helps review packaging; their overlap is not physical material or an implemented
mechanism. Do not include reservation bodies in a future manufacturing export.
