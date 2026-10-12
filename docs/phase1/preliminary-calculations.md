# Preliminary thermal and structural calculations

**Analytical screening, not simulation or measurements.** Numbers are rounded estimates using deliberately simple models. They establish sensitivity and test priorities, not approved tolerances, materials, geometry or safe operating limits. Reproduce with the standard-library-only [calculation script](screening_calculations.py): `python docs/phase1/screening_calculations.py` from the repository root. Python is only a calculation aid, not a selected CAD dependency.

## Assumptions and provenance

| Symbol / input | Screening value | Basis / limitation |
| --- | --- | --- |
| b, plate width | 180 mm | Mandatory nominal bed dimension; actual plate/sheet edges unknown |
| t, aluminum thickness | 3, 4, 6 mm | Sensitivity cases, not purchased stock |
| Aluminum E | 68.3 GPa | Kaiser 6061 sheet/plate typical value; actual alloy/temper unselected |
| Aluminum alpha | 23.6 × 10^-6 /K | Kaiser 20–100 °C coefficient; no extrapolation above 100 °C here |
| Steel E, alpha | 200 GPa, 12 × 10^-6 /K | Generic screening assumptions, grade/temperature must be verified |
| Temperature rises | 20, 40, 60, 80 K | Uniform idealized plate; 20 °C reference gives up to 100 °C, not heater authorization |
| Plate load P | 20 N | Approximate combined load case; actual mass, print load and clamp force unknown |
| Reinforcement span L | 400 mm | Unsupported member comparison; not final frame geometry |
| Rod load | 10 N per member | Two members sharing 20 N ideally; torsion and imbalance excluded |
| Latch force F, offset h | 50 N, 40 mm | Candidate reaction example; not a selected clamp |
| Carrier width / separated half-pitch | 160 / 130 mm | Packaging assumptions from [configuration study](configuration-feasibility.md) |

[References](references.md) identify the primary sources. NIST's cryogenic 6061 fits were inspected but **not** extrapolated into the heated-bed range. All generic properties require grade-specific replacement before design sign-off.

## Expansion and seam sensitivity

Free uniform expansion is `delta L = alpha L delta T`.

| Rise from 20 °C | Aluminum growth across 180 mm | Growth of one 90 mm half-width |
| --- | --- | --- |
| 20 K | 0.08496 mm | 0.04248 mm |
| 40 K | 0.16992 mm | 0.08496 mm |
| 60 K | 0.25488 mm | 0.12744 mm |
| 80 K | 0.33984 mm | 0.16992 mm |

For two plates anchored at their centers on a frame whose station pitch stays fixed, `g_hot = g_cold - alpha*b*(deltaT1+deltaT2)/2`. At rises 60/60 K, a 0.20 mm cold gap predicts **-0.05488 mm interference**, not a pass. At 60/20 K it predicts 0.03008 mm; at 80/80 K, -0.13984 mm. If steel frame pitch p=180.20 mm rises uniformly by 20 K, its growth adds 0.04325 mm to the gap; local gradients make that credit unreliable. With aluminum and steel both at +60 K, relative 180 mm growth differs by 0.12528 mm. A temperature-dependent pitch or different plate anchor can address this, but cannot demand motion of an active printed region. Set temperature and settle before registration/printing under the reviewed strategy.

Fully restrained one-dimensional aluminum expansion gives `sigma = E alpha deltaT`, about 96.71 MPa at +60 K. This is a warning about restraint forces, not a yield assessment: actual structures slip, bend, expand nonuniformly and share load. Strong latches are not an answer to thermal incompatibility. Plate alloy, sheet/magnet differential expansion and mount friction remain unknown.

For a free homogeneous plate with an approximately linear through-thickness temperature difference, a screening curvature is `kappa ≈ alpha*deltaT_through/t`; center-to-edge sag over span b is approximately `w ≈ kappa*b²/8`. At t=4 mm, a 1 K gradient gives 0.02389 mm; 5 K gives 0.11948 mm. This idealized free-curvature model excludes bonded layers, supports and residual stress. It shows why a single heater thermistor cannot characterize sheet height. Map top/bottom and edge/center temperatures together with surface shape.

## Plate and frame deflection

For a simply supported full-width beam strip, `I = b*t³/12`, `delta = P*L³/(48*E*I)`. With b=L=180 mm, P=20 N:

| Plate thickness | I | Estimated central deflection |
| --- | --- | --- |
| 3 mm | 405 mm^4 | 0.08785 mm |
| 4 mm | 960 mm^4 | 0.03706 mm |
| 6 mm | 3240 mm^4 | 0.01098 mm |

This is a one-dimensional strip estimate, **not a bound** for a three-point-supported square plate or a local nozzle/clamp load. A plate model and measured support geometry are required next. Deflection scales with load, inversely with E, with L³ and t^-3 for this model. Doubling load doubles deflection; 20% less thickness nearly doubles it. Moving supports inward can reduce central span but creates flexible seam overhangs. Sheet flex/magnetic compliance adds to plate bending.

For solid steel rods, `I = pi*d^4/64`, using 10 N at midspan and 400 mm span:

| Nominal comparison section | I | Simply supported deflection | Same-length cantilever end-load deflection |
| --- | --- | --- | --- |
| 12 mm solid rod | 1017.88 mm^4 | 0.06550 mm | 1.04793 mm |
| 1/2 in = 12.7 mm solid rod | 1276.98 mm^4 | 0.05221 mm | 0.83530 mm |

Cantilever formula is `P*L³/(3*E*I)`, sixteen times this simply supported load case. These are **different boundary/load cases**, not a universal sixteen-fold benefit from adding a support. Reducing span 400→300 mm multiplies deflection by 0.421875. A reinforced printed truss that uses metal primarily in axial load can be much stiffer than a long bending rod, but node slip and eccentric joints then dominate. Threaded rod uses root section and thread/fastener compliance; it is not a precision guide substitute. Tube screening uses `I = pi*(Do^4-Di^4)/64`; wall tolerance, local crushing and joint design matter before comparing its mass efficiency.

### Stock examples, not selections

Manufacturer catalogs establish plausible purchasable families, not local inventory or price. Metric example: Thomson `12 TCM` solid CF53 (1.1213) steel shaft, nominal 12 mm, listed h6 0/-11 micrometers (11.989–12.000 mm), 6000 mm minimum usable catalog length. Imperial example: Thomson `QSSS 1/2 L PD 48`, solid 440C stainless shaft, actual 0.4990–0.4995 in = 12.6746–12.6873 mm, predrilled, 48 in length with ±1/32 in length tolerance. Imperial details were visible in the manufacturer's search-indexed product record; direct page retrieval timed out, so order-drawing verification is outstanding. Material/finish differ; **these are not equivalent qualified structural replacements**. Check current distributor availability, machining restrictions and grade-specific properties before any bounded rig selection. The stiffness table deliberately uses nominal diameters and generic E, not certified performance of those products.

Maintain candidate parameter sets `MET-12` and `IMP-0500` with actual diameter ranges, grade, form, length/cut allowance and stock identity. No pipe nominal-size conversion is involved. Keep common bed/frame mounting datums but generate different socket/clamp geometry, fastener edge distances and strength checks. Use split clamps or reviewed inserts rather than relying on an unverified printed interference fit. No builder CAD edits, mesh scaling, reaming or ad hoc shims. Stock selection remains unresolved; both variants need print-fit, stiffness, creep and strength evidence and separately labeled BOM/cut lists/exports before release.

## Moments, angular error and drive screening

A 50 N latch at 40 mm offset gives `M=F*h=2 N m`. Across a 120 mm support spacing the reaction couple is 16.67 N, comparable to the assumed weight load. To keep edge displacement below an illustrative 0.05 mm at 90 mm radius, `theta <= 0.05/90=0.000556 rad=0.0318 degrees`; reacting 2 N m at that angle would require rotational stiffness of at least 3600 N m/rad. This is a load-path target for review, not measured stiffness. Yaw of 0.1 degrees produces about 0.157 mm edge error at 90 mm radius even if the center is perfect.

Guides, printed nodes, carrier and mount act approximately as compliances in series: `1/k_total = sum(1/k_i)` for a simple collinear load case. Increasing rod diameter does little if a hot printed joint supplies most displacement. Creep requires time-dependent measurements under load at the actual joint temperature; room-temperature modulus or nominal glass transition is insufficient. Place datum loads in mechanically captured metal paths where feasible; printed trusses can carry distributed load while replaceable precision inserts carry registration. Later 2020 adaptation changes node and torsional stiffness and requires revalidation.

For transport, `F_required = m*a + F_friction + F_cable + F_capture`; select drive force only after measuring those terms. Belt pulley torque is roughly `F*r/eta`; screw torque roughly `F*lead/(2*pi*eta)` before bearing/startup effects. Do not use motor microsteps as accuracy evidence. For stopping, `d_stop = v*t_delay + v²/(2*a_stop) + uncertainty`, with **verified** deceleration and latency; power loss may remove active deceleration. No permitted speed is established here.

## Cable and metrology sensitivity

Example only: a 5 mm cable with a hypothetical dynamic bend-radius requirement of 10 diameters needs R=50 mm, a loop about 100 mm across before chain walls/clearance. This is larger than the 80 mm separated sheet gap. Route outward/below and reserve its entire swept envelope; do not assume it fits between beds. The cable's actual manufacturer rating overrides this illustration. Four independent heaters need independent strain relief and fault isolation; no electrical rating is inferred.

For independent standard uncertainty components (instrument calibration 0.003 mm, fixture repeatability 0.004 mm, thermal drift 0.002 mm), `u_c=sqrt(sum(u_i²))=0.005385 mm`; illustrative `U=2*u_c=0.01077 mm`. Correlation, small samples or nonnormal effects require a different budget/coverage treatment. A measured step 0.045 mm with this U cannot establish a 0.050 mm upper limit: 0.05577 exceeds it. Guard-band decision rules and a suitable instrument are part of the [proof plan](two-bed-proof-plan.md), not an invitation to round away uncertainty.
