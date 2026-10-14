# Reproduction and verification

## Independent-review corrections — 2026-10-13

**Current boundary:** the completed historical matrix below verifies the earlier
CHECK implementation. The strengthened CHECK now has software-double coverage;
**its new acceptance behavior is not yet Fusion-runtime verified**. The matrix
must not be relabeled as testing this revision. PR #18 remains Draft and unmerged.

### New acceptance checks

CHECK retains the previous domain/one-ULP, sequence, complete component/pose,
0.001 mm bounds, max(0.001 mm³, 1 ppm) volume and nominal sweep gates. It also
requires the expected named sketches, offset datum and extrusion set; explicit
`HealthyFeatureHealthState`, valid objects, fully constrained one-profile
sketches, four rectangle orientations, and the original driving expression
multisets (ignoring whitespace only). It rejects suppression, lost parametric
history, changed profile association, operation, start/extent, taper and depth.
Datum/reference-plane and offset-expression checks preserve the common source
reference. No geometry, bore-sketch isolation or driving expression was changed.

For each of the four bores, CHECK measures sketch center/diameter and the final
B-Rep cylindrical side face associated with the named cut. It checks distinct
plate faces, expected X/Y axis location, diameter, vertical axis, two complete
circular rims at the plate's lower/upper Z, and full cylindrical area. These
reads distinguish a displaced bore or blind cut from matching outer bounds and
volume. Mount measurements are included in successful reports. Unavailable
required properties reject CHECK; optional diagnostics remain best-effort.

This is deliberately strict acceptance of the generated feature scheme, not a
general equivalent-CAD recognizer or arbitrary-topology proof. Reordered/algebraically
rewritten expressions, split faces or alternate feature constructions may be
rejected even if physically equivalent. It is not full assembly interference,
contact, capture, force closure, manufacturing or physical validation. The
unchanged thresholds are source/kernel comparisons, not docking tolerances.

The [durable evidence bundle](evidence/README.md) now preserves selected observations
from all 35 historical matrix reports and the original trapezoid failure,
with original hashes and explicit provenance gaps. This supersedes the earlier
statements that evidence exists only in temporary files. Future reports add a
run UUID, UTC time, source-file hashes at CHECK time, Fusion/OS versions and a
hashed document creation ID. The latter can be shared by copied documents;
it does not prove same-document continuity. Hashes identify checked source
files, not the source that originally generated an existing timeline. Missing
metadata is `unknown`; no private document title or source path is added to the
provenance header. Local failure tracebacks still require sanitization before
publication. Reports remain local until explicitly archived.

### Minimal targeted live Fusion smoke check — pending

Computer Use could inspect the existing unsaved design, but selecting Utilities
had no effect, including after raising the window. No CAD edits, saves, exports
or live CHECK execution were performed by the agent. Existing designs remain
untouched. A maintainer needs only the following bounded check, **not another
parameter matrix**:

1. Run the updated script to create a **separate unsaved B,inset** concept at
   defaults. Run `CHECK` and retain its report. Expect PASS with 59 components,
   healthy constrained history and four 5 mm cuts centered at
   (230.5,70), (230.5,170), (330.5,70), (330.5,170) mm, rims Z=-32/-28 mm.
2. In that disposable design, remove one footprint horizontal/vertical
   constraint without dragging geometry. CHECK must reject the underconstrained
   or altered history even if the current bounds still match. Undo and CHECK
   must pass. Preserve both reports.
3. Change one bore's X driving expression by adding `1 mm`. CHECK must reject
   altered driving history even though outside bounds and removed volume are
   unchanged. Undo, then suppress that bore cut and CHECK: expect rejection.
   Undo and CHECK must pass. Preserve the three rejection/restoration reports
   (the prior footprint restoration may serve as the starting healthy state).

Stop on an unexpected API error and retain the full local report. Do not weaken
checks to obtain a pass. The live test establishes property availability and
feature recognition on Fusion; deliberately corrupted B-Rep/dimension/health
combinations remain separately covered by API-shaped software doubles. No
physical test is requested. Before merge, inspect these results and review the
changed acceptance logic; human merge approval remains required. Mechanical
capture/retention/stiffness/access and safe-test planning block construction,
not acceptance of an explicitly unvalidated research concept.

### Autodesk API contracts consulted

Context7's official landing-page index returned no matching feature-health
content. Autodesk's official API pages were inspected directly on 2026-10-13:

- [FeatureHealthStates](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_FeatureHealthStates.htm): explicit healthy enum; warning/error/suppression/rollback/unknown are distinct.
- [Sketch.isFullyConstrained](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Sketch_isFullyConstrained.htm) and [Sketch.healthState](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Sketch_healthState.htm).
- [ExtrudeFeature](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ExtrudeFeature.htm), [DistanceExtentDefinition](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_DistanceExtentDefinition.htm) and [Profile.parentSketch](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Profile_parentSketch.htm).
- [ConstructionPlaneOffsetDefinition](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ConstructionPlaneOffsetDefinition.htm) and [ProfilePlaneStartDefinition](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ProfilePlaneStartDefinition.htm).
- [BRepFace.geometry](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepFace_geometry.htm), [Cylinder](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/core_Cylinder.htm), [BRepEdge.geometry](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepEdge_geometry.htm) and [face tempId](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepFace_tempId.htm). Temporary face IDs are compared only within an unchanged body during one check, never across runs.
- [Document.creationId](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/core_Document_creationId.htm) and [Application.version](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/core_Application_version.htm).

## Completed planned macOS CHECK matrix — 2026-10-13

The maintainer reports completion of the planned matrix on corrected Fusion
Personal/macOS designs. The agent read the available local reports directly,
including both new negative tests and their restorations. No new Fusion test
was run by the agent in this evidence-finalization task. Earlier Computer Use
could inspect the local application but could not operate the custom controls;
it produced no negative-test results. The maintainer subsequently performed them.

**Evidence classification:** report inspection independently confirms the recorded
parameter snapshots, CHECK outcomes and component data. It is not an independent
live rerun. Manual sequence continuity, visual movement/hole inspection and
same-document use remain maintainer observations. Reports lack document IDs,
embedded source hashes and Fusion/OS version numbers. Source is the corrected
implementation published as `ecdd68e`; its previously recorded hash is unchanged.

| Planned check | Result and evidence |
| --- | --- |
| Carrier 160→164→160→156→164→156→160 mm | Seven PASS reports, retained individually below; 59 fully constrained footprints |
| Gap 1→0.5→0.2→2→0.5 mm | PASS reports `c8bl8bzi`, `ktzo4_2p`, `493onqe6`, `xs753e5c`, `4s22_vxj` |
| (X,Y) (0,8)→(40,8)→(0,8)→(0,0) mm | PASS reports `m5w5komd`, `4lxhb_3v`, `6suhxuzl`, `krnw8b8w`; correct order also maintainer-reported |
| Mount pitch 90→110→100 mm | PASS reports `flqonjex`, `lntp606d`, `rlgahkc_` |
| Mount bore 4→6→5 mm | PASS reports `h1or_1v8`, `6ms7rolq`, `nu6ojds0`; visual geometry inspection and 100 mm center spacing maintainer-reported |
| Anchor inset 14→20→16 mm | PASS reports `oe73bpp7`, `ukhsf0as`, `13jlczwi` |
| B contact baseline 100→130→120 mm | PASS reports `8_3_xzwm`, `qb3wy0p3`, `_nfqa89y`; visible contact movement maintainer-reported |
| A,center / A,inset / B,center | PASS reports `99_zv4yv` / `mmm883gw` / `b8y4p1hz`; component-name sets match each model variant, 51/51/59 solids. Generation and selected variants maintainer-reported |
| B,inset | Confirmed throughout the carrier and negative/restoration records, 59 solids |

Each short report identifier above expands to
`/tmp/tesseract-phase1c-check-<identifier>.txt`. All listed files were examined;
PASS reports contain the expected component count, healthy fully constrained
footprints and bounds within 0.001 mm, and state that volume and nominal box
release-sweep checks passed. CHECK does not independently measure hole center
spacing or certify collision-free real geometry. No unexamined report is counted.

### Negative tests and restorations

| Test | Independently inspected report | Actual result |
| --- | --- | --- |
| Carrier=165 mm; gap0.5, X/Y0 | `tesseract-phase1c-check-uwuq5tzb.txt` | Expected CHECK rejection: `carrier=165.0 must be finite and within [156, 164]` |
| Carrier restored160; X/Y0 | `tesseract-phase1c-check-_hq6gs8v.txt` | CHECK PASSED; 59 named solids/reservations |
| X=1 mm, Y=0, carrier160 | `tesseract-phase1c-check-xhotdiee.txt` | Expected CHECK rejection: `Release Y fully before moving X; reverse this sequence to dock` |
| X restored0; Y0, carrier160 | `tesseract-phase1c-check-3nb7l73f.txt` | CHECK PASSED; 59 named solids/reservations |

The rejection snapshots contain the invalid values, and tracebacks originate in
`model.parameters`: these were CHECK domain/sequence rejections, not Fusion UI
refusals or unexpected feature failures. Both restoration files have identical
content hashes and matching default values. Their positions in local file-time
order agree with the maintainer's stated sequence; hashes alone do not prove
separate execution or document identity. The early rejections do not include
body diagnostics because they precede geometry validation.

| Report identifier | SHA-256 |
| --- | --- |
| `uwuq5tzb` | `d6d88978ff3b5667c99e198b527aefb67124c281845f8ab1e8a565116527067d` |
| `_hq6gs8v` | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `xhotdiee` | `4181dc24a84833c0102c9ff258147e945f8e259abc75a025d9e01c4f108eaf47` |
| `3nb7l73f` | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |

### Engineering conclusion and review boundary

The bounded planned macOS CHECK matrix is complete with expected results. It
demonstrates editable parametric concept geometry across the tested settings,
all four configurations, and rejection/recovery for the two invalid inputs.
The missing-constraint trapezoid failure and corrected carrier evidence below
remain part of the record. The 0.001 mm comparison and one-ULP normalization
were not relaxed; no source change was made in finalizing this evidence.

This is **not** physical docking, thermal/load validation, full collision/contact
certification, or independent Windows verification. Full Cartesian parameter
coverage, fabrication fit, force closure, preload/retention, stiffness, fatigue,
thermal drift, safe capture, exports and a non-proprietary reproducible CAD
backend remain unresolved. Independent engineering review of the corrected
constraint scheme, contact/support assumptions and verification limits is still
required; the original desk review does not cover later corrections. No hardware
proof gate or final architecture is approved. PR #18 remains Draft; no merge.

No further Fusion testing is requested by this task. Raw diagnostic files stay
outside Git and are preserved locally; `/tmp` is not a durable raw-data archive.
The sections below retain earlier investigation and acceptance checkpoints;
this completed matrix supersedes their narrower pending-status statements.

## Accepted carrier-resize runtime evidence — 2026-10-13

The maintainer reports that all seven requested CHECKs passed after creating the
corrected separate B,inset design on Forbidden Fruit (Fusion Personal/macOS).
The agent read all seven local diagnostic files directly, in modification-time
order, and confirmed **160 → 164 → 160 → 156 → 164 → 156 → 160 mm**. Every file
reports CHECK PASSED, 59 component snapshots, all 59 footprints fully constrained
with healthy sketch state, and no bounds discrepancies above 0.001 mm. All runs
have gap=0.5 mm and travel X/Y=0 mm. CHECK also passed volume comparison and the
nominal box release sweep. Fixed-carrier center remains (100,120,-21) mm within
floating-point noise; 164 mm bounds are (18,38,-24)/(182,202,-18) mm as intended.

This establishes an observed Fusion runtime pass for the **B,inset carrier resize
correction and restoration sequence**, including both supported carrier limits.
It supersedes earlier pending statuses only for this tested scope. The maintainer's
response supplies continuity of the requested same-new-document procedure; the
reports do not independently record document identity. No new gap edits, actual
Y/X release parameter edits or reverse-docking runs after this rectangle fix were
reported. Earlier such passes belong to the earlier source/design. Other variants,
Windows runtime, exports, full parameter combinations, physical docking and
interference safety remain unverified. The swept-box software check is not a
full Fusion contact/interference certification.

Reports remain under `/tmp/`, outside Git and PR #18. These names and hashes
record provenance without committing diagnostic files; temporary files are not
a durable raw-data archive.

| Carrier | Local report filename | SHA-256 |
| --- | --- | --- |
| 160 mm | `tesseract-phase1c-check-sdagtrxu.txt` | `5ba21785fc85964d03897969e00498876a04834fb3f3613e0811960f05905fcc` |
| 164 mm | `tesseract-phase1c-check-5_4b7dhl.txt` | `aab7a2a3f83f129c8a4ccff5bf505747f6ece87dd47d47376a3af93c8122c19d` |
| 160 mm | `tesseract-phase1c-check-g01ccjx0.txt` | `6bd28cc7c43f4b0e334024f9d15e278c957b7cc45f4c72fc04f4e45881024129` |
| 156 mm | `tesseract-phase1c-check-041lzbqg.txt` | `fe58e58556db7a0fe6da4bd131dd7f18e2fa192f845eecc966b2dfb6223da624` |
| 164 mm | `tesseract-phase1c-check-xzxem_9s.txt` | `5d3b23ee2b47b3d607f6f1ac5e425058157ddff138d053cb437e6462719c6730` |
| 156 mm | `tesseract-phase1c-check-by48kx2v.txt` | `fe58e58556db7a0fe6da4bd131dd7f18e2fa192f845eecc966b2dfb6223da624` |
| 160 mm | `tesseract-phase1c-check-b_834fp4.txt` | `6bd28cc7c43f4b0e334024f9d15e278c957b7cc45f4c72fc04f4e45881024129` |

Current local entry-point SHA-256: `4a9c5ad2c7df53dfd2579199ae63fc78810304994689aac5703ab56bc6370398`.
The files identify this worktree's script path, but do not embed a source hash;
the hash above was taken during evidence review. No source was edited between
the requested run and this review. Previous source tests: **47 passed (14.918 s)**.
This follow-up changes documentation only; Markdown/link and whitespace checks
were repeated, not the unchanged Python suite. No commit, push, PR update, merge,
Fusion save or hardware action was performed or authorized by the reported pass.

## Earlier evidence boundary (historical)

The maintainer reports successful `B,inset` generation on Fusion Personal for
macOS, with 59 named solids/reservations and four 5 mm mounting holes on 100 mm
centers. Gap edits/restoration, Y release, X release and reverse docking passed
CHECK; an invalid X-first move correctly failed the sequence-domain check.
These are user-observed CAD results, not physical evidence. After the numeric
correction, carrier 164 mm passed the parameter-range gate but CHECK failed on
`Fixed_cold_carrier` body bounds. This is a failed CHECK, not a runtime pass.
Other variants, the full parameter matrix, exports and physical validation
remain unverified. Software geometry checks cannot validate forces, temperatures,
fit, safe operation or repeatability. Fusion/macOS version numbers were not supplied.

## Full 164 mm runtime report — 2026-10-13, cause confirmed

The maintainer reran CHECK in the existing design. The short dialog reported
`Fixed_cold_carrier` failure and `/tmp/tesseract-phase1c-check-mm0alj_4.txt`.
The agent read that 240,226-byte local report directly; the diagnostic file is
not copied into the repository or included in PR #18. This evidence supersedes
the missing-164-vertex uncertainty in the earlier investigation below.

**The profile is a trapezoid, not a rigidly translated rectangle.** Its measured
vertices, rounded to mm for readability, are:

| Vertex | Actual XY (mm) | Intended XY (mm) |
| --- | --- | --- |
| Lower left | (18, 38) | (18, 38) |
| Lower right | (182, 36) | (182, 38) |
| Upper right | (182, 200) | (182, 202) |
| Upper left | (18, 200) | (18, 202) |

Both origin-to-lower-left driving dimensions reference the correct point and
evaluate to 1.799999999999999 and 3.799999999999999 cm. The horizontal size
references lower-left to lower-right; the vertical size references lower-right
to upper-right. Both evaluate to 16.400000000000002 cm and are driving. The
observed trapezoid satisfies all four scalar dimensions: lower-left=(18,38),
right-minus-left X=164, and upper-right-minus-lower-right Y=164. Nothing requires
the lower-right Y to equal the lower-left Y. The geometric constraint list is
empty and `fullyConstrained=False`. Sketch and extrusion health report `(0, '')`.

This confirms the missing edge-orientation constraints as the source defect.
The correct corner and evaluated expressions rule out a mistaken lower-corner
reference or missing parameter propagation for this failure. X happens to
retain vertical side alignment; that alignment was not constrained. The report
establishes the actual final vertices, not Fusion's internal choice of solver
trajectory. Native/proxy and regular/precise bounds agree; identity occurrence
and successful unchanged recompute remain confirmed. The 164 × 164 bounding-box
dimensions conceal a nonrectangular cross-section.

Across all 59 component snapshots, six exceed the unchanged 0.001 mm bounds
threshold: `Fixed_cold_carrier`, `Moving_cold_carrier`, `X_bridge`,
`Y_rail_1_ENVELOPE`, `Y_rail_2_ENVELOPE`, and `Common_cartridge_mount_plate`.
Each has -2 mm in both Y bounds. All 59 footprints report no geometric
constraints and an underconstrained state, including those whose current bounds
match. Passing bounds at one setting therefore cannot establish editability.

The same report captures carrier internal value `16.400000000000002` cm,
whose multiplication by ten is `164.00000000000003` mm. This is actual evidence
of the previously reproduced one-ULP conversion path in this run; the historical
first failing run's exact internal value remains unavailable. The existing
normalization produces model carrier=164 and correctly reaches geometric checks.

The existing local generator correction already adds the four missing edge
orientations for **new** footprints; no additional source repair is needed from
this report. A new regression uses the observed vertices to show that the old
four drivers permit the trapezoid while the corrected constraint graph rejects
it and solves to the intended rectangle. It does not emulate the Fusion solver.
The next maintainer test is the **separate new unsaved B,inset document** and
bidirectional resize procedure below. Preserve the old design. The corrected
generator still has no observed Fusion runtime pass, and no physical claim is made.

## Rectangle constraint correction — historical investigation before acceptance

The maintainer completed the earlier two-run comparison in the **same existing
B,inset design** on Forbidden Fruit (Fusion Personal/macOS). With travel X/Y=0
and gap=0.5 mm:

| Carrier | Result | Actual min XYZ (mm) | Actual max XYZ (mm) | Actual center XYZ (mm) |
| --- | --- | --- | --- | --- |
| 164 mm | **FAILED** | approximately (18, 36, -24) | approximately (182, 200, -18) | approximately (100, 118, -21) |
| 160 mm | **PASSED**, all 59 bounds/volumes and nominal box sweep | (20, 40, -24) | (180, 200, -18) | (100, 120, -21) |

At 164 the dimensions are 164 × 164 × 6 mm, but both Y bounds are 2 mm below
expected (38, 202). Native and assembly-proxy bounds agree, the transform is
identity, and `computeAll()` returned True without changing the failure. This
supports a placement/shape dependency investigation over a simple size,
occurrence-context or pending-compute explanation. At 160 the footprint reported
`fullyConstrained=False`; its four dimension expressions were the intended lower
X/Y expressions and `t1c_carrier` twice. The **evaluated sketch parameters and
vertex coordinates at 164 have not been supplied**. Their expected values are
1.8, 3.8, 16.4 and 16.4 cm; these are predictions, not measured API values.

### Demonstrated source defect and bounded correction

The old generator used `addTwoPointRectangle` seed coordinates and four driving
scalar dimensions without adding edge orientation constraints. Autodesk's
[official sketch-line sample](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/CreateSketchLines_Sample.htm)
explicitly adds two horizontal and two vertical constraints to the returned
rectangle. Initial rectangular coordinates alone do not encode that design
intent. The source constraint equations leave four of eight corner coordinates
free; this agrees with the observed unconstrained state. In particular, a
vertical dimension on one edge does not bind the other edge's Y coordinates.
The exact solver trajectory that produced the reported bounding box, and why
X happened to track correctly, remain unconfirmed without the 164 vertex and
dimension-reference report. A rectangular bounding box does not prove the
underlying profile stayed rectangular.

`constrain_footprint` now adds all four edge orientations before retaining the
existing lower-corner X/Y and width/depth driving dimensions. The lower corner
is selected by coordinates, independently of returned edge order. No geometry
is fixed at initial coordinates and no dimension becomes driven/reference-only.
Generation rejects a footprint that remains underconstrained and identifies the
component, edge and axis if an orientation constraint fails. This shared path
covers all generated box parts in all four variants; exposure is not confined
to the cold carrier. CHECK's strict 0.001 mm bounds comparison, volume and sweep
checks, previous bore fix, and one-ULP numeric boundary correction are unchanged.

CHECK additionally reports linear-dimension orientation and both referenced
entities' component-space XYZ coordinates in mm, using Autodesk's documented
[SketchLinearDimension entityOne/entityTwo](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_SketchLinearDimension.htm).
Unavailable optional readings remain labeled; they never override a mismatch.
Existing parameter snapshots report actual expression evaluations at either size.

### Complete local diagnostic files (implemented; first report read)

The maintainer reports that Fusion's unscrollable message box truncated the
previous diagnostic text. CHECK now writes its full success result or exception
traceback and all expected components' diagnostic snapshots into a unique UTF-8
`/tmp/tesseract-phase1c-check-*.txt` file on Forbidden Fruit. The dialog contains
only the short result (including the failing part when identified) and exact
path. Files are outside the repository and are not PR artifacts. On Windows,
the native temporary directory is used instead. Temporary reports may be removed
by the operating system; retain evidence separately if durable review requires it.

Snapshots include parameter expressions/evaluations, sketch dimensions and
references, constraint types, line endpoints, actual/expected bounds, context,
recompute and feature health. They are collected before geometry rejection so
the first failing component does not truncate the remaining component reports.
Failures before a usable model is available still produce the error traceback
and available user parameters; unavailable information is not invented.
The existing recompute call remains; no new compute, save, regeneration or
parameter mutation is introduced by logging.

**Completed evidence-capture action:** in the existing design set carrier=164 mm,
travel X/Y=0 mm and gap=0.5 mm, then run **CHECK** from this worktree. Tell the
agent that the run completed (or give only the short file path); the agent can
read that local file directly on the same machine. No transcription or screenshot
of the report is required. Investigate that evidence before claiming a repair.

### Minimum maintainer verification

Changing generator source does **not** retrofit an existing Fusion timeline.
No existing design was regenerated, saved, edited or overwritten by the agent.

1. If the old complete 164 report was not retained, use the existing document
   with carrier=164, gap=0.5 and travel X/Y=0; run the updated script with **CHECK**.
   The complete report is written to `/tmp/`; notify the agent to read it
   directly. Do not save over the design.
2. To test the corrected generation path, run this worktree's script with
   **B,inset**, which creates a **separate new unsaved document**; keep the old
   document intact. This is a maintainer action, not an automatic repair. If
   generation fails, retain the component/edge error and stop.
3. In that new document, keep gap=0.5 and travel X/Y=0. Change carrier and run
   **CHECK** after each value: **160 → 164 → 160 → 156 → 164 → 156 → 160 mm**.
   Do not regenerate between changes. Every run must check all 59 parts, and
   the fixed footprint must report `fullyConstrained=True`. Expected fixed
   carrier center is always (100,120,-21) mm; at 156 its min/max are
   (22,42,-24)/(178,198,-18), at 164 (18,38,-24)/(182,202,-18).
4. Repeat gap edit/restoration and the previously tested Y-then-X release and
   reverse docking sequence in the new document. Retain full failures, or report
   each passing setting and Fusion version. Do not save/export during this test.

Use **Utilities > Add-Ins > Scripts and Add-Ins > TesseractDockingFixture** from
`<phase1c-worktree>/cad/fusion/TesseractDockingFixture`.
The corrected implementation has **no observed Fusion runtime result yet**.
Other variants' kernel behavior and physical capability remain unverified.

## Earlier fixed carrier bounds diagnostics — 2026-10-13 (historical)

Observed in the existing `B,inset` document on Forbidden Fruit after setting
carrier=164 mm, travel X/Y=0 mm and gap=0.5 mm: the range error did not recur,
but `check_design` raised `Body bounds disagree with parameters:
Fixed_cold_carrier`. Neither actual body coordinates nor feature-health data
were included in that original message. At this earlier stage, diagnostics were
added without a geometry correction; the results above supersede that uncertainty.

Source inspection establishes the intended dependency chain: lower sketch
corner X=`t1c_fixed_x-t1c_carrier/2`, Y=`t1c_center_y-t1c_carrier/2`, driving
rectangle width/depth=`t1c_carrier`, construction plane Z=-24 mm, and positive
extrusion height=6 mm. All occurrences are created with identity transforms,
and CHECK rejects moved occurrences before comparing native component bounds.
Native and assembly coordinates should therefore coincide in this fixture.
No observed transform or feature state in the existing design has yet been
captured to independently confirm this expectation.

| Carrier | Expected min XYZ (mm) | Expected max XYZ (mm) | Size XYZ (mm) | Center XYZ (mm) |
| --- | --- | --- | --- | --- |
| 160 | (20, 40, -24) | (180, 200, -18) | (160, 160, 6) | (100, 120, -21) |
| 164 | (18, 38, -24) | (182, 202, -18) | (164, 164, 6) | (100, 120, -21) |

CHECK still uses native `body.boundingBox`, the same cm-to-mm conversion and
**0.001 mm bound comparison**. No part is skipped and no tolerance is expanded.
Diagnostics supplement a mismatch and also accompany a successful CHECK for
the fixed carrier, allowing the same existing document to be compared at both
settings. They report:

- Actual/expected min/max XYZ, signed actual-minus-expected discrepancies,
  actual dimensions and center, all in mm.
- Native bounds before the existing `computeAll()` call and after it; compute
  return value and timeline marker/count. No second recompute is added.
- Native tight (`preciseBoundingBox`) and assembly-proxy regular/tight bounds,
  plus occurrence transform. These are diagnostic comparisons only; they cannot
  override a failed regular bounding-box check.
- Relevant user parameter expressions/internal cm values before and after
  compute, normalized model values, source formulas, and component model
  parameters (including sketch/plane/extrusion parameter expressions).
- Sketch health/messages, fully-constrained state, dimension expressions and
  driving flags, constraint types, line endpoints transformed from sketch space
  to component space, and extrusion health/messages/suppression.

Autodesk documents that `computeAll()` completion does not guarantee successful
recomputation of each timeline item; feature health must be inspected. The
previous traceback establishes that compute returned true, not that geometry
was healthy. The diagnostic code does not roll the timeline, edit dimensions,
regenerate, save, export, or set parameters. Optional unavailable API diagnostics
are labeled unavailable and cannot suppress the original mismatch details.

Interpretation remains conditional: unchanged 160 mm bounds at carrier 164 may
indicate stale/failed regeneration or a missing dependency; a correct size at a
wrong center points toward offsets/datum/placement; different native and proxy
readings warrant a context investigation; different regular and tight boxes
warrant a bounding-box investigation. None is established by static tests.
Parameter snapshots also expose any value/expression change during recompute;
the existing extraction/check order is preserved until evidence justifies a fix.

### Minimum repeatable CHECK comparison in the existing design

1. Keep the existing B,inset document active. With X/Y travel=0 mm, gap=0.5 mm
   and carrier=164 mm, close the Parameters dialog.
2. In **Utilities > Add-Ins > Scripts and Add-Ins**, run **TesseractDockingFixture**
   from this folder and enter **CHECK**, replacing the default creation choice:

   ```text
   <phase1c-worktree>/cad/fusion/TesseractDockingFixture
   ```

3. Preserve the **complete** dialog text, including bounds/parameter/health
   diagnostics and traceback if it fails. A failure is expected to remain a
   failure unless the actual checked geometry agrees; this patch adds evidence.
4. Change only carrier to **160 mm** in the same document. Run **CHECK** again
   and preserve the complete result, including the fixed-carrier diagnostic
   appended to a successful result. Leave X/Y travel and gap unchanged.
5. Send both results, labeled 164 and 160, plus Fusion/macOS versions if known.
   Do not create a new fixture, drag components, delete constraints, save over
   the design, or substitute a visually similar result to get a passing check.

No new runtime pass is recorded. One-ULP correction and all prior fixes remain;
publication and any actual geometry repair await evidence and explicit approval.

## Carrier upper-bound correction — 2026-10-13, range gate passed; CHECK failed later

At travel X=0, travel Y=0 and gap=0.5 mm, the maintainer entered `164 mm` for
`t1c_carrier` (displayed `164.00`). CHECK failed in `model.parameters(inputs)`
with `carrier must be finite and within [156, 164]`. The actual internal
centimeter value was not captured, so the original runtime cause remains
unconfirmed. The entry point reads `parameter.value * 10` for length inputs
and leaves unitless `float_yaw_deg` unchanged. The model compared against strict
inclusive bounds before derived dimensions or geometry were checked.

**Confirmed source defect and representative reproduction:** Python binary64
arithmetic gives `(164 * 0.1) * 10 == 164.00000000000003`. The intermediate is
`16.400000000000002` cm; the final error is one outward representable step,
`2.842170943040401e-14` mm. The old checker rejects this value with the observed
error. Conversely, `16.4 * 10 == 164.0` passes. This distinguishes a demonstrated
numeric failure path from proof of Fusion's specific stored value; no incorrect
unit scale has been established.

Endpoint screening of the same conversion path reproduced upper-bound rejection
for `float_xy=0.8` (becomes `0.8000000000000002`) and `mount_bore=6` (becomes
`6.000000000000001`). Some lower endpoints move one step inward and already pass.
The original integer endpoint tests did not exercise these conversions.

The model now accepts **only the single immediately adjacent floating-point
value outside a nonzero declared bound**, determined with `math.nextafter`, and
normalizes it to the bound before subsequent validation/derived expressions.
This is the smallest representable outward allowance that covers the reproduced
defect. Two outward steps are rejected; no decimal rounding, general epsilon or
manufacturing tolerance is introduced. All already-valid inputs are preserved
exactly. Zero remains strict, as do nonfinite/type checks and the existing
travel-versus-stroke, release ordering, guard, geometry, bounds and volume checks.
Range errors now show `repr(value)` in model units, exposing any future rejected
converted value instead of hiding it behind a rounded display.

This is not a general correction for accumulated numerical errors or independent
near-equal expressions at dynamic travel limits. Those comparisons remain strict;
their adjacent-float negative controls still reject excess travel and incomplete
Y release. No geometry, dimensions, unit extraction or Fusion document is edited
by the correction. New `fixture_model.py` SHA-256:
`2cf8d206ab5bd22210a62209283dd2d93d10fd06d8e3bf8c6122aeacc5cf4c18`.
Use this with baseline `ed1c74a` and the prior uncommitted entry-point/manifest
hashes in [review](review.md); the commit alone does not identify this patch.

### Earlier numeric-correction rerun procedure (superseded by comparison above)

1. Keep the existing generated `B,inset` design open and active. In **Modify >
   Change Parameters**, confirm `t1c_travel_x=0 mm`, `t1c_travel_y=0 mm`,
   `t1c_gap=0.5 mm`, and set/leave `t1c_carrier=164 mm`. Close the parameter dialog.
2. In **Utilities > Add-Ins > Scripts and Add-Ins**, select
   **TesseractDockingFixture**, with Full Path:

   ```text
   <phase1c-worktree>/cad/fusion/TesseractDockingFixture
   ```

3. Click **Run**, replace the default `B,inset` with **`CHECK`**, and accept.
   The script reloads its sibling model file on each run; no regeneration of the
   design is needed. Expected: **Phase 1C CAD check**, reporting 59 checked
   solids/reservations and matching bounds/volume, without a carrier range error.
4. Confirm carrier/bridge widths 164 mm, mount plate 176 mm and retained sheets
   180 mm. Restore `t1c_carrier=160 mm` and run **CHECK** again.
5. Report the actual dialog or complete error text, Fusion/macOS versions, and
   measurements performed. If a range error persists, the new message includes
   the converted value; retain it without manually rounding parameters to hide it.

Do not mark this numeric correction runtime-passed until the user reports the
result. Commit, push, Draft PR #18 updates and merge require explicit approval;
a successful rerun by itself is not that approval.

## Earlier macOS runtime correction — 2026-10-13

Source baseline: `ed1c74a` on Draft [PR #18](https://github.com/VoidPhoenixApps/project-tesseract/pull/18),
plus the maintainer's uncommitted visibility and manifest corrections. Preserve
those edits and the local `.vscode` folder. No commit/push of this correction is
authorized until the requested observed run and user acceptance.

- **Confirmed API error:** assigning `ConstructionPlane.isVisible` raised a
  no-setter `AttributeError`. Autodesk documents it as read-only; the writable
  `isLightBulbOn` property is valid for both construction planes and sketches.
  All three local replacements are retained. The manifest's `windows|mac` is
  Autodesk's documented cross-platform value. This verifies API/manifest usage,
  not successful runtime behavior on either OS.
- **Observed solver failure:** the next `B,inset` run reached the mounting bores
  and rejected the horizontal driving center dimension with
  `VCS_SKETCH_OVER_CONSTRAINTS`. The supplied traceback does not identify the
  hole index or existing constraints. The bore code adds no explicit horizontal,
  vertical, coincident, fixed or AutoConstrain relations. Four free circles have
  twelve planar degrees of freedom; four X/Y/diameter triples are not inherently
  redundant. Inferred alignment, coincidence or another solver relation could
  make a dimension redundant, but **the specific cause is not confirmed**.
  The circle API reference does not establish what constraints this failed run
  actually contained. Do not report inferred constraints as observed evidence.
- **Bounded correction for interactive verification:** one circle per named
  sketch on the same construction plane, followed by one through-cut per hole.
  This removes cross-hole sketch coupling while preserving the common global
  datum, plate motion, pitch and driving diameter expressions. No constraints
  are deleted, dimensions changed to driven, points fixed or solver disabled.
  Failures retain the original exception and report component/hole, operation,
  expressions, constraint types, dimension count and center fixed state. Distance
  failures include constraint state before and after the rejected operation.

### Earlier creation procedure (B,inset creation now user-confirmed)

1. Inspect then close the incomplete generated document without saving if it
   contains no work you want to retain. Leave unrelated documents alone.
2. Open **Utilities > Add-Ins > Scripts and Add-Ins**. Select
   **TesseractDockingFixture** and verify its Full Path is:

   ```text
   <phase1c-worktree>/cad/fusion/TesseractDockingFixture
   ```

   If needed, use **Script or add-in from device** to register that folder.
   Do not select the main checkout or the separate smoke-test script.
3. Click **Run**, enter `B,inset`, and accept. The expected completion dialog is
   **Phase 1C concept generated**, reporting **59 named solids/reservations**.
   If it fails, preserve the complete error text, including chained exceptions;
   report the named hole and operation. Do not manually remove constraints to
   get past the failure.
4. In `Common_cartridge_mount_plate`, inspect four `Common_mount_hole_1` through
   `Common_mount_hole_4` sketches (names end `_NOT_fastener_selection`) and four
   `Common_mount_bore_*` cuts. Verify four through holes, diameter 5 mm, on a
   100 x 100 mm pattern; centers are X=230.5/330.5 and Y=70/170 mm. Inspect driving
   X/Y/diameter expressions and ensure the timeline has no warnings/errors.
5. Follow the parameter matrix below, especially pitch 110 / diameter 6, carrier
   164, gap, and ordered Y/X travel and restoration. Measure hole centers relative
   to the plate after edits: the pattern must remain centered on it. **CHECK's
   bounds/volume comparison alone cannot detect misplaced holes of equal volume.**
6. Report the completion dialog or error, Fusion About version, macOS version,
   parameter checks actually performed and whether you accept this correction.
   Record `ed1c74a` plus this uncommitted runtime patch (source SHA-256 if needed),
   rather than attributing the patched run to the unchanged commit. Successful
   creation alone does not pass the parameter matrix or the other three variants.

The reported results at the top supersede the earlier pending status only for
the checks the user actually performed. The current rerun is **CHECK in the
existing design**, as specified above. Windows runtime, remaining variants and
exports stay pending unless separately observed. Publication still requires
explicit approval.

## Register the new script

Replace `<phase1c-worktree>` with your existing checkout location; it is a
placeholder, not a literal directory. Use the folder separator for your OS.

Keep the existing registered smoke-test worktree unchanged. This generator has
its own name and manifest. Do not copy over any AppData script.

1. In Fusion open **Utilities > Add-Ins > Scripts and Add-Ins**.
2. Choose **Script or add-in from device** and select this folder on POTUS
   (use the Forbidden Fruit path above on macOS):

   ```text
   <phase1c-worktree>\cad\fusion\TesseractDockingFixture
   ```

3. Confirm the registered Full Path is that folder, select
   **TesseractDockingFixture**, and click **Run**.
4. Accept `B,inset` for the first concept. It creates a **new unsaved document**;
   existing documents remain open. A final check dialog appears only if source
   screening and the generator's body checks succeed. Error dialogs retain the
   traceback and leave any partial new document available for inspection.
5. Run again with `A,inset`, `A,center` and `B,center` for comparisons. There is
   no automatic save, export, network access, physical command or configuration
   change in the generator. Registration is an explicit user operation.

The entire script folder (entry point, manifest and `fixture_model.py`) is needed.
Ordinary Python cannot run `adsk` geometry; no external pip dependency is needed
inside Fusion. The source loads only the sibling model module. Moving/removing
the feature worktree will break registration. After a future approved merge,
register the corresponding main-checkout folder separately; do not unregister
or alter `.worktrees/fusion-smoke-test` as part of this task.

## Interactive acceptance matrix — not performed by Codex

Record Git commit, Fusion About version, OS, date, selection, parameter values,
results/screenshots and any failure text in the Draft PR. Do not record account
or license identifiers. Native F3D save/export is optional user work and must be
recorded separately if actually performed; no generated CAD file is claimed here.

| Check | Expected observation / limit |
| --- | --- |
| New document and naming | Separate unsaved concept; A 51 or B 59 named components; one solid/body per component including hidden reservations |
| Surface size | Inspect > Measure: each sheet 180 x 180 x 1; tops Z=0 |
| Docking datums | Centers X=100 and 280.5, Y=120; sheet gap 0.5; carrier gap 20.5 |
| Cartridge interface | Mount plate 172 x 172 x 4; four 5 mm through holes, 100 mm center spacing; plate bottom Z=-32 |
| Contact topology | A one X pad; B two with 120 mm separation; Y pad common; contact band Z=-22..-18 |
| Support | All three shoes/keys and plate support footprints visible after hiding upper components; no change in Z along path |
| Thermal reservations | Toggle hidden anchors/radial regions on individually; center versus lower inward-corner inset 16; recognize intentional reserved overlaps |
| Guide versus float | A rigid keys, B separate shoes/guard clearances; no claim of functioning bearing or hold-down |
| Parametric history | Inspect driving sketch offsets/width/depth, plane offsets, extrusion and bore expressions; timeline free of warnings/errors |
| Measurement access | Probe targets extend on +Y; assess real indicator/stand access separately, not from camera visibility |

Dimensions should agree within 0.001 mm for this numerical CAD comparison;
record displayed precision. This is not a physical tolerance.

### Parameter changes and CHECK

Use **Modify > Change Parameters**. After every edit, rerun the same script with
`CHECK` while that generated design is active. CHECK does not make a new document
or save the Fusion document; it recomputes and examines generated geometry and
writes a local diagnostic text file. It rejects added
untagged components/root bodies/nested components and moved occurrences rather
than silently certifying geometry outside its source model. It is not a general
Fusion interference solver; manual topology/history inspection remains required.

1. At dock, change `t1c_gap` to 1: expect moving X center 281 and sheet gap 1;
   reference bed remains at X=100. Restore 0.5 and CHECK.
2. Change `t1c_travel_y` to 8: both moving surfaces move +Y 8, X stage stays at
   its initial Y, surfaces stay Z=0. Then change `t1c_travel_x` to 40: upper
   assembly moves +X 40; sheet gap is 40.5 and Y stagger 8. CHECK each endpoint.
3. Restore X to 0 **before** restoring Y to 0; CHECK at each step. No animation
   or real-machine motion is being commanded.
4. Change `t1c_carrier` to 164: carrier/bridge widths become 164, mounting plate
   176; sheet remains 180. CHECK, then restore 160.
5. For B, change `t1c_pad_baseline` to 110: station and moving X contacts remain
   paired with 110 mm separation. CHECK, then restore 120.
6. Change `t1c_mount_pitch` to 110 and `t1c_mount_bore` to 6: holes move/resize
   while plate stays 172 square. CHECK, restore 100 and 5, CHECK again.
7. In inset variant, change `t1c_anchor_inset` to 20: hidden anchor reservations
   move inward relative to both joining edges. Restore 16. This does not simulate
   thermal expansion.
8. Negative check: at the original dock set `t1c_travel_x=1` while Y=0, then CHECK.
   Expect a sequence-domain rejection; undo X. Optionally set `t1c_guard_gap=0.5`
   and expect a domain rejection; restore 1.5. Fusion may temporarily draw an
   invalid state—the checker is not an edit-time interlock.
9. Run the creation mode again: new document, defaults restored, original concept
   untouched. Confirm no duplicate parameters within either document.

Use Fusion's manual interference inspection with reservation components hidden,
and inspect contacts and sliding support faces separately. Contact/touching is
intentional; positive-volume overlap is not. Look at intermediate path poses,
not just dock/released endpoints. CHECK's primitive volume/bounds tests cannot
detect every possible topology change with identical bounds/volume.

## Reproducible source checks

From the feature worktree root, use an existing Python 3.9+ interpreter:

```powershell
python -B -m unittest discover -s tests -p test_phase1c_fixture.py -v
python -B -m unittest discover -s tests -v
python -B scripts/check_fusion_smoke_test.py
git diff --check
git diff --cached --check
```

On POTUS this task used the existing Codex-bundled Python 3.12.14 at
`C:\Users\toddn\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.
No interpreter, package or PATH changes were made. The generic command above
requires a real Python interpreter, not a Windows Store alias.

The original nine Phase 1C tests cover source/manifest, four variant nominal/release
geometries, dimensions/dependencies, one-factor parameter endpoints, bad/nonfinite
inputs, rank loss/redundancy, shared cartridge interface, injected interference,
and the distinction between guard clearance and unsafe worst-case seam capture.
They use the same declarative specification as the generator. Six additional
tests cover writable visibility, the plate-relative bore pattern, isolated
driving bore/cut API calls, solver failure context, null diameter handling and
constraint diagnostics. The four API contract tests use small test doubles;
they **do not implement or verify Fusion's constraint solver**. Kernel
verification is deliberately separate. Existing reporting tests
remain unrelated to printer validation.

Four numeric regression tests additionally cover all 17 parameter domains:
exact endpoints and representative cm/mm roundtrips, one-step outward allowance
versus two-step/1e-9 violations, nonfinite/type rejection, unchanged nearby valid
values, the 164 mm derived plate size and four variant analytical sweeps, and
strict release/transport negative controls. These are source tests, not a Fusion
kernel emulation.

The separate `test_phase1c_diagnostics.py` tests use API-shaped doubles to compare
160/164 reports and injected stale/shifted geometry, before/after recompute,
optional diagnostic failure, recompute failure and moved-occurrence rejection.
They verify reporting and strict rejection behavior, not actual Fusion geometry
or kernel regeneration.

On macOS, use `python3` instead of `python` in the commands above. No new Python
environment or package installation is required.

Full Cartesian parameter-domain coverage, actual tolerances, angular capture,
material strength, force closure, stiffness, friction, fatigue and thermal
behavior are not tested. No whole-machine simulation is supplied.

## API source references

Autodesk documentation consulted for supported API behavior:

- [Script and manifest conventions](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm)
- [Driving sketch dimensions](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_SketchDimensions_addDistanceDimension.htm)
- [Offset construction planes](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ConstructionPlaneInput_setByOffset.htm)
- [One-sided extrusion](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ExtrudeFeatureInput_setOneSideExtent.htm)
- [Body bounding boxes](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepBody_boundingBox.htm)
- [Construction plane visibility (read-only)](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ConstructionPlane_isVisible.htm)
- [Construction plane light bulb (writable)](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ConstructionPlane_isLightBulbOn.htm)
- [Sketch light bulb (writable)](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Sketch_isLightBulbOn.htm)
- [Circle creation and centimeter radius](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_SketchCircles_addByCenterRadius.htm)
- [Sketch constraints](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Sketch_geometricConstraints.htm)
- [Point constraints](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_SketchPoint_geometricConstraints.htm)
- [Tight body bounding boxes](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepBody_preciseBoundingBox.htm)
- [Native geometry and assembly proxies](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ComponentsProxies_UM.htm)
- [Create a body proxy](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepBody_createForAssemblyContext.htm)
- [Compute completion limits (inherited Design method)](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_WorkingModel_computeAll.htm)
- [Feature health state](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Feature_healthState.htm)
- [Component model parameters](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Component_modelParameters.htm)

Runtime-correction API references were checked on 2026-10-13 against Autodesk's
current documentation. Context7 returned no matching constraint documentation;
the official Autodesk references above were consulted directly.

The Python implementation is original project code using the existing smoke
test's approach, not vendored Autodesk sample code. No project license is added.
