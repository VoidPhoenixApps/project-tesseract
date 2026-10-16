# D8 — editable conceptual diagrams and decision tree

[Study](d8-assembly-study.md) · [motion contract](d8-motion-contract.md).
Plain text is the editable source. Diagrams are not to scale and do not depict
selected components, validated geometry, safe motion or manufactured CAD.

## Top view: full-length sliding rail, not just its nozzle

```text
                       +Y (north)
  outer tail         root X=-320                         root X=+320
  <====== rail ======[Y slide]=====* nozzle    nozzle *====[Y slide]=====>
                     independent Y               independent Y
                           bed 1 | bed 2
                           ------+------      seams depend on mode
                           bed 3 | bed 4
  <====== rail ======[Y slide]=====*          *==========[Y slide]=====>
                       -Y (south)                         +X east ->

  WEST EXAMPLE, all mm hypothetical:
  print far edge:       tail=-425 ----- root=-320 ---------------- tip=175
  park at X=-260:       tail=-860 ---------------- root=-320 -- tip=-260
  Rail length remains 600 in BOTH poses. Root engagement must remain >=30.
  Enclosed inner boundary=halfwidth-20; reserve=2 is not a stop distance.
```

Each guide level is distinct in this thought experiment. Projecting them onto the
same page neither proves contact nor proves independent 3D clearance. The sketch
omits many dimensions; the code/contract owns all numerical hypotheses.

## Side view: identical XY levels, different relative Z

```text
 H: independent full-range head Z           B: independently supported bed-group Z

       column protrudes as head rises       fixed XY rail ======= root
       |                                    | fixed drop
 XY ===|========= root                     head/nozzle z=0 ----- current object top
       |                                    | object height h
       head at z=h ---- object top            | retained object, not erased
       |                                     bed z=-h ==========
       | object height h                     local guides/restraints: UNRESOLVED
 bed z=0 ============                        heater cable travels XYZ: UNRESOLVED

 H column lower face=z+35; top=z+level+30.   B column lower=35; top=level+30.
 These boxes do not specify a safe actuator or demonstrate stiffness/restraint.
 Finished H object stays tall. Finished B object stays at last depth; no auto-raise.
```

## Eight final grouping diagrams

```text
 beds numbered NW=1, NE=2, SW=3, SE=4; bars below indicate job grouping only
 S            R            C            M12          M34
 [1] [2]      [1---2]      [1] [2]      [1---2]      [1] [2]
 [3] [4]      [3---4]      [|] [|]      [3] [4]      [3---4]
                          [3] [4]
 M13          M24          J
 [1] [2]      [1] [2]      [1---2]
 [|]          [ ] [|]      [|   |]
 [3] [4]      [3] [4]      [3---4]

 Owners: S=1,2,3,4; R=1,3; C=1,2; M12=1,3,4; M34=3,1,2;
         M13=1,2,4; M24=2,1,3; J=1. All unused full assemblies remain present.
```

## Departure and return with retained neighboring occupancy

```text
 center of owned region -> outward home corner -> outward X -> Y to corner park
       *-------------------------*-------------------*
       | occupied neighbor stays |                   |
       | (live or finished)      |                   * complete park

 approach is the reverse geometric route; neighboring live trajectories must
 still be checked against its new timing. No teleport, no lifting occupied beds.
```

## R transformation obligations

```text
 operating cassette -> reserve affected empty region -> retract nested stages
        -> retained transfer carriage -> supported outer rotary cradle (if needed)
        -> captured destination -> lock/reference verification -> extend

 old support ======= overlap/handoff ======= new support
                      NEVER unsupported

 Overlap means a load-transfer contract with compatible freedoms, not two rigid
 guides forced into alignment. Unaffected jobs retain support/reference throughout.
```

## Pre-CAD decision tree

```text
 Exact identities/revisions, allowed geometry and full route bounds available?
  NO -> consolidated model request; finish analytical work; dependent CAD blocked.
  YES -> qualified review + maintainer authorizes bounded E1 strip?
          NO -> keep research pause.
          YES -> same selected XY components in H and B; two column jobs + park.
                  Missing reach/engagement under exact bounds?
                   YES -> reject that topology/range; review longer/fixed/nested rail.
                   NO -> continuous full-assembly/objects/panels conflict?
                          YES -> inspect actual solids vs conservative reservations.
                                  Actual conflict -> change route/topology; retain negative.
                                  Reservation only -> refine bounds; do not claim impossibility.
                          NO -> H column/harness burden vs B lift/support burden unresolved?
                                  YES -> request exact evidence; E2 gravity work stays separate.
                                  NO -> extend to transposed/mixed/J witnesses for review.

 If both H/B fail specified envelopes: investigate explicit R support/transform,
 not an imaginary shrinking rail. A clear CAD strip never authorizes physical work.
 First physical proof remains separately reviewed two-bed docking/cross-seam printing.
```
