# Stage C — source, revision and model-rights verification

Research on **2026-10-15**, for [issue #35](https://github.com/VoidPhoenixApps/project-tesseract/issues/35). Stage A [PR #32](https://github.com/VoidPhoenixApps/project-tesseract/pull/32) and Stage B [PR #34](https://github.com/VoidPhoenixApps/project-tesseract/pull/34) are merged. Stage B merged at `0f5c5adf9ccf5344b5a4fd6101a795da0ac4659e`, 2026-10-15 07:50:08 UTC. This record supplements [Stage B](stage-b-verification.md); it does not replace its measured observations.

**Result:** the Feather's unequal mounting diameters are supported by original and later PCB source definitions. Finished-hole tolerances and purchased revision remain unknown. Motor revisions, BTT hardware rights and a specific HIWIN assembly remain gated. See the additional [Fusion component-library assessment](fusion-library-research.md).

## Scope and authority

Started with a clean `main`, fetched origin, confirmed zero commits ahead/behind, and created `codex/stage-c-reference-verification`. Read project instructions, requirements, architecture, roadmap, contribution rules, reference workflow and Stage B evidence. Shared workflow/engineering/knowledge/secrets/review standards were at project-knowledge `147de4d979bba17120a4cc425983d590f85b6000`; Home Infrastructure instructions and workstation record were at `963185a4d528884473a28a87ef81ffb0d1e59dd4`. Both matched GitHub main. No Tesseract `CURRENT_STATE.md` exists there. AgentMemory was queried once and supplied no relevant continuity.

45 candidates / 13 categories remain; one approved local STEP, 44 link-only models. No additional vendor solid models downloaded, inserted, exported or uploaded. Official PCB text was read remotely in memory for the expressly requested source comparison; **no additional PCB source file was retained locally**. Public documentation PDFs were inspected separately. Only narrow factual observations, not vendor designs or PDFs, are committed. No software installation, external manufacturer contact, machine setting change, purchase, firmware or physical work occurred.

## Discrepancy matrix

| Part / physical revision | Source and revision | Source claim versus model / prior evidence | Finding and risk | Next evidence / permission |
| --- | --- | --- | --- | --- |
| Adafruit #4884; purchased revision unknown | Original PCB blob `8bb6c9c…`, later blob `6e193d2…`; pinned below | Two plated-pad drills 2.50 mm at X=2.54; two plain holes 2.54 mm at X=48.26; Stage B STEP cylinders agree | **Source explanation resolved**, not an import correction. Finished holes and fit unverified | Manufacturer finished-hole specification and physical lot/revision mapping |
| #4884 original versus later board | 2021 STEP header rev C v2; PCB update commit 2022-12-02; product change 2022-11-28 | Mounting source pattern retained; BOOTSEL and connectors require separate comparison | Old model is not a verified later-board clearance envelope | Matching later revision drawing/model and mated-cable/button envelopes; new model requires separate authorization |
| STEPPERONLINE 17HS08-1004S; revision unknown | Live official listing versus drawing approved 2018-08-18 in Stage B | Listing 21.5 mm body; old drawing 20 ±1 mm | **Unresolved**: 21.5 exceeds old upper limit 21.0; do not average or combine drawings | Dated current drawing, change notice, lot-to-STEP mapping |
| LDO-42STH48-2004AC(VRN); revision unknown | Live VRN listing versus generic Rev A PDF, dated literally `11/12/20` | Several mounting dimensions agree; electrical/inertia table differs | **Partial corroboration**, no proof generic drawing applies to VRN | Exact VRN suffix drawing and revision/change mapping |
| LDO-42STH40-1684CL350E(VRN); revision unknown | Live manufacturer store overview/specification table | 40 mm linear motor / Tr8x4 overview, but table identifies LDO-36STH20-1004AH | **Unresolved conflicting identity**; table is not usable for this part | Corrected exact Rev D drawing, screw/nut dimensions and lot identity |
| BTT SKR MINI E3 V3.0 / Octopus V1.0 | Pinned repositories listed below | STEP assets listed; no applicable hardware-CAD license established | **Rights unknown**; firmware grant does not resolve hardware rights | Explicit asset-specific rights for all five catalog actions |
| HIWIN MGN09C/H, MGN12C/H | Live HIRES size records; US catalog G99TE24-2410 | Size code is not an ordered rail-and-block assembly; no model inspected | **Configuration incomplete**; generic MGN cannot substitute | Manufacturer-confirmed order strings, drawing and options, then rights and retrieval approval |

## Feather: original and later PCB sources

Primary sources:

- [Official downloads, original and later fab prints](https://learn.adafruit.com/adafruit-feather-rp2040-pico/downloads); Stage B records the original print comparison and PDF hash.
- [Product #4884](https://www.adafruit.com/product/4884): announces the **2022-11-28** right-angle BOOTSEL change and GPIO4 connection. This is not a mechanical tolerance specification.
- [PCB update commit `ea881668…`](https://github.com/adafruit/Adafruit-Feather-RP2040-PCB/commit/ea88166891ee0a1697a3899a5d55ab3722a2f125), dated **2022-12-02**, currently the PCB repository head.
- [Original PCB source](https://github.com/adafruit/Adafruit-Feather-RP2040-PCB/blob/ea88166891ee0a1697a3899a5d55ab3722a2f125/Adafruit%20Feather%20RP2040%20Original.brd) and [later PCB source](https://github.com/adafruit/Adafruit-Feather-RP2040-PCB/blob/ea88166891ee0a1697a3899a5d55ab3722a2f125/Adafruit%20Feather%20RP2040.brd).

The original `.brd` blob is `8bb6c9c3e6748b08115e8cf83fd59995f9589ac3`, identical to `Adafruit Feather RP2040.brd` in [the 2021-03-03 board commit](https://github.com/adafruit/Adafruit-Feather-RP2040-PCB/tree/bcb719fedd6104ddb0f568529e978a11ab48471e). Later blob: `6e193d22da9639349278b825a786fb2d88d5ab40`. This establishes source continuity, not a serial-number mapping to physical inventory. The STEP's 2021-05-10 rev C v2 label remains its own provenance; Stage B identifies the later fab material as rev D.

### Hole definitions and supported dimensions

Both sources contain `U$31` and `U$32`, package `MOUNTINGHOLE_2.5_PLATED`, at `(2.54,20.32)` and `(2.54,2.54)` mm. Each package pad at local `(0,0)` specifies **drill 2.5**, **pad diameter 3.2**. The 3.2 value is the pad diameter, not the hole diameter. The opposite pair appears as plain board `hole` elements at `(48.26,20.32)` and `(48.26,2.54)` with **drill 2.54**. They are not pad elements. The package names and element types distinguish plated mounting pads from plain holes; no plating thickness or finished-hole acceptance limits were established.

Layer-20 outline coordinates in both sources span 0–50.8 by 0–22.86 mm. Together with the four centers, these corroborate the original fab print and the Stage B STEP measurements: 45.72 × 17.78 mm center rectangle, 2.54 mm edge offsets. The nominal difference **0.04 mm** is intentional in the source definitions in the limited sense that it is encoded there; its engineering rationale is unknown. Do not normalize the holes, infer a ± tolerance from the difference, or use drill fields as certified finished-hole diameters.

### Clearance changes — compare board coordinates, not footprint origins alone

| Item | Original → later source (mm) | Interpretation |
| --- | --- | --- |
| BOOTSEL | SW2 `BTN_KMR2_4.6X2.8`, `(49.022,15.24)` R90 → SW3 `SPST_TACTILE_RA_2*4*3.5MM`, `(49.149,15.3035)` R90 | New right-angle actuation; old model cannot establish lateral finger/button access, travel or newer 3D envelope |
| Battery connector X1 | Same `JSTPH2_BATT` package name; `(10.922,19.304)` → `(10.922,17.653)` | Origin moves 1.651 mm toward −Y; review housing, plug and cable route against exact revision |
| STEMMA QT CONN1 | `JST_SH4`, `(48.26,8.255)` → `(47.752,8.255)`, R90 | Origin moves 0.508 mm toward −X; same package name alone does not certify housing identity |
| USB X6 | Origin X 2.6035 → 3.8735, R270 in both; local package coordinates shift −1.27 in Y | **Not evidence that USB moved 1.27 mm on the board.** Transformed mounting-pad centers are identical; inspected package silkscreen segments compensate too. Exact 3D shell/plug clearance still unverified |
| Reset SW1 | Same package, `(11.811,6.4135)`, R180 | Selected source fields unchanged; not a complete component audit |

For USB, R270 maps local `(x,y)` to board `(origin_x+y, origin_y−x)`. All four mechanical pad centers agree between sources: M3 `(1.3935,15.75)`, M4 `(1.3935,7.11)`, M2 `(5.5735,7.11)`, M1 `(5.5735,15.75)` mm. Footprint/silkscreen data are not housing or mated-cable envelopes. No claim of full electrical equivalence or a comprehensive board diff is made.

### Reproduce the source comparison

[Extraction script](../../scripts/inspect_feather_pcb_source.py) uses Python's standard library, reads stdin only, writes summary JSON to stdout, makes no network requests and accepts only the two reviewed SHA-256 hashes. [Recorded output](feather-pcb-source-observations.json) preserves strings from source fields, source hashes and computed USB pad centers. It does not retain PCB artwork or solid geometry.

For an authorized remote-text review, run each source separately; no `.brd` is saved. Existing `gh` access is required. This is separate from and does not authorize downloading further solid models:

```sh
gh api -H 'Accept: application/vnd.github.raw+json' 'repos/adafruit/Adafruit-Feather-RP2040-PCB/contents/Adafruit%20Feather%20RP2040%20Original.brd?ref=ea88166891ee0a1697a3899a5d55ab3722a2f125' | python3 scripts/inspect_feather_pcb_source.py
gh api -H 'Accept: application/vnd.github.raw+json' 'repos/adafruit/Adafruit-Feather-RP2040-PCB/contents/Adafruit%20Feather%20RP2040.brd?ref=ea88166891ee0a1697a3899a5d55ab3722a2f125' | python3 scripts/inspect_feather_pcb_source.py
```

An unknown/empty input fails hash validation. The original-source SHA-256 is `ed5eff88e1ab8f1cc5ae8db1a1188c1932a65c35a5df9f06b8910f73ff65b0d7`; later is `8ed4623de172bab6f33e27ac1675b28ac32fe68f8a6caf89c444167db343dda2`. Neither source was edited. The PCB repository README says Creative Commons Attribution Share-Alike and references `license.txt`, absent in the inspected root; do not transfer the separate CAD repository's MIT grant to PCB files or infer a CC version. No PCB-source redistribution is proposed.

## Motor source revisions

**STEPPERONLINE:** [current official listing](https://www.omc-stepperonline.com/nema-17-bipolar-1-8deg-16ncm-22-6oz-in-1a-3-7v-42x42x20mm-4-wires-17hs08-1004s) still specifies 21.5 mm body and lists a STEP and [current Full Datasheet](https://files.omc-stepperonline.com/17HS08-1004S_Full_Datasheet.pdf). The older [official PDF](https://www.omc-stepperonline.com/download/17HS08-1004S.pdf) is the 20 ±1 mm source inspected in Stage B. Direct PDF retrieval returned HTTP 403 during Stage C; the web service recognized a one-page current PDF but did not provide usable dimensional text or an image to this session. Therefore its drawing revision and dimensions are **not newly verified**. Black/silver appearance and equal-performance language do not prove identical geometry or supplied lot. The URL's `20mm` slug is not dimensional authority.

**LDO 48 mm:** [VRN product page](https://store.ldomotion.com/products/ldo-42sth48-2004ac-vrn-nema17-stepper-motor-voron-z-axis?variant=55595352195240) names the correct suffix in its table and now supports explicit source-level mounting claims: 48 mm maximum body length, 24 ±0.5 mm shaft projection, 31 ±0.1 mm mounting pitch, four M3 holes 4.5 mm minimum deep. These agree with the generic [Rev A drawing](https://github.com/LDOMotors/ldo-stepper-datasheets/blob/fdc453d06e59b02ca5293f260e1d2b7259868901/nema17%2842mm_frame%29/LDO-42STH48-2004AC%20RevA.pdf), rendered and visually inspected. PDF SHA-256 `9aef7d3c609a0744cb55d74b7339a348cc723bab0f2460582d0eab4b1acc97b6`; printed date `11/12/20`, not assigned an ambiguous day/month interpretation. The drawing lacks `(VRN)`: it lists 2.8 V, 1.4 Ω, inertia 68 g·cm² versus the VRN page's 3.2 V, 1.6 Ω, 85 g·cm². These source differences prevent declaring revision equivalence; they do not authorize electrical settings.

**LDO linear motor:** [exact product page](https://store.ldomotion.com/products/ldo-42sth40-1684cl350evrn-nema17-linear-stepper-motor-with-tr8x4-lead-screw-peek-nut-450mn-m-torque-for-voron-trident-z-axis-motion) still mixes the 40 mm Tr8x4/PEEK overview and a table for `LDO-36STH20-1004AH`. Its reference to Rev D does not supply a verified exact drawing. The LDO datasheet tree at `fdc453d06e59b02ca5293f260e1d2b7259868901` contains CL200E, CL275E and CL600E alternatives, but no path matching CL350E or the exact VRN identities. Those alternatives are not substitutes. Do not infer exposed length from `350` or adopt the unrelated electrical table.

## BTT: exact assets, no inferred hardware license

Rechecked complete GitHub trees (`truncated=false`), root READMEs and Octopus `Hardware/readme.txt`. Current heads still equal the catalog pins:

| Board | Repository pin / exact mechanical asset |
| --- | --- |
| SKR MINI E3 V3.0 | [`d7fd822…`](https://github.com/bigtreetech/BIGTREETECH-SKR-mini-E3/tree/d7fd822006628143222d1c3c8cdea85ffee29e66), `hardware/BTT SKR MINI E3 V3.0/3D/BTT E3 SKR MINI V3.0.step` |
| Octopus V1.0 | [`9526ff1…`](https://github.com/bigtreetech/BIGTREETECH-OCTOPUS-V1.0/tree/9526ff16f68839626cb8875a299e73f99f2e57e8), `3D/BIGTREETECH Octopus V1.0.stp` |

No non-firmware LICENSE/COPYING path or applicable hardware-model grant was established in this scope. Nearby firmware licenses and “open source materials” language are not an explicit grant for STEP, board layout or schematic files. The Octopus readme identifies power-IC package and silkscreen changes for V1.1; a schematic equivalence statement does not establish mechanical equivalence. No model bytes were accessed. This is a scoped negative result, not proof that no permission exists anywhere.

For **each board**, download, local AI processing, derivative interface use, public redistribution and commercial reuse all remain **unknown** in the catalog. Maintainer retrieval authorization also remains absent. Firmware rights and electrical-design rights must be evaluated independently from mechanical model rights; none selects Tesseract's license.

## HIWIN configuration evidence

The [official US linear-guideway catalog](https://www.hiwin.com/wp-content/uploads/HIWIN-Linear-Guideway-Catalog.pdf), revision **G99TE24-2410**, SHA-256 `b9445d5ada1b19ec0d3fd1e702a78f45a77b638024a7eed786a6e4b256ee50fc`, has 245 PDF pages. Printed pp.78–85 / PDF pp.81–88 explain MG ordering, accuracy, preload, seals and rail drilling. Order-code and rail-length pages were rendered and visually checked. A newer indexed German PDF link returned 404; do not claim this US catalog is the newest worldwide revision or silently apply it to the German HIRES listings.

A complete request must establish:

- Manufacturer and market/catalog revision; MGN size, C/H block length, special block/rail options, number of blocks and rails on the same plane, interchangeable versus matched/non-interchangeable supply.
- Full block and rail order strings (or full assembly string). Separate rail orders use the interchangeable-rail code, not only a carriage size. Preserve all suffixes; get the manufacturer/configurator to confirm a purchasable configuration instead of inventing one.
- Rail length L, material/coating, mounting direction, pitch P, hole count n, both end distances, hole/counterbore dimensions, cut/length/end-distance tolerances and any jointed-rail matching. The catalog's symmetric relation is `L=(n−1)P+2E`; asymmetric drilling requires both ends explicitly.
- Preload ZF/Z0/Z1 and accuracy C/H/P, with applicability confirmed for the chosen size/market. C as an accuracy code is distinct from dynamic load rating C. Do not treat all three preload options as interchangeable.
- End/bottom seals, auxiliary lubrication, reinforced caps/recirculation options, lubricant and service conditions. Options can change clearance and overall length; exact drawing and model must include them.

The cited catalog gives MGNR9 pitch 20 mm and standard end distance 7.5 mm; MGNR12 pitch 25 mm and end distance 10 mm. These are **catalog examples, not selected rail specifications**. Its printed p.83 uses E1/E2 for mounting shoulder heights, while p.85 uses E for rail end drilling: never confuse these labels. A 300 mm rail cannot be assigned the symmetric standard pattern from either size without checking the arithmetic and allowed custom cuts.

Existing HIWIN entries remain `portal-unconfigured`; no generic rail model, guessed order code or replacement manufacturer was added. The igus SWM-08 needs exact cut/end machining and shaft tolerance; WS-10-40-CAM-500 needs a specific compatible carriage and full assembly configuration. They remain distinct candidates, not ways around the HIWIN gate.

## Consolidated information requests — prepared, not sent

| Recipient / exact identity | Required answer and desired source | Geometry purpose / blocked work |
| --- | --- | --- |
| Adafruit #4884, original rev C v2 STEP and later PCB | Confirm shipped revision/lot mapping; finished diameters/tolerances and plating convention for both hole pairs; exact connector/button part revisions and mated/actuated envelopes. Request matching drawing and, only after separate approval, STEP | Mounts, enclosure, plug/finger access; source drill values alone do not clear fit |
| STEPPERONLINE 17HS08-1004S | Which lots use 20 ±1 versus 21.5 mm body? Provide dated current drawing/change notice and identify the offered STEP revision, shaft/pilot/mount pattern and cable-exit envelope; confirm black/silver geometry equivalence or differences | Motor mount and collision envelope; STEP desired but no retrieval authorized |
| LDO-42STH48-2004AC(VRN) | Supply suffix-specific drawing and explain Rev A versus live-table electrical/inertia changes; confirm mechanical envelope/connector and supplied revision. Request exact STEP if available and rights | VRN mount/shaft/cable clearance; generic Rev A not adopted |
| LDO-42STH40-1684CL350E(VRN) | Correct mismatched table; supply exact Rev D drawing, body length, exposed/overall screw length and datum, Tr8x4 lead/pitch/starts, nut geometry, end machining, tolerances, connector, revision/lot mapping and STEP availability/rights | Linear drive, nut mount, stroke and end clearance |
| BTT, each exact asset above | Identify rights holder and license/version applying separately to mechanical CAD, PCB/layout and schematics. Explicitly address download, local automated/Codex inspection, derived mounts, model-containing assembly distribution, standalone redistribution and commercial reuse; attribution/share-alike conditions and cloud restrictions | All dependent CAD processing and public reproducibility; firmware license insufficient |
| HIWIN MGN09C/H and MGN12C/H candidates | After application requirements are reviewed, provide complete purchasable rail/block codes and options above, revisioned assembly drawing/configurator output and model rights. STEP plus configuration report preferred | Rail/block mounting, travel and service clearances; neither configuration nor final rail is selected |

Send only after explicit authorization to contact manufacturers. Approval of a source or receipt of a reply is not permission for bulk downloads or physical testing.

## Free/open reproduction path

Stage B's `adsk` script is Fusion-specific. Its millimetre observations and source hash are portable, but the script is not a FreeCAD program. A read-only local inventory found no FreeCAD application in `/Applications` or `~/Applications`, no FreeCAD executable on PATH, and no FreeCAD/Part/OCP/OCC/cadquery/build123d modules in system Python. This is a bounded inventory, not proof no copy exists elsewhere. Installed Fusion 2705.1.30 was confirmed live. No CAD software was installed.

[FreeCAD documents STEP import](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_Import.md). Proposed independent procedure, **not executed**:

1. Obtain separate installation authorization if needed; record FreeCAD and OCCT versions, OS and STEP importer settings (assembly handling, compound merging, healing and unit handling).
2. Verify the existing approved STEP's catalog SHA-256; open it in a new temporary document with its native placement, without scaling, repair or export. Preserve every assembly placement exactly once; avoid counting parent compounds and child solids twice.
3. Record import diagnostics and solid count, inspect topology, identify the PCB by geometry rather than Fusion-specific names. Measure its local outline, thickness, center rectangle and cylinder diameters and the assembly envelope in millimetres. Preserve face/edge identifiers and placements in numerical evidence.
4. Compare with Stage B: 58 solids; PCB 50.8 × 22.86 × 1.57; mounting rectangle 45.72 × 17.78; paired diameters 2.50/2.54; assembly 51.946 × 22.86 × 6.37 mm. Different topology naming/grouping alone is not a dimensional failure. Investigate unexpected values rather than heal to match.
5. Close without saving, repeat an independent import, rehash source and compare the two imports and Fusion observations. Report numerical precision separately from manufacturing tolerances. No passing second-engine result is claimed until this happens.

The existing offline validator can already reproduce hashes and STEP structural checks using free Python, but is not a topology or solid-geometry parser. The source-extraction script independently explains the holes; it does not replace the future second-engine check or physical measurement.

## Verification and handoff

Actual verification:

- `python3 scripts/check_reference_parts.py --write-index` then `python3 scripts/check_reference_parts.py`: pass, 45 records / 13 categories / one local asset. Regenerated `INDEX.md` is unchanged because its displayed fields did not change.
- `python3 scripts/check_reference_parts.py --library '/Users/todd/Development Projects/tesseract-cad-library'`: pass, existing STEP size 2,443,088 bytes and SHA-256 unchanged; original MIT notice checks pass. Structural text checks only.
- `python3 -m unittest discover -s tests -v`: **76 tests passed**. These test repository software, not physical geometry.
- Source extractor run on both pinned remote texts: reviewed hashes accepted; USB board-pad centers agree. Unknown input rejected. JSON facts checked against reported mounting definitions; Python syntax parsed with `ast.parse`.
- Catalog before/after invariants checked: identity, physical revision, permission flags, authorization, local assets and model URLs unchanged for all 45 records.
- Changed Markdown relative file links and fenced-block balance pass; linked local anchors manually checked. Tables, classification, requirement coverage and new files reviewed. `git diff --check` and staged whitespace/public-asset review required before commit; final result is included in the PR.

Complete changed-file list:

| File | Reason |
| --- | --- |
| `cad/reference-parts/catalog.json` | Narrow source findings and links; retain uncertain rights/revisions |
| `cad/reference-parts/README.md` | Current Stage C navigation and finished-hole distinction |
| `cad/reference-parts/stage-b-verification.md` | Correct merged status while preserving historical observations |
| `docs/research-first-plan.md` | Remove stale Draft status; link Stage C without lifting CAD pause |
| `cad/reference-parts/stage-c-verification.md` | Discrepancy matrix, evidence, requests and reproduction plan |
| `cad/reference-parts/feather-pcb-source-observations.json` | Narrow pinned-source factual evidence |
| `scripts/inspect_feather_pcb_source.py` | Reproduce hash-gated source extraction without files/network |
| `cad/reference-parts/fusion-library-research.md` | Installed-command evidence, coverage, rights and future workflow |

 No physical validation, new solid import, full topology audit, current motor PDF dimensional verification or FreeCAD import was performed. Source access failures are retained above rather than guessed around.

Requirements, research-first pause, all four-bed modes, printable-first and distinct imperial/metric variants, later 2020 edition, removable enclosure and unproven four-head cooperation remain unchanged. No final toolchain, part, architecture or license is selected. No consequential safety/architecture change was proposed. Historical handoff: independent review and human merge approval were pending when written. Stage C subsequently merged in [PR #36](https://github.com/VoidPhoenixApps/project-tesseract/pull/36) on 2026-10-15; [Stage D](stage-d-qualification.md) continues qualification without lifting the remaining gates.

Home Infrastructure and project-knowledge were not edited. A separately authorized Home Infrastructure update could link the verified Fusion library-command inventory and reproduction limitation; persistent Codex source attachment remains unverified despite this session's explicit filesystem access. The existing [manual attachment procedure](README.md#manual-codex-source-configuration) remains applicable. No new cross-project decision or memory save is needed; Tesseract owns this evidence.
