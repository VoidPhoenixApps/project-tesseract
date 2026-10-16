# D9 — support and coordinate contracts

[Overview](d9-study.md) · [faults](d9-faults.md) · [diagrams](d9-diagrams.md).
**Open obligations, not a verified mechanism.** X east, Y north, Z up; beds 1 NW,
2 NE, 3 SW, 4 SE. The common horizontal reconfiguration datum is z=0. Printing
height is relative nozzle-to-sheet separation, independent of that datum.

## Five functions that must remain separate

| Symbol | Physical obligation | Insufficient substitute |
| --- | --- | --- |
| P — registration | Locate cold carrier and head reference in specified freedoms; preserve relieved hot-plate mounting and calibrated nozzle-to-sheet transform | A motor position or seam-edge clamp alone |
| L — support | Continuous reaction path for gravity, acceleration, cable forces and overturning moments into the frame/foundation; include unilateral contacts and full stroke | A drawn line, torque link, guide assumed to resist axial gravity, or equal load division |
| T — transmission | Convey commanded motion/torque through known phase, backlash, compliance, routing and engagement | Assumed load capacity, restraint or actual output position |
| R — positive restraint | Retain/arrest gravity-loaded bodies under the named fault, independent of the failed T element; hold-down where uplift is possible; supported service state | Motor holding torque, assumed screw self-locking, software stop or upstream-only brake |
| O — downstream observation | Actual carrier/head pose, seam tilt, engagement and support evidence, with freshness, uncertainty, latency and common-cause coverage | Steps sent, motor encoder alone, selector command or one true limit switch |

A guide normally permits translation along its rail; it may resist lateral force and
moment without supporting axial gravity. Each L chain therefore names an axial load
support function as well as guidance. An actuator may carry normal gravity through T,
but its failure demands separately justified R. Some support/lock parts may serve P
and L; this is a coupled component needing analysis, not permission to merge the claims.
R catches may allow finite descent and rotation: a retained load is not necessarily a
printable surface or safe clearance. O detects a problem; it does not bear the load.

For every candidate, inventory four hot plates/sheets, four cold carriers, all four
complete head/carriage/column assemblies (active or parked), any disconnected platform,
all translating guide/actuator mass, harness loads and the supporting frame. Trace L
and R through anchors to foundation, not just to another floating member. Temporary
service supports also need a defined load/pose envelope. Unknown quantities stay unknown.

## H versus B and alternative mechanisms

Let h_g be independent job progress, b_i bed-sheet height, n_g nozzle height. Ideal
relative progress is h_g=n_g−b_i after calibration; thermal/elastic/sheet residuals
remain measured terms. A scalar equality does not establish roll/pitch, stiffness or
surface flatness.

| Candidate | P and normal L | T and relative Z | R and O | Distinct unresolved obligation |
| --- | --- | --- | --- | --- |
| H — full-range independent head Z | Beds → relieved hot mounts → cold carriers → stationary station/transport supports → frame. Head → axial lift support plus lateral/moment guide → XY arm/root → frame. P references cold beds and individual moving head axes | Four independently usable head lifts; active group uses n_g=h_g, b_i=0. Inactive heads retain a supported park, not zero mass | Load-side head restraint over full stroke and park; stationary bed hold-down/support. O actual nozzle-carriage pose/tilt, park capture and sheet plane; motor encoder insufficient | Reach-dependent arm/root/column moment, moving column tail and cable load, catching a parked head above another route; H simplifies bed lift synchronization only |
| B — E-sync baseline | Every bed retains its own axial support, guidance and cold registration within its moving lift. Hot mount remains relieved. Fixed-Z head/drop assembly still has full structural L path | n_g=0, b_i=−h_g; one group trajectory commands multiple independent lifts. No cross-bed L tie assumed | Independent load-side retention for each bed and structural retention for fixed-height/parked heads. O actual per-bed translation/roll/pitch and full seam, lift skew and locks | Guides must travel with horizontal carriers or undergo supported handoff. Full downward stroke and hot harness routing remain absent |
| B — E-hybrid | E-sync plus explicitly modeled cold load-sharing ties; released follower freedoms and remaining moment paths listed before adoption | Monitored group trajectory; drive load sharing depends on compliance, not identical commands | Local R retained unless a separately reviewed alternative covers every member and failed tie; O loads/pose on both sides | Redundant hard guides can bind; load-sharing tie may propagate a catch shock into the neighbor and printed object |
| B — T-link / E-drive | E-sync L unchanged; mechanical phase link receives no structural support credit | Selected belt/shaft/clutch tree per group; local torque owners isolated to prevent fighting | R must bypass failed link/shaft; O remains downstream of all couplings and guides | Equal input angle cannot eliminate lead mismatch, elastic twist or output slip; tree topology does not prove six-DOF compatibility |
| F-group — secondary moving frame | Partial modes retain E-sync L. Empty J transfers to positive platform load joints, guided/axially supported platform and frame | Partial local lifts; J platform lift selected only after supported compatible handoff | Platform has its own R even while unused; four loads restrained through verified locks; O actual platform/bed poses and load acceptance | Added platform mass, independent full-stroke clearance, load redistribution, release of incompatible local guidance and selector continuity |
| C-group — fixed J supports with head/gantry lift | Partial modes retain E-sync L; empty J transfers beds to stationary rated supports | J uses full-range head/gantry Z; partial bed lifts isolated appropriately | J beds positively retained; lifted J head/gantry restrained; O both support handoff and head axis | Duplicates bed/head Z hardware and needs supported constant-datum transfer; common gantry alone cannot serve unrelated partial-mode jobs |

F/C variants are challengers, not selected repairs. A single attached moving platform
with fixed-height heads cannot meet unrelated heights. Four selectable sections could
restore degrees of freedom but do not establish support or practical coupling in either
orientation. Stationary H beds do not violate automatic horizontal conversion: only
empty affected beds move horizontally at z=0; printing Z belongs to heads.

## All eight arrangements

P below means cold registration within the correct stationary (H) or moving (B) local
assembly, not a bed-Z guide pinned to the fixed frame. Every row retains all four L_i
and R_i bed paths and all four head paths, even if no jobs are active. Optional E-hybrid
L edges and T-link edges are separate alternatives; neither is implied by P.

| Mode | Group owners / count | H active heads; retained parks | B depth owners; cold P grouping | Optional within-group L or T edges | Isolation obligation |
| --- | --- | --- | --- | --- | --- |
| S | 1 / 2 / 3 / 4; 4 | H1,H2,H3,H4; none initially | b1,b2,b3,b4 unrelated; local stations | None | Four unrelated progress coordinates; unused platform independently parked |
| R | 12 / 34; 2 | H1,H3; H2,H4 | b1=b2, b3=b4; separate row datums | 12 and 34 | No hard row-to-row height link |
| C | 13 / 24; 2 | H1,H2; H3,H4 | b1=b3, b2=b4; separate column datums | 13 and 24 | No hard column-to-column height link; row supports cannot be silently reused |
| M12 | 12 / 3 / 4; 3 | H1,H3,H4; H2 | b1=b2; b3,b4 unrelated | 12 only | Both southern singles retain support/reference |
| M34 | 34 / 1 / 2; 3 | H3,H1,H2; H4 | b3=b4; b1,b2 unrelated | 34 only | Both northern singles retain support/reference |
| M13 | 13 / 2 / 4; 3 | H1,H2,H4; H3 | b1=b3; b2,b4 unrelated | 13 only | Eastern singles retain support/reference |
| M24 | 24 / 1 / 3; 3 | H2,H1,H3; H4 | b2=b4; b1,b3 unrelated | 24 only | Western singles retain support/reference |
| J | 1234; 1 | H1; H2,H3,H4 | All b_i equal; four cold references or released-follower registration | Example T tree 12,13,34; L topology separately justified | F/C handoff affects all four; no partial occupied exemption |

Head IDs follow D7's illustrative assignments, not demonstrated reach. Jobs completing
or cancelling create retained parked-head and occupied-object obligations. Bed-Z holds
the finished depth; it must not return an occupied bed to datum for convenience.
Owners count independent progress, **not motors, brakes, physical support points or
driver channels**. Four individual sheets and heater loops persist in joined mode.

## Spatial constraint audit required before CAD adoption

For every guide, lock and contact, reviewers need location, normal/direction, lever arm,
retained versus compression-only behavior, stiffness/preload and released freedoms.
Check residual DOFs, force closure, reaction signs and compliance together. At overlap,
releasing yaw does not cure vertical-guide pitch/parallelism error. Releasing too many
freedoms can remove moment support; a four-contact support is statically indeterminate
without stiffness. Evaluate the whole stroke and temperature/load range, including
loads caused by catching, docking and neighboring motion. Independent motors and graph
separation cannot establish negligible motion through a shared printed frame.
