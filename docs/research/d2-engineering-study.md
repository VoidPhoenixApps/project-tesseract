# D2 — toolhead reach and interference feasibility

**2026-10-14, America/Chicago. Research only; no architecture selected.** Built on D1
commit `25eb8a745cf8c4ddc54d64a65159e26f756bbc93` in [Draft PR #25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25).
D1 is still unmerged: this package belongs to a separate stacked draft targeting
`codex/research-d1-compatibility-screen`, not `main`. D1 files are unchanged.

**Answer:** A four-independent-head machine meeting every mode has **not yet been
established**. Local-only reach and shared-Y arrangements have explicit functional
failures. Extended systems retain sufficient degrees of freedom, but full bridge,
descending-column, parking and object interference prevent a whole-machine clearance
claim. This is negative and unresolved evidence, not a proof that every possible
four-head machine is impossible.

Read the [eight-mode matrix](d2-mode-coverage.md), [mirrored comparison](d2-mirrored-study.md),
[geometry and results](d2-calculations.md), [editable diagrams](d2-diagrams.md),
[reference/model catalog](d2-references.md), [verification](d2-verification.md) and
[public summary](d2-public-summary.md). The [requirements](../requirements.md) govern.

## Scope and complete motion layouts

Each active job needs independently commanded X, Y and relative Z, a single head
covering its complete region, and clear structures through its usable workspace.
Two X carriages on one translating beam have coordinates `(x1,y)` and `(x2,y)`:
three positional DOFs instead of four. Motors or firmware cannot remove `y1=y2`.
Similarly, four intersections of two X and two Y bars yield only four independent
planar coordinates for four nozzles needing eight; shared bar coordinates constrain
jobs. Neither duplication nor mirror printing supplies arbitrary unrelated paths.

| Layout | Physical structure / load path and travel | Coverage and interference result | Complexity, service and missing evidence |
| --- | --- | --- | --- |
| XY-A0 local Cartesian baseline | Four independent two-axis bridges bounded by quadrant frames, each with independent head/gantry Z; head → carriage → beam → side guides → frame | Singles plausible; a head confined to one quadrant cannot traverse a pair or full region. Rejected as complete baseline by containment, regardless of packaging | Mechanically simpler comparison with modular service; inner posts also obstruct seams. Useful control, not a waived requirement |
| XY-A+ extended local bridges with moving Z | Four independent full-span X bridges on separate Y guide lanes and independent Z stages; local home positions, overlapping travel | Nozzle reach possible; full-width low bridges cross another job's object. Two column jobs occupy overlapping Y intervals, so bridges cannot simply keep a north/south order. Hypothetical model finds conflicts; actual layout U | Eight XY coordinates plus four long Z coordinates, multiple belts/harnesses and fall restraint. All structures, guide ends and mounts require sizing; raising only nozzle does not raise bridge |
| XY-A+ perimeter cantilevers | Each outer column supports independent tangential and radial linear stages, with head Z at the end; orthogonal serial axes can cover a rectangle without a beam spanning the opposite bed | Can remove an unnecessary cross-machine beam; arms still cross at seams and may span tall parts. Pair and J paths require enough radial stroke and retracted parked arms, not just docked heads. U | Cantilever compliance scales approximately with length cubed for the same beam/load; bearing moment and root stiffness matter. Telescoping variant adds overlap/lost motion and internal cable routing. No stiffness claim or selected stock |
| XY-B1 ordered bridges on shared rails | Multiple independently driven Y bridges, each with its own X carriage; supports share rail surfaces but axes are independent | Genuine independent XY inside order-constrained workspaces. With no passing, `y1 + w/2 + c < y2 - w/2` is invariant. Row jobs can occupy separate Y lanes; column jobs require overlapping full Y ranges, so this layout cannot guarantee arbitrary independent column paths without bypass/stacking/reconfiguration | Longer end parking adds rail/frame length. Several carriages on one rail cannot pass merely because each has a motor. Rail preload, reference surfaces, support compliance and force coupling need review |
| XY-B2 vertically stacked fixed-height bridges + long head Z | Independent Y bridges on separated levels, each carrying independent X and a descending head slide; bridge levels above object ceiling | Separating beams clears beam-beam contact if spacing exceeds depth plus reserve, but high head columns penetrate lower beam planes. Model finds column/beam overlaps. U, not a passing stack | Stack raises enclosure; long slender slides, cables and service tools must pass lower structures. Side-mounted drop columns or apertures need actual swept proof, not holes drawn at one pose |
| XY-B3 shared rigid framework with separate Cartesian stages | Common static structure, separate guide lanes and cantilever stages; no shared moving Y member | Shared frame itself does not forbid independent XY. This is a packaging variant of A+; U until beams, guide supports and axes are specified | Potential frame consolidation but coupled vibration/compliance, outer service and cable crowding remain |
| XY-C four locals + one global head | Four quadrant machines plus a fifth independent full-region bridge with its own Z; globals and locals coexist structurally | Fifth supplies one candidate J or mixed pair path. With strictly local four, two simultaneous paired jobs are impossible: only one pair-capable head. Adding pair reach to at least two locals changes the proposal and needs a new proof | Highest head count; fifth beam must clear the two still-printing singles in mixed modes and all parked local gantries in J. A docked fifth head on a shared active gantry does not add an independent machine |
| XY-D modular / reconfigurable | Independent local stages automatically extend, relocate or couple beams while affected beds are empty at fixed datum; retracted beams park outside future path | Potentially changes ordered row lanes into column lanes or frees a global stage. U: joint constraints, transformation trajectory, retained support and homing not specified. Joining two powered bridges can reduce independent DOFs | Additional joints/locks, configuration verification and calibration. Must retain two independent pair machines and three mixed machines. No manual rebuild or routine occupied-bed movement is acceptable |
| XY-D single active toolchanger baseline | One XY gantry picks tools from peripheral docks | Credible conventional full-region strategy, but only one active XY path. Rejected for concurrent singles, two pairs and mixed jobs | Lower motion complexity; real toolchanging precedent in R4. It is a useful J comparison, not a solution for all modes |
| XY-E exact A/B/B/A overlay | Fixed orientations: H1=A, H2=B, H3=R180(B), H4=R180(A), B=mirror-X(A) | Changes offsets and envelopes only; cannot add a missing axis, remove beam crossing or supply an extra pair-capable head | Conditional inward clearance savings versus greater outer parking, duct/probe/filament/service constraints; see dedicated study |

`U` means geometrically unresolved. The explicit layout restriction is what gets
rejected, not the architecture letter. Aerotech's real dual-bridge system supports
independent bridge and vertical-axis precedent; it does not prove four unrestricted
Tesseract XY/Z jobs [R1](d2-references.md). Conventional IDEX illustrates why independent
X alone is insufficient [R5](d2-references.md).

## Quantitative structural constraints

For independently moving bridge heights `zi=hi+di`, full overlapping XY sweeps cannot
stay separated for arbitrary `hi∈[0,H]` unless the fixed level offset is strictly greater
than `H + beam depth + clearance`. For H=200, depth=30 and reserve=2 mm, the offset
must exceed **232 mm** for this sufficient bound; four such levels span more than
696 mm before head/guide depth. This is a hypothetical necessary burden for this
particular overlapping fixed-order stack, not a required machine height or an optimum.
Fixed overhead bridges avoid that H term in beam spacing, but their descending head
columns remain obstacles to every lower bridge. Bed-side Z can keep tools near one
height, yet retains D1's grouped-bed alignment and support obligations. It does not
remove XY ordering or beam-column collisions.

Full-span moving-bridge examples use 580 mm beams, 30 mm width/depth and nozzle-to-beam
lower-face offset 80 mm. The singles scenario has no head-machine overlaps but two
beam/other-object candidates at heights 10/150/60/200 mm. Treating only head bodies
would miss this. Conversely, a conservative overlap is not necessarily real contact:
spatial hulls lose timing and contain empty space. The model reports candidate pairs,
not fabricated millimetre clearances for unknown assemblies.

## Adversarial conditions and transition obligations

| Condition | Failure mechanism / desk evidence | Consequence for research and later controls |
| --- | --- | --- |
| Four unrelated job heights | D1's finite-trim bound; D2 low full-span beams encounter tall neighboring volumes | Provide truly independent usable relative Z and beam paths; no indefinite scheduling pause credited as independence |
| Tall completed object next to new job | Continuous sweep example: body at nozzle Z=10 spans Z=20..80 and crosses a 200 mm object; a 5 mm object is clear for this body only | Finished parts remain in occupancy map. Model includes hotend separately in mode screens; body-only fixture is no whole-head clearance claim |
| Two pairs at 10 and 150 mm | Row and column partitions exchange which shared-rail ordering can work; a row-only lane solution is incomplete | Demonstrate both orientations with separate X/Y/Z ownership and hot seam support |
| Global head past parked machines | Parked full beams remain across machine width; parks require carriage±280 beyond travel±240 and also exceed available enclosure | Park full assemblies, cables and supports; demonstrate exit, travel and return, not just dock coordinates |
| Heads at central seam | Mirrored body-only spacing improves from >60 to >18 mm in nominal sensitivity, but hotend/probe/cable and own/neighbor objects also count | Account for both envelope and braking uncertainty; 2 mm is not a validated protective clearance |
| Crossing beams at different Z | Level separation can fail with independent job heights; fixed levels create column crossings | Use full XYZ trajectories and level constraints. No automatic assumption of safe over/under passage |
| Reconfiguration with occupied neighbors | Start/end clear carrier can cross an object/overhang mid-path; explicit test catches it | Move only affected empty beds horizontally at datum, preserve occupied neighbors; reject blocked transitions. Final configuration reach does not prove a route to it |
| Failed homing / stale position | Clearance calculations lose their coordinate premise | Unknown actual positions mean unresolved/inhibit planned motion. Independent state sensing and bounded stop/recovery evidence required; no blind rehome through objects |
| Cable chains use parking space | Default cable reach is 80 mm outward, filament loop 80 mm; panel reservation adds 20 mm | Required frame half-width is 362 mm for park=260 plus 80+2+20. Current hypothetical 320 is insufficient. Chain minimum radius is payload-dependent |
| Enclosure / service interference | Tool-free panels may remove access obstruction but cannot be structural motion clearances only available open | Both enclosed and open configurations must support travel and practical service. Define hand/tool extraction corridors under energy isolation; no service clearance is numerically proven |

These are design review obligations, not a completed hazard analysis or operating
procedure. See [D1 failure study](d1-failure-study.md) for support, energy isolation,
locks, sensing and controlled recovery. No new safety-integrity or stop-distance claim.

## Next-stage comparisons, without a winner

Retain three **investigation paths**, all unresolved:

1. **A+ perimeter cantilevers with independent head Z.** First establish an actual
   axis/envelope graph for both paired directions and one J path, including retracted
   arm length, column placement and loads. This challenges full-span obstruction
   without claiming stiffness or dimensional fit.
2. **B separate/stacked bridges with explicit drop-column routing**, compared with
   a grouped-bed-Z alternative. Obtain beam/rail/carriage and column swept dimensions,
   show same-Y column jobs and full-region transit through parked levels. A bridge
   stack alone is inadequate; a failed column-route study should remain negative evidence.
3. **D automatic workspace reconfiguration**, with C's pair-capable-local-plus-global
   variant as a cost/complexity comparator. Specify how two independent pair stages
   survive both orientations, and prove empty-bed fixed-datum transition paths without
   disturbing adjacent jobs. Strict-local-plus-fifth C remains rejected for two pairs.

Minimum discriminating evidence: nozzle-centered component envelopes and offsets;
complete structural/kinematic graph including fixed supports and belts; usable strokes
and object height bound; all eight final states plus transition routes; time-resolved
independent-job sweeps with stopping/uncertainty margins; enclosure and service paths;
and qualified mechanical/controls critique. Only then request narrow CAD authorization.
Two-bed hot docking/seam proof remains the first physical proof. D1's thermal negative
result, support constraints and Z-C/Z-F corrections are preserved.

The printable/reinforced edition, Ender 3 part fit, separately validated imperial/metric
interfaces, later 2020 edition, four retained sheets, tool-free enclosure and reproducible
native sources remain mandatory. No structural stock is sized here; all variants need
separate stiffness, fit and thermal evidence. No architecture, purchased component,
firmware, CAD platform, license or budget is approved by this report.
