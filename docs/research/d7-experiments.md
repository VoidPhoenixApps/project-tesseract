# D7 — future discriminating experiments and reference-geometry requests

**Proposals only. No CAD, model download, installation, purchase, firmware change,
supplier contact or physical execution authorized.** [Shortlist](d7-integrated-study.md).
All experiments preserve four sheets and the complete [requirements](../requirements.md).

## Prioritized queue

Numerical pass limits are not invented here. Each proposed test must pre-register
reviewed limits, range, repeats/sample count and uncertainty decision rule before
execution. Where the observable is a logical contradiction, exclusion is possible
without a numerical physical acceptance limit. Otherwise unknown input means inconclusive.

| Priority / question | Scope and dependencies | Observables and discriminator | Uncertainty, review and stop gate |
| --- | --- | --- | --- |
| E1 — can any complete XY layout retain all eight modes? | Future bounded envelope/kinematic CAD comparison of H versus B and one R transformation; exact head, guide, motor, cable and stage geometry approved first. One full-region J head, no cooperation assumption | Reachable paths, same-Y column jobs, all four mixed placements, full assembly parks/approach/return, unrelated height extrema and tall finished neighbors; enumerate frame/column/cable clashes. Reject actual missing DOF; unresolved geometry cannot pass | Mechanical/controls review of swept representation, usable strokes, deflection/stopping allowances and coordinate transforms. Stop on identity/rights mismatch, unbounded sweep, required occupied-bed motion or panel-dependent ordinary travel |
| E2 — can support stay compatible through grouping? | Future symbolic P/L/T and bounded two-carrier cold-interface study, E-sync versus E-hybrid; include both seam orientations, eccentric payload, guide error and lost drive. F/C only as additional handoff cases | Reaction signs, residual DOFs, positive retention, guide mismatch, load sharing, seam step/tilt and transient load path. A zero-load/unsupported intermediate or redundant hard constraint excludes that topology | Qualified mechanical review; real contact stiffness/friction absent, so analytical reaction magnitudes are sensitivities. Before physical work define load limits, catches, uncertainty and safe isolation. Abort any loss of support, unexpected motion or out-of-limit load/pose |
| E3 — does thermal relief preserve traversable seams? | Preserve first physical proof: separately authorized/reviewed two-bed docking then thermal registration and cross-seam printing; actual plate/heater/magnet/sheet stack, relieved mount and safe wiring. Compare center versus inward-corner reference only within reviewed safe test scope | Repeated X/Y/Z registration, gap/step at endpoints/midspan, full height map, cold-anchor and support temperatures, differential/reversed heating, sheet slip, cross-seam adhesion/nozzle transit. Retain raw failures and cycles; no exact usable area inference | Thermal/electrical/mechanical review, calibrated uncertainty budget, first-layer-derived limits and repetitions before running. Abort reviewed thermal/current/pose limits, sensor/lock inconsistency, restraint or adhesion loss, abnormal heating/motion; supervise and isolate safely |
| E4 — does head-Z compliance outweigh bed-group error? | Future printed-joint and reinforced-member comparison using actual stock and separately generated US/metric specimens after approval; no full frame first. Use E1 load paths and E2 budgets; test panels absent/present without structural credit | Root rotation, loaded tip displacement, hysteresis, time/temperature creep and mode response; compare total nozzle-to-sheet error for H/B, not member stiffness alone | Actual grade/tolerances, print orientation/material/process and instrument uncertainty; structural/thermal review. Stop at reviewed strain/deflection/temperature limits, cracking/slip or invalid linear-model regime. Both stock interfaces and Ender 3 envelope required |
| E5 — does the secondary frame earn its extra mechanism? | Only if E1–E4 show H/B weakness and R potential. Future finite-radius belt-path comparison against dedicated belts/positive selector and no-selector C-group; exact selector, pulley and restraint geometry required | Continuous path length/wrap/tooth phase, tension and actuator reaction, unused-frame clearance and support at every shift state. Measure added seam stability versus extra mass/calibration/fault paths | No endpoint-only proof. Mechanical/safety review and exact vendor ratings before any powered rig; stop on partial engagement, support ambiguity, slack/wrap loss or guide binding. A selector experiment does not replace first two-bed seam proof |
| E6 — can firmware preserve the proven mechanical contracts? | Future bounded offline lifecycle/model study after exact immutable geometry and resources from E1/E2, with identified firmware versions and actual load data; no firmware modification/runtime authorized now | Four unrelated jobs, row/column pairs, every M, J, cancel/finished occupancy, restart and stale lock/sensor faults, shared-power peak admission; track deadlines and reserved resources | Controls/electrical independent review. Stop if implementation serializes required independent work, accepts stale/unbounded geometry, moves occupied beds or cannot bound fault response. Software results still cannot validate physical cutoff/restraint |
| E7 — do both enclosure states preserve access and function? | Future panel-retention/removal envelope and passive thermal/service study with exact panel/retainer material and electronics ratings; coordinate with E1/E4 | Entire panel/hand extraction, positive retention, service access, temperature/drift in both states, motions without removing panels | D5 hazard-specific review, no automatic panel interlock. Before physical work define safe handling/cooling conditions and uncertainty. Stop if panel is necessary bracing, defeats assigned protection or obstructs a required mode |

E1/E2 are the first CAD-scope requests to prepare, not permission to execute them.
E3 remains the first physical printer proof; any other physical specimens/rigs require
a separately reviewed sequence consistent with that priority. E5 is deliberately later:
there is no reason to optimize a selector before showing a useful full-machine benefit.

## Consolidated missing-model requirements

The [generated appendix](d7-model-requests.md) uses existing Stage D triage for seven
**candidate references, not selected components**. It preserves exact catalog IDs,
source URLs/revisions and each of the five rights fields. It is a review packet,
not a current approval request requiring the maintainer to answer before D7 completes.
No sample is downloaded. Exact manufacturer/configuration selection is itself still
an upstream decision; it cannot be inferred from the request list.

| Dependency / catalog identity | Desired geometry and format | Purpose / blocked experiment | Specific uncertainty |
| --- | --- | --- | --- |
| `e3d-revo-hemera-xs-direct-drive` | STEP + applicable native assembly/drawing; nozzle and mount datums, motor/fan/lever/connector/service volumes | H/B/R head reach, E overlay, parking; E1 | Physical revision/rights unresolved; exact thermal/electrical variant and full assembly correspondence required |
| `hiwin-mgn12h-carriage-size-preload-accuracy-seal-options-unresolved` | Configured rail+block STEP and manufacturer drawing, rail length/end holes, preload/accuracy/seals | Stage guide root, column and parked support; E1/E2 | Catalog name explicitly lacks final options; no generic MGN12 substitute, portal is unconfigured |
| `stepperonline-17hs08-1004s-short-body` | Revision-matched STEP and shaft/connector drawing | Candidate motor envelope/root/drive clearance; E1/E2 | Stage C corrected body/shaft drawing discrepancy; physical revision and inspected asset absent. Not a motor torque selection |
| `gates-2mr-20s-06` | Exact pulley pitch/flange/bore/hub drawing plus STEP | Transmission routing only if selected; E2/E5 | Bore/drive configuration and rights unresolved; do not transfer pitch geometry from another pulley |
| `gates-200-2mgt-06` | Exact belt section/pitch and material/rating documentation; permitted CAD if useful | Finite path, wrap, tension limits; E5 | Fixed catalog belt length does not select a route or adequate lifting rating; deformation cannot be inferred from static CAD |
| `antclabs-bltouch-smart-v3-1` | Revision-matched STEP, deployed/retracted probe and cable/datum drawing | Candidate probing reach, seam access and parking; E1/E3 | V3.1 named but geometry uninspected and model not located; not selected surface/fault sensor |
| `omron-d2f-01l-hinge-lever-pcb-terminals` | STEP and full lever operating-travel/mount/terminal drawing | Candidate lock-state observation envelope; E2/E6 | No located approved model or protective-function qualification; ordinary position switch is not a safety design |

Other categories have **no exact selected identity** and must remain explicit missing
requirements, rather than invented manufacturer records:

| Missing category | Required exact evidence before dependent CAD | Blocked work / source route |
| --- | --- | --- |
| Nominal 180 mm bed, heater, magnet and retained sheet stack | Selected manufacturer/part/revision, native/STEP plus dimensioned outlines, flatness, anchor/hole pattern, cable exits, material/thermal ratings | E2/E3 thermal and docking interface; no established exact model source in catalog |
| Downstream fall restraint, brake/catch, structural lock and selector | Exact rated part/configuration, STEP/native, engagement/support datums, load/failure behavior and rights | E2/E5 continuous support; D3 references are precedents, not selected parts or approvals |
| Flexible harness/chain, filament path and connectors | Exact moving lengths, minimum loaded bend radii, connector/strain relief/service envelopes and ratings | E1/E6 swept paths; candidate electrical catalog entries alone are insufficient |
| Imperial/metric reinforcement and printed node interface | Exact grade/finish, actual OD/ID/wall and tolerances, cut/end details and source correspondence; dimensioned stock drawings often more useful than generic STEP | E4; [D4 stock ledger](d4-reinforcement.md) has specific candidates, but they must not be replaced by similarly named library stock. Public links there are leads, not final purchases |
| Panel material/retainers and any separately justified protection | Exact thickness/grade/retention and extraction geometry, temperature limits, rights | E7; no selected panel hardware/model. Do not fabricate a vendor latch |
| Electronics, power/heater switching and cooling | Exact board/PSU/protection and fan revisions/ratings, connector and service envelopes, approved circuit architecture | E6/E7; catalog Feather sample and LRS-350-24 entry do not size this printer or select a controller/PSU |

At later selection, search catalog and approved local library again for the **exact**
identity. If absent, request correct files or approval of a source in one consolidated
packet: part/revision, format/link, geometry purpose, rights/accuracy gap and blocked
work. Native editable project CAD plus permitted STEP derivatives must remain publicly
reproducible without paid/proprietary tools. No license, AI-processing, redistribution
or cloud-upload permission is assumed; no approximate vendor stand-in is authorized.
