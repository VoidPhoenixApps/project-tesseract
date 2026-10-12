# Risks, unresolved questions and requirement coverage

**No risk is closed by this study.** Priorities express investigation urgency, not calculated failure probabilities: P1 blocks prototype operation or mandatory capability; P2 can invalidate accuracy/reproducibility; P3 affects cost/serviceability. The proposed owner is a review role, not an assigned person.

## Risk register

| ID / priority | Failure and consequence | Affected concepts | Proposed mitigation / evidence | Review role |
| --- | --- | --- | --- | --- |
| R01 P1 | Coupled motion disturbs an active surface or printed object | B, C, carousel; shared frame in all | Freeze busy-region supports, prove allowed transitions and full object/head envelopes; measure disturbance | Motion/planning reviewer |
| R02 P1 | Compact mechanism cannot form a required mixed layout | B1, C0, D0 | Preserve documented failures; compare wide/trims/independent branches before selection | Mechanical reviewer |
| R03 P1 | Horizontal dock requires lifting or trapped release | Taper/pin/side-entry coupling | Constraint and insertion-path audit, cold fixture proof; reject incompatible capture | Mechanism reviewer |
| R04 P1 | Thermal edge interference bows plates or opens locks | All, especially bed-to-bed loops | Thermal anchor/gap budget, differential maps, no force-closing the fourth edge | Thermal/mechanical reviewer |
| R05 P1 | Seam step catches nozzle or destroys first layer | All | Map actual sheets, total Z budget, slow supervised crossing with controls | Print/metrology reviewer |
| R06 P1 | False lock/capture signal permits printing or drops support | E and all powered locks | Direct state observation, contradiction inhibit, passive support, fault/restart tests | Safety/control reviewer |
| R07 P1 | Heater/wiring fault causes shock/fire/burn | All | Component-specific electrical design, independent protective means, isolation and qualified review | Electrical/safety reviewer |
| R08 P1 | Link/cable sweep strikes neighboring bed, object or person | C/D/E; nested loops in B | Full fixed-height-band swept solids, guards, stop-distance allowance | Mechanical/safety reviewer |
| R09 P2 | Guide/dock overconstraint causes bind, twist or wear | All hard-located variants | Explicit six-DOF ownership and compliant releases; preload/force measurement | Precision-mechanism reviewer |
| R10 P2 | Printed joints creep or frame twists under clamp/bed load | All | Real-temperature dwell, load/deflection tests, short metal datum paths, variant verification | Structures/materials reviewer |
| R11 P2 | Differential heating, magnetic slip or edge curl defeats cold alignment | All | Sheet/plate/carrier metrology separated, hot/cold maps and cycle history | Thermal/metrology reviewer |
| R12 P2 | Central four-way gap/chamfers fail where straight seam works | J | Later central-cross coupons and four-bed thermal closure tests | Print reviewer |
| R13 P2 | Nominal shaft substitution or Ender 3 envelope assumption breaks reproduction | Both reinforcement variants | Actual stock drawings, separate generated outputs, print coupons and independent builder | Reproducibility reviewer |
| R14 P2 | Dock wear/contamination changes calibration unnoticed | All | Accessible replaceable contacts, inspection intervals, contaminated-state inhibit experiments | Maintenance/metrology reviewer |
| R15 P2 | Small samples or inadequate instruments create false passing evidence | All | U budget, guard bands, raw outliers and drift; limited scope of inference | Independent reviewer |
| R16 P2 | Arm singularity, backlash or weak vertical stiffness undermines reach | D / articulated C | Full-path Jacobian/sweep and loaded platform tests before heated rig | Kinematics/structures reviewer |
| R17 P3 | Saved motors are outweighed by locks, transfer hardware and downtime | E, selectable C | Quoted subsystem BOM after geometry; service/failure comparison | Cost/maintainer review |
| R18 P2 | A two-bed success becomes an unsupported final-machine claim | All | Gate-by-gate evidence labels, separate four-bed/head/frame/safety validation | Maintainer |

## Decisions requested for the next stage

1. Review whether A1 with frame-referenced docking is the preferred **comparison fixture baseline**, and whether E1 should be retained as the first transport challenger. This does not approve a final machine.
2. Review guide-retained yaw versus a planar floating registration substage. Which error source should the first rig isolate? Determine allowable compliance and clamp force from a drawing and load model.
3. Establish intended material/temperature and first-layer ranges so seam gap/step limits can be justified. Review center versus seam/corner thermal anchoring; a 0.20 mm fixed cold gap is already analytically inadequate in one screened hot case.
4. Review candidate metrology budgets, counts, thermal conditions and acceptance criteria in the [test plan](two-bed-proof-plan.md). Name competent mechanical, electrical and safety reviewers before physical work.
5. Decide whether B1's wide stagger deserves further packaging effort or whether B2 trims erase its benefit. Preserve required modes and active-job protection regardless of preference.
6. Bound one-platform linkage/lattice investigations by a required stiffness/packaging advantage before purchasing precision joints.
7. Select actual rig stock, printed materials, Ender 3 envelope and supported spans only after drawings, manufacturer data, local sourcing and fit/load review. Imperial and metric are separate qualifications, not rounded equivalents.

Still open: printing Z strategy, head count/reach/parking, final frame geometry, allowable vibration during another job, controller/firmware, heater power, electrical protection, sensors/interlocks, CAD toolchain, suppliers/budget, license and eventual release criteria. No study ranking settles these. The later 2020 edition must preserve all core capabilities and undergo separate structural/safety review. Cooperative four-head printing remains stretch work.

## Requirement coverage audit

| Requirement / task obligation | Study treatment | Evidence limit |
| --- | --- | --- |
| Four nominal 180 × 180 heated beds; four retained sheets | [Geometry](configuration-feasibility.md), [thermal model](preliminary-calculations.md), [rig plan](two-bed-proof-plan.md) | No usable 360 × 360 claim or single-sheet workaround |
| Horizontal conversion, common fixed-height plane | Height bands, path certificate and rejected vertical pin seating | Static under-bed band offsets are not operational bed lifting |
| Independent, two H pairs, two V pairs, both mixed modes, J | Six-mode matrix for A/B/C/D/E and repaired variants | Conditional paths distinguished from endpoint and physical proofs |
| Busy-job protection, empty moving modules, collision avoidance | Frozen-region transitions, shared-row limitations, object/head/cable envelopes | No concurrency demonstration; incompatible requests queue/reject |
| A independent XY, B rows/columns, C lattice, D linkage plus alternatives | [Motion study](motion-architectures.md) and mechanism top views | No final architecture selected |
| Docking six DOFs, thermal release and four-bed closure | [Docking](docking-registration.md) | Rank/constraint reasoning, not manufactured coupling evidence |
| Printable reinforced frame first; Ender 3 parts | Load paths, segmented trusses, explicit envelope/fit gate | Actual allowed print volume/material/orientation remain to be established |
| Distinct imperial/metric family and reproducible outputs | Sourced dimension examples, datum-preserving parameter sets and qualification obligations | No stock selection, CAD edits/scaling/reaming/shim workaround |
| Later 2020 edition with same core modes | Interface intent and independent structural revalidation | No drop-in stiffness equivalence |
| Editable parametric sources and public reproducibility | No CAD dependency; later native-source/variant requirement retained | This is documentation plus a plain Python calculation aid, not CAD delivery |
| Structural/thermal estimates and credible sources | Equations, assumptions, sensitivities and [references](references.md) | No FEA or physical data; sourcing is catalog evidence only |
| Objective matrix, relative cost and distinctiveness | Qualitative criteria, no total score overriding hard failures | Cost unknown without drawings/quotes |
| First physical proof is two-bed docking/cross-seam | Staged plan, U, candidate limits, hazards, aborts and evidence gates | Not approved to run; component-specific safety blanks remain |
| Small underside seam mark allowed | Coupon acceptance distinguishes mark from adhesion/collision failure | Cross-seam material compatibility unproved |
| Open-source intent; undecided license; no vendor lock-in | Study status and references; no licensed assets copied | No grant, supplier, CAD/controller or electronics selection |
| Four-head cooperative printing stretch | Explicitly separate from independent jobs | No slicer or firmware capability assumed |
| Preserve requirements and unrelated documents | Requirements unchanged; architecture receives only study link | No Home Infrastructure/project-knowledge edits |

## Review and knowledge handoff

Independent desk review should challenge mode/path claims, constraint redundancy, arithmetic, source applicability and whether the test plan falsely authorizes operation. Human engineering review remains necessary before adopting any consequential architecture or safety decision. A second AI review is a document check, not qualified electrical or machinery-safety sign-off.

No new authoritative Tesseract knowledge record is invented. After human review/merge, a separately authorized project-knowledge update may record the study link, **only approved** shortlist decisions and remaining gates in whichever project record the maintainer establishes. Home Infrastructure needs no hardware inventory update: no hardware was changed. Routine planning/calculation findings already here should not be copied into AgentMemory.
