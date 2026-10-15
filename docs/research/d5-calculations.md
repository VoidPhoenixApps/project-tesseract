# D5 — reproducible analytical calculations

[Python](d5_analysis.py) · [tests](test_d5_analysis.py) · [JSON](d5-results.json).
Python 3.9+ standard library; no CAD engine, controller or hardware access. From root:

```sh
python3 -B docs/research/d5_analysis.py > /tmp/tesseract-d5-results.json
cmp /tmp/tesseract-d5-results.json docs/research/d5-results.json
python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v
```

Inputs can be varied by importing the named functions. Output is deterministic sorted
JSON without timestamps; `results()` owns the published cases. D2 geometry and D4 input
validators are imported unchanged; D4 in turn imports D3. All dimensional inputs are SI
except D2/removal coordinates explicitly in mm; outputs state their units.

## Assumption and uncertainty register

| Class | Inputs and provenance | Limits |
| --- | --- | --- |
| Requirement | Eight partitions and nominal 180 mm beds inherited from D2 | No approved enclosure dimensions, print height or temperatures |
| Reference properties | M1 PC, M2 PMMA, M5 glass proxy, M6 5754 from [ledger](d5-references.md) | Typical source data, not selected stock, tolerances or warm allowables; glass proxy is not tempered-panel evidence |
| Hypothetical geometry/load | .6 × .6 m panel; .004 m PC/PMMA/glass and .0015 m Al; 50 Pa uniform pressure; 2 m/s² vertical acceleration; 30 N outward force; .03 m weight offset; .5 m retainer spacing | Comparison inputs, not fabrication dimensions, design loads or safety factors; 50 Pa represents distributed lateral loading, not predicted chamber pressure |
| Thermal sensitivities | Panel rise 40 K, frame rise 20 K; steel alpha 12e-6/K; frame Al 23.6e-6/K inherited from D4; 5 K differential leg heating | Different panel/frame temperatures intentional; unknown gradients, moisture, restraint and contact |
| Heat balance | A=2.16 m², PC t=.004 m, k=.21 W/m/K; hi=4, ho=8 W/m²/K; Q=100/300/600 W; exchange=0/5/20 m³/h; rho_air=1.2 kg/m³, cp=1005 J/kg/K; bridge=0 W/K; C=10000 J/K | Uncalibrated inputs, not a measured physical bound; six-face toy cube is unrelated to D2 packaging size. hi/ho are convection only; radiation omitted |
| Two-zone | Qlower=80 W, Qupper=220 W; Glower=Gupper=4 W/K, coupling=1/4/20 W/K | Separate thought experiment, not calibration of lumped case |
| Joint relaxation | Initial preload 200 N, remaining fraction 1/.5/.25, friction .2, shear 20 N | No time/temperature law, measured friction, fatigue or capacity |
| Clearances | D2 assumptions retained; clear half-width 300/320/360 mm, 2 mm numerical reservation; abstract panel/lip path in service document | Not purchased-component stand-ins or approved stop distances; no hands/rotation/fault displacement |

No statistical confidence interval is justified. For final use, measured dimensions,
material scatter, temperature distributions, load histories, restraint stiffness,
contact/friction, uncertainty and correlations must replace these assumptions. A finite
sensitivity range is not a proven worst-case bound. Invalid/negative/nonfinite inputs are
rejected as appropriate; zero loss conductance is not accepted as a finite equilibrium.

## Expansion, mass and structural-frame effects

Free expansion `delta = alpha L deltaT`. Differential free movement against a frame is
`delta_rel = L(alpha_panel deltaT_panel - alpha_frame deltaT_frame)` along a common
length from a common datum. Actual constraint loads require support stiffness/contact.
Mass `m = rho width height thickness`; hardware and cassette mass are omitted.

| Reference | Thickness mm | Mass kg | Growth at 40 K mm | Relative growth versus steel frame at 20 K mm |
| --- | --- | --- | --- | --- |
| PC | 4 | 1.728 | 1.560 | 1.416 |
| PMMA | 4 | 1.714 | 1.680 | 1.536 |
| Glass property proxy | 4 | 3.600 | .216 | .072 |
| Al5754 | 1.5 | 1.436 | .574 | .430 |

These are intentionally unequal thicknesses, not an equal-strength ranking. A centrally
located fixed datum halves the travel to each edge compared with an edge datum, but the
full edge-to-edge growth remains. Slots must also retain capture through tolerance,
thermal reversals and wear. No generic slot length follows from this table.

D4 free frame growth over .6 m at 20 K is .144 mm steel and .2832 mm Al. Unequal 5 K
heating of steel legs gives .036 mm differential length; any plane tilt depends on
support spacing/constraints. Frame expansion affects panel fit and head/bed alignment
through distinct load paths; do not equate it directly to seam step.

## Panel bending and latch loads

For a simply supported unit-width strip under uniform pressure q:
`I=t^3/12`, `wmax=5q L^4/(384 E I)=5q L^4/(32 E t^3)`.
This is an elementary Euler–Bernoulli strip, not a four-edge plate, impact barrier or
fracture model. Two opposite support edges are ideal; actual edge/corner clips, holes,
membrane action, prestress and compliant framing change behavior.

At 50 Pa and 600 mm span, linear outputs are PC 6.878 mm, PMMA 4.794 mm,
glass .226 mm and 1.5 mm Al 4.255 mm. PC/PMMA/Al exceed half their thickness;
JSON marks `linear_warning=true`. Those values are **invalid small-deflection design
predictions**, retained as warnings to revise the model/support/thickness. The .5 ratio
is an analyst caution flag, not an acceptance criterion. Glass below the flag is still
not validated for strength, edge flaws, impact or guarding. Halving span divides the
linear displacement by16; doubling thickness divides it by8. Actual plate analysis and
measured supports are required before a stiffness/clearance rating.

For ideal lower weight supports, `W=m(g+a)`, per-support force `W/n` only if equal sharing.
With outward force P at mid-height and weight offset e, upper retention total
`Rtop=(W e + P h/2)/h`; lower normal reaction `Rbottom=P-Rtop`.
This separates force and moment equilibrium, not retainer capacity. Both signs need
physical load paths. The example results and lost-support limitations are in
[attachments](d5-attachments.md). Dynamic impact, user slam, panel drop and one-corner
prying are absent; none is bounded by the 2 m/s² input.

Relaxation sensitivity: friction-only shear resistance `F=mu N0 r`, where r is retained
preload fraction. The output exposes loss of nominal margin without predicting a creep
rate. Actual viscoelastic and gasket data, temperature/stress history and positive-capture
geometry are needed; no time-to-failure claim follows.

## Heat equations and limiting checks

Series wall resistance per area `R=1/hi + t/k + 1/ho`; `U=1/R`.
Total conductance `G=A U + rho_air cp exchange/3600 + Gbridge` in W/K.
Steady lumped excess `theta_inf=Q/G`; transient
`theta(t)=theta_inf+(theta0-theta_inf) exp(-tG/C)`; `tau=C/G`.
No active heating is modeled. Cooling uses Q=0 after heat input ceases; physical hot parts
need separate nodes rather than assuming every component instantaneously shares theta.

To vary uncertain films, call `heat_conductance` with alternate hi/ho (e.g. 2/4 and 8/12
W/m²/K), bridge conductance, area and flow; these are hypotheses requiring measurement.
At fixed temperature rise an extra 1 m³/h adds .335 W/K under the assumed air properties.
Higher G lowers rise at fixed Q, but actual heater duty and leakage respond to temperature.
Radiation and buoyancy require a nonlinear treatment; high-rise output is not a safe bound.

For two zones with rise x/y and mixing K:
`(Gl+K)x-Ky=Ql`, `-Kx+(Gu+K)y=Qu`.
Determinant `Gl Gu+K(Gl+Gu)` is positive for positive external losses.
The sum verifies `Gl x+Gu y=Ql+Qu`; at zero mixing each zone is independent, and strong
mixing tends toward a common rise. This demonstrates why a uniform-temperature assumption
is not mandatory even in a minimal heat balance; it does not locate real hot spots.

## Geometric kernel and test meaning

D2 closed AABB contact is conflict. `path_hits` performs continuous intersection on each
fixed-orientation translation segment, catching obstacles between clear endpoints.
Reversing the path checks installation for the same rigid bodies. This does not establish
a physically realizable release sequence, hand clearance, rotational sweep or full machine.
D2 reach rejection is retained even when the enlarged enclosure boundary contains every
sampled box. Tests verify arithmetic, conservation, scaling, boundary/invalid cases,
lost-support load sharing, lost friction margin and deterministic output. They do not
validate input assumptions, mechanical performance, emissions or safety.
