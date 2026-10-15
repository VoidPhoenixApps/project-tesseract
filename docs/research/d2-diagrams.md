# D2 — editable conceptual top and side views

Plain-text drawings are editable sources; **not to scale, CAD or manufacturing data**.
Rectangles indicate full head/beam/column reservations, not only nozzle points.
Dimensions refer to the hypothetical [model](d2-calculations.md). X right, Y up, Z up
in side views. `n` is nozzle, `H` body, `Z` descending column; dashed areas are proposed
parking/retraction allocations, never proven routes. Each bed retains its own sheet.

## 1. Local-only versus extended bridges — top

```text
 LOCAL A0: independent axes, no seam-spanning head travel
                         +Y
      outer guides        ^         outer guides
   +------------------+   |   +------------------+
   |==== full beam1 ===|       |==== full beam2 ===|
   | [H1]--n          |       |          n--[H2] |
   |  bed1 / sheet1   |       |  bed2 / sheet2   |
   +------------------+       +------------------+
          inner guide/post strips obstruct extension
   +------------------+       +------------------+
   |  bed3 / sheet3   |       |  bed4 / sheet4   |
   | [H3]--n          |       |          n--[H4] |
   |==== full beam3 ===|       |==== full beam4 ===|
   +------------------+       +------------------+ --> +X
   Each full system has local X,Y and relative Z. Enlarging software bounds
   cannot extend rails or remove the inner posts.

 EXTENDED A+: separate Y guides, full-width independent X beams
       side guide lanes                        side guide lanes
     ||||                                           ||||
     |||| +--------------+  +--------------+        ||||
 y1  ||||=|====[H1]--n====|==|==============|========|||| beam1
     |||| |    bed1      |  |     bed2     |        ||||
 y2  ||||=|==============|==|==n--[H2]=====|========|||| beam2
     |||| +--------------+  +--------------+        ||||
     |||| +--------------+  +--------------+        ||||
 y3  ||||=|====[H3]--n====|==|==============|========|||| beam3
     |||| |    bed3      |  |     bed4     |        ||||
 y4  ||||=|==============|==|==n--[H4]=====|========|||| beam4
     |||| +--------------+  +--------------+        ||||
          <-------------- X beam 580 mm ------------>
   Y beam bands are 30 mm wide, not infinitesimal lines. X carriage travels
   along its beam; each beam has its own Y. Separate rail lanes do not prevent
   crossbeams from meeting over the bed. Vertical ordering is a separate problem.
```

## 2. Ordered shared rails versus stacked bridges — side and top

```text
 B1 TOP: shared Y rail pair, independent bridges, no passing
   rail |======================================| rail  upper bridge
        |          [H2]--n -> X                 |
        |     minimum Y separation = width+c    |
        |======================================|       lower bridge
        |     [H1]--n -> X                      |
        +--------------------------------------+
   Row jobs can stay above/below each other. Two column jobs both need the
   entire Y range; at equal requested Y the full bridges cannot share this plane.

 B2 SIDE along X; Y positions may coincide while jobs are independent
 Z ^
   |  ======== upper X bridge, z=360..390 ==================
   |                 [upper carriage]
   |                       ZZ  descending upper-head column
   |  ===== lower X bridge, z=320..350 ==XX=================
   |                                    XX overlap when crossing
   |                       ZZ
   |                       ZZ                 all bridge levels > parts
   |                       ZZ
   |                       [H2 body]
   |                          n at job height150
   |              [H1]--n at height10      [tall part]
   +================ sheets at Z0 =========================> X
   Separation of horizontal beams alone is insufficient: upper descending
   columns occupy lower beam planes. Moving the lower beam past a stationary
   column requires a verified bypass, aperture, retract route or disjoint workspace.
```

## 3. Unequal-height jobs and full-region parking — side/top

```text
 MOVING-Z SIDE: a low bridge reaches a neighboring tall object
 Z ^                          +----------+ part height200
   |                          |          |
   |  beam at90..120 ==========XXXXXXXXXX=======
   |          [H low]         |          |
   |            n at10       |          |
   +======== bed1 =========== bed2 ========================> X
   Head1 is over its own bed, yet its full-span beam intersects the other job.
   Raising only the head does not move this beam or protect its cables.

 J TOP: one active head, three entire inactive machines
        hypothetical reserved panel/frame boundary: +/-300
       +---------------------------------------------------+
       |                           chain ---> [H2] park NE  |
       |== parked beam2 spans whole X at Y=+260 ============|
       |      +----------------+----------------+          |
       |      | sheet1         | sheet2         |          |
       |======|==[H1]--n active full X beam =====|==========|
       |      |      full-region Y travel       |          |
       |      +----------------+----------------+          |
       |      | sheet3         | sheet4         |          |
       |      +----------------+----------------+          |
       |== parked beams3 AND4 at Y=-260 ====================|
       | [H3] SW <---cable                  cable--->[H4] SE |
       +---------------------------------------------------+
   Equal parked Y is not proof two beams coexist: their Z and all descending
   structures must clear. Corner nozzles at +/-260 plus outward cable80 and
   reserve2 exceed +/-300. The nominal pose fails this enclosure allocation AND carriage reach:
   required carriage +/-280 exceeds declared +/-240. Enlarging panels alone cannot fix it.
   Approach/return routes remain unproven; do not infer them from parked boxes.
```

## 4. Preserve the alternatives and fixed A/B relationship

```text
 A+ PERIMETER CANTILEVER, TOP (U; no detailed dimensions)
       outer column/support                    outer column/support
       [ROOT1]==== radial/telescoping arm ===[H1]--n
             |             bed1 | bed2                  |
 tangential  |  both linear stages independent;         | tangential
 stage rail  |  root load moment grows with extension   | stage rail
             |             bed3 | bed4                  |
       [ROOT3]==== retractable arm ===[H3]--n
   Show/size ALL arms, moving stages, columns and harnesses before counting
   clearance. Two arms drawn do not imply the other two vanish. Four analogous
   independent roots are required; opposing arms may still cross.

 XY-E HOME TOP: fixed orientations; bodies represented by full boxes
        H1=A                   H2=B=mirror-X(A)
       +---------+              +---------+
       | outward |              | outward |
       | body    |              | body    |
       +-------n-+              +-n-------+
                  central seams
       +-------n-+              +-n-------+
       | body    |              | body    |
       | outward |              | outward |
       +---------+              +---------+
      H3=R180(B)                H4=R180(A)
   Probes, ducts and umbilicals have additional boxes in code. Inward body
   extent8 is smaller than outward50 in this example. These bodies DO NOT
   rotate toward the center as they traverse it.
```

A retracting or modular XY-D system must supply its own complete intermediate-state
diagrams and swept route before clearing a transition. Detaching a beam is not an
implicit operation in these figures. Required checks include support retention, lock
state, belt tension/path, calibration and protected adjacent occupied beds at fixed datum.
