# Configuration and motion feasibility

**Conceptual geometry, not a collision-checked assembly.** Coordinates and envelopes below are deliberately explicit so a later model can disprove them. All dimensions are mm. No Z displacement or sheet removal is used to convert layouts.

## Datums, envelopes and six target layouts

Frame X points right, Y up in top view, Z upward; yaw is rotation about Z. Bed labels remain A northwest, B northeast, C southwest, D southeast; labels never exchange quadrants. Sheet tops target the same datum Z = 0. Printing Z is unspecified. Let nominal sheet side `b = 180`, demonstration docking gap `g = 0.20`, joined half-pitch `q = (b+g)/2 = 90.10`, separated half-pitch `s = 130`, stroke `d = s-q = 39.90`. The 0.20 gap is a cold geometric example, **not a thermal design or approved limit**; see [calculations](preliminary-calculations.md).

```text
                 +Y                  +X ->
 I: separated       H: two rows       V: two columns
 [A]     [B]         [A]|[B]           [A]     [B]
                                      ---     ---
 [C]     [D]         [C]|[D]           [C]     [D]

 MH: row + singles  MV: col + singles J: four joined
 [A]|[B]            [A]     [B]       [A]|[B]
                    ---              ---+---
 [C]     [D]        [C]     [D]       [C]|[D]
```

Whitespace is schematic; coordinates below control. Mirror/rotate mixed layouts to select the other pair. Four individual sheets remain installed, including J.

| Mode | A (X,Y) | B (X,Y) | C (X,Y) | D (X,Y) |
| --- | --- | --- | --- | --- |
| I | (-s,s) | (s,s) | (-s,-s) | (s,-s) |
| H | (-q,s) | (q,s) | (-q,-s) | (q,-s) |
| V | (-s,q) | (s,q) | (-s,-q) | (s,-q) |
| MH | (-q,s) | (q,s) | (-s,-s) | (s,-s) |
| MV | (-s,q) | (s,s) | (-s,-q) | (s,-s) |
| J | (-q,q) | (q,q) | (-q,-q) | (q,-q) |

I has an 80 mm inter-sheet gap and 440 mm overall sheet envelope. J has a 360.20 mm envelope, illustrating why nominal 360 mm is not an exact usable dimension. No head or cable allowance is included in those two numbers.

### Physical packaging assumptions to test

At each height band, use the actual swept solid enlarged by uncertainty and stop distance, not just the sheets. A possible packaging allocation is:

| Height band relative to top | Conceptual allocation, not selected parts |
| --- | --- |
| Z = 0 to -8 | Separate sheet, magnetic layer, plate; edges have no projecting clips, handles or tabs into joining faces |
| -8 to -35 | Heater, insulation, strain relief and three-point hot-plate mounts; inward envelope at most 180 mm per module |
| -35 to -95 | Carrier bearings, horizontal latches and stacked guides; moving per-module envelope provisionally 160 × 160, leaving 20.20 mm between adjacent carrier edges at J |
| Below -95 / outside array | Frame bracing, actuators and separated cable corridors; dimensions to be engineered |

These allocations are feasibility hypotheses, not a BOM or proof of available component fit. Bed thickness affects bearing moment arms and thermal stand-offs. A 190 mm undercarriage cannot occupy the assumed same-height J pockets: overlap is 9.80 mm. Move its protrusions outward, redesign it, or allocate a permanently different under-bed band; do not raise/lower a bed during conversion. Below-bed mechanisms may occupy different fixed height bands while every sheet stays at Z = 0.

For same-band rectangular envelopes i,j, require `abs(dx) >= (wi+wj)/2+c` OR `abs(dy) >= (hi+hj)/2+c`. Docking faces instead use their explicitly designed engagement/gap. An illustrative noncontact allowance `c = 10` must later include positioning error, thermal motion, flex, stop distance and build uncertainty. Do not inflate sheet rectangles by 10 mm at their intentionally joined edges. No component may protrude through a reserved neighbor pocket. Cable radius must meet its selected cable's dynamic rating; allocate its complete loop and endpoints, not a centerline.

## Transition certificate for independent motion

For A1 and other truly independent XY mechanisms, reach every table row from I by monotone axis moves within each quadrant. I→MH moves only A and B along X; I→MV only A and C along Y. I→H moves both rows along X; I→V both columns along Y. I→J first forms H, then translates the empty rows inward along Y (beds can be commanded individually if their docking interfaces do not rigidly link them). Throughout these paths opposite quadrant sheet centers remain separated by at least `b+g` along X or Y. Carrier envelopes of 160 mm therefore retain at least 20.20 mm clearance under the assumptions above. Bed orientation remains fixed.

For arbitrary empty-machine transitions, disengage applicable locks, expand monotonically back to I, then execute the target path. Release both adjoining edges before retracting a corner from J; trapped undercuts are prohibited. This is a constructive path for **the specified rectangular envelope model**, not proof about bearings, arms, cables or toolheads omitted from it. Docking hardware must accept those approach directions or add an explicit approach waypoint inside the reserved quadrant.

With an active bed or active joined region, freeze its carrier, lock state, thermal setpoint and object volume. Only use the subset of paths that leaves it unchanged. Example: while C and D print at I, A+B can form MH. Example of a prohibited request: a J job cannot be split while it exists. A busy bed at a separated position cannot be demanded at a new joined coordinate. Queue such jobs; do not silently move the active surface. Add the moving toolhead's full time-dependent workspace and all objects, purge structures, cables and parking positions to collision checks. Independent drives do not prove vibration isolation.

## Mechanism-specific top views and paths

### A — independent XY sleds

```text
 fixed NW pocket                  fixed NE pocket
 Y guide: [ X slide <-> A ]        [ B <-> X slide ] :Y guide
                  ^ v              ^ v
 ---------------- central seams -----------------
 Y guide: [ X slide <-> C ]        [ D <-> X slide ] :Y guide
 fixed SW pocket                  fixed SE pocket
```

A1 uses four identical two-axis assemblies mirrored around the frame: eight controlled translations plus locks. Each has at least d travel per axis and the envelope allocation above. The transition certificate applies. A2 shares **stationary** guide foundations but uses independent carriages and noncrossing order; it can use the same certificate if cross-axis slides remain in their pockets. A3 nested stages per bed are still independent XY but put stacked bearings and motors into the 60 mm provisional mechanism band; exceeding it requires a deeper static frame. Shared full-width *moving* rails are B, not A2. Belt drives need docking to remove holding compliance; screws reduce some holding compliance but introduce nut backlash, heating and motor packaging. Remote belt routing reduces moving mass but adds tension reactions and sweep corridors.

### B — moving rows or columns

```text
 frame Y guides   ||== A <-> ===== B <-> ==||  y = u
                  ||== C <-> ===== D <-> ==||  y = v
                    four independent X slides
```

B1 has four X coordinates and two row Y coordinates (six axes). I→H/MH uses X only; I→V uses rows inward at fixed x=±s; I→J uses H then both rows inward. Row beams must pass below the 180 mm plate band, remain separated when `u-v=180.20`, and provide separate cable loops. For canonical MV, `yA != yB` and `yC != yD`; B1 cannot do it. The transposed column version has the symmetric MH problem.

B1-wide recovers a *different* MV layout with A=(-s,q), C=(-s,-q), B=(s,q), D=(s+b+c,-q)=(320,-q). First move empty D outward from x=130 to 320 while rows remain separated, then move rows to ±q. B and D are now separated by 190 mm along X, leaving 10 mm between their sheet projections; they are not inadvertently joined across Y. A/C form the sole pair. Sheet envelope spans x=-220 to 410: 630 mm, before structure/cables/head access. Reverse via row separation before returning D. This requires D's X travel of 190 mm plus normal stroke, a long bottom row, and wider head reach. A mirrored layout needs corresponding travel on the opposite side. It does **not** preserve an active B or D during row convergence. B2 adds independent per-bed Y compensation (two differential trims plus two row axes can span four Y coordinates), reaching all canonical layouts at roughly eight axes; the planner must account for trim stroke and row motion even when a plate is position-compensated.

### C — mechanical lattice

```text
 C0 rectangular lattice           C1 independently sliding branches
 A ===== x-pitch ===== B          frame -> [XY branch A] [XY branch B]
 |                    |          peripheral telescopes below plates
 y-pitch          y-pitch         frame -> [XY branch C] [XY branch D]
 |                    |
 C ===== x-pitch ===== D
```

C0 has global horizontal and vertical pitches. Vary X alone to form H, Y alone to form V, both for J; inverse expansion restores I. It cannot form either mixed mode because closing one parallel edge closes the opposite edge. A single scissor input tying both pitches cannot even form H or V. Adding clutches without independent grounded support leaves a released bed underconstrained. A four-edge closed rectangle still forces opposite lengths equal; independent motors merely fight those constraints.

C1 breaks that loop using four grounded, guided telescoping branches with independent orthogonal slides or serial parallelograms that preserve orientation. It can follow the A certificate if branches remain in dedicated under-bed pockets and have full d × d reach; it is then a joint-heavy XY implementation. Articulated bars require fixed separate bands at crossings and guards around every pinch point. A deformable rhombus with rotating plates does not preserve adjoining square-sheet orientation; add anti-yaw constraints and check singularities. Telescoping support overlap must remain adequate at I, where stiffness is lowest. These repairs preserve requirements but discard the simplicity of a uniform lattice.

### D — linkage-supported platforms

```text
 O_NW -- elbow -- A                B -- elbow -- O_NE
       dedicated arm pocket      dedicated arm pocket
 O_SW -- elbow -- C                D -- elbow -- O_SE
 O = grounded pivot; links and orientation followers below plates
```

D0, one pivot and one rigid swing per bed, only reaches a circular arc. For the screened positive-quadrant outer pivot (300,300), a radius of 240.42 reaches I at (130,130), but the H/V endpoint radius is about 270.11 and J requires 296.84; mirror this arrangement for the other beds. It also rotates the bed unless a follower is added. Thus this specific outer-pivot design fails the other modes. A specially placed pivot at the center of the four target corner positions could put all four on one circle, but would require a separate orientation follower and a new collision/path study; endpoint coincidence alone does not prove that alternative feasible. The matrix rejection applies to the screened outer-pivot swing, not every conceivable one-input mechanism.

D1 gives each bed a planar two-revolute-joint arm plus a **separate orientation-preserving linkage** (or controlled wrist, making twelve rotary axes instead of eight). Illustrative positive-quadrant pivot (300,300), link lengths 180 and 160: the required square x,y ∈ [90.1,130] has radial reach 240.42–296.84, inside the 20–340 annulus. `cos(theta2)=(r²-l1²-l2²)/(2*l1*l2)` stays away from ±1; choose and retain one elbow branch. Continuous inverse kinematics along the A path is possible for the point endpoint. The arm and follower sweeps must be assigned separate fixed under-bed bands or disjoint outer pockets; the annulus calculation **does not certify those solids**. Mirrored arm bands need different static pedestals to put all sheets at the same Z. Long overhangs, follower collisions and vertical bending make packaging unresolved rather than demonstrated compact feasibility.

D2 grounded five-bar drive can remotely actuate two endpoint coordinates with two motors per bed; an endpoint alone does not fix yaw. Add an orientation parallelogram or wrist and avoid both serial and parallel singularities along every path. It inherits the same envelope obligations but has two load paths. No link dimensions/singularity map has been developed for D2, so its reach is conditional rather than demonstrated.

### E — serial shared mover and horizontally captured pallets

```text
 top:    [A on XY support]          [B on XY support]
 bottom: [C on XY support]          [D on XY support]
 below:  common X/Y tug -> horizontal dog -> one empty carrier
```

E1 replaces eight continuously engaged drives with one two-axis tug and a dog engagement actuator, while each bed retains its own supported XY guidance and positive parking locks. Engage the dog horizontally, verify capture, release that bed's lock, move one A-certificate segment, relock/verify, disengage. Others remain mechanically registered. The tug and retractable dog need an unobstructed fixed lower band across the array; attachment points must remain reachable at all endpoints, without reaching through a busy bed's cable loop. Sequential moves suffice; simultaneous transport is not required by the layouts. Complexity moves from motors into transfer safety, locks, cable routing and tug access. E2 switched orthogonal rails need uninterrupted vertical support through intersections and automatic horizontal route selection; a lifting turntable or manual rail exchange violates the conversion requirement. Do not count E2 feasible until intersection support is designed.

## Capability matrix

P = constructive rectangle-model path above, conditional on packaging; W = wide/staggered path; C = added mechanism/envelope analysis required; F = stated mechanism cannot meet mode. None means physical validation.

| Candidate | I | H | V | MH | MV | J | Can move some empty modules with busy neighbors? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 independent quadrant XY | P | P | P | P | P | P | Kinematically yes; head/cable/vibration proof pending |
| A2 stationary shared guides / A3 nested per-bed | P | P | P | P | P | P | As A1 if support truly independent |
| B1 compact rows | P | P | P | P | F | P | X only when row containing busy bed stays fixed |
| B1-wide rows | P | P | P | P | W | P | Same restriction; wide-mode convergence needs both rows idle |
| B1 compact columns | P | P | P | F | P | P | Y only when busy column stays fixed |
| B2 differential trims | P | P | P | P | P | P | Conditional; shared beam disturbance persists |
| C0 two-pitch rectangle | P | P | P | F | F | P | Generally no pitch change with busy bed |
| C0 one-input symmetric scissor | P | F | F | F | F | P | No independent conversion |
| C1 decoupled grounded branches | C | C | C | C | C | C | Only with independent support/actuation |
| D0 screened outer-pivot swing | P | F | F | F | F | F | Restricted arc only, not full mode set |
| D1 oriented articulated arm | C | C | C | C | C | C | Endpoint independence; full sweep unproved |
| D2 five-bar + orientation | C | C | C | C | C | C | Grounded motors help; singularities/sweeps unproved |
| E1 shared tug + XY pallets | P | P | P | P | P | P | Sequentially, subject to tug/cable/lock envelope |
| E2 switched rails | C | C | C | C | C | C | Intersection support and routes unresolved |

This matrix deliberately distinguishes an analytical endpoint/path construction from full mechanical feasibility. Next-stage clearance evidence must include assembled thickness, bearings, fasteners, latches, cables, sheet tabs, heads and printed objects, with tolerances and fault stopping distance. No candidate is permitted to bypass that gate.
