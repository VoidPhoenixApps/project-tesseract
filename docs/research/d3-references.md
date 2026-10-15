# D3 — primary evidence and missing-model ledger

Accessed **2026-10-14 America/Chicago**. External publications were read as references;
no third-party CAD, code, illustrations or manufacturer models were imported into this
repository. Public access is not a license for AI ingestion of CAD, derivatives or
redistribution. Project licensing remains undecided.

## Evidence inspected

| ID | Primary source / revision and locator | Claim supported and limits |
| --- | --- | --- |
| E1 | [Gates PowerGrip GT3 design manual](https://www.gates.com/content/dam/documents-library/catalogs/powergrip-gt3-drive-design-manual-en.pdf), copyright 2014; printed p.2, p.171, pp.174–175 | Safety policy excludes reliance solely on belt for lifting/braking without independent backup; linear drives require working-tension consideration; idlers/wrap require geometry. No Tesseract selector approval, belt selection or safety rating. D1 previously left revision unestablished; copyright now inspected, not proof of newest edition |
| E2 | [Miki Pulley 546 catalog excerpt](https://www.mikipulley.de/wp-content/uploads/2025/08/546_Catalog_2021.pdf), filename 2021, printed pp.118–120, publication revision unconfirmed | Tooth clutches transmit through engagement; full/single-position and symmetric/directional forms differ. Does not prove arbitrary phase engagement, gravity holding, retained engagement on power loss or suitable scale |
| E3 | [Slocum kinematic coupling review](https://web.mit.edu/2.70/Reading%20Materials/Kinematic%20coupling%20review%20article.pdf), manuscript 2009, journal DOI 10.1016/j.ijmachtools.2009.10.006 (2010) | Exact-constraint/preload/contact-stiffness principles; not a horizontal hot-bed implementation or transferrable repeatability claim |
| E4 | [THK master guide and combined use](https://www.thk.com/us/en/products/lm_guide/maintenance/0001/), undated live page | Reference-surface discipline, matched rail/block identity and joint deflection/misalignment concerns. No selected rail, allowable printed-frame mismatch or proof of compatible linked guides |
| E5 | [mayr vertical-axis braking overview](https://www.mayr.com/en/industries/vertical-axes~517), undated live page | Gravity-loaded axes require purpose-designed restraint; rotary/linear options exist. No selected brake, response time, capacity or claimed safety integrity for Tesseract |
| E6 | [Kaiser 6061 sheet/coil/plate data](https://online.kaiseraluminum.com/depot/PublicProductInformation/Document/1015/Kaiser_Aluminum_6061_Sheet_Coil_and_Plate.pdf), Rev.05/06 pp.1–2 | Typical E=68.3 GPa, density 2700 kg/m³ and alpha=23.6e-6/K over 20–100 °C support inherited sensitivities only; actual material and laminate behavior unknown |
| E7 | [NIST TN1297 §5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty), 1994 technical note, live section | Combined uncertainty accounts for sensitivity coefficients and covariance; arbitrary independent RSS is not justified. Does not supply this study's missing measurement uncertainties |

Gates safety-policy page and Miki tooth-form page were also requested as PDF screenshots;
numeric analysis relies on extracted source text and original mechanics, not pixel-derived
geometry. These are precedents and constraints, not endorsements or exhaustive literature
coverage. No primary evidence retrieved demonstrates the proposed literal automatic
belt rerouting lift; retain that as an evidence gap rather than a universal impossibility.

Repository sources: [Phase 1B thermal](../phase1b/thermal.md) and
[docking](../phase1b/docking.md); [Phase 1C scope/evidence](../phase1c/README.md);
[D1 references](d1-verification.md) and [D2 dependencies](d2-references.md).
Exact source branch revisions are in [verification](d3-verification.md). Earlier failed
experiments are preserved; no new physical data exists.

## Consolidated future reference-model dependencies

The repository inventory contains conceptual envelopes and reference links, not an
approved purchased-part model folder/catalog with selected D3 parts. No exact lift,
clutch, belt, motor, brake, rail or lock has been chosen. Thus there is **no current
part-specific CAD request to fabricate or substitute**. When those choices and bounded
CAD work are authorized, ask the maintainer once for the exact files or approved sources
below; do not begin dependent interfaces first. STEP plus authoritative tolerance drawings
is preferred; native vendor models may supplement it with reviewed rights.

| Dependency / identity status | Established source lead | Required file/data and purpose | Rights/availability uncertainty and blocked work |
| --- | --- | --- | --- |
| Belt, sprockets, idlers, tensioner; manufacturer/part/revision unselected | E1 Gates is guidance, not selection | STEP + pitch-line/radius, flange, bend/wrap/tension and fatigue data; continuous selector path | Exact stock/ratings and model permission unchecked; blocks finite-radius switching, packaging and tensioner sizing |
| Positive selector/clutch; no size/variant selected | E2 Miki 546 family is precedent only | Exact part/revision STEP, tooth phase/depth, axial force, backlash and power-loss behavior; shaft interfaces | Catalog is not model-use permission; blocks engagement and torque/retention sizing |
| Z guide and screw/belt actuator; unselected | E4 THK is guide discipline only | Matched exact rail/block and actuator drawings/STEP, permissible moments/preload/error, travel limits | No geometry or rights approved; blocks guide-loop/interface design and capacity checks |
| Independent restraint and load locks; unselected | E5 mayr is restraint precedent only | Exact model/revision, holding/dynamic ratings, release behavior, diagnostic coverage and STEP | No certified assembly or suitability inferred; blocks fault support/arrest design |
| Motor, servo, bearings and couplings; unselected | No approved exact source | STEP and torque-speed/thermal/axial load data, inertia and supply-loss state | Blocks actuator/selector-force/shaft-support implementation; no generic motor substituted |
| Heated plate, retained sheet and cold support stack; unselected | Phase 1B; E6 only material sensitivity | Actual outlines, heater exclusions, layer properties, thermal maps and approved models/drawings | Blocks real seam/error budget and hot/cold mounting interfaces |
| Toolhead/gantry/harness interfaces | D2 ledger retains candidate leads, none a complete approved assembly | Exact nozzle-relative assemblies, full stroke/sweeps, cable and service data | Blocks coupled XY/Z clearance; no reuse of hypothetical D2 boxes as vendor geometry |
| Reinforcement and enclosure hardware; unselected | Requirements and research-first plan | Actual purchasable imperial and metric profiles, tolerances/grades, panel retention/interface data | Blocks fit, stiffness, Ender 3 segmentation and both-variant outputs; no nominal size equivalence assumed |

Before obtaining/using any model: exact identity/revision, units/axes, source, access date,
rights for local AI processing/derivatives/public sharing, hash after legitimate receipt,
dimensional validation and portable reproduction instructions. Unclear rights require
maintainer-approved alternatives, not silent download or redrawing. No model acquisition,
source subscription, purchase or detailed CAD was needed for this research.
