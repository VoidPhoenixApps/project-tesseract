# D5 — eight-mode and clearance matrix

[Inherited D2](d2-mode-coverage.md) · [D4 load paths](d4-load-paths.md).
Axes X east, Y north, Z up; beds 1 NW, 2 NE, 3 SW, 4 SE. S/R/C/M12/M34/M13/M24/J
are mandatory arrangements. “U” means unresolved, never a clearance or safety pass.
Both panel states must preserve independent jobs and horizontal automatic reconfiguration;
removing panels is **not** a prerequisite for changing bed arrangement.

## Explicit operating matrix

| Mode / independent groups | Panels installed: critical complete-envelope obligations | Panels removed: persistent obligations | Conversion/service discriminator | Status |
| --- | --- | --- | --- | --- |
| S: 1 / 2 / 3 / 4 | Four active heads at unrelated heights, outer roots/cables and four separate Z stages clear walls, roof, catches | Same internal motion conflicts; any justified guards and panel supports cannot intrude into four jobs | Reach all latches without reaching through active-head zones; later service requires safe isolation | U / U |
| R: 12 / 34 | Two independent row seam paths; full H2/H4 parked assemblies and beams clear side/roof panels | Removing wall does not make ±260 parks reachable or remove stationary beams; two groups still independent | NE/SE parked assemblies compete with right-side catches and removal sweep | U / U |
| C: 13 / 24 | Two full Y paths; H3/H4 parks; stacked columns and full-width bridge restrictions persist | Full-width nonpassing bridge conflict remains; no scheduling restriction silently substitutes for independence | SW/SE parks compete with front extraction, door swing and hands | U / U |
| M12: 12 / 3 / 4 | Top row pair plus two independently progressing lower singles; H2 park and north-side roots | Necessary protective functions remain effective for all three regions; no blanket region-guarding requirement; moving pair cannot strike active singles | NE park competes with north/right panel; no assumed mirror equivalence | U / U |
| M34: 34 / 1 / 2 | Bottom row pair plus top singles; H4 park; asymmetric heater/cable routing | Same three-group obligations and open-air thermal gradients | SE park competes with front/right panel and service route | U / U |
| M13: 13 / 2 / 4 | Left column pair full Y stroke beside independent right singles; H3 park | Internal columns/objects, any justified guards and support remain obstacles | SW park competes with left/front extraction and left cantilever root | U / U |
| M24: 24 / 1 / 3 | Right column pair full Y stroke beside independent left singles; H4 park | Independent progress and right-side frame loads unchanged | SE park competes with right/front path; harness asymmetry assessed separately | U / U |
| J: 1234 | One full-region head and three entire parked assemblies; center crossing; secondary lift if adopted | All four sheets retained; lift restraint and parked masses remain; wall absence supplies neither reach nor safety | Largest parked population; lifting roof panel must clear filament/stacked bridges without disconnecting primary systems | U / U |

Assignments are D2 thought experiments, not selected heads or approved parks. D3's shared
secondary platform stays detached, independently supported and clear in partial modes;
in J a proposed handoff must preserve support. Include its full underside and lateral
sweeps, not just the beds' upper surfaces. Independent Z guide towers and transport may
move together; if not, support handoff remains unresolved.

## Quantitative inheritance, not a new collision claim

The [code](d5_analysis.py) reuses D2 `mode_screen` unchanged for both moving-bridge and
stacked-bridge thought experiments. It varies the clear half-width to 300/320/360 mm,
keeps the 2 mm numerical reserve, Z bounds −50..600 mm and all other D2 assumptions.
Counts below are **component envelope excursions** outside that box, not collision counts
or a validated minimum enclosure size. Both topologies happen to give these counts.

| Clear half-width mm | S | R | C | M12 | M34 | M13 | M24 | J |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 300 | 0 | 10 | 10 | 5 | 5 | 5 | 5 | 15 |
| 320 | 0 | 4 | 4 | 2 | 2 | 2 | 2 | 6 |
| 360 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

At 360 the modeled boxes fit this boundary, but all non-S modes still inherit
`REACH_REJECTED` because the park carriages exceed travel. S remains `UNRESOLVED`.
Panel-removed mode is not simulated as a safe infinite workspace; underlying collisions,
travel limits, frame and any hazard-justified guards remain. D2's limited layer samples are not full
Z histories or transition sweeps. No 56-directed-transition pass is claimed.

## Architecture-independent reservations

| Interface | Must include beyond an installed flat sheet |
| --- | --- |
| Perimeter cantilevers | Entire arm/root bearing, maximum reach/deflection, retract path, outer cable bend and bracing; panel mounted outside root can enlarge machine markedly |
| Stacked/reconfigurable gantries | All bridge elevations, descending columns, belts and tallest object; roof and side-panel lift cannot pass through these |
| Parked heads | Full carriage/hotend/probe/fan/duct/cables/filament and approach path; nozzle dock alone is insufficient |
| Bed transport / independent Z | Carrier sides and undersides, guides/locks, heater-wire flex and connector service; no bed vertical step introduced for conversion |
| Secondary lift | Parked and working platform, guides, restraint, selector access and intermediate load transfer; nothing may hang from removable panels |
| Cables / filament | Minimum bend, sweep, strain relief, abrasion and slack at all poses; permanent feeds through fixed bulkheads or openable split panel edges, not trapped closed holes |
| Doors / hardware | Cam backs, screw ends, hinge barrels, swing, pins, fingers/knuckles and full removal/reverse path |
| Bracing / service | Permanent brace envelope plus tool, eye and replacement-part corridor after isolation; no brace removal for panel conversion |

For future geometry, require swept panel+handles+hands not to intersect motion/park/brace
volumes at the designated safe service pose, including uncertain deformation and stopping
state. Runtime motion and service trajectories are separate analyses. A service pose
must be reachable without disturbing occupied jobs; if conversion needs an empty machine,
record that operating restriction for review rather than allowing manual bed rearrangement.

## Edition coverage

| Edition | Common functional interface proposed | Independent checks still required |
| --- | --- | --- |
| Printable/reinforced imperial | Accessory datum referenced to permanent frame, load-spread retained boss, floating panel followers | Actual fractional stock/socket bulk, Ender-fit adapter, creep, thermal map, all eight modes in both panel states |
| Printable/reinforced metric | Same datum where practical; separately generated ready-to-print adapter | Actual metric stock/tolerance and joint size; no rounding, mesh scaling, reaming or improvised shim substitution |
| Later 2020 | Adapted dedicated slot/interface hardware, independent bracing | Exact profile/slot/fastener family, latch access and bonding; aluminum expansion, joint slip and complete mode/access revalidation |

Shared panel cut patterns are an upgrade hypothesis, not promised interchangeability.
No extra essential print mode is reserved for extrusion. Frame checks must use all
removable panels absent; panel removal must not change primary gravity restraint.
