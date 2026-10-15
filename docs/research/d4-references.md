# D4 — primary references and future model dependencies

Accessed **2026-10-14 (America/Chicago)**. Sources support catalog facts or methods,
not Tesseract validation. Undated live pages have no inferred revision. Original
analysis/diagrams/code only; no third-party CAD, images or source code copied. No license
selected, files downloaded from CAD portals, or rights assumed.

## Structural methods and properties

| ID | Source identity / revision | Application and limits |
| --- | --- | --- |
| A1 | [MIT 2.002 Mechanics and Materials II, Lab 1, Spring 2004](https://ocw.mit.edu/courses/2-002-mechanics-and-materials-ii-spring-2004/9aebe9fc6669d928aa716a5033cc9c9f_lab_1_s04.pdf); [MIT 1.050 readings, Bucciarelli text, 2002 / Fall 2004 course](https://www.ocw.mit.edu/courses/1-050-solid-mechanics-fall-2004/pages/readings/) | Elastic bending, axial behavior, vibration and buckling framework. D4 derivations are idealized; no joint/material certification |
| A2 | [MIT 16.888/ESD.77 assignment 4, Spring 2010](https://www.ocw.mit.edu/courses/ids-338j-multidisciplinary-system-design-optimization-spring-2010/418d122938db3b1d7085b2312b6aa3c3_MITESD_77S10_assn04.pdf) | Teaching steel E=210 GPa, density=7850 kg/m³; Al example 70 GPa. D4 rounds Al to 69 GPa as proxy, not exact 6063 data; no strength or historical price adopted |
| A3 | [Kaiser 6061 sheet/plate, Rev. 05/06](https://online.kaiseraluminum.com/depot/PublicProductInformation/Document/1015/Kaiser_Aluminum_6061_Sheet_Coil_and_Plate.pdf), rechecked inherited source in [Phase 1 ledger](../phase1/references.md) | Typical alpha 23.6e-6/K over 20–100 °C; D4 uses this explicitly as Al example, not a specification for 2020 or selected plate. Steel alpha remains an assumed D3 value |
| A4 | [Snappy RepRap author repository, README v3.0.3](https://github.com/revarbat/snappy-reprap) | Existing printable modular printer precedent, editable OpenSCAD sources. Inspires segmentation question only; its performance/license does not transfer to this larger, enclosed, multi-bed concept. No files adopted |

## Catalog stock and tolerance sources

| ID | Source / revision | Retrieved evidence and limits |
| --- | --- | --- |
| S1 | [Thomson 1/2 L RL](https://www.thomsonlinear.com/en/product/1/2%20L%20RL), live product table | Actual Class L diameter, material and cut length. Rounded 13 mm field must not override inch tolerance table. No structural clamp/load data |
| S2 | [Thomson T-Case brochure BRUK-0026-04, 20191113SK, pp.4–5](https://www.thomsonlinear.com/downloads/bearings_guides/T-Case_Shafting_bruk.pdf) | 12 TCM h6, straightness and finish options. Distinct family from [12 MM RL](https://www.thomsonlinear.com/en/product/12%20MM%20RL), which also has current ordering evidence; do not combine their tolerances/grades silently |
| S3 | [Speedy Metals product 3494, dom1x.065](https://www.speedymetals.com/showproduct.aspx?productid=3494); [DOM material page](https://www.speedymetals.com/information/material17.html), undated | US exact tube offering and custom cut tolerance. Supplier's general A513 Type 5 description is not a lot certificate; grade ambiguity and missing dimensional tolerance retained |
| S4 | [Fluidics HR 25X1,5 / FL-312264](https://fluidics-equipment.com/e/praezisions-hydraulikrohr-nahtlos-25x1-5mm-schwarz-phosphatiert-312264.html), live supplier's own listing | EU purchasable form, E235+N, 25×1.5, standard/finish. Numeric tolerance absent from inspected technical table; pressure/temperature claims not adopted as structural or joint ratings |
| S5 | [Parker EO tubes catalog CAT-4041-2/UK, pp.17–19](https://www.parker.com/content/dam/Parker-com/Literature/HPCE/New/CAT-4041-2-UK.pdf), catalog ID; date not established | R25X2/R25X2CF and OD tolerance; final delivery standard, wall and cut tolerances need confirmation. No pressure rating used for frame capacity |
| S6 | [Bolt Depot product 23747](https://boltdepot.com/Product-Details?product=23747), live | US threaded-rod dimensions, ASTM A193 B7 and ASME B18.31.3. Thread limits and structural connection design not provided |
| S7 | [norelem threaded rods DIN 976-1, family 07640](https://www.norelem.it/en/Product-overview/Flexible-standard-component-system/07000/Nuts-screws-washers-securing-elements/Threaded-rods-steel-and-stainless-steel-DIN-976-1/p/agid.4193) | Search-indexed manufacturer's datasheet identifies 07640-08, M8 RH, 8.8 bright, 1000 mm; direct indexed PDF returned 404. Live family page and [manufacturer catalog entry](https://norelem.partcommunity.com/?info=norelem%2Fflexibles_normteilesystem%2Fgruppe_07000%2Fmuttern_schrauben_u-scheibe_sicherungselemente%2F07640.prj&varset=%7BBEST%3D07640-08%7D) retrieved, confirming M8/RH/1000; exact drawing/fit still needed |
| S8 | [80/20 20-2020](https://8020.net/20-2020.html), live | I=.6826 cm⁴ both axes and 6063-T6. Older catalog/model listings differ; live modulus punctuation malformed. No assumption that all 2020 sections share properties; CAD account/rights unreviewed |
| S9 | [SSAB Precision Steel Tube Handbook](https://www.ssab.com/-/media/C7B2AA431A3545C38796EA08EC59B148.ashx), author Juha Tulonen, date not established, p.105 example; [Form Tube 420](https://www.ssab.com/en-gb/brands-and-products/ssab-form-deep-drawing-steel/product-offer/tube-420), live tolerance table | E=210 GPa example and actual tube-tolerance/cut-end caveats. Different tube product family; its tolerances are not transplanted onto other candidates |

Supplier listings are primary evidence of what each seller offers, not independent
verification of manufacturing quality or stock on hand. US/European routes do not prove
worldwide low-cost supply. Prices/lead times change and are intentionally not a cost model.
Failed direct RoundRail PDF and guessed OnlineMetals product retrieval were not used as
verified evidence. No approximation of a purchased component was created.

## Print material and process sources

| ID | Source / revision | Use and limitation |
| --- | --- | --- |
| P1 | [Prusament ASA TDS v1.1, 16-02-2022](https://prusament.com/wp-content/uploads/2022/10/ASA_Prusament_TDS_2022_16_EN.pdf), pp.2–3 | Flexural modulus and stress-dependent HDT; specimen preparation on MK3S, 100% infill. Not an Ender joint, long-term creep curve or generic ASA/ABS guarantee |
| P2 | [Prusament PC Blend TDS v1.1, 16-02-2022](https://prusament.com/wp-content/uploads/2022/10/PCBlend_Prusament_TDS_2022_16_EN.pdf), pp.1–3 | HDT and demanding process conditions. No chamber service rating inferred |
| P3 | [Prusa material guide](https://help.prusa3d.com/filament-material-guide); [Prusament PETG](https://prusament.com/materials/prusament-petg/), live | Qualitative material/process comparison. PETG guessed TDS URL failed; no numerical PETG properties adopted. Filled materials need formulation-specific data |
| P4 | [Creality Ender-3 Pro specification](https://www.creality.com/ae/products/ender-3-pro-3d-printer), live/indexed | Nominal 220×220×250 mm reference; actual ordinary-Ender envelope and process capability remain unverified |

## Consolidated missing-model and data dependency list

The approved reference-library workflow is still [planning only](../research-first-plan.md#future-codex-cad-reference-parts-library-planning-only).
No approved populated reference folder/provenance catalog or selected final part is
established by the current record. This research requires no purchased-part geometry,
so it does not request model uploads or block independent analytical work. **Before
future dependent detailed CAD**, check the maintainer-approved folder/catalog for the
exact selected manufacturer/part/revision; if absent, ask for the correct file or an
approved source in one consolidated request. Do not substitute or fabricate geometry.

| Identity / current status | Desired format and source | Geometry/data purpose and blocked future work |
| --- | --- | --- |
| Thomson US-S and M-S candidates above; none selected | STEP plus certified dimension/tolerance PDF via S1/S2 or maintainer | Shaft ends, finish and permitted retention machining; blocks exact sockets/retainers. No model obtained; local AI-use/redistribution rights unreviewed |
| Speedy dom1x.065, Fluidics HR 25X1,5, Parker R25X2 candidates | Dimension/inspection PDF preferred; STEP only if end treatments require it; S3–S5 | Exact grade, coating, OD/wall/straightness/cut limits; blocks final clamp and crush calculations. Public listing not rights clearance |
| Threaded rod and matching nuts/washers, S6/S7; drawing not selected | Dimension PDF and STEP as needed | Thread class/root area, nut envelope/engagement and plate bearing; blocks fastener pockets and strength analysis. Norelem retrieval incomplete |
| 80/20 20-2020 and exact joining hardware | Manufacturer drawing/STEP, S8 | Slot, corner-joint compliance and clearances; blocks later edition interfaces. Account and CAD terms need review |
| Bed guides, lift/restraints, docking locks, selectors | Exact part remains unresolved; retain [D3 ledger](d3-references.md) | STEP + installation/load PDF for complete stroke, hold-down and load handoff. Do not silently select a part to fill this row |
| Complete head/gantry, rails, motors, parks, cable/filament hardware | Exact identities remain unresolved; [D2 ledger](d2-references.md) | STEP and rated routing data for whole swept assemblies; blocks integrated brace/park/service clearance |
| Panel retainers and electrical protection | No implementation/material selected | Later manufacturer drawing/ratings, STEP where relevant; blocks exact hand-access, retention and electrical-cover interfaces |
| Polymer/node coupons and joints | No vendor CAD can replace this evidence | Directional stiffness, creep, preload, fatigue and temperature/time data for the actual process; blocks structural rating |

Panel-retainer data must establish hand access, engagement, removal sweep and temperature
behavior before interfaces can be designed. No source link is invented for an unselected
part. Publicly reproducible drawings/design sources and an acceptable rights basis are
needed before using third-party geometry; public access alone grants neither
redistribution nor AI-processing permission.

## Authoritative source audit

Shared workflow/engineering/knowledge/secrets/review/model policies read from
project-knowledge `147de4d979bba17120a4cc425983d590f85b6000`, matching live main.
No Tesseract `CURRENT_STATE.md` exists in the inspected tree; none invented.
Current Home Infrastructure instructions read via GitHub, without repository changes.
AgentMemory queried once; returned unrelated entries, so no continuity claim adopted.
Tesseract source stack is pinned in the [study](d4-engineering-study.md).
