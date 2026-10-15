# D5 — editable conceptual diagrams

Original editable text diagrams; not to scale, CAD, fabrication data or verified vendor
geometry. Coordinates follow D2/D4. All dimensions in the one numerical example are
hypothetical. The concepts do not select motion, support, enclosure or safety architecture.

## Top view: separate motion, structure and panel-handling reservations

```text
                                 +Y north
          external panel/hand removal and storage corridor
       . . . . . . . . . . . . . . . . . . . . . . . . . .
       .  environmental panel boundary (unselected size)   .
       .  +-------------------------------------------+   .
       .  | permanent structure / independent guards |   .
       .  |   root/park/cable reservations at edges   |   .
       .  |        +---------+  +---------+          |   .
       .  |        | 1 NW    |  | 2 NE    |          |   .
       .  |        +---------+  +---------+          |   .
       .  |        +---------+  +---------+          |   .
       .  |        | 3 SW    |  | 4 SE    |          |   .
       .  |        +---------+  +---------+          |   .
       .  | full assemblies sweep beyond bed edges  |   .
       .  +-------------------------------------------+   .
       .       front opening and door swing --->          .
       . . . . . . . . . . . . . . . . . . . . . . . . . .
                                      +X east --->
```

Each partition S/R/C/M12/M34/M13/M24/J changes active and parked volumes. Rectangles
show bed identities only. This is not a proposal for a conventional cube frame or proof
that the reservations can be nested as shown. Perimeter roots may cross the panel boundary,
requiring a revised enclosure concept rather than a hole assumed safe around moving parts.

## Side view: independent load paths and panel thermal relief

```text
                         +Z
                          ^
 permanent braced frame   |       removable panel/cassette
          |               |          |  hand grip
          +-- accessory --[retainer]--+----O
          |             normal hold  |    outward removal -->
          |                          |
          |  full gantry envelope    |  floating followers
          |  (includes cables)       |  permit in-plane growth
          |                          v
          +-- dedicated lower ledge--+   weight -> ledge -> frame
          |
 bed / independent lift -> restraint -> frame -> foundation
 secondary lift parked -> own restraint -> frame -> foundation
```

The panel supports its own weight only. Removing it cannot release a brace, bed/head
restraint or electrical cover. The one fixed locating datum and floating followers need
out-of-plane capture throughout their travel; thermal float is not a loose guard.

## Removal-path counterexample: Y–Z section

```text
 Z mm                     overhead lip Y310..350, Z615..630
 630                         +---------+
 615                         +---------+
                              ^ collision after lift
 600                           | panel top initially
                               |
                               | panel Y320..324, Z0..600
   0                           |
                               +------------------------> +Y

 Path A: lift40, then outward100 -> lip intersection
 Path B: outward100, then lift40 -> clears this lip only
 Reverse B: lower40, then inward100 -> same isolated obstacle clear
```

Path B is possible only with an interface that releases outward first. This diagram
omits hands, hooks, rotation and other machine obstacles and earns no service clearance pass.

## Passive thermal network: avoid one-temperature assumptions

```text
 Qupper (hypothesis) --> [upper air / nearby hot parts] -- Gu --> ambient
                                  |
                            mixing K (unknown)
                                  |
 Qlower (hypothesis) --> [lower air / nearby cool parts] -- Gl --> ambient

 Each future node also needs:
 local radiant sources -> panel / printed root / motor / wiring
                      -> conduction to frame -> outside environment
```

The two-zone calculation is steady only. Actual parts need separate transient capacities,
view factors and convection paths. No active chamber heater is represented.

## Protection decision flow (conceptual review, not control logic)

```text
Does removing environmental panels remove an essential protective function?
             | no                                  | yes
             v                                     v
Assess remaining local guards,          Develop independent effective protection
hot zones, emissions and service        for open-air mode, preserving all modes
             |                                     |
             +---------- qualified review ---------+
                              |
          If unresolved: no physical adoption; no bypass to make a mode work
```
