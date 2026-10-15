# D2 — eight explicit configurations

[Report](d2-engineering-study.md) · [model](d2_geometry.py) · [results](d2-results.json).
D1 axes: X right, Y north, Z up; beds 1 NW, 2 NE, 3 SW, 4 SE. Head home IDs
match bed IDs. Each group retains its original sheets. All dimensions below are mm.

**Assignments are conditional reach assignments, not validated collision-free jobs.**
The hypothetical layout uses 180 mm modules, 40 mm separated gaps, zero ideal joined
gap and 5 mm outer region margins. The margins do not remove a strip on either side
of an internal seam. Real hot seam gaps and printable margins are unresolved; even
350 × 350 is only a test rectangle, not advertised usable volume.

| Configuration / groups | Candidate A+/B/D assignment | Necessary single-head movement in this example | Inactive heads / park opportunities | Unproven condition and main conflict |
| --- | --- | --- | --- | --- |
| S: 1 / 2 / 3 / 4 | H1→1, H2→2, H3→3, H4→4 | Each 170 × 170; four independent XYZ job coordinates | None inactive; outer home/service zones still needed | Independent height and whole bridge travel; low beam can cross tall neighbor |
| R: 12 / 34 | H1→12, H3→34 | Two 350 × 170 paths across X seam; unrelated heights | H2 NE, H4 SE corners, or full assemblies retract outside shared travel | Two independent Y paths in distinct row lanes; parked beams/cables and full stroke must clear |
| C: 13 / 24 | H1→13, H2→24 | Two 170 × 350 paths across Y seam; unrelated heights | H3 SW, H4 SE corners | Both jobs need same Y range; nonpassing full-width bridges fail unrestricted scheduling; stacked columns remain obstacles |
| M12: top pair + singles 3,4 | H1→12, H3→3, H4→4 | One 350 × 170 seam path + two 170 squares | H2 NE | Three independent progress coordinates; paired gantry cannot sweep lower singles' objects |
| M34: bottom pair + singles 1,2 | H3→34, H1→1, H2→2 | Same dimensions, reflected placement; fixed H3 orientation | H4 SE | Same issue with top singles; reflection changes harness and panel access, not just ID labels |
| M13: left pair + singles 2,4 | H1→13, H2→2, H4→4 | One 170 × 350 seam path + two 170 squares | H3 SW | Pair traverses both Y lanes beside independent singles; full-width beam conflict |
| M24: right pair + singles 1,3 | H2→24, H1→1, H3→3 | Same dimensions, reflected placement; fixed H2 orientation | H4 SE | Right column travels full Y beside left singles; probe and outward cable routes differ |
| J: 1234 | H1→1234 | One head covers 350 × 350 including both seam directions and center crossing | H2/H3/H4 corner or outboard whole-machine parks | Full-region carriage reach plus clear stationary beams/columns/harnesses; no cooperative four-head assumption |

Corners at (±260,±260) are **rejected hypothetical parks**: their required carriage
positions (±280,±280) exceed the ±240 travel by40 mm on both axes. At park220 the
carriage reaches its boundary; no reserve remains and no route is proven.
The model's Z parks are 300 mm for moving bridges; fixed-stack park Z is capped at
beam lower face minus 100 mm, to avoid placing the head above its attachment.
No full approach/departure route to those parks has been established. Whole beams
span X=−290..290 even when their nozzles park. A service or nozzle dock is not a
mechanism retraction system.

## Functional coverage before collision screening

`R` = reach-only assignment exists, `X` = functional rejection, `U` = no specified
geometry. None is physical feasibility. Model performs an injective head-to-region
matching, so the same head cannot be counted twice for two concurrent pairs.

| Arrangement | A0 four strictly local | A+ extended four | C strict locals + fifth | D single active toolchanger | Unspecified shared rails |
| --- | --- | --- | --- | --- | --- |
| S | R | R | R | X | U |
| R | X | R | X | X | U |
| C | X | R | X | X | U |
| M12 | X | R | R | X | U |
| M34 | X | R | R | X | U |
| M13 | X | R | R | X | U |
| M24 | X | R | R | X | U |
| J | X | R | R | R | U |

For C's mixed rows, H5 takes the pair and the two local heads take singles; for J,
H5 takes all beds. Those assignments require a fifth independently moving gantry
clear of the locals, not a fifth tool attached to an existing shared beam. Giving
locals pair reach repairs the functional deficit only if **two** pair assignments
coexist in R and C. Shared-Y B fails arbitrary simultaneous jobs regardless of reach.

## Coordinates and transitions

`beds()` specifies final poses only: joined row gaps close in X; joined column gaps
close in Y; in a mixed mode only its paired row or column closes that gap. Opposite
singles retain their gap. All bed top Z remains zero. `regions()` takes group bounds
and applies an outer inset; `required_carriage()` subtracts each fixed oriented nozzle
offset. Full numeric bounds and height assignments are in JSON, avoiding hidden origin
shifts in prose.

The default fixture rejects unreachable parks in all modes except S, which has no
inactive heads. Structural feasibility remains U for every architecture, including
cases with zero counted overlaps. Fixed guide supports, actual belts and harness deformation are
missing. Moving/grouped bed Z would transform objects by bed displacement and require
D1's seam/support proof. The code tests that transform on a 200 mm object lowered
195 mm; the downward travel is hypothetical, not an authorized reconfiguration method.

A future transition search must hold occupied beds fixed, move only affected empty
modules horizontally at datum, include all supports/locks/cables and any overhanging
objects, and check the complete path. The carrier mid-path test demonstrates the
kernel, not all 56 directed mode-to-mode transitions. Some transitions may correctly
be rejected until adjacent jobs finish; this does not excuse indefinitely pausing jobs
during normal printing in an otherwise claimed independent mode.
