# D3 — loads, selector sensitivity and seam error budget

**Analytical sensitivities, not measurements, component ratings or approved limits.**
[Source](d3_analysis.py) · [generated JSON](d3-results.json) · [tests](test_d3_analysis.py).
Python 3.9+ standard library; imports unchanged D1 lift functions, D2 mode partitions
and Phase 1B thermal functions by repository-relative path. No CAD or hardware access.

```sh
python3 -B docs/research/d3_analysis.py
python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v
```

Stdout reproduces the JSON. Public functions accept explicit parameters; edit `results()`
for a deliberate sensitivity sweep, regenerate JSON and rerun tests. A calculation passing
its software tests does not establish that inputs describe a mechanism. Dimensional
functions are hypothetical abstract models, not purchased-part envelope substitutes.

## Assumptions, units and provenance

| Quantity | Value/range | Classification / missing evidence |
| --- | --- | --- |
| Bed side | 180 mm nominal | Requirement; not measured plate/sheet size or printable area |
| Module masses including carried parts | 1,2,3,4 kg on beds 1,2,3,4 | Deliberately asymmetric subset of D1's 1–4 kg sensitivity; not payload limits. Actual heater, sheet, carrier, guide, part, fasteners and moving cable mass require BOM/measurement |
| Extra secondary-frame mass | 0,2,4 kg | Hypothetical; includes none of the module mass twice. Actual platform, bearings, locks, reinforcement and moving actuator inventory unknown |
| Drive | 40 mm belt travel/rev; 8 mm screw lead; efficiency .7, reduction 1, advantage 1 | Unchanged D1 nominal examples; no selected pulley, lead or efficiency. D1 retains .3/.7/.9 and 1/3 reduction sweeps |
| Gravity / dynamic terms | 9.80665 m/s²; zero acceleration/drag for tabulated static loads | Conventional g and lower-order assumption; D1 lift function accepts upward acceleration and resisting drag. Rotation inertia, friction, wire tug and shock still missing |
| Two-line supports / tripod | 240 mm separation; tripod (-120,-120),(120,-120),(0,120) mm | Abstract statics examples only; not proposed cross dimensions |
| Arm | 20 N at 90 mm, EI=1e6/1e7/1e8 N·mm² | Sensitivity, no stock selection; linear prismatic cantilever excludes joints/torsion and distributed mass |
| Guide mismatch | 200 mm travel; .01/.05/.1°; initial .02 mm; free accommodation .05 mm; k=1000 N/mm | Hypothetical signed mismatch and piecewise linear loop stiffness; not vendor tolerances or bearing load predictions |
| Belt selector point path | Half-span 100 mm, q=-20..20 mm, imposed tension 50 N | Mathematical counterexample; zero-radius idealization cannot predict actual wrap/tooth engagement |
| Seam contributions | See budget below | All arbitrary sensitivities, not established bounds or acceptance values |
| Arrest | 12 kg; downward .01 m/s; delay 10/20/50 ms; catch stroke 1 mm | Illustrative dynamic model only; no specified sensor latency, catch or safe stroke |
| Thermal constants | Phase 1B alpha=23.6e-6/K, 20–100 °C; D1 steel example alpha=12e-6/K | Aluminum typical Kaiser data [E6](d3-references.md), not chosen alloy. Steel generic assumption; no grade selected |

## Mass, forces, torque and support reactions

`m_group=Σm_module+m_added_frame`, `F=m(g+a)+drag`, `ΔT_belt=F/A`,
`torque_belt=F*r/(efficiency*R*A)`, `torque_screw=F*lead/(2π*efficiency*R)`.
R=motor revolutions per output revolution; A=belt travel per load travel. Lengths in
torque equations are meters. Reduction lowers torque at increased motor speed; gravity
and guide forces do not disappear. Belt ΔT is tension **difference**, not tight-side
tension or bearing load; add pretension/vector forces and manufacturer checks.

JSON tabulates all eight mode partitions. For unequal module masses, R has 3 and 7 kg
groups, C has 4 and 6 kg; equal-size regions need not have equal lift loads. J carries
10 kg before its platform. Adding 2 kg yields 117.6798 N and nominal belt torque
1.07025 N·m (8 mm screw example 0.21405 N·m). Adding 4 kg yields 137.2931 N and
1.24862 N·m. No actuator is sized by these static examples.

Two support lines at ±d/2 satisfy `Rminus+Rplus=F` and
`(Rplus-Rminus)*d/2=F*e`. Thus `R±=F*(.5±e/d)`. At 12 kg, d=240 mm and e=60 mm,
reactions are 29.41995 and 88.25985 N. At e=150 mm one becomes **-14.70998 N**:
a compression-only support would lift off. For a three-point support, solve
`ΣRi=F`, `ΣRi*xi=F*xCOM`, `ΣRi*yi=F*yCOM`. At COM=(90,90) the illustrative tripod
requires **-36.77494 N** at its first contact. Three noncollinear supports establish
a plane but not positive force closure for arbitrary payloads. Four rigid supports are
statically indeterminate; stiffness/preload is required rather than equal quarter-loads.

An eccentric gravity load gives bending moment `M=F*e`; for the ideal arm
`delta=F*L³/(3EI)`. The 20 N/90 mm example yields 1.8 N·m root moment and
4.86/.486/.0486 mm tip deflection across the EI sweep. The largest value also cautions
against trusting small-deflection assumptions. Printed joints/fasteners, torsion, creep,
temperature and actual support geometry must be modeled before using a real EI.

## Guide compatibility and phase

`mismatch=initial+H*tan(phi)`;
`F_loop≈k*max(0,abs(mismatch)-free_accommodation)` for a deliberately simplified
clearance-plus-linear-spring loop. The .05° example produces .19453 mm mismatch and
144.53 N internal force despite zero payload term. Relieving yaw alone does not relieve
vertical guide parallelism or pitch/roll conflicts. A real contact/preload model may
behave differently; this is a sensitivity and reason to specify released freedoms.

Drive phase error: `dz=travel_per_rev*(upstream_deg/R+output_deg)/360`. For 40 mm/rev,
1° at each side of 3:1 reduction yields .14815 mm. Equal angular motion with different
leads `l1,l2` gives relative travel `n*(l1-l2)` after n output revolutions; thermal
growth, cumulative pitch error and tension stretch are additional terms. A one-tooth
jump moves a simple direct lift by p/A, as D1 records; microstep command size is not accuracy.
The [selector study](d3-selector-study.md) documents L(q), force, wrap and unresolved
finite-radius geometry. It preserves literal rerouting separately from torque selection.

## Thermal and seam-alignment budget

For each plate's local reference, use small-angle surface approximation
`z_i(x,y)=z0_i+Rx_i*y-Ry_i*x+elastic_i(x,y)+thermal_i(x,y)+sheet_i(x,y)`.
Subtract plate surfaces at corresponding seam points. Evaluate both seam endpoints,
interior bow residuals and all four J corners; a center measurement can miss tilt.
Use actual coordinates relative to the **chosen** datum: 90 mm example levers below
are not the lever arms of a proven inset mount. Normal gap and tangential registration
must be tracked separately from vertical step.

| Contribution | Illustrative worst-sign magnitude mm | Required evidence before a real bound |
| --- | --- | --- |
| Relative drive translation | .020 | Downstream carrier observation, backlash, lead/tension errors and following error |
| Both plates' pitch/roll | .036 | Four slope terms of .0001 rad at 90 mm levers; actual support-plane covariance and lever arms |
| Differential elastic motion | .020 | D1's 10 N / 500 N/mm sensitivity; loads include part growth, cable tug and transfer preload |
| Residual differential thermal height | .020 | Standoffs, carrier, plate thickness and bow residual after plane terms; unmeasured and not a thermal prediction |
| Sheet stack/curl/slip height | .020 | Actual sheets, retention, magnet/adhesive, contamination and hysteresis |
| Engagement/settling | .010 | Loaded repeatability and flank seating, beyond drive error already counted |
| Measurement guard | .010 | Placeholder only; calibrated method and justified uncertainty required |
| Total illustrative budget | **.136** | Sum of assumed magnitudes, not a certified upper bound or passing threshold |

Avoid double-counting: when measured slopes already include support thermal gradients,
do not add that same tilt in thermal residual; likewise exclude clutch phase already
included in drive translation from engagement. Worst-sign sum avoids unjustified RSS,
but is conservative only if the component bounds themselves are valid. NIST uncertainty
guidance includes covariance [E7](d3-references.md); shared support/heating errors can be
correlated. No distributions, safety factors or print acceptance limits are invented.

The script **calls Phase 1B**, retaining its center-anchor 20–100 °C cold-gap interval
[.43984,.30000] mm: empty for its unapproved .10–.30 mm window. Its hot gap at cold
.20 mm is -.13984 mm, marking interference/model breakdown, not material penetration.
Inset10 retains [.13776,.30000] and hot gap .16224 mm before other errors. It reduces
normal closure to .03776 mm, but not sheet slip, tangential mismatch or Z bow.

Additional unchanged sensitivities from [Phase 1B](../phase1b/thermal.md) and
[D1](d1-calculations.md): 4 mm aluminum thickness grows .007552 mm at +80 K;
20 mm steel standoff grows .0096 mm at +40 K; a 4 mm homogeneous strip's 1 K
through-thickness gradient gives .023895 mm chord-relative bow. These cannot simply
be summed as independent worst-case surface errors without actual load/temperature
paths. D1's 360 mm steel-cross +20 K growth is .08640 mm end-to-end. Neither uniform
cross growth nor cold-side registration guarantees a level hot seam. Inward-corner
reference investigation remains promising, not physically demonstrated.

## Fault displacement and restraint demand

With initial downward speed v0 and unrestrained delay t,
`drop=v0*t+g*t²/2`, `v=v0+g*t`. A catch stopping in stroke s must absorb
`E=mass*v²/2+mass*g*s`; average resisting force `Favg=E/s`.
This includes gravity during stopping, unlike a kinetic-only estimate. Peak force,
contact stress, rebound, structural modes and asymmetric catch engagement remain unknown.

| Delay ms | Free drop before catch mm | Total descent including 1 mm stop mm | Energy J | Average catch force N |
| --- | --- | --- | --- | --- |
| 10 | .59033 | 1.59033 | .18775 | 187.75 |
| 20 | 2.16133 | 3.16133 | .37262 | 372.62 |
| 50 | 12.75831 | 13.75831 | 1.61968 | 1619.68 |

These are illustrative 12 kg/.01 m/s cases, not allowable delay/stroke values or upper
bounds on failure motion. Friction/transmission inertia may reduce descent, other forces
or pre-existing velocity may increase it. Compare with D1's from-rest free-fall examples,
not a replacement. A passive hold may avoid free fall altogether, but its capacity,
fault independence and release behavior still need evidence. No catch/brake is selected.
