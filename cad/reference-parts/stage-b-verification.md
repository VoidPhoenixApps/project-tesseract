# Stage B verification — 2026-10-15

[Issue #33](https://github.com/VoidPhoenixApps/project-tesseract/issues/33) continues merged [Stage A / PR #32](https://github.com/VoidPhoenixApps/project-tesseract/pull/32). Evidence is **reference CAD measurement and documentation/software checks**, not physical validation or detailed machine design. [Stage A evidence](verification.md) remains historical; this record supersedes its import limitation only.

## Scope and access

Started from clean, fetched `main` at `60f219a`, branch `codex/reference-parts-stage-b`; preserved unrelated PRs #17/#19 and existing CAD. Current repository instructions and merged reference workflow were read, with shared workflow/engineering/knowledge/secrets/review standards at project-knowledge `147de4d979bba17120a4cc425983d590f85b6000` (matching GitHub main), and current Home Infrastructure instructions/local-project setup standard. No project `CURRENT_STATE.md` exists in the inspected shared checkout. AgentMemory queried once for this stage, with no relevant result; GitHub governs. No other repository changed.

The library remains readable at `/Users/todd/Development Projects/tesseract-cad-library/`. The existing STEP and MIT notice still pass hashes, size, upstream blob identity and structural checks. **One local CAD asset, zero new CAD downloads.** Public documentation PDFs were read separately; they are not model assets. Numerical inspection evidence was added under `evidence/2026-10-15-feather-fusion/observations.json` locally. No vendor geometry or PDF was added to Git.

Persistent Codex attachment remains **unverified**, not proven absent. Project enumeration exposes the primary path but not additional-source settings. Computer Use explicitly refused access to the Codex app; no alternate route was used to bypass that restriction. To inspect/fix manually: open Project Tesseract's menu → **Edit project**; inspect sources and, only if missing, **Add folder** `/Users/todd/Development Projects/tesseract-cad-library/`. Keep `project-tesseract` **Primary** and `project-knowledge` additional. [Official instructions](https://learn.chatgpt.com/docs/projects#use-local-projects-for-folders-and-codebases). Attaching does not enforce read-only access. POTUS/cloud access remains unverified.

## Actual Fusion import

Installed **Autodesk Fusion 2705.1.30**, Personal license, on Forbidden Fruit. No software/add-in installed. File → Open → Open from my computer imported the existing pinned local STEP into a **new unsaved `4884-feather-rp2040` document**. No import error was observed; a populated board assembly was visible. Existing saved projects were not opened or modified. After inspection, the sample document was closed with **Don't Save**; the preexisting empty Untitled document remained.

[Autodesk's local-translation instructions](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-use-the-local-translation-process-to-open-files-in-Fusion-360.html) distinguish local open from Save, which starts cloud translation. No Save/export/upload was performed. This is not a claim about all application telemetry.

Source remains the Stage A STEP at `c128bceb1f96b6ea8b68f250bda986ba85da24ea`, SHA-256 `de85fb7f6644cdea17808208d888e64264d691573da8cd0fee808e2fd44d477f`. Header labels rev C v2, dated 2021-05-10; physical purchased-board revision remains unknown.

### Reproduce without changing a design

1. Run the [local validator](README.md#reproduce-checks) to verify existing authorized bytes before import. Do not retrieve another model.
2. In Fusion, use the local-open sequence above; confirm the new document name and that it is unsaved. Do not insert into an existing assembly, transform, scale or save.
3. View → Show Text Commands; explicitly select **Py** (a visually selected radio initially still dispatched as Txt in this session; `There is no command import` means Py was not active). Use the built-in console, not an installed script/add-in:

   ```python
   import runpy, json
   inspection = runpy.run_path('/Users/todd/Development Projects/project-tesseract/scripts/inspect_feather_fusion.py')
   result = inspection['inspect']()
   print(json.dumps(result))
   print(inspection['inspect']() == result)
   ```

4. Capture the returned numbers as evidence. The read-only [inspection script](../../scripts/inspect_feather_fusion.py) checks document name/unsaved status, but that guard is not source authentication: the prior hash check and exact-file open are necessary. It neither changes CAD nor writes files. Optional numerical JSON capture with `Path(...).write_text(json.dumps(result, indent=2))` is separate from Fusion document saving.
5. Close only the sample document, choose **Don't Save**, and rehash the original file.

The script uses [preciseBoundingBox](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepBody_preciseBoundingBox.htm), [occurrence body proxies](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_Occurrence.htm) in root assembly context, and cylindrical surface radii. [Fusion API internal lengths are cm](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Units_UM.htm); multiplying by 10 reports mm. Do not multiply unitless axes/rotation entries. No manual model transform was applied. Context7 did not provide a matching official Fusion library; Autodesk's own API documentation was used.

### Observations and comparison

[Committed numerical subset](feather-fusion-observations.json) records unrounded API values and source hash. Full raw numerical output is local; SHA-256 `bbabd08bbf84dca9db9020f80b2952de368fa0b50e706fe3ef09c19a7f4db702`. This is metadata, not a reconstructable vendor CAD export. Two reads within the **same import** returned identical results. Independent reimport/second-engine repeatability was not tested.

Official reference: [Adafruit Downloads → Original Schematic and Fab Print](https://learn.adafruit.com/adafruit-feather-rp2040-pico/downloads). The [generated official guide PDF](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-rp2040-pico.pdf), SHA-256 `180e8af7193411606706c083ee26be58ec5d0151664f559a8327d7560cff4037`, had 163 pages; page 162 contains the original fab print beside a rev C schematic dated 2021-02-23. Page 161 is the newer rev D material and was not used to assert exact revision equivalence. Both pages were rendered/read with existing bundled PDF tools. The PDF is a live generated resource; its pagination/hash may change. Original placement alongside rev C supports the comparison but does not certify any purchased board or all model features.

| Quantity | Official original fab print | Imported reference (mm) | Result / limit |
| --- | --- | --- | --- |
| PCB length X | 2.00 in | 50.8 | Matches nominal |
| PCB width Y | 0.90 in | 22.86 | Matches nominal |
| Hole-center longitudinal spacing | 1.80 in | 45.72 | Matches nominal |
| Hole-center transverse spacing | 0.70 in | 17.78 | Matches nominal |
| Hole-center edge offsets | 0.10 in | 2.54 | Matches nominal |
| Board thickness | Not established on inspected print | 1.57 | Observation only |
| Mounting hole diameters | No explicit diameter callout established | 2.50 at X=2.54; 2.54 at X=48.26 | Unequal pairs; unresolved source detail |
| Complete assembly X/Y/Z extents | No matching envelope dimension established | 51.946 / 22.86 / 6.37 | Observation only; includes connector protrusion |

Comparison arithmetic uses exactly 25.4 mm/in. Display rounding to 0.001 mm is an evidence presentation choice, **not manufacturing tolerance, metrology uncertainty or an acceptance specification**. Numerical equality does not establish fabrication fitness.

47 occurrences; 58 BRep bodies, all 58 report `isSolid`. Board `PCB Component:1+Board:1` / `Body1`, 143 faces, identity occurrence transform. Native board bounds `(0,0,0)` to `(50.8,22.86,1.57)` mm: X long edge, Y width, +Z components. Assembly bounds `(-1.146,0,0)` to `(50.8,22.86,6.37)` mm, USB side extending toward negative X. Hole centers `(2.54,2.54)`, `(2.54,20.32)`, `(48.26,2.54)`, `(48.26,20.32)`, axes +Z. The board also has 5.08 mm cylindrical outside corner surfaces; those were excluded from the hole list. A cylinder alone does not prove a hole; selection used corner location, diameter and visible board layout.

No comprehensive topology/repair audit, purchased-part measurement, mounting fastener fit, cable mating clearance, tolerance stack or physical test. Importing 58 solids is not proof all shapes are correct. The differing hole diameters and connector clearances must be resolved before dependent interface design. Fusion is an available inspection route, **not** the selected final CAD toolchain; public reproduction must still support a free/open route, which was not tested here.

## Source corrections and bounded growth

**45 candidates in 13 categories**, up 11 from Stage A. Only one is partially dimension-checked; the other 44 have documentation-only geometry. All 11 additions remain link-only with all five model permissions unknown and no retrieval authorization.

| Addition | Useful coverage | Remaining limit |
| --- | --- | --- |
| NTN 625ZZ, 608ZZ | Second bearing maker; shielded CN/class 0 identities, bore/OD/width | CAD format/rights unconfirmed; inconsistent load fields omitted |
| ANTCLABS BLTouch Smart V3.1 | Genuine probe revision | Exact solid model and mounting/stroke drawing not established |
| LDO-42STH48-2004AC(VRN) | Second motor maker with retained suffix | Exact VRN drawing; generic Rev A not assumed equivalent |
| LDO-42STH40-1684CL350E(VRN) | Integrated Tr8x4 leadscrew/PEEK nut candidate | Store specification table names another motor; sold out; corrected drawing required |
| igus SWM-08 | 8 mm Cf53 smooth shaft | Length, machining and tolerances remain unconfigured |
| igus WS-10-40-CAM-500 | Exact 500 mm double-rail alternative | Camera threads; carriage not configured; not an MGN substitute |
| Aluminium Warehouse variant 42374512902332 | Actual metric 20×20×2 mm tube, 1000 mm mill finish | Grade only 6000-series; contradictory cut tolerances; mill unknown |
| Online Metals 18014, 12 in option | Actual imperial 1×1×1/8 in 6061-T6 tube | Section/corner/length tolerances need specific review; mill unknown |
| Gates 200-2MGT-06 + 2MR-20S-06 | Manufacturer profile/width matched 2 mm / 6 mm belt and pulley | Bore machining, current drawing, drive load/tension/center distance unverified |

Each catalog entry links its official manufacturer or explicitly labeled stock supplier. No new price, availability guarantee, performance or interchangeability claim. The metric tube is not a rounded imperial profile; neither is selected reinforcement. Exact grade/tolerances are deliberately unknown where the seller does not establish them. The Gates manufacturer's indexed manual supports GT3 belt / GT2 sprocket pairing; direct manual retrieval returned 404, so current drawings remain a prerequisite. No third-party marketplace model was substituted.

- **STEPPERONLINE 17HS08-1004S:** current official listing is 21.5 mm body, offers a 1.2 MB STEP and Full_Datasheet.pdf; the older drawing approved 2018-08-18 is 20 ±1 mm. Current PDF returned HTTP 403. The source URL slug still says 20mm; that is not revision evidence. Model availability is corrected from not-located to listed, while geometry/revision remains blocked pending manufacturer mapping of drawing, STEP and supplied lot. Do not mix the old mounting drawing with the current envelope.
- **BTT:** metadata-only audit of pinned SKR `d7fd822006628143222d1c3c8cdea85ffee29e66` and Octopus `9526ff16f68839626cb8875a299e73f99f2e57e8` trees, root readmes, and Octopus `Hardware/readme.txt` found no applicable hardware/3D license grant. License files under firmware do not establish CAD rights; “open source” prose is insufficient. Octopus hardware readme also notes V1.1 silkscreen and power-IC package changes, so V1.0 geometry is not silently reused. This is a scoped negative finding, not proof no grant exists anywhere. Keep all five permissions unknown until explicit hardware-model terms are supplied.
- **HIWIN MGN:** existing size records are not fully ordered rail/carriage assemblies. The official configurator redirected to login. Required fields: exact carriage suffix/count, rail length and end-hole pattern, preload, accuracy, seals/lubrication, rail material/grade, and matched versus interchangeable status. No exact MGN assembly was added on speculation. A reviewed configuration/output and rights are needed before a model request; adding the igus alternative does not resolve MGN fit.

## Verification, changed files and next gates

Checks: generated index and offline catalog validation; local asset hashes/size/blob/STEP structure; **76 passing repository unit tests**; Python script syntax; numerical summary versus raw output; changed Markdown relative links/anchors; complete diff and staged diff whitespace/public-asset review. Fusion inspection was performed live as above, not emulated by unit tests. CI only verifies repository software/catalog, not Fusion or physical geometry.

Changed files:

- `catalog.json`: 11 sourced candidates, bounded Feather observations and motor/BTT/HIWIN corrections.
- `INDEX.md`: regenerated from catalog, no independent claims.
- `README.md`: current counts, partial geometry state, access limitation and next gates.
- `verification.md`: historical Stage A evidence retained with a Stage B pointer.
- `stage-b-verification.md`, `feather-fusion-observations.json`: method, measured evidence, limitations and source audit.
- `scripts/inspect_feather_fusion.py`: reproducible read-only numerical inspection in existing Fusion.
- `docs/research-first-plan.md`: Stage A merged / Stage B evidence status, with pause intact.

Requirements, architecture, roadmap, original/Phase 1C CAD, licensing and hardware are unchanged. No hardware was operated, purchased or selected; no new model, engine or toolchain was authorized. Independent review and human merge approval remain pending for the Draft PR. No consequential architecture or safety change is proposed.

Next: resolve Feather mounting diameters/revision and cable clearances; obtain corrected LDO/STEPPERONLINE drawings, BTT model-specific permission, and a complete HIWIN configuration; then request approval for a specifically identified additional sample if needed. Keep every request consolidated with exact part/revision, desired format/source, geometry purpose, rights uncertainty and blocked work per the [missing-model workflow](README.md#future-codex-sessions-missing-model-request). No additional download is required to review this Stage B PR.

After review, separately authorized Home Infrastructure/project-knowledge updates could record persistent source attachment and the verified local Fusion inspection route by linking this evidence. Neither repository was edited; do not duplicate the candidate catalog there.
