# D8 — assembly motion contract and falsification ledger

[Study](d8-assembly-study.md) · [results](d8-results.md) · [source](d8_geometry.py).
All numerical geometry is **hypothetical**, not an approximation of a selected
purchased component. The contract is deliberately incomplete for real hardware;
unknowns listed below prohibit a feasibility certificate.

## Moving and stationary volume contract

Nozzle is the local origin; X/Y signs use the D2 exact E transform:
H1=A; H2=mirror-X(A); H3=R180(B); H4=R180(A). Common orientation uses A for all.
The physical perimeter roots remain west/east in both comparisons. Reflection describes
original functional allocations, never permission to reflect purchased motors,
extruder gearing, connectors or fan impellers. Every box retains an identity in output.

| Member | Local dimensions / datum in mm | Motion and evidence class | Missing actual evidence |
| --- | --- | --- | --- |
| Nozzle | X/Y ±2; Z 0..5 | Fixed to head; intentionally contacts own deposition plane only | Exact tip/shoulder geometry, hot dimensions and print-path contact model |
| Heater/hotend | X/Y ±8; Z 5..35 | Follows complete head XYZ | Heater block, insulation, nozzle variant, thermal keep-out |
| Fan/duct | X −50..8, Y −8..50, Z 10..70 | E transforms complete allocation; body-scale sweep .7/1/1.3 affects XY only | Separate intake/exhaust flow needs and actual solids; empty box volume is not solid contact |
| Extruder motor/housing | X −45..−5, Y −5..35, Z 65..100 | Head XYZ; same allocation in H/B | Lever opening, shaft, connector, torque and thermal rating |
| Probe | X −25..−15, Y −10..0, Z 2..35 | Deployed/retracted union reservation, fixed to head | Actual stroke, sensing locations and reachable sheet points; nozzle reach is not probe reach |
| Head carriage | X −40..0, Y 5..35, Z 35..65 | Head XYZ | Bearings/mounts and nozzle datum; not D2's separate carriage-offset contract |
| Local cable | X −50−r..−40, Y 15..35, Z 30..120 | Head XYZ; r=18/30/50 | Real connector, bend, strain relief and cable lifetime |
| Local filament | X −50−r..−20, Y 20..40, Z 85..150 | Head XYZ | Full spool/feeder route, friction, bend and twist; local loop alone cannot bound it |
| Moving radial rail/arm | Length L outward from nozzle; width 20/30/50; depth30 at fixed level | XY translation; full rail retained in park. L=450/600/750 | Exact guide/member cross-section, root engagement/moment capacity, belts/screw/end blocks |
| Root carriage and motor | root X ±25, Y nozzle ±30, level−15..level+55 | Y translation at root X=±320 | Bearing/drive/fastener envelopes and root stiffness |
| Fixed Y guide | root X ±15, Y ±330, level..level+30 | Static; four levels 420/460/500/540 | Frame posts, braces, motor/belt return and real mounting datums |
| H Z column | nozzle X/Y ±15, Z z+35..z+level+30 | Full fixed-length column moves XYZ; guide intersection retained over tested stroke | Actuator/guide ends, anti-rotation, restraint, usable stroke and protruding tail |
| B Z column | nozzle X/Y ±15, Z35..level+30 | XY only, nozzle at zero | Drop rigidity; independent guided bed supports and downstream positive restraint |
| Root cable corridor | X min(nozzle,root)−r..max(nozzle,root)+r, Y ±20, level+35..+65 | Affine envelope; includes empty space, not asserted cable shape | Complete head-to-root vertical connection, fixed return, loaded bend radii and cable-chain geometry |
| Frame/panels | open allocated cavity ±halfwidth; enclosed reduces XY by20 and roof=700 | Boundary reservation; primary roots/guides stay in both states | Actual braces/retainers, extraction path, panel thermal limits; no structural credit or panel interlock assumed |
| Beds/objects | D2 final rectangles; object solid prism over whole illustrative region, bottom−depth, top h−depth | H bed stationary; B bed/object down by h, finished depth retained | Actual workpiece, overhangs, skirt/purge, bed/carrier stack, lift guides, heater cables, fault pose |
| Maintenance extraction | **Unknown** beyond ordinary parked assembly | Not a zero-sized object and not simulated | Tool/hand, nozzle withdrawal, lever/fan replacement, isolation and supported service pose |

The table accounts for omissions rather than hiding them inside a “complete” label.
No belt, vertical umbilical, frame brace, filament feeder, under-bed lift or maintenance
route is assigned zero size or credited clear. Consequently the model can falsify
specified assumptions but cannot close the full-assembly obligation. No component
intersections inside the same assembly are generally interpreted as collisions:
intended mounts/bearing interfaces overlap. Only the four named head bulk/own-rail
pairs are screened for unintended self interference; all other self interfaces need
exact geometry. Own object contact is exempted only for its active nozzle, not its
motor/duct/column or parked former owner. Foreign-object reserve is 2; own adjacent
ideal workpiece uses zero reserve to avoid treating intended nozzle adjacency as
an approved protective spacing.

## Eight-mode ledger

Codes: **F** mathematical exclusion of the specified contract; **B** intersection or
boundary failure of supplied boxes; **U** unknown real geometry/mechanism; **C** a
condition worth testing, never a machine pass. Every cell below includes both panel
states, arbitrary independent job intent, and permanent finished-object occupancy.
The fixture paths are a subset of that intent. The generated baseline contains 696
cases: 8 candidate/orientation/panel combinations × (3 routes per mode + each finished
owner + departure/return of each individual owner while others print). The sensitivity
adds 1,728 cases (9 factors ×3 values ×2 candidates ×2 orientations ×8 modes ×2
live/first-finished states), all enclosed. It is OFAT, not a factorial search or global optimization.

| Mode; groups | Owners; inactive parks | H finding | B finding | R finding / required transformation |
| --- | --- | --- | --- | --- |
| S; 1/2/3/4 | 1,2,3,4; none until a job finishes | B boundary; common orientation has tall-object witnesses; E tested paths have none; U full independent paths | B boundary; C ideal object tops stay at zero; U bed/support/harness and all paths | U four independently retained stage cassettes; no common moving coordinate allowed |
| R; 12/34 | 1,3; 2,4 | B tail/roof; common object witnesses; U two X-spanning sweeps | B tail; C retained-depth geometry; U two independently supported bed pairs | U keep two independent pair stages; retire 2/4 only through clear continuously supported paths |
| C; 13/24 | 1,2; 3,4 | B tail/roof; common object witnesses; U same-Y unrelated jobs | B tail; C retained-depth geometry; U column-support/harness | U two Y-spanning stages; ordered full-width bridges F unless mechanism changes |
| M12; 12/3/4 | 1,3,4; 2 | B tail/roof and common object witnesses; U lower live/finished neighbors | B tail; C three distinct depth owners; U neighboring lift/flex corridors | U cassette2 retires while bottom jobs retain support/reference |
| M34; 34/1/2 | 3,1,2; 4 | B tail/roof and common object witnesses; U upper live/finished neighbors | B tail; C three depth owners; U lift/flex | U cassette4 retires without disturbing top jobs |
| M13; 13/2/4 | 1,2,4; 3 | B tail/roof and common object witnesses; U right neighbors | B tail; C three depth owners; U lift/flex | U cassette3 retires without disturbing right jobs |
| M24; 24/1/3 | 2,1,3; 4 | B tail/roof and common object witnesses; U left neighbors | B tail; C three depth owners; U lift/flex | U cassette4 retires without disturbing left jobs |
| J; 1234 | 1; 2,3,4 | B tail/roof; F rail450 cannot reach far edge; U complete three-park traversal | B tail; same F rail450; C one group depth; U support, full paths | U extend one retained global stage; no cooperation credit; J support handoff separately unresolved |

Baseline synchronized assembly-to-assembly counts are zero for these selected paths,
not proof of arbitrary independence. H/E object counts are also zero at baseline;
this is useful conditional counterevidence to blanket “all perimeter stages collide”
claims. H/common object events do occur. All baseline rows fail the allocated boundary.
The sensitivity and raw first witnesses preserve changes without declaring an optimum.
R receives no borrowed H/B collision counts: no modeled transformation geometry exists.
For **every mode**, the complete functional E comparison must also establish real
handed mounts, probe access, cooling, outer parking and service; none is waived by E's
synthetic inward saving. All physical E/common conclusions remain U.

## R/D+ challenger with explicit intermediate contract

A concrete **proposed** repair to fixed rail-tail crowding is a nested radial stage
on an automatically relocatable cassette. Each cassette keeps its own independent
XY drives, captured Y carriage and positively retained frame attachment. Nested
members retract along X into an outer bay; they may not disappear as a single
shrunken AABB. To change edge orientation, an empty cassette would translate in a
captured outer transfer lane, enter a supported rotary cradle, turn 90° outside the
bed/object envelope, then lock onto the new side rail. This is mechanically much
more complex than H/B. It is a transformation description, **not a designed joint,
selected actuator, supplied route or assumed clear rotation**.

| Intermediate | Support/motion invariant | Falsifier / missing evidence |
| --- | --- | --- |
| 0 operating | Each active job has separate XY/Z owner and retained reference | Shared drive/beam permanently ties unrelated paths: F for that implementation |
| 1 reserve transition | Affected beds are empty at fixed datum; unaffected jobs/finished objects remain reserved, including shared structural influence | Moving a busy bed or disturbing its support to obtain room is forbidden; queue transition |
| 2 retract nested members | All slides retain minimum rated overlap and independent anti-fall/load path; cables retract with actual lengths | Loss of overlap, tail collision or bend violation: B if exact geometry; presently U |
| 3 transfer cassette | Old support remains engaged until captured transfer carriage carries load and restrains rotation | Unlock-before-support is unsupported as proposed; unknown brake/lock cannot pass |
| 4 rotate if needed | Captured cradle carries cassette continuously; union of actual rotating solids clears neighbors/panels | D2/D8 linear translation CCD cannot certify rotation; bounding hull alone can only flag candidates |
| 5 engage destination | New support verified before transfer support releases; no redundant hard loop fighting guides | Unknown load transfer and released freedoms: U; position sensor is not load capacity |
| 6 extend/calibrate | Separate stages retain two pair jobs or three mixed jobs, then one J job with all unused cassettes retained | Failed injective reach or ordinary panel removal requirement falsifies this configuration |

For D7's Z-F-group alternative, partial modes retain independently supported E-sync
lifts; only empty J may transfer to the secondary frame. Continuous positive support
and compatible guide release remain E2/E5 work. A clutch or belt reroute supplies no
implicit support. D3's intermediate belt-path loss counterexample remains applicable.
A no-rotation nested stage is a distinct, simpler challenger; if full tangential/radial
stroke already covers all modes, relocation should be eliminated rather than retained
for novelty. Neither version is selected or simulated here.

## What would settle the remaining questions

- **Stroke/tail:** exact rail plus carriage/motor assembly and allowable engagement;
  measure nozzle-to-root reach and full parked tail, with tolerances and end stops.
- **H column:** actual Z member and harness at low/high head positions; obtain guide
  overlap and protrusion, then inspect every lower-stage crossing and roof path.
- **B objects:** actual bed/object/lift/heater-loop volumes through full depth; include
  final/cancelled occupancy, skew and stop states. Ideal top=0 alone is insufficient.
- **E packaging:** original A/B mounts using unchanged purchased parts, with all fan,
  probe, motor, connector and filament orientations preserved; compare equal functions.
- **R:** exact captured transfer/rotation/retraction support sequence and continuous
  swept solids. Missing support or unknown geometry remains U, never a path certificate.
- **Both environmental states:** actual panels, retainers, primary frame and independent
  service extraction paths; no routine removal to make enclosed printing work.

A future measurement needs source revision, temperature/load/pose, instruments and
uncertainty, repeats, reviewed acceptance/abort limits and independent qualified review.
D8 sets none of those physical limits. Numerical reserve and sample counts are not
safety qualifications. Unknown recoverable state inhibits dependent motion planning;
blind homing through retained objects is not a repair.
