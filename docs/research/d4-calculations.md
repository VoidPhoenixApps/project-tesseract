# D4 — reproducible structural sensitivities

[Python source](d4_analysis.py) · [tests](test_d4_analysis.py) · [generated JSON](d4-results.json).
Python 3.9+ standard library. Imports D2 mode partitions and D3 guide/reaction functions
from this dependency stack; unchanged Phase 1B/D1 imports are transitively required.

```sh
python3 -B docs/research/d4_analysis.py
python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v
```

Stdout reproduces committed JSON. Edit explicit inputs in `results()` to investigate
another range; regenerate JSON and tests together. Public functions accept SI inputs
unless a name explicitly says otherwise; imported D3 guide/reaction inputs use mm/degrees.
These are abstract members/springs, not fabricated parts or purchased-part CAD envelopes.

## Input classification and uncertainty

| Input | Value / sensitivity | Basis and limitation |
| --- | --- | --- |
| Steel E, density | 210 GPa, 7850 kg/m³ | MIT steel teaching reference [A2](d4-references.md), SSAB E example [S9](d4-references.md); typical elastic proxy across candidate steels, not lot-specific certificates or strength values |
| Aluminum E, profile I | 69 GPa; 6826 mm⁴ | Rounded educational aluminum proxy [A2](d4-references.md), exact catalog reference I [S8](d4-references.md). Live vendor E punctuation malformed; not silently corrected into a specification |
| Printed solid square struts | 20 × 20 mm, E=.5 or 2 GPa | Hypothetical solid section; 2 GPa motivated by ASA flexural coupon [P1](d4-references.md). .5 GPa is arbitrary degraded-effective-modulus sensitivity, not measured creep. No infill equivalence |
| Beam span / arm / forces | 600 mm at central 100 N; 300 mm tip 20 N | Hypothetical comparison, excludes self-weight and joints unless explicit. Not machine dimensions or limits; 20 N could represent inertial force but no actual moving mass selected |
| Truss geometry | b=300 mm; h=50/150/300 mm; apex vertical 100 N | Two symmetric compressed struts with fixed feet and separately restrained out-of-plane motion; not a full space frame |
| Each end-joint axial stiffness | 10⁵/10⁶/10⁷ N/m | Unknown sensitivity; two joints per bar, four total. Not published fastener or print ratings |
| Root rotational stiffness | 10³/10⁴/10⁵ N·m/rad | Unknown sensitivity, friction/slip excluded |
| Torsion | 10 N·m, 600 mm spring separation, side stiffness 10⁴–10⁶ N/m | Rigid crossbar and two opposed lateral spring paths; not a full frame solver |
| Pair supports | F1=20 N, F2=40 N; k1,k2=10⁶ N/m; tie=0 or 10⁶ N/m; mismatch 0/.2 mm | Unequal abstract loads; includes k2=0 loss case. Vertical translation only, no guide rotational stability or capacity |
| Thermal | steel alpha=12e-6/K assumed; Al alpha=23.6e-6/K; L=600 mm, ΔT=20 K | Steel inherits D3 generic assumption; Al sourced Kaiser typical [A3](d4-references.md). 5 K differential steel heating also shown; no chosen enclosure temperature |
| Dynamics | k=10⁴/10⁵/10⁶ N/m, mass=2/10/20 kg | Independent lumped-mode sensitivity, not mass/stiffness of the compared complete machines |

Uncertainty is predominantly model-form and unknown joint/thermal data, not floating
point precision. No probability distributions, confidence intervals or acceptable seam
budget have been established. Nominal stock calculations exclude diameter/wall tolerance,
straightness, residual stress, cut damage and local contact. Confirm actual inputs before
any sizing. Strength/yield/fatigue limits, creep laws and contact allowables are absent.

## Beam bending, mass and root rotation

For a circular section `A=π(D²-d²)/4`, `I=π(D⁴-d⁴)/64`, `mass/length=ρA`.
Euler–Bernoulli small-deflection models: center-loaded simply supported beam
`δ=F L³/(48 E I)`; tip-loaded cantilever `δ=F L³/(3 E I)`, root moment `M=F L`.
A root rotational spring adds `θ=M/kθ`, tip motion `δroot=F L²/kθ`.
These formulas assume linear elastic prismatic members and the specified supports
[A1](d4-references.md); shear, distributed load and local joint deformation are excluded.

| Nominal section | I mm⁴ | Steel mass kg/m | 100 N / 600 mm simple center δ mm | 20 N / 300 mm cantilever member δ mm |
| --- | --- | --- | --- | --- |
| 12 mm solid | 1017.9 | .888 | 2.105 | .842 |
| ½ in solid (12.7 mm nominal) | 1277.0 | .994 | 1.678 | .671 |
| 25 × 1.5 mm tube | 7675.7 | .869 | .279 | .112 |
| 25 × 2 mm tube | 9628.2 | 1.134 | .223 | .089 |
| 1 × .065 in tube | 8726.4 | .967 | .246 | .098 |
| 20-2020 reference, E=69 GPa | 6826.0 | Not a steel section | .955 | .382 |

At similar steel mass per length, the larger-diameter tube has much better bending
stiffness than the small solid rod. This is a member-level result, not a tube-frame
win: nodes may dominate, thin walls can crush, and space for the diameter/brace matters.
For 25 × 1.5 mm tube, root springs add 1.800/.180/.018 mm, giving total tip motion
1.912/.292/.130 mm. A stronger tube cannot repair an arbitrarily soft root.

Doubling span multiplies bending deflection by eight; doubling force doubles it.
Doubling solid diameter multiplies I by sixteen and mass by four. Nominal 12.7 versus
12 mm is about 25% greater I, not dimensional interchangeability. If E changes from
210 to 200 GPa, elastic deflection increases 5%; a tenfold joint-stiffness uncertainty
can be more important. No beam result includes all fixture/carrier compliance layers.

## Axial truss, buckling and node transfer

For fixed feet at (±b,0), apex at (0,h), `l=sqrt(b²+h²)`, `s=h/l`.
Vertical equilibrium gives each compressive force `N=F/(2s)`. Effective axial bar
stiffness with two end joints is `ka=1/(l/(EA)+2/kj)`; vertical stiffness
`kv=2 ka s²`; `δ=F/kv`. Virtual-work strain energy independently checks this expression.
Euler `Pcr=π²EI/(K l)²` is an ideal elastic buckling reference, not capacity; compare
K=1 and 2 as end-restraint sensitivities, not calibrated joint behavior.

At E=2 GPa and kj=10⁶ N/m, h=50/150/300 mm gives N=304/112/70.7 N and
δ=4.403/.605/.253 mm. A shallow truss amplifies force and joint motion. K=2 Euler
references are 711/585/366 N respectively; a deeper truss reduces axial force but
lengthens the unbraced struts. With E=.5 GPa, the shallow K=2 reference drops to about
178 N, **below its 304 N axial demand**: the corresponding linear deflection is not a
stable load prediction. Imperfections, layer weakness, node eccentricity and missing
out-of-plane bracing can cause failure earlier. No safety factor is implied.

At the soft-joint extreme kj=10⁵ N/m and h=50 mm, linear sag reaches 37.703 mm
(E=2 GPa) or 39.813 mm (E=.5 GPa): about 75–80% of truss rise. These are **invalid
linear extrapolations**, not stable deflection predictions, even when the Euler
reference is not exceeded. Changing geometry can soften the structure or cause
snap-through; a nonlinear analysis would be needed. JSON reports deflection/rise,
a `large_displacement_warning` at ratios ≥.1 and `K2_euler_demand_exceeded` separately.
The .1 trigger is an arbitrary caution diagnostic, not an acceptance limit; absence
of either flag does not validate geometry, stability or strength. Negative controls
exercise large-motion failure independently of Euler failure.

Load transfer into metal chords must be explicit: `N≈M/h` for a bending couple separated
by h, plus web shear and node eccentric moment `N e_node`. A hypothetical 6 N·m couple
and 100 mm chord separation implies 60 N axial chord force before other loads. Average
socket bearing `F/(D l_contact)` and bolt/insert bearing are only preliminary screens;
actual contact patch, splitting, pullout and tube ovalization prevent a capacity claim.
All-thread must use effective root/tensile area appropriate to the failure mode, not
major-diameter solid I. No threaded-rod capacity is calculated from unverified root sizes.

## Torsion, guide mismatch and thermal drift

For two side spring paths separated by w, pure torque produces `±Fside` with
`Fside=T/w`; `Kθ=k_side w²/2`. At 10 N·m and w=.6 m, side stiffness 10⁴/10⁵/10⁶ N/m
produces edge motion 1.667/.167/.0167 mm. Remove one restraint and this assumed pure
couple model is no longer valid: translation and rotation couple, and another return
path must be established. Member circular-shaft torsion `θ=T L/(GJ)`, `J=2I`, is a
separate local model; it must not be applied to an open 2020 section using polar I or
substituted for frame racking. No open-section torsional constant was sourced.

D3 guide loop sensitivity is reused: `mismatch=.02+200 tan(phi)` mm with free
accommodation .05 mm and assumed loop stiffness 1000 N/mm. At .05°, mismatch=.19453 mm
and inferred elastic force=144.53 N. This is not a bearing rating; real contacts may
slip, open or bind. More rigid frame mounts can increase this force if freedoms are wrong.

Uniform free growth `ΔL=alpha L ΔT` gives .144 mm steel and .2832 mm Al over 600 mm
at +20 K; difference=.1392 mm. At equal geometry, 5 K unequal heating of steel legs
gives .036 mm relative length change. This can tilt a supported plane; it is not
necessarily the same as seam step. Local hot-sheet behavior remains governed by Phase
1B/D3. Thermal stress only follows after specifying restraints/compliance; no fully
restrained stress is presented as an actual node load.

## Hybrid support, loss of a path and dynamics

With downward coordinates u1,u2 and second ground datum e, equations are
`(k1+kc)u1-kc*u2=F1` and `-kc*u1+(k2+kc)u2=F2+k2*e`.
The determinant is `k1*k2+kc*(k1+k2)`. Nonpositive determinant is rejected as unsupported.
A negative computed grounded reaction flags loss of a unilateral contact, not tension
capacity. Results for the inputs above:

| Case | u1 / u2 mm | Ground reactions N | Interpretation |
| --- | --- | --- | --- |
| Independent | .020 / .040 | 20 / 40 | .020 mm differential compliance |
| Hybrid, matched datums | .02667 / .03333 | 26.67 / 33.33 | Less differential motion, transferred force |
| Hybrid, e=.2 mm | .09333 / .16667 | 93.33 / -33.33 | Gravity-only support opens; linear contact assumption fails |
| Support 2 lost, tie intact | .060 / .100 | 60 / 0 | Tie carries 40 N; surviving support takes total gravity in this scalar model |
| Support 2 lost, no tie | No stable solution | Undefined | Lost support cannot be hidden by a zero-load result |

For a lumped linear mode `f=(1/2π)sqrt(k/m)` [A1](d4-references.md): the sensitivity grid
spans 3.56–112.54 Hz. These are not predicted printer resonances. Effective modal mass,
damping, joint slip, belt/guide modes, moving carriage position, added print mass,
periodic drive forcing and servo interaction are omitted. Four simultaneous accelerations
may reinforce a mode; changing bed grouping changes mass and stiffness matrices.

Static lost-support cases omit impact. D3's [arrest energy](d3-calculations.md) includes
gravity during stopping and shows much higher force than static weight; peak force and
local node failure remain unknown. A backup using the same printed root is a common-mode
failure, even if it has a different actuator. No restraint or stop system is approved.
