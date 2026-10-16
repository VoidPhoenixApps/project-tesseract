# D7 — editable integrated concept diagrams

**Conceptual, not to scale, not validated.** These text diagrams define ownership and
questions, not solid geometry, purchased-part envelopes or a mechanism. X east,
Y north, Z up. [Profiles](d7-compatibility.md), [D2 geometry](d2-diagrams.md),
[D3 support diagrams](d3-diagrams.md), [D4 load paths](d4-diagrams.md),
[D5 panels](d5-diagrams.md) and [D6 state diagrams](d6-diagrams.md) supply prior context.
Edit the text directly; no proprietary renderer or CAD tool is required.

## Top view — eight target groupings

Each numeral is one retained sheet. A horizontal dash joins across X; a vertical
bar joins across Y. Blank spaces are separated groups, not dimensioned clearances.

```text
          S                 R                 C                 J
      1       2         1---2             1       2         1---2
                                          |       |         |   |
      3       4         3---4             3       4         3---4

        M12               M34               M13               M24
      1---2             1       2         1       2         1       2
                                          |                       |
      3       4         3---4             3       4         3       4
```

The matrices expand these to four, two, three and one independent job-height owners.
J's four seam edges do not require four rigid torque/locator links; P/L/T graphs differ.

## Top view — H/B perimeter-stage question

```text
                  NORTH / +Y
        outer root 1                 outer root 2
              [XY]                     [XY]
                \      H1 A    B H2     /
                 \   [bed 1][bed 2]   /
                  ?---- seam ----?       ? = unproven arm/park route
                 /   [bed 3][bed 4]   \
                /    H3 B180 A180 H4   \
              [XY]                     [XY]
        outer root 3                 outer root 4
                                      EAST / +X ->
```

Perimeter roots propose removing unnecessary full-width low beams; arms still occupy
space above objects. The arrow-like arms do not specify joints, rail lengths or an
approved diagonal mechanism. Each must implement independent serial tangential/radial
translation. In R park complete H2/H4 mechanisms; in C park H3/H4; in J park H2/H3/H4.
All their supports, harnesses and approach/departure routes remain obstacles. Compare
common head orientation against the exact E arrangement shown, fixed during travel.
No nozzle is credited with full reach from this sketch.

## Side view — independent head Z versus bed-group Z

```text
H: head-side Z                         B: bed-group Z
    permanent frame                       permanent frame
          | guide + restraint                   | XY/root
          | <---- XY arm ----> head             +------ head
          |                    ^                         |
          | independent Z      |                 job A / job B
       job A      job B       ...                heights unrelated
      [sheet 1] [sheet 2]                    [sheet 1] [sheet 2]
z=0 --[carrier]-[carrier]-- datum             [lift 1] [lift 2]
       retained local supports                 |   Dg   |
          |          |                        Li       Li
          +-- permanent frame --+          downstream restraint each
```

H beds stay stationary during printing; whole head structures must clear neighboring
heights. B group members descend coherently for their job while other groups can have
different heights; each attached object moves with its bed. **Printing motion is not
reconfiguration:** only empty affected modules return to common z=0 before horizontal
conversion. Supports do not disappear while a carrier translates; moving guides versus
support handoff remains unresolved. Both sides omit actual geometry intentionally.

## R candidate — separate position, load and transmission ownership

```text
PARTIAL S/R/C/M                        JOINED J ONLY (proposed)
D1 D2 D3 D4 or D12/D34 etc.             selected drive -> transmission -> platform
 |  |  |  |                                                    |
local guided lifts + local restraint                 independently retained support
 |  |  |  |                                                    |
carrier P locators -> relieved plates                  L locks -> four carriers
                                                              P datums separate
secondary frame: detached, restrained, clear          hot plates still relieved
```

Literal rerouting changes belt path continuously; the positive-selector comparison
keeps tensioned paths and selects torque. Neither path supports the bed just because
it transmits torque. J's old local guides must be compatible or explicitly released;
unused frame and drives remain retained. In C-group, substitute stationary rated bed
supports and gantry printing Z for the J platform; that is a different mechanism.

```text
Research handoff obligations (ordering needs mechanical proof):
empty affected group + known datum + clear route
    -> independent load retention established
    -> positional capture / new support and guide compatibility checked
    -> unloaded, phased drive selection and positive engagement observed
    -> verify new support + isolate unused path
    -> release only the old constraints proven redundant
    -> printing enabled only with all evidence fresh
Any unknown/fault -> retain support, inhibit unsafe motion, no automatic retry
```

This is not an executable procedure. A design that cannot preserve support in an
intermediate state is rejected; software cannot repair the missing load path.

## Parking, panel and occupied-object envelope

```text
outside        environmental panel       permanent frame         printing region
               | (tool-free removal)     | root/rail               |
hand/panel --->|--- removal sweep ? -----|                         |
               |       parked arm + cable + column                 |
               |       [not just a nozzle] ---- swept route ? ---- X tall object
```

Neither panel removal nor completed job status removes X from the collision model.
Panel handling has its own assessed conditions; ordinary open-air printing remains
available. Any actual protective function is assigned separately and retained in both
panel states. The permanent frame, load restraints and electrical covers stay effective
without environmental panels. No physical guard or interlock is selected by this diagram.
