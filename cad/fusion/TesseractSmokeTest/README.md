# Fusion geometry smoke test

This bounded API experiment creates a **40 x 30 x 10 mm solid block**, not an
approved mechanical component or validated printer design. Fusion remains a
preferred candidate, not the selected project toolchain. This Fusion-only script
does not establish the required public reproduction path without proprietary
software. Project licensing and Fusion entitlement suitability remain unresolved.

The maintainer reports that Fusion Personal is installed on POTUS and that a
separate AppData script displayed the active document name. That is not execution
evidence for this repository script. **Repository-script execution, dimensions,
and parametric editability in Fusion remain pending interactive verification.**

## Behavior and files

- `TesseractSmokeTest.py`: original project Python source using `adsk.core` and
  `adsk.fusion`; no third-party Python dependencies or copied sample code.
- `TesseractSmokeTest.manifest`: Windows script registration metadata; no startup execution.
- Every run creates a **new, unsaved design**, leaving previously open documents
  intact. It does not save, export, print, change application settings, or modify
  the existing AppData script. Re-running creates another document.
- On failure, a dialog shows the traceback. An incomplete new document is left
  open for inspection; close it without saving before retrying. No automatic
  deletion of documents or files occurs.

The component is `TesseractSmokeTest_Block`, its sketch is
`TesseractSmokeTest_Footprint`, its extrusion is `TesseractSmokeTest_Height`, and
its body is `TesseractSmokeTest_Solid`. The footprint starts at the component
origin on XY and extrudes along positive Z. No material, fit tolerance, or
manufacturing process is specified.

| User parameter | Initial expression | Drives |
| --- | --- | --- |
| `tesseract_length` | `40 mm` | X sketch dimension |
| `tesseract_width` | `30 mm` | Y sketch dimension |
| `tesseract_height` | `10 mm` | Positive-Z extrusion distance |

Sketch coordinates use Fusion's internal centimeters; parameter expressions use
explicit millimeters. Length and width are driving dimensions, not just initial
rectangle coordinates. The design explicitly enables parametric history.

## Register from the repository on POTUS

1. Keep the feature checkout available. For this Draft PR its root is
   `D:\Development Projects\project-tesseract\.worktrees\fusion-smoke-test`.
   After merge, use the corresponding folder in your updated main checkout and
   register that location instead; moving/removing a worktree breaks its registration.
2. In Fusion, open **Utilities > Add-Ins > Scripts and Add-Ins**.
3. Choose **Script or add-in from device** (the local-device/add control), then
   select the **folder**
   `D:\Development Projects\project-tesseract\.worktrees\fusion-smoke-test\cad\fusion\TesseractSmokeTest`.
   The folder, `.py`, and `.manifest` base names must match.
4. Check the selected entry's **Full Path** points to this repository checkout,
   not AppData. The existing test has the same name, so use the path to distinguish
   them. Do not overwrite or delete that original script.
5. Select the repository entry and click **Run**. This registration and execution
   are user actions; Codex has not performed them. External `python` cannot run
   the Fusion API geometry operation.

## Interactive acceptance checklist

Record the Git commit (`git rev-parse HEAD`), Fusion version from About, date,
Windows version, and the registered Full Path with the results in the PR.

1. Confirm a new unsaved document appears and the previous document is unchanged.
   Confirm the named component contains exactly one solid body and that sketch
   and extrusion features appear in the timeline without warnings/errors.
2. Use **Inspect > Measure**, selecting one edge parallel to each of X, Y and Z.
   Set/read the measurement units as mm. Expected lengths: **40, 30, 10 mm**.
   Record displayed precision and results; agreement within **0.001 mm** is a
   software geometry check, not a manufacturing tolerance or physical measurement.
3. In **Modify > Change Parameters**, confirm the three user parameters above.
   Inspect the sketch dimensions and extrusion distance: their expressions must
   reference the corresponding parameter names.
4. Without rerunning the script, change length to **45 mm**: expect **45 x 30 x
   10 mm**. Then width to **35 mm**: expect **45 x 35 x 10 mm**. Then height to
   **12 mm**: expect **45 x 35 x 12 mm**. Measure after each edit and check for
   timeline warnings/errors. Restore **40, 30, 10 mm** and remeasure.
5. Run again: expect a second new document with the original defaults, no parameter
   name collision, and no changes to the first test document. Close unwanted
   unsaved test documents manually. Save native Fusion data only if desired.

If any check fails, retain the error text and observations in the PR; do not label
the smoke test passing. No hardware test, export verification, reinforcement
variant validation, or CAD-toolchain adoption is implied.

## Static checks outside Fusion

From the repository root, with Python 3.9+:

```powershell
python -B scripts/check_fusion_smoke_test.py
git diff --check
git diff --cached --check
```

The checker compiles source without importing `adsk` or writing bytecode and
checks manifest identity/metadata. These checks cannot prove API compatibility,
geometry, constraints, or graphical execution. No Fusion runtime is mocked as
evidence of CAD success. No software installation is needed inside Fusion.

## API references

Autodesk documentation consulted 2026-10-12:

- [Script entry points and manifest](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm)
- [Rectangle creation](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_SketchLines_addTwoPointRectangle.htm)
- [Driving sketch dimensions](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_SketchDimensions_addDistanceDimension.htm)
- [One-sided extrusion](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_ExtrudeFeatureInput_setOneSideExtent.htm)
