# D5 — source/provenance and missing dependencies

**Accessed 2026-10-15.** Primary sources below support bounded research only. No vendor
CAD, figures or full documents are redistributed. Links/public facts do not establish
rights to ingest or redistribute models. Unspecified live-page revisions are recorded as
such rather than guessed from crawl dates. Typical data are not procurement guarantees.

## Materials

| ID | Primary source and revision/location | Evidence used / limit |
| --- | --- | --- |
| M1 | [Palram PALSUN Australian leaflet](https://www.palram.com/au/wp-content/uploads/sites/3/2019/07/PALSUN_Au_Leaflet.pdf), PDF p.2; footer contains 2.2016 and 11/2014 | Typical properties, formats, grade/thickness-dependent fire classifications. Old published reference; verify latest regional grade data before selection; marketing robustness is not unbreakability |
| M2 | [PERSPEXre product guide](https://www.perspex.co.uk/Perspex/media/General/technical-library/PDFs/EN_PERSPEXre_PDL-LR.pdf), EN 01/2022, PDF pp.3–4 | Cast acrylic sizes and typical mechanical/thermal data. Source notes production variation; not generic PMMA or printed-part data |
| M3 | [Röhm PLEXIGLAS temperature behavior](https://www.plexiglas.de/en/temperature-behavior), live, no revision shown | GS/XT use-temperature distinction and expansion considerations; not a loaded printer-panel rating. Customer-center technical PDFs not retrieved; no missing values invented |
| M4 | [Pilkington Glass and Mechanical Strength](https://www.pilkington.com/~/media/Pilkington/Site%20Content/UK/Reference/BRGlassMechanicalStrengthPDF.ashx), technical bulletin, revision not established | Glass selection, support/fixing and application dependence; historical building examples/standards not adopted as current printer compliance |
| M5 | [AGC Imagin & Oltreluce patterned-glass data](https://www.agc-yourglass.com/sites/default/files/brochures/original/Sandblasted_InfoSheet_EN_1019.PDF), UK 10/2019, PDF p.4 | Glass property proxy only: density/modulus/expansion/conductivity and distinction between reaction-to-fire and undeclared fire resistance. Not a selected transparent tempered panel; exact supplier evidence absent |
| M6 | [thyssenkrupp EN AW-5754 data sheet](https://ucpcdn.thyssenkrupp.com/_legacy/UCPthyssenkruppBAMXUK/assets.files/material-data-sheets/aluminium/5754.pdf), MX/TIS_06.2017, PDF pp.2–3 | Sheet/temper dependence and guidance physical properties; k150 W/m/K is midpoint of 140–160 range. No warm strength, formed-panel or fire rating inferred |
| M7 | [3A Composites DIBOND FR1077](https://www.display.3acomposites.com/en/products/details/dibond-registered-brand-fr-1077/), live, no revision shown | Mineral-core FR product and classification; regional/core differences require checking. No equivalence to generic aluminum composite board |
| M8 | [Palram polycarbonate chemical resistance](https://www.palram.com/us/wp-content/uploads/sites/2/2020/09/Chemical-Resistance-of-Palram-Polycarbonate-Products_en.pdf), room-temperature table, revision not established | Conditions matter for cleaner selection; not permission for arbitrary solvent on hot/prestressed sheet or coatings |

Unavailable/incomplete: Pilkington Global Glass Handbook EXP11 endpoint returned a browser
retrieval error; no calculation relies on its search snippet. M5 is explicitly a different
property proxy, not a recovered tempered-glass specification. No final glass thermal-shock,
PMMA fire, panel aging, gasket, adhesive, magnet-grade or printed-node creep data exists.
These gaps prevent material/safety approval, not this comparison.

## Retention mechanisms

| ID | Source / revision | Application boundary |
| --- | --- | --- |
| A1 | [K&J Magnetics magnet shear force with doors](https://www.kjmagnetics.com/blog/magnet-shear-force), updated 12/30/2024 | Measured and modeled magnet-to-magnet shear examples differ from axial attraction. Do not apply its rough fraction to arbitrary magnet/steel/painted friction joints |
| A2 | [K&J temperature and neodymium magnets](https://www.kjmagnetics.com/blog/temperature-and-neodymium-magnets), live | Temperature loss depends on grade and magnetic operating point; generic 80 °C shorthand is not a panel-system rating or Curie temperature |
| A3 | [Southco DZUS quarter-turn families](https://southco.com/en_gb_int/fasteners/emdzusemreg-quarter-turn-fasteners) and [actuation table](https://media.southco.com/media/static/documents/marketing/hb65/en/files/basic-html/page430.html), live/HB65 p.376 | Hand bail/wing/knob and tool types exist, with matched receptacles/captive arrangements. Family claims do not specify selected grip, force, temperature or vibration capacity |
| A4 | [Southco removable hinge brochure](https://media.southco.com/media/static/documents/brochures/202108-BR-Hinges-EN.pdf), filename202108; [96-series drawing](https://media.southco.com/media/static/Literature/96.en.pdf), revision not established | Retractable-pin/lift-off families provide candidate tool-free removal mechanisms. Exact part, pin trajectory, ratings and model rights remain open |

## Environmental and safeguarding references

| ID | Source / edition | Scope actually consulted |
| --- | --- | --- |
| E1 | [NIOSH Approaches to Safe 3D Printing](https://www.cdc.gov/niosh/docs/2024-103/pdfs/2024-103.pdf), DHHS 2024-103 | Emissions/exposure controls for makerspaces and similar settings; does not validate Tesseract enclosure capture, purge, filtration or room safety |
| S1 | [HSE introduction to machinery safety](https://www.hse.gov.uk/work-equipment-machinery/introduction.htm), live | Safeguarding, safe interventions and isolation principles; UK workplace context is not a jurisdiction/compliance determination for this project |
| S2 | [ISO14120:2015](https://www.iso.org/standard/59545.html), public abstract/catalog | Fixed/movable guard design scope; full normative text not acquired. Listing reports revision work; recheck applicable edition before adoption |
| S3 | [ISO14119:2024](https://www.iso.org/standard/75942.html), public abstract/catalog | Guard interlocking and defeat considerations; not protective circuit validation |
| S4 | [ISO13849-1:2023](https://www.iso.org/standard/73481.html), public catalog | Safety-related control-system scope; no required performance level or achieved reliability calculated |
| S5 | [ISO13850:2015](https://www.iso.org/standard/59970.html), public abstract/catalog | Emergency-stop design scope; not isolation or proof of a selected stop architecture |

Full standards, jurisdiction-specific electrical requirements, contact-temperature limits,
reach/access distances, stopping performance and professional interpretation remain future
review dependencies. No standards text was copied or compliance invented. Formulae in
[calculations](d5-calculations.md) are explicitly derived elementary models; unknown heat
transfer/retention inputs remain hypotheses rather than attributed manufacturer data.

## Inherited and authoritative sources

[D1–D4 exact heads](d5-engineering-study.md#dependency-and-authority) preserve prior
calculation, collision and load-path evidence. Read D4 enclosure, joints, frame report and
load paths; D2 geometry/modes; D3 support/selector constraints; Phase1B thermal findings.
All remain unmodified. Current fetched Tesseract main supplied authoritative instructions
and requirements; the complete requirements document is byte-unchanged by D5.

Shared workflow skill and System engineering/development/knowledge/secrets/model/review
standards read from project-knowledge `147de4d979bba17120a4cc425983d590f85b6000`, matching
live GitHub main. No Tesseract project CURRENT_STATE exists in that inspected checkout;
none created. Home Infrastructure instructions read via GitHub, main observed at
`963185a4d528884473a28a87ef81ffb0d1e59dd4`; current brief links Tesseract as authority.
The [original approved brief](https://github.com/VoidPhoenixApps/home-infrastructure/blob/75f40a677e00407e40b0995504476f473c4c23f7/3d-printing/reconfigurable-quad-bed-printer-concept.md)
remains the historical baseline retained by the requirements. AgentMemory queried once;
returned unrelated context, so none adopted. No cross-repository changes or sync performed.

## Consolidated future model/data dependencies

No approved populated reference-model folder/catalog is established by the repository;
the [library plan](../research-first-plan.md#future-codex-cad-reference-parts-library-planning-only)
remains planning-only. No exact enclosure hardware selected. This package needs no vendor
geometry, so no upload request, download, substitute component or fake model is warranted.
Before dependent detailed CAD, inspect the maintainer-approved folder/catalog and request
missing exact parts/revisions or acceptable sources in one consolidated list.

| Part identity / current status | Desired source/format | Geometry purpose and blocked work | Availability/rights uncertainty |
| --- | --- | --- | --- |
| Hand quarter-turn stud and matching receptacle; Southco families only | A3; exact-part STEP + grip/installation/load PDF | Mount spacing, back projection, finger access and engagement; blocks actual latch interface | Family availability established, part/revision and model terms not reviewed |
| Lift-off/retractable hinge and anti-lift latch; no selected SKU | A4; STEP + drawing, pin-removal and load data | Complete swing/pin/release path and panel load return; blocks hinge cassette geometry | Catalog drawings do not grant model redistribution or establish suitability |
| Magnet and mechanical capture; no grade/part selected | A1/A2 supplier entry; STEP/drawing plus force-gap-temperature data | Location, fastener pocket and adjacent sensor interference | Public data is not permission for model use; adhesive/corrosion limits missing |
| Sheet/window, edge gasket, grips and retainers | M1–M7 exact regional grade/thickness; dimensional/thermal/fire/chemical PDF, STEP only if needed | Cut pattern, edge capture, growth and seal stack; blocks fit and material approval | No purchased sheet or assembly geometry; certificates/rights/latest revisions unverified |
| Complete heads, gantries, parks, chains and filament feeds | [D2 dependency ledger](d2-references.md); exact manufacturer STEP/drawings | Real full motion, hand and roof extraction envelopes | Inherited missing models; no invented component dimensions |
| Bed transport, independent Z, secondary lift and restraints | [D3 ledger](d3-references.md); exact STEP + installation/load data | Underbody panels, cable clearance, load-transfer/service corridor | Architecture and parts unresolved |
| Imperial/metric frame interfaces and later 2020 slot hardware | [D4 ledger](d4-references.md); exact stock drawings/tolerances and joint source | Boss geometry, socket bulk, thermal datum and separate adapter variants | No nominal-to-rounded-metric substitution; public reproduction rights still required |
| Protective sensors/locking, electronics covers and wiring hardware | No selected part/source; qualified review first, then STEP + ratings/safety manuals | Guard access/actuation, electrical clearance and fault behavior | No sensor choice, safety rating or license adopted |

All diagrams and geometric boxes here are original abstract research constructs, not
approximations offered in place of selected purchased-part CAD. Keep third-party assets
separate; inspect permission for AI processing, local reference, derivatives and public
redistribution before use. Project licensing remains undecided.
