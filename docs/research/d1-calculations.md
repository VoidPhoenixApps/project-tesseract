# D1 — equations, assumptions and sensitivity

**Analytical screening only.** [Study](d1-engineering-study.md) / [source](d1_analysis.py) /
[results](d1-results.json) / [tests](test_d1_analysis.py). Python 3.9+ standard library.
No inputs are vendor ratings, measured Tesseract geometry or acceptance limits.

```sh
python3 -B docs/research/d1_analysis.py
python3 -B -m unittest discover -s docs/research -p test_d1_analysis.py -v
```

The stdout JSON reproduces the committed results; redirect only to that results file
when deliberately regenerating. Public functions accept explicit parameters; edit the
`results()` sensitivity lists for additional cases. No Monte Carlo probabilities are
assigned to arbitrary ranges.

## Inputs and load model

| Parameter | Study values/range | Provenance and uncertainty |
| --- | --- | --- |
| Plate side; thickness | 180 mm; 3/4/6 mm | Requirement nominal width; Phase 1 sensitivity thicknesses, no stock selected |
| Aluminum density; expansion | 2700 kg/m³; 23.6e-6/K | Kaiser typical 6061 data, 20–100 °C expansion range, [R3](d1-verification.md); actual plate alloy unknown |
| Moving mass per bed module including part | 1/2/4 kg | Hypothetical engineering sweep; not an upper mass limit; plate alone is 0.26244/0.34992/0.52488 kg at 3/4/6 mm |
| Group mass | sum of module masses plus added frame | Compare 2/4/8 kg pairs and 4/8/16 kg quads; default examples exclude secondary frame and must add it before sizing |
| Pulley pitch circumference; screw lead | 40 mm/rev; 8 mm/rev | Illustrative geometry only; radius 40/(2π)=6.3662 mm; no pulley, belt or screw purchased/selected |
| Efficiency; reduction; reeving advantage | 0.3/0.7/0.9; 1/3; 1 nominal | Sensitivities, not equal actual screw/belt efficiencies; reduction=motor rev/output rev; advantage=belt travel/load travel |
| Upward acceleration; opposing drag | 0 nominal; parameterized | Static lower-order comparison only. Must measure friction/cable load and add inertia/startup torque |
| Relative tilt; lever arm | 0.01/0.05/0.1°; 90 mm | Hypothetical differential tilt and local edge lever, not guide tolerance |
| Differential load; effective stiffness | 10 N; 100/500/2000 N/mm | Hypothetical system compliance sensitivity; printed joints/guide/carrier/plate in series |
| Cold cross alpha/rise/span | 12e-6/K; 20 K; 360 mm | Generic steel assumption inherited from Phase 1; not selected material or measured cold-side temperature |
| Illustrative head-body box | X −35..15, Y −25..25, Z 5..65 mm about nozzle | Synthetic mathematical counterexample, **not a vendor model or approved CAD stand-in** |

Vertical force `F=m(g+a)+F_drag`, g=9.80665 m/s². Belt tension difference
`ΔT=F/A`; motor torque `τ=Fr/(ηRA)`. Screw torque `τ=Fℓ/(2πηR)`.
`r, ℓ` are meters in torque equations; A is reeving advantage. Required work at ideal
efficiency is checked independently as `τ Δθ = F Δz`. Higher reduction lowers motor
torque but increases motor speed for the same lift speed; it does not reduce gravity
force in guides. Opposing belt pretension adds bearing load; ΔT is **not** total tight-side
tension, allowable belt load or a belt-width selection. Add rotary acceleration,
eccentric moments, cable drag, friction, brake release and service margins before sizing.

| Static mass kg | Force N | Belt motor N·m, η=.7 | Screw motor N·m, η=.7 |
| --- | --- | --- | --- |
| 1 | 9.80665 | 0.08919 | 0.01784 |
| 2 | 19.6133 | 0.17837 | 0.03567 |
| 4 | 39.2266 | 0.35675 | 0.07135 |
| 8 | 78.4532 | 0.71350 | 0.14270 |
| 16 | 156.9064 | 1.42700 | 0.28540 |

For 16 kg, η=.3..9 gives belt torque 3.3297..1.1099 N·m at 1:1; 3:1 reduces
those values by three. Every additional kilogram of secondary frame adds 9.80665 N
and 0.08919 N·m at the nominal belt case. A common motor can carry unequal support
loads: with two support lines spacing d and COM offset e, `R1,2=F(1/2 ± e/d)`.
At e=d/4 one side carries 75%, not 50%; uplift occurs beyond the support polygon.
This equilibrium model cannot allocate reactions in a redundant four-support frame
without stiffness information. Screw self-locking is not assumed; lead, friction,
wear and back-driving behavior require component evidence and separate retention.

## Seam step, binding and thermal growth

A conservative magnitude budget is
`|Δz_seam| ≤ |Δz_drive| + L tan(|Δθ|) + |ΔF|/k_eff + |Δz_thermal| + |Δz_sheet| + |Δz_engage|`.
Use separate pitch/roll contributions for both plates at their actual seam coordinates;
the script's tilt term is an already aggregated relative contribution, not a universal
90 mm geometry. Worst-sign addition is appropriate to unknown correlation; root-sum-square
would require a justified stochastic model.

At 90 mm lever, tilt 0.01/0.05/0.1° contributes 0.01571/0.07854/0.15708 mm.
A 10 N differential load yields 0.100/0.020/0.005 mm at the three stiffnesses.
The illustrative drive .02 + tilt .07854 + compliance .02 + thermal .02 + sheet .02 +
engagement .01 totals **0.16854 mm**. This is a sensitivity, not a predicted seam step or
pass/fail comparison. A rigid connection does not remove those terms; it redistributes
loads. For compatible serial paths `1/k_eff=Σ1/k_i`. For guide spacing mismatch δ,
a linear restrained loop force is approximately `F_loop=k_loop δ`; a hypothetical
1000 N/mm loop with .10 mm mismatch produces 100 N internal load even without payload.
At guide travel H, relative angular misalignment φ produces lateral mismatch
`δ≈H tan φ`: H=200 mm, φ=.05° gives .17453 mm. Actual clearance/preload and guide
compliance are unknown; do not label this an allowable misalignment.

Uniform free growth `ΔL=α L ΔT` reproduces Phase 1B: 180 mm aluminum at +80 K grows
.33984 mm; two 10 mm inward anchor offsets close their seam by .03776 mm. A 360 mm
steel cross at +20 K grows .08640 mm end-to-end (a centered symmetric cross moves each
end half that). Differential gradients and torsion can move Z datums as well. A
common cross does not automatically cancel differential sheet expansion. The existing
[Phase 1 bow model](../phase1/preliminary-calculations.md) gives .023895 mm bow for a
4 mm strip and 1 K through-thickness gradient; not a laminated hot-bed solution.
No new physical thermal evidence exists. Historical center-anchor failures remain intact.

Transmission angle error ε gives displacement `δz=ε/360 × travel_per_revolution`.
One degree means .02222 mm for 8 mm lead or .11111 mm for 40 mm belt travel.
For multiple stages, refer each backlash angle to the final output before summing;
a 3:1 upstream reduction divides an upstream angle contribution by three, not an
output-side clutch error. Tooth skips and lost steps are discrete: one skipped belt
tooth of pitch p gives p/A load displacement for this simple path; one full motor
step gives travel/(steps_per_rev × R × A). Microstep command size is not accuracy.

An unsupported body starting at rest falls `d=gt²/2`: 10/20/50 ms gives
.4903/1.9613/12.2583 mm before a catch. This free-fall idealization excludes friction,
transmission inertia and existing velocity; it is not a response-time requirement or
worst-case stop bound. Catch impact must absorb `mgh` plus other kinetic energy;
removing motor power can worsen the event unless independent restraint remains.

## Relative height, nozzle reach and swept volumes

For Z-D, `h_i=g+q_i`, with head trim `q_i∈[qmin_i,qmax_i]`.
A common gantry position exists iff the intervals
`[h_i−qmax_i, h_i−qmin_i]` and the gantry travel interval have nonempty intersection.
Identical usable total trim s requires `max(h)−min(h)≤s`, **plus absolute travel
limits**. ±10 mm trim permits a 20 mm difference only at both end stops, leaving
no reserve for leveling, retract or recovery. A 21 mm difference has no solution.
Long independent head stroke repairs the DOF issue but trends toward Z-A complexity.
The same interval calculation applies to retained downward bed travel in Z-C.

Let P_i be carriage translation range and o_i the nozzle offset in its fixed
orientation Q_i. Nozzle reach is `N_i=P_i+Q_i o_i`; required region R is contained
in N_i **only if** every required toolpath point is reachable and the full body
is collision-free. Body sweep is `union_t(p_i(t)+Q_i B_i)`. Test this against every
other moving/parked head, gantry, harness, frame and object, with reviewed uncertainty
and stopping clearance. Rotation or deformation requires more than endpoint boxes.
For paired/J baselines one active head must span that job; a union of disjoint local
head footprints is not a single-head coverage proof.

The script supplies conservative 3D AABB sweeps for a fixed-orientation translating
body. It catches a mid-path collision that endpoint checks miss. In its synthetic
example a body moving at nozzle Z=10 mm occupies Z=15..75 mm: an 80 mm-tall adjacent
object conflicts, while a 5 mm object does not. The nozzle/hotend below this body box
is **omitted** and must be modeled separately; the low-object result is not a safe-path
claim. AABB overlaps are conservative candidates, not exact contact proofs; nonoverlap
is useful only if boxes truly enclose all geometry and the modeled path.

No selected head, stroke, cable or gantry dimensions exist. Consequently **actual**
reachable area, two-assembly interchangeability and whole-machine 3D collision clearance
remain unresolved, not computed from fictional vendor geometry. Later reference CAD
must meet the approved provenance/rights workflow before interface design.
