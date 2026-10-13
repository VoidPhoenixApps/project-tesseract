# Reproduction and verification

## Evidence boundary

The generator and analytical checks are source artifacts. **Fusion execution,
CAD kernel validation, native export and physical testing of Phase 1C are not yet
observed.** PR #16's successful user-run smoke test is a prerequisite, not a
substitute. Software geometry checks below cannot validate forces, temperatures,
fit, safe operation or repeatability.

## Register the new script

Keep the existing registered smoke-test worktree unchanged. This generator has
its own name and manifest. Do not copy over any AppData script.

1. In Fusion open **Utilities > Add-Ins > Scripts and Add-Ins**.
2. Choose **Script or add-in from device** and select this folder:

   ```text
   D:\Development Projects\project-tesseract\.worktrees\phase1c-docking-fixture\cad\fusion\TesseractDockingFixture
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
or save files; it recomputes and examines generated geometry. It rejects added
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

The nine Phase 1C tests cover source/manifest, four variant nominal/release
geometries, dimensions/dependencies, one-factor parameter endpoints, bad/nonfinite
inputs, rank loss/redundancy, shared cartridge interface, injected interference,
and the distinction between guard clearance and unsafe worst-case seam capture.
They use the same declarative specification as the generator and **do not mock
Fusion**. Kernel verification is deliberately separate. Existing reporting tests
remain unrelated to printer validation.

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

The Python implementation is original project code using the existing smoke
test's approach, not vendored Autodesk sample code. No project license is added.
