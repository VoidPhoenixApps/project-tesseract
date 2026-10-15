# D4 — structural frame and load-path feasibility

**2026-10-14, America/Chicago. Comparative research and preliminary calculations only.**
No frame, stock, polymer, chamber temperature, CAD toolchain, component or license is
selected. No physical validation, fabrication or hardware operation is authorized.

**Finding:** Deep triangulated structures with continuous metal chords or replaceable
braces deserve further investigation, alongside printed nodes with tubular members.
Small smooth rods are more promising as axial members than as long unsupported beams.
Joint rotation, guide compatibility and local carrier compliance can overwhelm the
benefit of a stiff member. Evidence does not discriminate a whole-machine winner.

## Package and dependency

| Artifact | Purpose |
| --- | --- |
| [Public summary](d4-public-summary.md) | Readable result and next questions |
| [Load paths and modes](d4-load-paths.md) | Eight support/constraint graphs, D2/D3 interfaces |
| [Stock study](d4-reinforcement.md) | Actual imperial/metric candidates and fit uncertainty |
| [Printing and joints](d4-printable-joints.md) | Segmentation, orientation, materials and creep |
| [Enclosure](d4-enclosure.md) | Hand-removable panel interfaces independent of primary structure |
| [Editable diagrams](d4-diagrams.md) | Original conceptual top/side views and force graphs |
| [Calculations](d4-calculations.md) | Assumptions, equations, numerical interpretation |
| [Python](d4_analysis.py), [tests](test_d4_analysis.py), [results](d4-results.json) | Dependency-light reproducible analysis |
| [Risks](d4-risks.md) | Negative findings, faults and unresolved evidence |
| [References and missing models](d4-references.md) | Source ledger and later CAD blockers |
| [Verification](d4-verification.md) | Actual checks and independent review |

Live pre-edit inspection found Draft [D1 #25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25)
at `25eb8a745cf8c4ddc54d64a65159e26f756bbc93`, Draft
[D2 #26](https://github.com/VoidPhoenixApps/project-tesseract/pull/26) at
`5957b80a5478e1cc669cbd7f81d71a5934326d63`, and Draft
[D3 #27](https://github.com/VoidPhoenixApps/project-tesseract/pull/27) at
`096ae806c08d437bf1c84c77d217cacdfd6f3231`. Each is an ancestor of the next.
D4 branches from that D3 head and targets `codex/research-d3-bed-coupling`.
D3's recorded AI desk review is a research-publication review, not human approval or
mechanical certification. No parent branch or PR is changed or merged.
Current main `952c2202bc001d1aff38fa7bce9a0b86410695d6` supplied instructions.

## Requirements and inherited evidence

The unchanged [requirements](../requirements.md) govern: four nominal 180 × 180 mm
heated modules, four individual sheets in every mode, automatic horizontal conversion
at a common fixed-height plane, all eight arrangements, independently progressing
jobs, printable-first/ordinary Ender 3 parts, distinct imperial/metric outputs from one
parametric family, later 2020 edition, tool-free removable enclosure, editable sources
and public reproduction without a required paid/proprietary tool. Nominal joined area
is not usable area. Four-head cooperation on one object remains a separate stretch goal.

[Phase 1](../phase1/README.md) retained rejected uniform-lattice and outer-pivot layouts.
[Phase 1B](../phase1b/results.md) found an empty center-anchor cold-gap interval
[0.43984, 0.30000] mm over its 20–100 °C example; inward-corner anchoring reduces
normal closure but does not solve thermal bow or sheet slip. [Phase 1C](../phase1c/review.md)
retains capture/retention concerns, including the roughly 0.944 mm float envelope versus
0.5 mm gap and illustrative tower flexibility. Software/CAD checks do not resolve them.
[D1 failures](d1-failure-study.md), [D2 reach limits](d2-public-summary.md) and
[D3 support limits](d3-engineering-study.md) remain unchanged. No structure cures
shared-beam XY dependence, descending-column collisions, single-platform partial-mode
Z restrictions or incompatible guide loops.

## Architecture comparison

These are topology families, not build instructions. Relative mass/complexity statements
are engineering inferences for comparable envelopes; only individual member examples
are quantified. A triangulated face needs a three-dimensional return path and restrained
nodes; counting triangles alone does not establish rigidity.

| Candidate | Loads, torsion, stiffness and joints | Dynamics, temperature and mass | Assembly, service, availability and modularity | Disposition / discriminator |
| --- | --- | --- | --- | --- |
| A: triangulated printable space frame | Deep tetrahedral or triangulated bays turn bending into axial loads; compression buckling and node eccentricity matter. Planar triangles alone leave out-of-plane motion. Many segmented joints add compliance | Low material density but deep members and many nodes; changing polymer modulus/preload lowers modes. Hot joints can creep even under modest gravity | Ender-sized cells repeat; many mating datums and fasteners; triangulation may obstruct bed extraction. Polymer/process availability does not prove reproducible structural properties | Retain as printable control; quantify node compliance and braces in three planes before comparing mass |
| B: reinforced printed trusses | Continuous metal chords carry axial force; printed webs maintain separation and transfer shear. Load must enter chords through retained joints; no assumed perfect bond. Torsion requires a box/space truss | Larger depth can outperform a shallow beam; metal reduces chord creep but web shear and end anchorage remain temperature-sensitive. Added metal and joint mass | Replaceable printed cells; continuous chords reduce splice count. Hard to service if rods must withdraw through the whole machine; end access required | Shortlist for frame rails and towers; compare deep truss with accessible chord end anchorage |
| C: printed nodes with smooth rods or tubes | Axial rod cage versus bending tube skeleton. Tubes put material farther from neutral axis; node rotation may dominate. Round members need anti-rotation or triangulation | Tube shell ovalization at clamps and nodal creep are unmodeled. Solid rods add mass for less bending stiffness at similar mass; tubular chords can buckle locally | Region-specific sockets, split clamps and positive axial retention; precision shafts cost more and may need difficult machining. Tube cutting/squareness and broad dimensional tolerances need planned accommodation | Shortlist tubes; rods retained mainly for axial/short-span roles. Compare measured root stiffness, not catalog diameter alone |
| D: printed nodes with threaded reinforcement | Tension ties/preloaded chords can brace bays; threads reduce effective section and add stress concentrations. Slender threaded compression/bending members are weak references, not precision rails | Preload adds compression to printed nodes; relaxation or one slack tie creates directional loss of stiffness and rattle. Steel mass remains; no free rigidity from tightening harder | Easy length adjustment using matching nuts, load spreaders and lock features; many torque/alignment operations. Thread family and grade must be traceable | Retain tension-brace role; screen out unsupported all-thread as a default precision gantry beam |
| E: hybrid printed assemblies with replaceable metal bracing | Metal diagonals or straps close selected force loops; stiffness bypasses some polymer bending. Compression-capable brace or opposing tension pair needed for load reversal | Potentially small added mass; stress concentrates at anchors. Losing one brace can create a mechanism. Polymer anchors still creep | Replaceable braces permit maintenance but must stay installed when panels are removed. Front opening can use permanent rear/side/base returns if torsion is proven | Shortlist as serviceable topology; discriminate through lost-brace and open-front torsion analysis |
| F: conventional 2020 extrusion reference | Known section bending properties; corner connections, slot fasteners and bracing govern frame racking. Profile bending inertia is not frame torsional stiffness | Lower member mass than steel examples; aluminum thermal growth and bolted slip persist. No automatic vibration advantage | Good modular mounting and accessory access; differing slot standards and joints prevent generic interchangeability | Reference and later edition only; does not replace printable-first development |

Neither a hollow plastic extrusion replica nor a decorative lattice earns credit without
load-path and joint analysis. Conversely, more printed content is not useful if it adds
creep in a gravity-restraint path. A metal load-spreading sleeve can be justified while
retaining a printable-first topology; exact implementation needs review.

## Separate compliance layers

For a nozzle-to-sheet error, distinguish: (1) global frame displacement/rotation;
(2) gantry/root/rail compliance; (3) lift guides and cold bed-carrier deformation;
(4) docking contacts and locks; (5) plate, sheet and thermal mount deformation.
A common rigid-body translation can cancel in relative geometry; differential bending
and rotations at separated attachment points do not. Use a future compliance matrix
`u = C F` at bed and head datums, including off-diagonal coupling between occupied and
reconfiguring regions. Adding unrelated scalar deflections is not a validated error bound.

## Conditional shortlist and narrow next investigation

1. **Compare B and C+E at the same clear motion/service envelope:** a deep printed-web,
   continuous-metal-chord truss against tube-and-node bays with permanent replaceable
   bracing. Keep both imperial and metric stock definitions independent. Ask whether
   root/node compliance destroys the predicted member advantage.
2. **Bound one hybrid bed-pair link against independent support:** release explicitly
   identified guide freedoms, calculate eccentric reactions and thermal/preload mismatch,
   and remove one support path. A force-sharing link is only useful if it does not bind
   or transmit unacceptable disturbance into another job.
3. **Integrate a perimeter head root and one stacked-bridge alternative into the same
   structural envelope:** include parked assemblies, descending columns, cable loops,
   braces and panel-handling corridors. D2 still has no all-mode collision pass.
4. **Before detailed CAD:** obtain supplier tolerance/drawing data and agree an error
   allocation and operating/load envelope. Subsequent reviewed coupon/joint metrology
   could discriminate candidates; this package does not authorize printing or testing.

No weights, safety factors or numeric acceptance limits are chosen to force a ranking.
If required bracing blocks a mandatory path, revise the topology rather than dropping
a mode. The first hardware milestone remains the separately reviewed **two-bed docking
and cross-seam printing proof**.
