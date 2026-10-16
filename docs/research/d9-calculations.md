# D9 — bounded calculations and executable counterexamples

[Source](d9_support.py) · [tests](test_d9_support.py) · [raw JSON](d9-results.json).
All numerical inputs below are hypothetical sensitivities inherited from D3 or clearly
identified extensions, **not selected hardware, measured masses, ratings or limits**.
The code directly calls unchanged D3 functions; no FEA or vendor stand-in is created.

## Reproduction

Python 3.9+ standard library, repository root; no installation/network/hardware required.

```sh
python3 -B docs/research/d9_support.py > /tmp/tesseract-d9-results.json
cmp docs/research/d9-results.json /tmp/tesseract-d9-results.json
python3 -B -m unittest discover -s docs/research -p 'test_d9*.py' -v
```

The public functions accept explicit inputs. Deliberately change `results()` for a
new sweep, regenerate JSON and rerun tests. Graph/transfer checks accept declared
assumptions, not a sensed machine; they are not deployable safety logic. An empty
error list is only internal consistency of those assumptions. No capacity, six-DOF
rank, continuous trajectory, thermal contact or coupled dynamic solver is present.

## Signed reactions and moment

Reuse D3 `R−=F(1/2−e/d)`, `R+=F(1/2+e/d)`, with F=mg, g=9.80665 m/s²,
d=240 mm, m=12 kg. e is signed eccentricity along the support spacing. Two vertical
support lines represent one-plane statics, not a real four-bearing assembly.

| e (mm) | R− (N) | R+ (N) | Interpretation |
| --- | --- | --- | --- |
| −150 | 132.38978 | −14.70998 | Positive-side compression contact cannot remain closed without hold-down |
| −120 | 117.67980 | 0 | Contact boundary; no robustness margin established |
| 0 | 58.83990 | 58.83990 | Symmetric assumed loading only |
| 120 | 0 | 117.67980 | Opposite contact boundary |
| 150 | −14.70998 | 132.38978 | Negative-side lift-off or tensile restraint demand |

Moment balance remains signed: `(R+−R−)d/2=Fe`; at e=150 mm, M=17.65197 N·m.
A negative reaction falsifies a compression-only *contact assumption*, not every
possible topology. A hold-down changes the contact model and must withstand real
forces/moments. Four supports require compliance/preload; do not divide weight by four.
D3's 1/2/3/4 kg bed example also gives R group masses 3/7 kg versus C 4/6 kg; equal
nominal areas do not imply equal lifting load. A full platform adds its own mass once.

## Reach and guide mismatch

D3's ideal prismatic cantilever uses `M=FL`, `δ=FL³/(3EI)` with consistent N/mm units.
D9 extends its 20 N, EI=10^7 N·mm² example across reach; these are abstract lengths,
not selected rails or approximated vendor components.

| L (mm) | Root moment (N·m) | Ideal deflection (mm) |
| --- | --- | --- |
| 90 | 1.8 | 0.486 |
| 180 | 3.6 | 3.888 |
| 360 | 7.2 | 31.104 |

Doubling reach doubles moment and increases ideal deflection eightfold. The largest
example is a warning that small-deflection assumptions become questionable, not a
credible machine prediction. No inferred allowable reach follows. Distributed mass,
joints, torsion, column buckling, modal response, actual section and temperature are
absent. D4's separate .112 mm member + .180 mm printed-root example shows why a
beam-only improvement cannot resolve nozzle error. B retains drop structures and XY
cantilevers; H's extra moving Z column cannot be analyzed only at minimum reach.

D3 guide model: `mismatch=initial+H*tan(phi)` and
`Floop=k*max(0,abs(mismatch)−free)`. For initial=.02 mm, phi=.05°, free=.05 mm,
k=1000 N/mm, D9 tests H=0/100/200 mm: mismatch .02000/.10727/.19453 mm and
loop force 0/57.27/144.53 N. Those are synthetic spring-model results, not rail
ratings. Unilateral contact, friction, preload and nonlinear stiffness may change them.
A rigid tie can create force even at zero payload; disconnecting a motor cannot release
a hard guide constraint. Seam tilt remains separate from mean height.

## Arrest sensitivity and asymmetric catch warning

Reuse D3 `drop=v0*t+gt²/2`, `v=v0+gt`, `E=mv²/2+mgs`, `Favg=E/s`.
The mass sweep 1/4/12 kg contrasts possible small and grouped loads without asserting
which is a head or a bed. v0=.01 m/s downward; delay 10/20/50 ms; stop stroke s=1 mm.
No listed delay/stroke is safe or physically available.

| Delay (ms) | Pre-catch drop (mm), all masses | Total descent (mm) | Favg at 1 / 4 / 12 kg (N) |
| --- | --- | --- | --- |
| 10 | 0.59033 | 1.59033 | 15.65 / 62.58 / 187.75 |
| 20 | 2.16133 | 3.16133 | 31.05 / 124.21 / 372.62 |
| 50 | 12.75831 | 13.75831 | 134.97 / 539.89 / 1619.68 |

At equal speed/delay/stroke, descent is independent of mass and average force scales
with mass. Real friction, inertia, initial speed, catch law and external forces can
change motion; this is neither peak force nor an upper bound. An upstream motor brake
cannot absorb energy from a disconnected load through a broken transmission.

For two *uncoupled* equal-speed coordinates, the 10 versus 20 ms examples differ in
pre-catch descent by 1.57100 mm. That is a counterexample to assuming simultaneous
arrest; it is **not** a predicted seam step in a tied pair. A rigid tie, guide and
adhered object convert differential motion into forces/rotation. Their dynamic model,
contact, catch timing and peak anchor loads remain unknown. Do not sum two independent
catch forces as a validated grouped-stop load. Injury, equipment and print-quality
acceptance limits must be separately justified.

## Model boundaries and falsifiers

The test inventory checks exact eight partitions, transitive affected membership for
64 ordered pairs, declared idle-load coverage, failed common anchors, upstream brake
counterexamples, stale/future/wrong-epoch/disagreeing/upstream observations, supported
handoff and invalid intermediate states. Twenty-four subcases mutate six obligations
at each of four declared handoff states. Positive cases show the checker is not an
always-reject predicate; they do not describe a built mechanism. Observation age .2 s
in a unit test is an arbitrary software boundary, not a response-time requirement.

No numeric uncertainty distribution is invented. Mass/COM, stiffness, reaction sensing,
pose calibration, thermal drift and latency all require measurements. Correlated shared
frame and thermal errors forbid unqualified root-sum-square combination; D3's seam
budget remains illustrative. The [review packet](d9-review-packet.md) sets the required
measurement record and decision rule before any future experiment.
