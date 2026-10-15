# D2 — reproducible geometric screening

[Source](d2_geometry.py) · [tests](test_d2_geometry.py) · [JSON](d2-results.json) ·
[report](d2-engineering-study.md). Python 3.9+ standard library, millimetres, no CAD engine.

```sh
python3 -B docs/research/d2_geometry.py
python3 -B -m unittest discover -s docs/research -p test_d2_geometry.py -v
```

Run from repository root. Stdout JSON is deterministic, with sorted keys and no timestamp.
To regenerate intentionally:

```sh
python3 -B docs/research/d2_geometry.py > docs/research/d2-results.json
```

To explore values without editing the source, import `Parameters`, use
`dataclasses.replace`, and call `mode_screen(mode, parameters, topology, mirrored)`.
The two supported structural thought experiments are `moving-bridge` and
`stacked-bridge`. Unknown topologies raise an error rather than silently reusing a
convenient kinematic model. `eligibility()` separately returns U for an unspecified
reach architecture. These are analytical tools, not motion control or fabrication data.

## Input classes and units

| Class | Input / source | Meaning and limit |
| --- | --- | --- |
| A approved | Four modules, nominal side 180 mm, D1 IDs/axes, eight group partitions; retained sheets and horizontal common-datum reconfiguration | Only nominal footprint is dimensionally approved. No approved usable print volume, height, gap, clearance, motion speed or stopping distance |
| B traceable reference | R2 Bondtech motor Ø36 × 20 mm; R3 HIWIN MGN12H assembly H13, W27, L45.4 mm; R6 igus 07.06.018.0 radius18, inner height10.3, inner width6 mm | Reference facts only; **not used as assembly geometry**. Exact revisions/limits and missing models in [catalog](d2-references.md). A motor dimension is not a complete extruder/head dimension |
| C sensitivity | All other numbers below and in `Parameters`/`components()`/`results()` | Explicitly invented research bounding boxes. Not purchased parts, verified fits, approved limits or substitutes for vendor CAD |

C defaults: separated gap40; joined gap0; outer inset5; nozzle head-Z travel300;
alternative downward bed-Z travel200; required object-height bound200. Hypothetical
carriage-center XY limits ±240 and Z50..350 give a nozzle Z range0..300 with offset
Z=−50. Plate/mechanism boxes extend 5 mm past each nominal footprint and Z=−40..−5.
Bed-side travel is a declared alternative envelope only, not active in the two mode
screens; the bed-Z transform test exercises the relative-object case separately.

Head A about nozzle: body (−50,−8,10)..(8,50,70); hotend (−6,−6,0)..(6,6,20);
probe (−25,−10,2)..(−15,0,25); carriage (−40,5,35)..(0,35,65).
Nozzle minus carriage-reference offset (20,−20,−50). Cable reservation
(−50−r,15,30)..(−40,35,100), r=30; filament reservation
(−40−f,20,60)..(−20,40,130), f=40. These are coarse enclosing volumes, not actual
chain curves, duct meshes or service access. All transform with fixed head orientation.

Beam X=−290..290; Y extends 15 mm each side of nozzle Y range; depth30. Moving beam
lower face is nozzle Z+80. Fixed beam lower faces 320/360/400/440. A descending
column extends from nozzle Z+35 to beam upper face, with local X=−40..0,Y=5..35;
orientation transforms with head. Columns model a broad obstruction, not a telescoping
mechanism. Beam-to-head attachment and guide constraints are unspecified, so the
assembly's existence is not established by drawing both boxes.

Nozzle corner parks at (±260,±260), Z as in [matrix](d2-mode-coverage.md). Frame inner
half-width320 minus 20 reservation leaves ±300 for moving boxes; vertical clear box
−50..600. The 20 mm reservation lumps enclosure/structure allocation but does **not**
model actual fixed guide posts, rail end stops or panel latches. Numerical reserve2
inflates one collision operand; inflating both would double the stated pair reserve.
Own deposition contact is excluded from other-object comparisons; other active jobs
use a conservative solid box over their whole region at heights10/150/60/200 in
assignment order. Complete-job height histories and exact parts are not modeled.

## Algorithms and interpretation

A box uses closed XYZ intervals, including contact at equality. For fixed orientation
and piecewise-linear translation, every intermediate position of a segment lies in
the hull of its endpoint boxes. `sweep()` therefore conservatively encloses **the whole
path**, not just its endpoints. It can overestimate diagonal or multi-leg motion.
`path_hits()` applies exact continuous box collision detection (CCD) separately to
each linear segment against a stationary box. `ccd()` also accepts two moving boxes
on a synchronized linear interval, using relative velocity.

For each axis, overlap requires `b.lo − a.hi ≤ v*t ≤ b.hi − a.lo`, with t∈[0,1].
Intersect the three resulting time intervals. Zero relative velocity needs an initially
overlapping interval. Empty intersection is no collision for the exact specified boxes;
a nonempty interval identifies contact even when both endpoints are clear. This is
exact for translating AABBs, not curved/deforming/rotating mechanisms. Mirror-X and
180° rotations preserve axis alignment and are fixed before motion.

For asynchronous jobs, `mode_screen()` encloses each head's entire rectangular operational
region at a stated layer, the full beam sweep, and its Z-column. Comparing these hulls
screens all relative XY phases conservatively at those fixed heights; it does not rely
on convenient synchronization. Overlap is labeled a candidate, not inevitable contact.
Nonoverlap at one height vector does not prove arbitrary-height clearance. Regions and
carriage containment are calculated separately so nozzle reach cannot mask a collision.

True rotating/reconfiguring mechanisms, flexible cables, unknown supports and missing
axis definitions are **unresolved**. The helper `classification()` cannot return a
clear model result with incomplete geometry or unknown kinematics. Any explicit active or parked reach failure is REACH_REJECTED; otherwise the
structural screen remains U even where counted candidates are zero. No global collision-free
path planner or physical clearance certification is claimed.

## Generated comparison results

Counts refer to named component pairs, not number of physical crashes. One physical
obstruction can produce multiple pair candidates. These counts reproduce from JSON.

| Mode | Moving bridge machine / other-object candidates | Fixed stack machine / other-object candidates | Bed-mechanism candidates, both | Components outside reserved enclosure, both |
| --- | --- | --- | --- | --- |
| S | 0 / 2 | 2 / 0 | 0 | 0 |
| R | 0 / 0 | 0 / 0 | 0 | 10 |
| C | 3 / 1 | 2 / 0 | 0 | 10 |
| M12 | 3 / 1 | 1 / 0 | 0 | 5 |
| M34 | 3 / 1 | 1 / 0 | 0 | 5 |
| M13 | 6 / 1 | 2 / 0 | 0 | 5 |
| M24 | 6 / 1 | 2 / 0 | 0 | 5 |
| J | 3 / 0 | 1 / 0 | 0 | 15 |

Every default active-region nozzle containment check succeeds. However, every mode
with an inactive head has **REACH_REJECTED parking**: nozzle parks at ±260 require
carriage coordinates ±280, exceeding the declared ±240 travel by 40 mm. S has no
inactive heads and remains U. Reducing park to220 reaches the stroke boundary but
does not establish structural clearance or a safe route. All actual architectures
remain unvalidated. Active reach is not complete-machine feasibility. Zero bed-mechanism candidates follows
from the assumed below-datum boxes, not proof of real docking locks or wiring clearance.
The J parked-beam overlaps include parked-to-parked structures: parking must be mutually
compatible as well as clear of the active head. Model parks are deliberately tested,
not optimized to hide interference.

Continuous witness: a body X/Y±5, Z0..20 translating nozzle X−30→30 at Y0,Z10 past an
obstacle X±2,Y±10,Z0..100 has clear endpoints but contact during
`t=0.38333333333333336..0.6166666666666667`. A separate test crosses two moving boxes,
and a parallel-motion test is clear despite overlapping spatial hulls. A diagonal
false-positive fixture explicitly prevents equating hull overlap with physical collision.

Sensitivities in JSON:

- Moving stack level offset: height divergence100/200/300 × beam depth20/30/50;
  offset must exceed divergence+depth+2 in the overlapping fixed-order scenario.
- Body inward/outward extent and reserve: 27 mirrored/common comparisons.
- Park220/260/300 × cable radius18/30/50: required half-width
  `park + 50 + radius + 2 + 20`, ranging310..422. Filament or other parts can dominate;
  this particular lower bound is cable-based, not the entire enclosure solution.
- Separated gaps20/40/80 for all eight modes: final region bounds and required travel
  change; nominal module size stays180. A gap200 negative test exceeds available travel.

Repeat with larger actual uncertainty, full strokes, job geometries and braking margins
once defined. Sweeping an arbitrary sensitivity range does not establish manufacturing
limits, a probability distribution or a safe operating envelope.

## Remaining analytical limits

No actual component assemblies, fixed supports, belt runs, carriage order solver,
automatic extension joints, thermal bow, compliance, vibration, cable deformation,
collision response time, sensor fault model or service extraction motion exists here.
Not all transition paths are supplied: the model implements conservative sweeps and
specific adversarial tests rather than pretending to route unspecified mechanics.
A later detailed model must resolve each omission before a true clearance can pass.
No paid/proprietary CAD dependency or vendor model has been introduced.
