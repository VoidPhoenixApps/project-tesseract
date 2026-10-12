# Proposed two-bed docking and cross-seam proof

**For engineering and safety review; not an executable authorization.** No hardware has been built, purchased, energized or tested for this study. Before each physical stage, reviewers must approve the fixture drawing, operating envelope, risk controls, calibrated measurement plan and numerical abort limits. A desk review cannot certify machine safety.

## Questions and minimum fixture

Determine whether repeatable carrier docking can produce stable, printable seams between two independently heated nominal 180 × 180 mm beds with their separate sheets retained. Compare frame-referenced planar registration against a partial bed-to-bed reference without buying an entire four-bed mechanism.

The fixture must reproduce: actual plate/sheet/magnet/heater stack; horizontal docking stroke and bidirectional approach; continuous fixed-height support; representative support spacing and seam overhang; cold carrier and hot plate datums; controllable latch preload/load path; representative reinforced printed joints at realistic temperatures; independent heater channels; full cable loops/strain relief; and intended sheet edges/retention. Include replaceable datum cartridges and accessible indicator/temperature targets. A rigid laboratory base may first isolate interface behavior, but cannot establish printable-frame performance; repeat on representative imperial and metric frame coupons before transfer of conclusions.

Use one fixed reference module and one horizontally moving module initially. Later make both mobile to reveal station-to-station errors. A bounded linear test slide is acceptable for the seam experiment and does not select final XY transport. Reorient the *cold, de-energized fixture between separately reviewed experiments* to examine both seam directions; do not introduce bed lifting into the operational conversion cycle. No test object may remain on a module being reconfigured. A seam-spanning object must be removed before undocking.

Compare cartridges:

1. Guide-retained Tx/Ty stops with compliant horizontal latch; guide owns yaw/Z/tilt.
2. Planar 2+1 locator with explicit yaw compliance between drive and carrier; same continuous vertical support.
3. Partial bed-to-bed planar reference with released matching frame freedoms, measured thermal slip and bounded preload. Do not hard-fix both systems simultaneously.

Only add a side-entry six-DOF coupling if a cold geometry review demonstrates full-rank constraint and engagement/release with no commanded vertical reseating. Reject it before heating if the lead-ins force a lift. Record why rejected; do not quietly omit it from results.

## Variables, metrology and records

Control or log plate/sheet IDs, alloy/temper/thickness, source revision, stock variant and actual dimensions, print material/orientation, fastener torque procedure, support spacing, preload, approach speed/direction, home procedure, cable position, cleaning condition, room/draft conditions, each heater setpoint and independent surface temperatures, stabilization time, instrument calibration and operator. Change one interface factor at a time initially; randomize cartridge test order where practical to expose drift. Preserve unsuccessful cycles and cleaning interventions.

Frame-mounted reference targets establish F. Two lateral indicators or equivalent calibrated probes separated by a known baseline estimate translation and yaw; probe at least three noncollinear carrier targets for plane pose. Measure the **sheet separately**: height at both sides of the seam at the two ends, center and quarter positions; map each sheet on a repeatable grid (proposed 5 × 5) plus inner corners. A fitted plane captures rigid tilt, while residuals reveal bow. Report seam step versus seam position, not only one average. Measure cold/hot gap optically with calibrated scale or suitable metrology; a feeler gauge may disturb hot edges and is not automatically appropriate. Quantify probe force effects on thin sheets.

Measure X/Y registration against carrier and sheet fiducials; avoid treating thermally moving sheet edges as invariant carrier datums. Record separation of measurement axis from the seam (Abbe offset) and yaw contribution. Use independent temperature probes at centers/edges and near printed supports; the control thermistor alone is inadequate. Instrument choice remains open. Resolution is not uncertainty.

Develop a NIST-style uncertainty budget for each measurand: calibration, resolution, repeatability, cosine/Abbe error, fixture deflection, thermal drift, optical edge detection and correlations. Report expanded uncertainty U with coverage factor and assumptions. For an upper limit L, a proposed conservative rule is `observed worst absolute error + U <= L`; intervals straddling a limit are inconclusive. Do not divide single-cycle uncertainty by sqrt(n) to certify every cycle. Thermal stability is established by surface drift as well as temperature.

Suggested raw table columns: run ID, timestamp, revision, variant, cartridge, cycle, approach, commanded pose, measured carrier XYZ/angles, sheet-grid readings, gap profile, seam-step profile, preload, temperatures, elapsed dwell, lock/seated sensor states, fault/intervention and photo/log reference. Store all readings, including outliers, with calibration records and failed tests. Record only actual observations; empty templates are not results.

## Sequential experiment gates

| Stage | Proposed sample / conditions | Eliminate or learn | Advancement evidence |
| --- | --- | --- | --- |
| 0 — paper and unpowered geometry | Constraint audit, horizontal approach/release, cable mockup, fixture and hazard review | Overconstraint, trapped latches, unsupported transfer, prohibited lifting | Reviewed drawings and measurable limits; no energizing |
| 1 — cold manual seating | 10 approach/release cycles per cartridge at ambient, guarded and isolated from drive energy | Obvious binding, seating sensitivity, indicator force and cleaning effects | No forced Z reseating; raw pose/gap/step and instrument budget |
| 2 — reviewed low-energy automation | 30 dock/undock cycles per surviving cartridge, both approach histories, at ambient | Lost steps, latch variability, hysteresis, cable pull | Each cycle held and verified; meet reviewed cold limits without outlier deletion |
| 3 — thermal characterization while locked | Ambient/ambient, 60/60, 80/80, 80/40 and reversed 40/80 °C as **candidate** setpoints if all ratings permit | Bow, unequal heating, thermal restraint, support creep | Full temperature and height maps; safe stabilization; no edge interference |
| 4 — hot cycling / dwell | 30 cycles at each approved representative condition; proposed 2 h locked hot dwell and full cool-down | Hot docking friction, drift, relaxation and irreversibility | Limits met after equilibrium and cooldown; inspect wear and fasteners |
| 5 — supervised seam printing | Proposed 0.4 mm nozzle, 0.20 mm first layer; 5 coupons per condition/orientation plus same-sheet controls | First-layer discontinuity, snagging, adhesion and material sensitivity | Reviewed print metrics and safe crossing; no reconfiguration with objects present |
| 6 — endurance / transfer | 1000 cold/hot cycles in inspected blocks, then repeat stages 2–5 on both stock/frame variants | Wear, cable fatigue, printed-node creep, transferability | Drift/wear trend and post-endurance metrology remain within reviewed limits |

These counts are cost-controlled screening proposals, not lifetime qualification or reliability statistics. At 30 independent cycles with zero failures, the approximate 95% upper failure-rate bound by the rule of three is 10%; correlated cycles weaken even that inference. Inspect after the first 10/30/100 cycles and every proposed 100-cycle endurance block; stop at a trend toward binding or wear rather than completing a quota. Endurance rate must not overheat drives or bypass stabilization.

Stabilization candidate: all monitored surface points change less than 0.2 °C/min and maximum measured surface-height drift less than 0.01 mm over 10 minutes, followed by another mapped reading. Review sensor uncertainty and settling window before use. Do not assume "heater at setpoint" means mechanical equilibrium. Maintain an ambient control measurement to separate instrument/frame drift. Test differential heating because individual regions can have different temperatures; incompatible material recipes may need job rejection, not fictitious seam compatibility.

## Candidate acceptance criteria — all require review

Assume a 0.20 mm first layer and 0.40 mm extrusion width **only to propose a budget**. Different process settings require re-derivation. Values below are not current project requirements or approved pass/fail limits.

| Measurand | Proposed screening limit | Rationale and qualification |
| --- | --- | --- |
| Carrier return error X/Y | Worst absolute deviation from approved reference ≤0.05 mm including U | About one eighth of illustrative line width; separate accuracy, drift and repeatability |
| Yaw contribution at seam edge | ≤0.05 mm including U (≈0.032° at 90 mm) | Prevent center-only registration masking edge displacement |
| Adjacent sheet height step | ≤0.05 mm including U at every seam station | 25% of assumed first layer; nozzle clearance may require tighter limits |
| Total local Z error during print | ≤0.05 mm including seam step, drift, bow and uncertainty | These errors share a budget; each may not independently consume 0.05 mm |
| Positive hot seam clearance | Candidate 0.10–0.30 mm interval, uncertainty inside both bounds | Avoid contact while testing bridging below nominal line width; actual adhesion evidence controls; thermal strategy must deliver this at test temperature |
| Docked hot drift | Candidate ≤0.02 mm over 30 min | A proposed suballocation of total Z budget, not additive permission |
| First-layer / crossing behavior | No observed nozzle contact, lifted crossing, detached coupon or skipped motion in the screening set | A small underside seam mark is acceptable; document images and profiles, not merely "looks good" |
| Seam bond screening | No through-break at seam under handling; proposed seam coupon strength ≥80% of matched same-sheet control | Requires defined coupon geometry, loading direction/rate, calibrated force and failure-mode record; 80% is an investigation threshold, not structural part certification |
| Lock / state detection | No print enable with any injected unsafe or contradictory state | Every tested fault must latch an inhibit; zero failures in limited tests does not prove safety integrity |

For gap, require `min gap - U >= lower` and `max gap + U <= upper`. A cold gap outside that window can be deliberate if the hot window is met and cold contact is excluded. The 0.20 mm cold layout example fails the +60/+60 K expansion case with fixed center datums; redesign the anchor/pitch/gap strategy before heating. Reject arbitrary offsets that fix one temperature while creating interference at another.

Print thin rectangles crossing the seam normally, parallel-bead crossings, diagonal paths and multilayer coupons, each in both crossing directions; compare to same-sheet controls with matching material, surface preparation and thermal history. Log nozzle geometry, layer/line settings and measured part underside. A 2-bed seam cannot test a four-way central intersection: reserve a separate four-bed cross coupon, corner-gap map and all-four thermal closure test for later.

## Hazard review and operating prerequisites

| Hazard | Required proposal to review before testing | Abort / recovery principle |
| --- | --- | --- |
| Crush/pinch at bed edges, arms, tug, latches | Guarded swept volume; no hands in automated test area; service isolation; verified empty modules | Unexpected contact/force, guard access or position disagreement: stop, inhibit restart, inspect after isolation |
| Unsupported bed on release/power loss | Continuous gravity support, retained brakes/locks where needed, captured drive coupling | Any support/capture doubt: no unlock; no automatic homing recovery |
| Heater runaway, sensor detachment, stuck output | Independently reviewed temperature sensing, cutoff path, fusing and power isolation; suitable noncombustible fixture | Exceed approved temperature/rate/deviation limit or sensor fault: remove heater energy via reviewed independent means |
| Hot surfaces and printed-joint softening | Rated materials/insulation, measured support temperatures, supervised cooling/access procedure | Support temperature or creep exceeds reviewed limit: cut heat and prevent further motion as required |
| Electrical shock, short or cable fatigue | Qualified electrical review; rated supply, conductors, insulation, connectors, grounding where applicable, strain relief and protective devices | Damaged insulation, abnormal current/odor, exposed conductor or connector heating: isolate power; no touching live apparatus |
| Nozzle catches upward seam or object | Surface map, parked head during conversion, verified print path, initial supervised slow crossings | Contact, lifting or unexpected drag: stop; inspect nozzle, surface and datum before restart |
| Sensor, software or communications failure | Plausibility checks, watchdog and reviewed protective circuit independent of ordinary command success | Missing/stale/contradictory state inhibits heater/print/motion as assigned in reviewed state table |
| Fire / fumes / stored heat | Supervision, appropriate ventilation and emergency access, site-specific fire response | Smoke or unexplained heating: emergency isolation and site response; do not continue testing |

**Release-blocking blanks:** exact supply voltage/current, fuses, wire/cable ratings, safe force/speed, stopping distance, surface/support maximum temperatures, overtemperature/rate thresholds, sensor-fault times, structural proof loads and emergency-stop category/circuit must be determined from selected rig components and a qualified review. Generic numbers would create false safety. The experiment cannot run until these blanks are resolved in a signed/recorded procedure.

The emergency stop proposal must remove hazardous energy as the hazard assessment requires while preserving mechanical support; cooling or protective monitoring may need power. Never assume switching off a computer is adequate. Reset must not restart heaters/motion or release locks. Service requires physical energy isolation and verification, distinct from an emergency stop. No unattended energized tests.

Fault injection order: first logic simulation without hardware energy, then isolated sensor-state checks, then supervised bounded physical faults only under a separate reviewed method. Cover failed-open/stuck-closed lock indication, absent seated state, loss of position, communication timeout, power interruption during approach and partial latch, heater sensor disconnect/implausibility and stuck-command behavior. Do not intentionally create uncontrolled heater runaway or short live wiring to test protection. Use safe signal injection or a rated test load where appropriate. Record actual protective response times and restart state.

## What qualifies a candidate for further work

Advance only with complete raw records, a defensible uncertainty budget, repeated cold/hot/differential registration and seam results, stable support/load paths, inspected wear/cables, successful reviewed fault responses and independent review of conclusions. Failures or inconclusive limits lead to redesign and retest with revision IDs. Success supports **that two-bed rig within its measured envelope**; it does not validate four-bed closure, arbitrary materials/temperatures, concurrent printing, full-machine safety or either frame edition without their own evidence.
