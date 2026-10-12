# Thermal anchoring and seam sensitivity

**Analytical screening, not measured plate behavior or a permitted operating range.** Uniform free expansion is the solvable first case; gradients, friction and bonded layers must subsequently be measured. Four independent heaters and four separate build sheets remain in every mode. Numerical outputs are reproduced by [analysis.py](analysis.py), with [results](results.md).

## Parameters and equations

Use local cold plate coordinates `u,v ∈ [-b/2,b/2]`, b=180 mm, anchor `a=(ax,ay)`, and cold carrier origin `c`. For a homogeneous, isotropically expanding plate at uniform temperature:

`r(u,v,T) = c + dF + a + (1 + alpha*(T-T0))*([u,v]-a)`.

Here dF is actual displacement of that carrier's anchor system from frame/carrier expansion or elastic load; it is not commanded compensation. Defaults: T0=20 °C, alpha=23.6e-6/K and E=68,300 N/mm², typical 6061 values from [Kaiser](verification.md), valid as screening inputs in 20–100 °C. No alloy, thickness or material is selected. The sweep uses 20,40,60,80,100 °C independently for each plate: ambient, equal heat, differential heat and reversed differential heat. It extends Phase 1's proposed 60/80 °C experiments to the cited coefficient's 100 °C endpoint for sensitivity only. No extrapolation above 100 °C and no heater authorization.

For left/right plates with initial normal gap g0:

`gx = g0 + (dF_Rx-dF_Lx) - alpha_L*(90-ax_L)*dT_L - alpha_R*(90+ax_R)*dT_R`.

The analogous bottom/top gap is `gy = g0 + (dF_Ty-dF_By) - alpha_B*(90-ay_B)*dT_B - alpha_T*(90+ay_T)*dT_T`. These assume cold edges truly at ±90, square plates, no yaw and expansion free at supports. Use measured edge coordinates otherwise. Sheet edges require their own version of the equation. For a yaw error theta, the normal edge error varies with seam coordinate, approximately `-theta*(v-ay)` for X-facing seams; a scalar mean gap is insufficient.

| Anchor strategy | Local anchor assignments | Horizontal row joins | Vertical column joins / J | Mechanical limitation |
| --- | --- | --- | --- | --- |
| Center | All a=(0,0) | Both inward half-widths grow | Same in Y | Symmetric external growth; normal seam closes with heat |
| X inner-edge midpoint | Left ax=+90, right ax=-90; ay=0 | Ideal normal edge position unchanged | Center-like Y growth; fails to solve column joining | Cannot rotate this mount on demand without changing datums |
| Y inner-edge midpoint | Bottom ay=+90, top ay=-90; ax=0 | Center-like X growth | Ideal normal edge position unchanged | Symmetric limitation; retain as comparison |
| Inward corner | a=(-sx*90,-sy*90), quadrant signs sx,sy | Zero ideal normal growth | Zero ideal normal growth on both inward faces | Reference lies at hottest/crowded joining corner; no room for a finite anchor exactly on the mathematical edge |
| Inset inward corner | a=(-sx*(90-h),-sy*(90-h)); screened h=10 mm | Residual growth over h per plate | Same in Y; compatible with permanent quadrant assignment | Anchor stiffness, thermal standoff and heater exclusion zone need design |
| One fixed reference + radial secondary + free third | Anchor location chosen from rows above | Behavior follows anchor position, not number of supports | Same | This is the physical relief scheme, not a different expansion law |
| Three radial in-plane flexures around virtual center | Symmetric effective center if stiffness/temperature symmetric | Similar to center anchoring ideally | Same | Anisotropic stiffness or unequal heating moves virtual center; flexures have travel/stress limits |
| Temperature-adjusted carrier pitch | Pose selected before job starts | Can compensate one known equilibrium | Four-bed compatibility and station travel required | Cannot move active regions; no cure for later drift, sheet curl or gradients |

The inward corner is fixed to the module's quadrant even when separated or row/column paired. Its two inward faces are exactly those that can join in the specified no-quadrant-exchange layout. Thus it has **no geometric conflict between row, column, mixed and J modes under uniform free expansion**. It does not establish thermal feasibility in the real stack. If future layouts exchange quadrants or rotate plates, this conclusion no longer applies.

## Gap findings and infeasibility test

With g0=0.20 mm, stationary frame and center anchors, calculated gaps at temperatures `(20,20)`, `(60,60)`, `(80,80)`, `(100,100)`, `(80,40)` °C are respectively **0.20000, 0.03008, -0.05488, -0.13984, 0.03008 mm**. Negative gap marks breakdown of the free-expansion solution: contact and distortion would occur; it is not physical interpenetration. The historical 0.20 mm example is rejected as a general center-anchor cold design dimension.

For h=10 mm inset corner anchors the corresponding values are **0.20000, 0.18112, 0.17168, 0.16224, 0.18112 mm** in either joining direction. An ideal edge/corner anchor leaves the normal gap at g0 in its stabilized direction(s), but finite mount size and sheet slip invalidate zero-error claims.

Let C(T) be positive thermal closure minus actual frame pitch growth, and let e bound other signed normal errors (including a separately justified measurement guard band when applying a test). Keeping every case within proposed `[gmin,gmax]` requires:

`g0 >= gmin + max(C) + e` and `g0 <= gmax + min(C) - e`.

A fixed gap exists only if `max(C)-min(C)+2e <= gmax-gmin`. With the **unapproved Phase 1 0.10–0.30 mm window**, zero e and stationary frame:

- Center anchors over 20–100 °C require g0≥0.43984 and g0≤0.30000 mm: empty intersection. This is a mathematical incompatibility of these assumptions, not a proof the mandatory printer requirements are impossible.
- Center anchors over 60–80 °C only permit g0 from 0.35488 to 0.46992 mm before error allowance. This narrower recipe range must be explicitly approved and tested, not silently substituted for the requirement.
- Inset corners h=10 mm over 20–100 °C allow g0 from 0.13776 to 0.30000 mm before errors. With an *illustrative*, unvalidated e=0.03 mm they allow 0.16776–0.27000 mm. This makes 0.20 mm worth a comparison experiment only; the real e is unknown.

Inset sensitivity at 100/100 °C: h=0,5,10,20,90 mm produces closure 0,0.01888,0.03776,0.07552,0.33984 mm. At h=10 each 1 K error in either plate's uniform temperature contributes 0.000236 mm normal gap error; at center it contributes 0.002124 mm. A ±1 mm anchor-position error contributes ±0.001888 mm per plate at +80 K. These are partial derivatives, not a complete uncertainty budget.

## Sheet, frame and central junction

Do not assume magnetic retention defines a repeatable sheet anchor. Three bounding scenarios are useful: (1) sheet follows plate in-plane strain, (2) sheet freely expands about a known independent datum, (3) stick/slip with unknown effective datum and hysteresis. Scenario 1 induces mismatch stress; scenario 2 changes edge motion; scenario 3 is not bounded by either without friction/retention evidence. An illustrative steel-sheet coefficient of 12e-6/K versus 23.6e-6/K aluminum gives **0.16704 mm differential free growth over 180 mm at +80 K**. Steel grade is unspecified; this is sensitivity, not a catalog specification. Sheet retention must restrain unintended gross motion without hard-fixing two separated points against expansion. Edge lips or registration pins cannot protrude into joining seams.

If a homogeneous frame expands from its center, `dF=alphaF*dTF*c`; normal adjacent center pitch adds `alphaF*dTF*p` to gap for center-mounted carrier references. With p=180.2 mm, hypothetical steel alphaF=12e-6/K and +20 K, growth is 0.043248 mm. A near-seam anchor carried by an expanding carrier has a different transfer path: **do not substitute center pitch growth for measured anchor separation automatically**. Model frame, cold carrier and standoffs as separate thermal paths. Signed local gradients/twist can remove any favorable pitch-growth credit. No frame temperature follows heater setpoint by assumption.

For J, model A NW, B NE, C SW, D SE independently. Four inward corner positions follow the vector equation; AB/CD use gx and AC/BD use gy. At inset corners h=10, the inner-corner movement magnitude in each coordinate is alpha*h*dT. With A/B/C/D=100/80/40/20 °C and g0=0.20, the normal gaps are AB=0.16696, CD=0.19528, AC=0.17640 and BD=0.18584 mm. Nonuniform corner positions create a skew central opening, not a single scalar seam. These four positive normal gaps do not establish a printable center: chamfers, sheet radii, sheet setback and local curl enlarge or distort it.

At ideal inward-corner references, uniform heating leaves corner coordinates fixed but differential expansion changes material coordinate alignment away from that corner. At 180 mm distance and 100/20 °C, mismatch is 0.33984 mm for the aluminum model. This tangential mismatch does not itself cause normal interference or a gap for perfect straight square edges; it moves features/outer endpoints and matters for already-adhered objects and nonuniform gradients. Do not mechanically tie seam edges to suppress it. A cross-seam print also couples the expanding substrates through the object; adhesion stress is not included in free-plate calculations. Set and stabilize temperatures before printing and evaluate drift during printing without moving occupied carriers.

## Height, tilt, bow and restraint loads

Three plate-height supports set a plane, not flatness. For supports `(xi,yi)` with vertical changes zi, solve `z(x,y)=z0+px*x+py*y`; small Rx≈py, Ry≈-px. A stack of standoffs/layers contributes `zi=sum(alpha_j*Lj*dT_j)+elastic_i+creep_i`. Plate thickness growth must also be included above the support reference: for a 4 mm aluminum plate at +80 K it is 0.007552 mm. A hypothetical 20 mm steel standoff at +40 K grows 0.0096 mm. If two standoff heights differ by 0.01 mm across 120 mm, tilt is 83.3 µrad, adding 0.0075 mm at a 90 mm overhang. Shared heating can shift both beds together; differential heating creates a seam step.

For a freely bending homogeneous plate with a linear through-thickness gradient, `kappa≈alpha*DeltaTthrough/t`; strip sag relative to its chord is `kappa*b²/8`. At t=3,4,6 mm and a 1 K gradient, sag is 0.03186,0.023895,0.01593 mm; at 5 K multiply by five. Sign follows gradient direction. This is a one-dimensional curvature sensitivity, **not a bound or plate-support solution**. Bonded heater/magnet/adhesive layers, residual stress, patterned heating, in-plane gradients, support reactions and sheet curl can alter shape and sign. Uniform free heating predicts no bow in this idealization; it does not predict a real plate remains flat. A three-point plane fit plus residual height map is required.

The practical relieved mount has one reference fixing two in-plane directions, a second point with radial slot/low-stiffness radial flexure fixing tangential yaw, and a third point free in-plane. All three height contacts stay engaged. At a=(80,-80), a secondary at (-60,-60) requires radial travel `alpha*sqrt(140²+20²)*80≈0.267 mm`; clearance must include tolerances, differential carrier expansion and reversals. Shoulder fasteners clamped tightly through slots can defeat relief by friction. Design hold-down and radial freedom separately; record preload, breakaway force and support slip.

If expansion is fully prevented in one axis, `sigma=E*alpha*dT`: 128.95 MPa at +80 K, or about 92.84 kN for a hypothetical 180×4 mm section. This is a limiting elastic restraint calculation, **not an actual latch load, strength rating or biaxial model**. A compliant restraint of stiffness k has force approximately `k*delta_free` when other compliance is negligible: at 0.33984 mm, k=10/100/1000 N/mm gives 3.40/33.98/339.84 N. With plate stiffness kp in series use `F=delta_free/(1/k+1/kp)`; friction may slip first and compressive plates may bow. Actual lock force requires the full load path and contact solution. Never select a stronger latch to force incompatible edges together.

## Uncertainty and unresolved conflict

Required measurements: actual plate/sheet outlines, anchor coordinates and compliance, thermal map through thickness and across surfaces, alloy/temper, sheet/magnet/adhesive properties, support temperatures/heights, friction, preload, frame drift and repeatability. Gap uncertainty includes two edge determinations, relative carrier motion, yaw, sheet slip and correlations. A statistical root-sum-square model needs justified independent inputs; worst-case sums are conservative only when each bound is established. Resolution alone is not uncertainty; follow [NIST guidance](verification.md).

The unresolved requirement tension is stable, safely traversable seams across independently heated surfaces while retaining separate sheets and fixed-height horizontal conversion. No approved temperature/material range, printable gap/step window or measured distortion budget exists. Corner anchoring improves one term without resolving height/adhesion. If measured bow or sheet behavior exceeds a defensible first-layer budget, pursue plate/support/thermal redesign or explicit requirement review. Do not hide the conflict with a cold offset, forced seam clamp, moving active bed, or a larger bridge sheet.
