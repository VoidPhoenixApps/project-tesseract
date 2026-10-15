# D1 — editable conceptual kinematics and power paths

**All diagrams are conceptual, not validated CAD, to scale, or manufacturing data.**
Markdown/text is the editable source. [Study](d1-engineering-study.md) and
[calculations](d1-calculations.md) define the unresolved dimensions.

## Top-view mode map and height ownership

X points right, Y up, Z toward viewer. Beds: 1 NW, 2 NE, 3 SW, 4 SE.
Adjacent joined IDs share one job height coordinate. Sheets remain separate.
Lines between cells below denote nominal seams, not structural joints.

```text
 S: four jobs           R: horizontal pairs     C: vertical pairs
 [1:h1] [2:h2]          [1:hA | 2:hA]            [1:hA] [2:hB]
 [3:h3] [4:h4]          [3:hB | 4:hB]            [3:hA] [4:hB]

 M horizontal          M vertical               J: one head/job
 [1:hA | 2:hA]         [1:hA] [2:hB]             [1:hJ | 2:hJ]
 [3:hB] [4:hC]         [3:hA] [4:hC]             [3:hJ | 4:hJ]
 Also pair 34.         Also pair 24.             Four retained sheets.
```

For Z-A the h groups belong to independently moving heads; beds stay at the
printing datum. For Z-E they belong to separate lift groups. For Z-F partial modes,
these diagrams require an E-like local-lift solution or a genuinely sectional frame;
a unified frame alone supplies only hJ. No horizontal reconfiguration occurs by Z motion.

## Exact XY-E relationship and reach

```text
             +Y
              ^
 H1 TYPE A                             H2 TYPE B
 Head | Fan                            Fan    | Head
 Fan  | Nozzle                         Nozzle | Fan
             nozzles at inner corners
              ... central bed seams ...
 Fan  | Nozzle                         Nozzle | Fan
 Head | Fan                            Fan    | Head
 H3 TYPE B                             H4 TYPE A             +X -->

 H4 = rotate180(H1). H3 = rotate180(H2).
 Type B = left/right mirror counterpart of Type A.
 Nozzle is the inward corner; extruder bulk is outward at home/quadrant position.
```

“Outward” describes the intended quadrant arrangement, not a body that continuously
rotates when crossing a seam. For fixed orientations use transforms about each nozzle:
H1=identity(A), H2=mirror-X(A), H3=rotate180(H2), H4=rotate180(A). Mount translations
are separate. Reflection is a design operation, not a claim that chiral purchased
motors, fans or extruders can physically be mirrored.

| Check for only two assemblies | Evidence needed / possible failure |
| --- | --- |
| Mounts/rail/belt connections | Diagonal 180° mount congruence including fastener access; handed external adapters count as additional distinct interfaces |
| Filament feed | Same local entry and rated bend radius after rotation; overhead feed may require different guides despite common head BOM |
| Cooling | Mirror ducts may use the same purchased fan without mirroring rotor; measure flow and heat effects in both orientations |
| Probe/nozzle offset | Probe remains inside accessible surface at all needed calibration points; inward nozzle does not guarantee inward probe reach |
| Wiring/strain relief | Connector access, chain attachment and bend/twist envelopes through full XYZ travel and parking |
| Service | Heater, nozzle, fan and extruder replacement with retained neighboring heads and removable panels; no hidden unreachable fasteners |

Two complete assemblies are **achievable as a design hypothesis**, but not established
for any selected hardware. Conventional common orientation can reuse more head parts
and simplify service offsets, while placing more bulk between some inward nozzles.
XY-E can move that bulk outward locally, yet increase outer frame/parking width and
change probe/duct access. Neither wins without the same full-travel comparison.

```text
 REACH TEST (top; not actual dimensions)
       outer park H2/H3/H4 + their beams and cables
       +--------------------------------------+
       |     candidate P1 carriage travel     |
       |   [bed1] seam [bed2]                 |
       |   [bed3] seam [bed4]                 |
       +--------------------------------------+
 Required J path must lie inside N1 = P1 + rotated nozzle offset,
 and outside obstacles inflated by the full oriented head/gantry envelope.
 For R and C, TWO such pair-spanning paths must coexist independently.
```

## Side-view kinematics and unequal-height interference

```text
 Z-A (beds fixed)                         Z-E (head framework fixed in Z)
 frame | guide1  [XY beam/head1] ^        frame ----- [H1] --- [H2] -----
       | guide2  [XY beam/head2] | Z                 object1   object2
       |          |    body     v                  [bed1]     [bed2]
       | object1  v nozzle                         [lift1]    [lift2]
       | [bed1]      [bed2]                           | group drive |
 base  +==carrier supports==+                  guides/supports --> base

 Low head at h1 ---- [body] ---> | tall object on another bed |
 Parked beam at Zp  ============| also an obstacle           |
 Head lift alone cannot clear an entire low crossbeam or its cables.
 Objects occupy bed-relative volumes transformed by each bed's current Z.
```

Z-A support path is bed→carrier→base plus head→beam→Z guides→frame. Z-E support path
is bed→carrier→lift→guides/drive restraint→transport/frame. Three-dimensional collision
analysis must include those entire structures. The figures deliberately do not claim
that stacked crossing beams fit within a full height envelope.

## Z-E coupling graphs: three distinct kinds of edge

```text
Position graph:       P = holds horizontal registration; not a gravity rating
Structural graph:     L = carries specified gravity/moment loads
Transmission graph:   T = transmits drive torque; not necessarily support

 R group edges:  1---2    3---4        C group edges:  1---3    2---4
 M group edges:  1---2    3    4       (or 34, 13, 24)
 J connected example T graph:  1---2
                              |
                              3---4     (three edges; no torque-loop closure)

 Each drawn edge must specify P / L / T separately.
 Real L contacts and guide freedoms may differ from this T graph.
```

## Z-F power selection and support handoff

```text
 LITERAL BELT-PATH SWITCH (one schematic channel; repeat/specify group ownership)
 motor --> same timing belt --> movable idlers/selector --+--> local lift
                                                         +--> secondary frame lift
       Investigate full path length, tension, wrap, phase and tracking during shift.
       No state is allowed to suspend bed weight from an unengaged/slack path.

 POSITIVE TORQUE-PATH ALTERNATIVE
 motor --> retained/tensioned input --> positive selector --+--> fixed belt: local lift
                                                          +--> fixed belt: frame lift
       Actuator positions selector; positive engagement carries torque.
       Separate restraint holds gravity during selection; selector is not a brake.

 GRAVITY / INDEXING (independent of either power diagram)
 hot sheets/plates --> thermally relieved mounts --> cold carriers
                              |                           |
                    local guided supports       seated load contacts
                              |                           |
                         restraint/base     secondary frame + cold cross
                                                        |
                                              guided lift + restraint --> base
```

For S: four local paths active, secondary frame clear and isolated. R/C/M: selected
local lifts form the two/three independent E-like groups; secondary frame isolated.
For J: all four empty carriers seat at the common horizontal datum before the frame
assumes load. An alternative sectional frame must reproduce R/C/M ownership explicitly.
These are conceptual state allocations, not an executable switch sequence.

```text
 normal printing
       |
 affected modules empty + objects elsewhere protected + supported at common datum
       |
 isolate motion / verify passive support (old drive still restrained)
       |
 horizontal dock + verify location and structural seating
       |
 phase-align unloaded candidate drive path; verify engagement and exclusive ownership
       |
 controlled load transfer while independent fall protection remains available
       |
 verify support/reactions and position --> enable selected group's printing motion

 Any disagreement/power loss --> restrained fault state --> inspect/re-establish state
 No automatic unlock, rehome through an object, or resume from remembered commands.
```

The exact force-transfer order remains unresolved: two stiff drives engaged at once
can fight, while neither engaged can drop the bed. A supported unloaded transition
must avoid both. The [failure study](d1-failure-study.md) identifies evidence needed
before these blocks can become a reviewed physical procedure.
