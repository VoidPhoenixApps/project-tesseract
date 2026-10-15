# D2 — references and missing geometry

Accessed **2026-10-14 America/Chicago**. These primary sources establish the statements
below, not Tesseract performance. No vendor CAD was downloaded, imported, substituted
or redistributed. Public access is not permission for AI processing, derivative use,
commercial use or redistribution. Document publication dates are distinct from access.

## Primary reference evidence

| ID | Source and revision | Evidence used | Applicability and confidence |
| --- | --- | --- | --- |
| R1 | [Aerotech dual-bridge multi-head gantry](https://www.aerotech.com/product/dual-bridge-multi-head-gantry-system/), undated live page; [gantry structure documentation](https://help.aerotech.com/automation1/Content/Gantry-Systems.htm), undated | Manufacturer describes independent bridges, eight independent vertical axes and cable management; control documentation describes mechanically coupled gantry spars | Strong topology precedent, no complete dimensions or unrestricted bridge passing. Not evidence of four arbitrary XY printing paths, printable frame suitability or affordability |
| R2 | [Bondtech LGX Lite V2 TDS, SKU EXT01LGX41003](https://www.bondtech.se/downloads/TDS/Bondtech_EXT01LGX41003.pdf), Rev.2024.01.23, p.1; [product page](https://www.bondtech.se/product/lgx-lite-v2-large-gears-extruder/) | Datasheet identifies Ø36 mm round motor, 20 mm motor length and asymmetric mounting locations; product page links STEP and warns against a plate between motor and extruder | High confidence for stated motor dimensions, not full head envelope. Original LGX Lite product data differs from V2 and must not be mixed. Product shipping dimensions are not component geometry |
| R3 | [HIWIN MGN/MGW dimensional table](https://www.hiwin.com/wp-content/uploads/Linear_Guideway-E-1.pdf), section2-4-19, publication revision unconfirmed | Indexed manufacturer table: MGN12H H13, W27, L45.4 mm; rail width12, height8, pitch25 mm | Medium: primary table was retrieved by search extraction; direct PDF open failed twice. Dimensions need drawing revision and visual confirmation before any CAD. No rail length/preload/accuracy grade/end machining selected |
| R4 | [E3D Motion System and Tool-Changer R&D](https://e3d-online.com/blogs/news/research-and-development-motion-system-and-tool-changer), 2018-03-21, V1 history with later discontinued notice | One carried printhead at a time and peripheral stored tools; real coupling development and failures | Conventional comparison for J and tool storage only. Does not establish multiple simultaneous jobs or current product availability; no E3D CAD imported |
| R5 | [BCN3D IDEX technology](https://bcn3d.com/technology/) and [manufacturer IDEX whitepaper](https://blog.bcn3d.com/hubfs/WebinarWhitepapper%20-%20New%20products%20content/BCN3D%20Whitepaper%20-%20IDEX%20technology-1-new.pdf?hsLang=en), revisions unconfirmed | IDEX X independence, duplication/mirror-mode context | Independent extrusion is not evidence of independent Y or unrelated-Z jobs. Kinematic rejection in this study is algebraic, not a claim that every commercial IDEX product has identical mechanics |
| R6 | [igus Series07 configured page](https://www.igus.com/product/series-07?c=US&l=en), undated, displayed part07.06.018.0 | Inner height10.3 mm, inner width6 mm, bend radius18 mm for displayed variant | High confidence in displayed data, not outer envelope or suitability for a complete head harness. Dynamic configurator can change variant; capture exact datasheet at selection |
| R7 | [igus carrier fill guidance](https://www.igus.com/cable-carriers/resources/energy-chains-designing-filing-com) and [bend selection](https://www.igus.com/company/energy-chains-select-bend-radius-cable-carrier-ca), undated | Cable separation/free movement and payload-dependent radius must be considered | Supports reserving complete swept cable space. Neither the 18 mm chain option nor D2's hypothetical30 mm radius proves a heater/filament bundle is suitable |

The Bondtech PDF was opened and its drawing screenshot requested; numeric facts used
above are the retrieved datasheet's explicit specifications, not inferred dimensions
from pixels. No entire purchased-head dimensions are claimed. HIWIN retrieval limitations
remain visible rather than promoting indexed data to fit-validated geometry.

D1 already catalogs thermal, belt, lift, coupling and controls references; see
[D1 verification](d1-verification.md) instead of duplicating them. Its Voron Phoenix
technical-evidence gap remains unresolved; no forum description is used as verified
Phoenix geometry in D2. No claim that research exhausted all possible architectures.

## Actionable reference-model dependencies before future CAD

None of these parts is selected or purchased. Candidate IDs below are reference leads,
not a BOM. Obtain exact identities/revisions and rights approval first; then request
legitimate STEP and native sources/drawings as available, verify units/origin, compare
critical dimensions and catalog file hashes. Keep restricted models out of public Git.

| Dependency / manufacturer | Exact candidate or unresolved choice | Needed format and dimensions | Source / confidence / rights and blocked work |
| --- | --- | --- | --- |
| Extruder/motor, Bondtech | LGX Lite V2 EXT01LGX41003, TDS Rev.2024.01.23; exact motor assembly revision still to confirm | STEP/native plus drawing: complete motor/lever/connector envelope, mounting datums, screw engagement, filament entry and opening/service envelope | R2 links STEP; not downloaded. Motor dimensions high, assembly placement unverified. Terms for local AI/reference/redistribution unchecked. Blocks real A/B packaging comparison |
| Rail/block, HIWIN | MGN12H family; rail length, accuracy/preload, suffix and end machining unresolved | STEP/native plus current revision drawing: complete block/seals/nipples, mounting, travel end restrictions, rail supports and fastener access | R3 indexed values medium, direct PDF failed. No exact configured model or rights established. Blocks true carriage travel, structural layout and mount design |
| Cable carrier, igus | 07.06.018.0 displayed example, brackets and actual harness unspecified | STEP plus datasheet for exact chain/brackets: outer width/height, pivot axes, swept bend, unsupported length, anchors and travel mounting | R6/R7; inner dims high, outer routing absent. Rights unreviewed. Blocks parking and frame/enclosure clearance; 6 mm inner width may be inadequate, not selected |
| Hotend/nozzle/heater, manufacturer TBD | No selected product or revision | STEP/native and thermal/service drawings: nozzle datum, heater/sensor leads, hot zone, fan inlet/outlet, nozzle wrench and heater extraction | Exact source not yet established; confidence unavailable; rights unknown. Blocks low-Z collision and service checks. Do not substitute an invented hotend |
| Probe/endstops/sensors, manufacturer TBD | No selected part/revision | STEP/drawings for deployed/retracted states, sensing datum/target distance, connector, mount and trigger repeatability | Source/rights unknown. Blocks probe reach, homing uncertainty and fault-response assessment |
| Belts/idlers/motors/beam guides, manufacturers TBD | No selected sizes, actuators or revision | STEP/native and drawings/ratings: belt line, pulley/idler OD/flanges, motors/connectors, tensioners, stroke ends and service adjustment | R1 is topology precedent, not a parts supplier selection. Blocks complete gantry and transmission envelopes and axis sizing |
| Filament tube, cable bundle, connectors, manufacturers TBD | Materials, diameters, temperature/flex ratings and bend limits unspecified | Manufacturer dimensional/rating documents, connector STEP where allowed; minimum dynamic radii, strain relief, slack and service loops | R7 guidance only; actual package unknown. Blocks trustworthy flexible swept reservation and lifespan claims |
| Original Tesseract structures and enclosure | Frame, beam joints, docking locks, mounts and tool-free panels unselected | Later original editable sources and measured constraints, both stock variants and 2020 edition | Not a missing vendor-model request. Blocks stiffness, support, panel/service clearance and real transition verification; new CAD still requires separate authorization |

There is no established selected-part reference library in this D2 work. We did not
create or assert one. These missing files block future dependent interface CAD, **not**
the authorized hypothetical analytical investigation. Reference dimensions in class B
are intentionally not scaled into fabricated purchased-part replacements.
