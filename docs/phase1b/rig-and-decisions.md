# Two-bed fixture implications and review decisions

**Recommendations for subsequent design review. No physical operation, fabrication or purchasing is authorized.** Preserve the [Phase 1 staged plan](../phase1/two-bed-proof-plan.md): cold characterization → reviewed supervised heating → hot cycling → supervised cross-seam printing → endurance/transfer. Its sample counts and numerical acceptance values remain proposals, not validated limits.

## Ranked shortlist

| Rank | Candidate for further engineering | Why advance / disqualifying evidence |
| --- | --- | --- |
| 1 | Hybrid cold carrier + relieved hot plate; compare guide-retained and floating 2+1 cartridges | Separates measurable error sources and avoids inter-bed force loops. Reject a cartridge if it needs vertical reseating, insufficient contact preload, or unacceptable added Z/tilt compliance |
| 2 | Inset inward-corner plate reference with radial secondary and free third support, versus center reference | Uniform model improves both joining directions; reject if real sheet slip/bow, anchor heating, corner bridge compliance or support friction defeats gap/height budget |
| 3 | Independent supported XY transport as fixture packaging baseline | Strongest coordinate-path evidence; full guide/stop/cable fit and stiffness still open. A linear rig slide is sufficient initially and does not select machine transport |
| 4 | Shared tug using the same carriers and precision cartridges | Retains serial independent movement; advance only after a drawn continuous dog-access path and retained-restraint fault sequence exist |
| 5 | Side-open planar V or master/slave locating tree | Useful contingency if pads cannot capture reliably. V has friction/inspection burden; tree propagates loads/errors and complicates occupied-region isolation |

Confidence: high in elementary algebra under stated assumptions; medium in the comparative experimental value; low in achieved precision, lifetime, real thermal flatness, packaging completeness and cost. No weighted total score converts an unmet mandatory constraint into an acceptable tradeoff.

## Replaceable fixture modules

Use one fixed reference bed and one horizontal moving bed initially, with two retained sheets and independently controlled heaters only in later authorized tests. Both remain continuously supported. Common cartridge interfaces expose datum targets, latch-force measurement, adjustment references and sensor targets. Match support geometry and latch reaction plane when comparing cartridges so fixture changes do not masquerade as docking improvement.

1. **A cartridge:** single X/Y stops with guide-retained yaw, compliant lateral preload, accessible wear pads.
2. **B cartridge:** two X pads at a measured baseline plus one Y pad, planar float and travel-limit observation; preserve continuous out-of-plane support. A nominal ±0.5 mm/±0.2° float range may be an initial drawing variable only; calculate required capture travel from measured errors before adopting it.
3. **Thermal mount cartridges:** center reference and inward-corner/inset reference with radial secondary and third free support. These swap independently of A/B docking; do not confuse plate anchoring with carrier location. Evaluate both joining directions by changing the isolated cold fixture orientation between reviewed experiments, not by lifting during operational conversion.
4. **Optional V cartridge:** only after its contact normals, force closure and horizontal release have passed geometry review. Defer relative bed-to-bed reference until independent frame registration has a measured baseline.

Calibrate cold stop position, station pitch, X-pad differential/yaw, plate support heights, float neutral position/travel, preload magnitude and line of action, anchor inset and radial-slot direction, sensor trip points and cable strain-relief neutral position. Calibration adjustments must lock reproducibly and be recorded; they are not builder shims or mesh scaling. Never add a fourth hard Z screw to flatten an unexplained thermal bow.

## Separate the experiments

| Question | Isolation method | Measurement and limit of inference |
| --- | --- | --- |
| Does the dock repeat? | Rigid laboratory reference, unheated representative mass, fixed cable condition; A/B comparison | Carrier six-DOF pose, actual contact states and preload across both approach histories. Does not establish printable-frame behavior |
| Does preload distort the carrier? | Hold thermal condition; sweep reviewed force range, measure hysteresis | Simultaneous force, carrier plane and sheet plane; no numerical force range authorized yet |
| Does the thermal anchor work? | Dock held; compare anchor positions at equal and differential temperatures | Sheet/plate/carrier fiducials separately, gap profiles, top/bottom temperature and height maps; separate rigid tilt from residual bow |
| Does wiring disturb the seam? | Repeat with representative loops in extremes of stroke, connector and strain-relief states | Cable drag and induced carrier/sheet displacement; not just continuity |
| Can a printable frame reproduce it? | Replace laboratory supports with reinforced printed nodes at realistic spacing and temperature | Repeat measurements for separately labeled imperial/metric coupons, actual sourced stock and verified Ender 3 part envelope |
| Can printing cross it? | Only after approved thermal/mechanical/safety gates; matched same-sheet controls | Seam step/gap, safe nozzle crossings, adhesion/coupon behavior and uncertainty; no four-bed central-junction claim |

The laboratory base may isolate docking and plate effects. It cannot substitute for representative guide foundations, latch-reaction nodes, standoffs and reinforced printed joints. Repeat those load paths on the printable frame variants; later 2020 adaptation has its own qualification. Actual reinforcement profiles, grades, tolerances and regional availability require supplier drawings and measurement before CAD sockets are defined. This study specifies no new stock and cannot claim either variant fits.

## Measurements required before detailed CAD

- Plate/sheet/stack outlines and thickness, heater footprint and prohibited fastener zones, sheet tab/edge radii and chamfers; inner-corner anchor space and allowable temperature at its support.
- Mass, center of gravity and credible print/nozzle/cable/acceleration loads; guide moment and deflection requirements; latch preload window, pad radii/contact stress and release force.
- Guide/block/rail and fastener envelopes, actual available rail lengths, rail mounting datum tolerances and float capture mismatch; station-stop retraction sweep at all four endpoint combinations.
- Sheet retention/slip behavior, plate/sheet coefficients over proposed temperature range, support stiffness/friction, thermal maps and frame drift. Obtain available manufacturer data first; physical characterization awaits separate authorization.
- Instrument uncertainty, datum stability, probe-force effect and thermal measurement lag; geometric collision allowance and required stopping distance.
- Tug stem or offset bracket route, guide apertures and lower-frame load path; cable dynamic radius, loop sweep, strain relief and service extraction.

These unknowns can invalidate the fixture: a rigid base hiding frame drift; instrument targets on the wrong thermal body; magnetic sheet movement mistaken for carrier error; tangential contact friction preventing seating; a hot plate modeled as uniform; unsupported support-triangle corners; a latch unloading a height support; overlapping four-station stops; a tug requiring vertical capture; an object coupling both plates during differential heating; correlation or drift hidden by averaged cycles.

## Human decisions and release-blocking risks

| Decision / risk | Required evidence and approval |
| --- | --- |
| Comparison fixture scope and cartridge order | Approve bounded A/B hybrid comparison and whether corner anchor merits the first thermal cartridge; no final architecture selection |
| Temperature/material/process envelope | Define intended operating recipes and independently heated combinations; establish defensible gap/step/adhesion criteria rather than adopting 0.20 mm cold gap or Phase 1 limits |
| Float and support stiffness | Review constraint allocation, preload force closure, out-of-plane deflection/fatigue, support retention and stop travel |
| Frame/stock and component choices | Reviewed drawing, actual purchasable stock dimensions, separate imperial/metric interfaces, printable part envelopes and reproducible source plan |
| All-mode station hardware / tug feasibility | Draw retractable nests and uninterrupted horizontal access; reject overlap or lost-support paths before fabrication |
| Safety and metrology procedure | Named competent mechanical, electrical and safety reviewers; hazard assessment, uncertainty, supervision, numerical acceptance and abort values before any test |
| Future requirement conflict | If real thermal seams cannot meet print criteria, explicitly review requirements or redesign; no automatic removal of independent heaters, layouts or retained sheets |

The previously proposed 0.05 mm registration/total local Z budgets, 0.10–0.30 mm hot gap, 0.02 mm drift, stabilization thresholds, coupon-strength ratio and cycle counts are all unsupported as acceptance requirements until process evidence and uncertainty justify them. The new e=0.03 mm gap allowance, 10 mm carrier clearance and envelope dimensions are analytical examples, not accepted manufacturing tolerances or safety margins.

Before physical work, retain all Phase 1 release-blocking blanks: electrical ratings/fusing/grounding, cable thermal/flex limits, independent heater fault protection, safe speed/force and stop distance, support/temperature limits, fault response times and emergency-stop/restart states. Verify locks/seats independently, preserve gravity support, isolate service energy, prevent reconfiguration with objects, and prohibit automatic restart. Desk review does not sign off these controls.

## Next recommended experiment and durable follow-up

The next *design package* should be a dimensioned cold, two-bed fixture comparing A and B at equal measured preload on a rigid reference, with targets on carrier and sheet and continuous Z support. A reviewed cold repeatability/preload experiment should precede heating. Its second step compares center and inset-corner thermal mounts under equal/differential temperatures, followed only then by cross-seam coupons. Keep the later four-bed central-cross test separate.

After human review/merge, separately authorized project-knowledge work should record the study link, narrowed hypotheses, fixed-gap incompatibility under the stated center-anchor assumptions and outstanding station/tug/thermal evidence. There is no existing Tesseract CURRENT_STATE file to update in the inspected knowledge checkout; do not invent one as part of this task. Home Infrastructure and project-knowledge remain unchanged.
