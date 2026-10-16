# D8 — full-assembly XY reach and parking falsification

**2026-10-16 · Research for [issue #41](https://github.com/VoidPhoenixApps/project-tesseract/issues/41). No architecture selected, no physical validation, no CAD authorization.**

Perimeter stages remain research candidates, but “park the nozzle outside the bed” is
not a sufficient motion contract. In the explicit sliding-rail topology studied here,
retraction pushes a long rail tail outward. Independent head Z adds a moving tall
column; grouped-bed Z keeps object tops near the printing plane but retains bed-load,
heater-flex and fault-skew problems. Neither candidate has a complete all-mode path
certificate. The reconfigurable challenger needs an independently supported mechanism
at every intermediate state before its apparent packaging advantage can be credited.

**Practical next step:** obtain exact geometry and review the smallest E1 comparison
below, starting with a two-column-job strip and one full assembly parked beside it.
Do not resume a detailed full-machine CAD build. Preserve the first physical proof:
**two-bed docking and cross-seam printing**.

## Evidence and reproducibility

| Artifact | Purpose |
| --- | --- |
| [Motion contract and falsification ledger](d8-motion-contract.md) | Named parts, transforms, eight modes, R intermediate states, limitations and counterexamples |
| [Editable top/side sketches and decision tree](d8-diagrams.md) | Text diagrams; no render or manufactured geometry |
| [Python model](d8_geometry.py), [tests](test_d8_geometry.py) | Standard-library analytical experiment using D2 geometry |
| [Generated readable results](d8-results.md), [raw JSON](d8-results.json) | Every baseline fixture, first timed witnesses, bounded sensitivity totals |
| [Exact-reference request appendix](d8-model-requests.md) | Existing catalog/tool output; no retrieval approval |
| [Verification and file inventory](d8-verification.md) | Commands, outcomes, review and publication limitations |

Inputs are the repository at D7 merge
[`7657641742bc7d612457dfbdf414c5413fc60e14`](https://github.com/VoidPhoenixApps/project-tesseract/tree/7657641742bc7d612457dfbdf414c5413fc60e14):
[requirements](../requirements.md), [architecture](../architecture.md),
[roadmap](../roadmap.md), [research-first plan](../research-first-plan.md),
[D2](d2-engineering-study.md), [D7](d7-integrated-study.md),
[compatibility](d7-compatibility.md), [experiment queue](d7-experiments.md),
[failure chains](d7-failure-chains.md), and [catalog](../../cad/reference-parts/README.md).
The shared standards were read at project-knowledge revision
`147de4d979bba17120a4cc425983d590f85b6000`; no Tesseract CURRENT_STATE exists there.
Current Home Infrastructure instructions and issue #41 were read through GitHub.
AgentMemory's one continuity query supplied no relevant Tesseract record.

D8 adds **analytical synthetic evidence**, not manufacturer dimensions. D2's historical
PR-state text remains historical. D7's 1,536 cells are subsystem compatibility
classifications, not geometric certificates. No new vendor specification, stock,
price, rights or physical measurement is asserted. Source links in the generated
request appendix are catalog leads at their recorded access/revision, not freshly
qualified CAD. Unknown sizes remain unknown outside explicitly hypothetical boxes.

## What the bounded calculation establishes

All dimensions below are **hypotheses in mm**, except the mandatory nominal bed side
180. D2 supplies the final layouts: 40 separation, ideal zero joined gap and 5 outer
inset. Neither ideal seams nor that inset specifies usable production area. X east,
Y north, Z up; modules 1/2/3/4 are NW/NE/SW/SE. Horizontal conversion datum is z=0.
D8 samples fixed final layouts; it does not execute or certify bed conversion.

Four separate Y slides carry radial X rails from west/east roots at x=±320. Their
fixed levels are 420/460/500/540. Each **600-long rail translates in full**; it does
not shrink when parked. A 30 engagement margin at both ends gives
`30 ≤ 320 − sx*x_nozzle ≤ L−30`, where sx is −1 west and +1 east.
Y nozzle travel is ±300. Head/nozzle X is the rail's inward tip datum; no hidden
D2 carriage offset is reused. This is a different explicit topology, not a claimed
repair to every D2 bridge. Four distinct Y coordinates preserve the necessary eight
XY DOFs; separate bearing levels avoid imposing shared-rail order by definition,
but do not establish collision clearance or stiffness.

A west head serving J's illustrative far edge x=175 needs radial distance 495 and
therefore **L≥525** with the 30 engagement margin. L=450 fails reach even in an
arbitrarily wide enclosure. At west park x=−260, a 600 rail reaches x=−860; with
2 numerical reserve and 20 panel allocation, the enclosed half-width must be
**at least 882** for that rail alone. This is a consequence of this topology, not a
required Tesseract footprint. Park=300 instead gives only 20 engagement at root=320
and fails the 30 engagement condition even though it looks farther from the beds.
Increasing rail length improves reach while increasing the tail burden.

The H column travels with the nozzle: its Z bounds are `[z+35,z+level+30]`.
The B column is fixed vertically at `[35,level+30]`; XY rails, guide levels, root,
functional volumes, and routes otherwise match. H's full-length translating column
can protrude above its XY guide. At H4 z=200 its top is 770, outside a hypothetical
700 roof. B avoids this particular roof demand; it does not inherit a gravity-restraint
or alignment pass. The lower column end must still overlap its guide band over the
usable H stroke; the declared 240 stroke stays below the lowest level−35=385 bound.

For B, an object of current height h is translated by bed Z=−h: its top is zero,
not erased. Finished objects remain at their last depth and head departure/parking
is represented separately. H retains objects on stationary beds with top h.
The generated suite uses unrelated live heights 10/150/60/200 by group order,
then replaces **each** owner in turn with a finished object at height 200 and parks
that owner's head. A separate 60/200/300 sweep changes the first finished owner's
height. This is a bounded set of histories, not all height permutations. A bed
raised under a completed part, curled/overhanging geometry, or unknown recovered
position would require a new reservation; no automatic raised-bed clearance is assumed.

Each active route has six vertices: region corners, a diagonal and center for a
printing witness; center→outer home corner→outward X→Y park for departure, and the
exact reverse for approach. Each owner also departs/returns individually while other owners keep their print
witness trajectories. Previously inactive assemblies remain fully present. Foreign objects
fill their illustrative regions, including finished occupancy. Sweeps use continuous
segment tests; clear endpoints alone never pass a route. Simultaneous path vertices
share normalized segment time, **not specified speeds**. Reversing departure does not
prove reversal against a different live-job schedule.

D2's rigid AABB continuous test is reused. D8 extends it to affine box bounds for
the variable root-cable reservation: solve six inequalities `a_low(t)≤b_high(t)` and
`b_low(t)≤a_high(t)`, intersect their time intervals with [0,1]. Touching is interference.
The root stays outside all tested nozzle paths, so min/max cable bounds are affine
within each segment. If a future path crosses the root, split at that breakpoint.
The 2 reserve is numerical sensitivity, **not** a stopping distance or thermal tolerance.

An interval is an actual intersection of the specified mathematical boxes. When a box
represents a cable corridor, empty duct volume or full possible object extent, this
is only a candidate physical conflict. Spatial hulls additionally discard timing:
`independent_hull_candidates` cannot be called unavoidable collision. Conversely,
zero events would establish only the supplied paths/boxes; unbounded hardware,
whole-life print occupancy, service routing and uncertainty preclude a machine pass.
Counts are duplicate segment/component events, not independent failures or risk scores.
Reach-rejected desired trajectories are still collision-screened to expose additional
constraints; their event counts do not imply those paths are physically executable.
Baseline/sensitivity paths hold each layer height fixed; isolated Z-motion fixtures
exercise continuous column/bed travel. They do not certify every combined XYZ path.

## Findings and preserved negative controls

| Finding | Classification and scope | Evidence that could reverse or narrow it |
| --- | --- | --- |
| L=450 cannot span J from the selected root with required engagement | Mathematical reach failure of that rail/root contract | Longer usable rail, shifted root, different single-head assignment with independently demonstrated stroke; wider panels alone cannot help |
| Park260 with L600 exceeds half-width520 | Exact synthetic rail boundary failure; tail at ±860 | A larger full frame/panel cavity; fixed-rail carriage topology with all unused rails retained; an explicitly supported telescope. No nozzle-only park credit |
| Park300 loses root engagement | Stroke failure despite greater bed clearance | Different root/guide length and actual load/moment-rated engagement; no assumed bearing capacity |
| H tall translating columns encounter other stages and roof reservations | Box witnesses in generated results; actual shape/route remains unresolved | Shorter or telescoping independently guided Z, higher roof, different column offset or stage levels, with full stroke and rigidity review |
| B lowers object tops to the fixed print plane in the ideal retained-depth scenario | Conditional analytical benefit; isolated body/tall-object fixture reverses H contact to B no-contact | Finished bed not retained at −h, tilted/warped objects, under-bed mechanisms/cables or fault skew may remove advantage |
| Mirroring improves inward body clearance but enlarges outward reserve | Equal functional-volume comparison, not a mirrored vendor assembly | Actual unmirrored motors/fans/extruder plus original handed mounts/ducts may erase or reverse savings |
| Nonpassing full-width bridges cannot serve arbitrary overlapping column-Y jobs | Preserved D2 ordering exclusion, not a perimeter or one-job J exclusion | Independent lanes, over/under routing or a specified transformation creates a different topology |
| R can change workspace only after specifying an entire supported transformation | Unknown, no numerical clearance credited | Exact nested-stage/joint/rail/lock geometry, continuous support and control dependencies at every intermediate pose |

Deliberate fixtures retain a tall-object midpath hit with clear endpoints, a parked
rail obstructed by an outer fixture, adjacent live bodies crossing, inadequate stroke,
a rising full H column crossing an overhead obstruction, B lowering into an
under-bed obstruction, and D2's low/nonpassing bridge controls. A clear isolated B body fixture is **not** a
clear B full assembly. B's supports, guide compatibility, brake/catch behavior and
heater routing remain E2 obligations; XY does not solve them.

## Smallest future E1 experiment — proposal, not authorized

Use one **two-column-job strip** from C: two independent perimeter stages, their
complete heads/Z columns, one parked assembly at its nearest interfering level,
a retained finished-object volume, the frame roots and installed panel boundary.
Compare H and B using the **same** selected XY components and nozzle targets. Include
both equal-height near-seam operation and unrelated low/tall histories, departure and
return. Then transpose the seam strip for R and the four mixed placements; do not
claim the strip certifies all eight modes or J. A later J far-corner stroke/three-park
extension is required if the strip survives. This is smaller than detailed full-machine
CAD and directly tests whether H's column burden or B's retained-depth benefit matters.

Before authorizing it, the maintainer should provide or approve exact files/sources
in one consolidated packet. No substitute purchased parts or fabricated vendor solids:

| Priority / existing catalog candidate ID | Minimum geometry request and purpose | Present blocker |
| --- | --- | --- |
| 1: `e3d-revo-hemera-xs-direct-drive` | Revision/configuration-matched STEP + drawing; nozzle/mount datums, heater, fan, motor, lever, connectors and service travel; head collision and handed adapter comparison | Not selected; no locally cataloged asset; physical revision and rights unresolved |
| 1: `hiwin-mgn12h-carriage-size-preload-accuracy-seal-options-unresolved` | Exact rail length/end machining, block configuration/preload/seals and usable travel; STEP plus rated moment/engagement drawing | Portal unconfigured; exact rail/block identity not selected; no approved asset |
| 1: `stepperonline-17hs08-1004s-short-body` | Exact revision STEP/drawing, shaft/connector/mount envelope; root and moving actuation housing | Prior body/shaft discrepancy must be resolved against actual revision; no inspected asset |
| 1: `antclabs-bltouch-smart-v3-1` | Deployed/retracted probe, cable exit and mounting drawing/STEP; seam access and parking | Exact model not located/approved; sensing performance not established |
| 1: no selected harness/filament identity | Cable/chain loaded bend radius, anchors, lengths, connectors, strain relief, feeder/spool route and service envelope | Local boxes do not bound the whole moving route; exact identity and rights/source absent |
| 1: no selected column/actuator/retainer/panel identity | Actual Z stroke/end stops, rail protrusion, bearing overlap, panel cavity/retainer projections, existing original frame-root envelope | No configured purchased model; obtain authoritative drawing/STEP or separately approved original concept scope |
| 2: no selected bed/support stack identity | Bed/heater/magnet/sheet and guided support, downstream restraint, full downward stroke and heater loop | Required before B can be credited as complete; detailed load-path work belongs to E2 |

Established source links and five separate rights flags are in the generated
[request appendix](d8-model-requests.md). The approved local library inventory contains
the Feather sample only as a CAD asset; it supplies none of these exact head/stage
models. The existing tooling was used offline; no assets downloaded or catalog
permissions changed. Geometry-dependent CAD remains blocked until selection, rights,
model correspondence and authorization are resolved. Maintainer response is **not**
needed to finish this analytical report.

Mechanical reviewers should challenge the radial-tail assumption, root engagement,
Z-guide overlap, every solid/void distinction, independent trajectory coverage,
loads/deflection and uncertainty. Electrical/controls reviewers need actual cable/filament
routing, stopped/unknown-position envelopes, occupancy persistence and bounded stop/fault
behavior. Neither review can infer positive gravity restraint from motor torque or position.

The [Phase 1B thermal negative](../phase1b/thermal.md) remains: the uniform center-anchor
model closes a 180 mm seam by 0.33984 mm over 20–100 °C, wider than the historical
unapproved 0.10–0.30 window. Inward relief does not solve sheet slip, bow or hot seam.
No XY finding supersedes it. Qualified independent engineering review, maintainer
acceptance and bounded authorization remain prerequisites. AI desk review is supplementary.

All mandatory modes, four retained heated sheets, fixed-height horizontal conversion,
printable-frame-first work, Ender 3-sized printed parts, separately validated actual
imperial/metric interfaces, future 2020 edition and tool-free convertible enclosure
remain unchanged. No stock, toolchain, firmware, final component or license is selected.
Four-head cooperation is still a separate unproven stretch goal. No external repository
was modified; any accepted cross-project context link requires separately authorized work.
