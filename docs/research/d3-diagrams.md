# D3 — editable conceptual constraint, power and load paths

Original text schematics; editable in this file. **Not dimensioned CAD or a validated
mechanism.** [Report](d3-engineering-study.md) · [matrix](d3-mode-constraints.md).
Arrows labeled P, L and T have different meanings; dashed/optional functions need design.

## Top view: group partition, Z up out of page

```text
          Y north                         X right ->
   1 NW             2 NE
    +----------------+       R:  1--2     C: 1  2
    | four retained  |           3--4        |  |
    | sheets; gaps   |                       3  4
    | unresolved     |
    +----------------+       M12:1--2     M34:1  2
   3 SW             4 SE          3  4         3--4

 M13: 1  2     M24: 1  2       J torque-tree example:
      |               |            1--2
      3  4          3  4            |
                                   3--4
 Lines specify group relationships, NOT enough structural contacts.
 S has no inter-bed lines. J's missing fourth edge avoids a torque loop;
 it does not authorize omitting necessary gravity or moment support.
```

## Side view: local supported-lift baseline

```text
   nozzle -> seam transit volume must remain clear
 retained sheet ===================================
 heated plate  -------- datum + radial relief ------
                         o       o       o   three height supports
 cold carrier =========================  P: XY/yaw station lock
                  | L              | compatible Z guidance (moments)
             local lift <--- T motor/transmission
                  | L              | independent restraint -> frame
          supported horizontal transport -> main frame -> ground

 P stops sit on the moving Z assembly during bed-Z printing.
 XY conversion: affected beds empty; sheet datum Z=0 throughout horizontal travel.
 Exact guide order/packaging unresolved; no vertical landing is depicted.
```

## Competing secondary-frame power paths

```text
 ORIGINAL (belt physically rerouted):
 motor --T--> belt --T--> [servo-positioned idlers, path L(q), wrap(q)]
                                      /                  \
                         individual lift path     secondary lift path
 Independent L restraint is outside this switched/breakable path.
 Servo position alone establishes neither belt engagement nor load support.

 ALTERNATIVE (paths stay installed):
 motor --T--> positive selector ----T----> installed tensioned local path
                    |      neutral
                    +--------------T----> installed tensioned secondary path
 Outputs independently retained; neutral or dual engagement is not 'ready'.
 Selected output requires phase/full-depth/retention observation, not command echo.
```

## Load path and cross interpretation

```text
 J transfer concept (not a mechanism):
    each sheet -> plate supports -> cold carrier
                             | L              | L
                       old local support   NEW positive platform lock
                             |                |
                           frame       cross arms + guided platform
                                              | L
                                   secondary lift + independent restraint
                                              |
                                       main frame -> ground

 During controlled overlap: old + new support may share load through compliance.
 Never make two incompatible rigid position references fight to 'prove seating'.
 Remove old ownership only after new reactions/retention are established.

 Four-arm cross:       T alternative:
        |                 ---+---    fourth module needs another load path;
     ---+---                 |       three arms do not imply four supports.
        |
 All contacts cold-side; hot sheet edges remain free to expand.
```

## Handoff state and selector counterexample

```text
 occupied/printing -> affected empty -> independently retained at datum
 -> horizontal dock with continuous local support -> verify P
 -> engage new L unloaded -> establish compatible load share
 -> unload/align/select T -> verify T and pose -> release old ownership
 -> eligible for separately validated printing

 Any ambiguous state -> retain existing supports, inhibit transition, latched fault.
 Reverse handoff also establishes destination support BEFORE releasing source.

 Point-path thought experiment (no pulley radii, no proposed hardware):
                     q=+20  o
   fixed (-100,0) o-----q=0-----o fixed (+100,0)
                     q=-20  o
 L(q)=2*sqrt(100^2+q^2); L(-20)=L(+20), but L(0) is shorter.
```

No whole-machine clearance is implied. D2's beams, columns, tall objects, full-assembly
parks, heater harnesses and removable panels must all be added to any later spatial model.
