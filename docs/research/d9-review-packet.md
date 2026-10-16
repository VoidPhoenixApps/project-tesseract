# D9 — engineering-review packet and future E2 gate

[Study](d9-study.md) · [contract](d9-contract.md) · [fault map](d9-faults.md).
**No CAD or physical execution authorized.** This packet asks what must be known before
bounded E2 work could be approved. Independent AI critique is only a desk check.

## Evidence and source revisions

Repository source baseline: `bf8a55f40e2d6ff99069950e8ddc27874cf32e9d` (D8 / PR #42).
Read D1/D3 load/selector studies, D4 load paths and structural risks, D6 protective
functions, D7 compatibility/failure chains/E2 proposal, D8 motion contract/results and
Phase 1/1B/1C evidence at that baseline. Existing sources retain their original revision
and limits; D9 does not represent old vendor information as newly qualified geometry.

Primary reference pages revisited on 2026-10-16 (America/Chicago), text only:

| Source / revision | Supported principle | Limit and review question |
| --- | --- | --- |
| [mayr vertical axes](https://www.mayr.com/en/industries/vertical-axes~517), undated live page | Gravity-loaded axes need a suitable restraint/braking concept; rotary and linear arrangements differ | No selected device, capacity, engagement delay or Tesseract suitability. Where does the actual restraint act relative to every failed transmission element? |
| [THK master guide and combined use](https://www.thk.com/us/en/products/lm_guide/maintenance/0001/), undated live page | Rail/block correspondence and mounting references matter | No configured rail or allowable frame mismatch. Which follower freedoms remain/release during every handoff? |
| [NIST TN1297 section 5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty), 1994 note, live section | Uncertainty propagation includes covariance | No uncertainty values supplied. How will shared datum, thermal and sensor errors enter the actual decision rule? |

[D3 references](d3-references.md) preserve Gates lifting/backup guidance, Miki selector
precedent and coupling literature with their inspected revisions. [D6 safety](d6-safety.md)
preserves the distinction between emergency stopping and supported maintenance isolation.
These are engineering context, not a compliance finding, product recommendation or
qualification of a complete machine. No external CAD or source illustration was copied.

## Questions requiring qualified review

| Reviewer | Concrete question / evidence requested | Adoption blocked until resolved |
| --- | --- | --- |
| Mechanical/load-path specialist | For each H head, B bed and unused platform, trace normal and fault force/moment to foundation. Identify unilateral contacts, supported DOFs, anchor failures, preload and actual COM extrema | Selecting a support, restraint or release sequence |
| Mechanical/metrology specialist | Can constant-datum horizontal capture transfer load without incompatible guide closure? Which freedoms release, and where do their moments go? Bound settling, hysteresis, backlash and seam tilt with measurement uncertainty | Declaring compatible transfer or assigning a seam budget |
| Structural/thermal specialist | What happens to printed roots, stock interfaces and catches under worst reach, asymmetric catch, warm creep, repeated loads and shared-frame disturbance? Compare actual imperial/metric variants and later 2020 separately | Crediting stiffness, fault independence or transferable capacity |
| Electrical/controls safety reviewer | What retains gravity during power/brownout, stalled drive, failed catch or stale downstream data? Define fault-domain stop/heat/cooling behavior and deliberate recovery, including retained objects and service isolation | Energized tests, firmware/control adoption or protective-function claims |
| Combined review | Does B's complete lift/harness/fault envelope preserve D8's clearance gain? Is H nozzle-to-sheet error actually smaller with stationary beds after column/root error? | Narrowing H/B or approving dependent detailed CAD |

The complete dependency graph must include shared supply, wiring, sensor mounts, printed
anchors, heat exposure and maintenance actions. Two apparently redundant devices with a
common disabling cause are not independently qualified. No reviewer is asked to approve
an undefined safety level or limits from the illustrative calculation tables.

## Smallest useful E2 comparison, proposed only

First deliverable after this desk study should be a **reviewed specification** for a
cold two-carrier comparison, not a four-bed machine. Keep the separately reviewed
two-bed docking/cross-seam rig as the first physical printer proof. Any cold support
measurements should be an approved precursor within that program; the head-Z comparison
must receive explicit separate scope/sequence approval rather than displacing it.

Compare (A) two continuously supported carriers with independent lifts and downstream
pose observation, (B) the same with a removable cold load-sharing tie and explicit
follower relief, and (C) stationary carriers with one representative restrained head-Z
load path. The head comparison is one bounded axis/arm, not four-head CAD. Use common
endpoint error metrics and measured masses, not equal fictional masses that favor one
candidate. Do not introduce the secondary platform/selector unless A/B/C data establishes
a specific question it can answer. Orthogonal pair arrangements must be represented
by a reviewed orientation change, not assumed equivalent.

| Stage / controlled factor | Measurements and raw record | Discriminator / limit of conclusion |
| --- | --- | --- |
| Pre-CAD inventory and force sketch | Exact masses, COM and inertia bounds; real stroke/overlap, contact normals, guide freedoms, catch/anchor specification, electrical power-loss states | Missing continuous support or mandatory independent coordinate excludes that specified topology before building |
| Cold static support, after authorization | Reactions at relevant supports; downstream six-DOF carrier/head pose, both seam endpoints and midspan; offsets at reviewed COM extrema; frame/reference motion at an untouched neighbor witness | Uplift, insufficient retained DOF or binding contradicts assumed support. A passing small range limits only that range, not all modes |
| Loaded capture/release at fixed datum | Time-correlated reactions, lock travel, pose/tilt, load acceptance and residual settling across approach/overlap/release; both seam orientations | Any unsupported interval or required vertical reconfiguration rejects that handoff. Sensor indication alone cannot pass |
| Stroke and reach sweep | Same nozzle-to-sheet reference for H/B; displacement, hysteresis, guide drag and cable/filament forces at reviewed extrema; support/reference disturbance | Separates head compliance from bed differential motion. Unknown temperature/creep remains open after cold results |
| Fault plan, not initial live drop testing | First review restrained/de-energized fault representations; later separately approved instrumented loss-of-drive/power and catch characterization only with independent containment | Determines whether a named failure bypasses R; static holding cannot qualify dynamic arrest or repeated catch life |

Do not cut belts, disable catches or energize a rig under this proposal. The review
must decide safe fault emulation, containment, instrumentation and supervision first.
Two carriers can discriminate support mechanisms; they cannot demonstrate all eight
mode routes, four-bed closure, real concurrency, full-machine reach or thermal printing.

Before any physical procedure, preregister source revision, stock variant, materials,
print process/orientation, temperature, load/COM/stroke/velocity ranges, calibrated
instruments and sampling bandwidth, repeated cycles and order, uncertainty/covariance,
raw-log format, and separate safety/equipment/print-quality limits. A numerical result
is acceptable only under the reviewers' uncertainty rule; overlap with an acceptance
boundary is inconclusive. D9 intentionally supplies no invented pass tolerances,
sample count, catch load, latency rating or safe operating range.

**Proposed abort conditions for reviewers to quantify:** loss/uncertainty of support
or restraint, lift-off where not allowed, unexpected gravity motion, partially engaged
load joint, reaction/pose/skew/temperature/current beyond reviewed limits, guide binding,
crack/slip, unexpected reference motion at the neighbor witness, cable snag, invalid
sensor freshness/disagreement or failed containment. Abort disposition must preserve
loads while controlling hazardous energy; power removal alone is not necessarily safe.
Stop at uncertainty rather than increasing drive force. Recovery requires supported
inspection and deliberate authorization; no automatic homing, release, reheat or resume.

## Consolidated geometry and data dependencies

The [approved catalog workflow](../../cad/reference-parts/README.md) and
[D7 exact request ledger](d7-model-requests.md) own identities/rights; D8's
[focused appendix](d8-model-requests.md) retains the head/guide/motor/probe subset.
No part is selected by this packet. Local catalog/library checks verify only existing
records and the authorized Feather sample, which is irrelevant to support geometry.
There is no approved exact E2 restraint/bed/guide assembly in that library.

| Identity or unresolved category | Desired source/format and geometry purpose | Availability/rights gap and blocked work |
| --- | --- | --- |
| `hiwin-mgn12h-carriage-size-preload-accuracy-seal-options-unresolved` | Configured manufacturer rail/block STEP plus tolerance/moment/preload drawing; real guide support, overlap and follower relief | Exact length/options/revision still unresolved; catalog portal is not configured geometry. Blocks E2 guide interfaces |
| `e3d-revo-hemera-xs-direct-drive` | Revision-matched complete head STEP/native and mount/nozzle drawing through catalog source; mass/COM and head-Z load entry | Exact variant/rights and physical correspondence unresolved. Blocks H load/park interface; no reflected purchased parts |
| `stepperonline-17hs08-1004s-short-body` | Matched STEP, shaft/connector drawing and torque/inertia data through catalog source; drive envelope and support loads | D8/Stage C revision discrepancy remains; no assumed lifting capacity. Blocks drive interface |
| `gates-2mr-20s-06`, `gates-200-2mgt-06` | Exact configured pulley/belt drawings, pitch/flange/bore, routing and ratings; permitted STEP if useful | No route/length/bore selection or lifting qualification; rights unresolved. Blocks optional T-link finite geometry |
| `omron-d2f-01l-hinge-lever-pcb-terminals` | Exact travel/mount/terminal drawing and permitted STEP through catalog source | Candidate engagement observation only, not safety qualification or load sensing. Blocks exact lock-sensor mounting |
| Bed/heater/magnet/sheet and carrier stack — identity unselected | Exact manufacturer/revision STEP plus dimensioned outlines, thermal stack, anchors and cable exits | No established exact source or rights; blocks B hot-stack/support interfaces. Nominal 180 mm is not an actual outline |
| Load-side catch/brake, lock, axial support and selector — identity unselected | Manufacturer-rated configuration, STEP/native/drawings, engagement travel, holding/dynamic loads, response and failure behavior; mayr/Miki in D3 are leads only | No selected/approved device or model; blocks all real R and handoff/capacity design |
| Downstream pose/load observation — identity unselected | Exact sensor frame, range, resolution/uncertainty, latency, diagnostics, wiring and mount drawing | Motor encoder, probe and switch are not interchangeable. Blocks actual support/tilt/freshness assurance |
| Harness/filament, stock and printed anchors — unresolved selections | Exact cable bend/strain-relief details; actual imperial/metric stock grade/dimensions/tolerances and printed-node process | D4 stock ledger supplies candidate leads only. Blocks full-stroke forces, interface fit, independent anchors and thermal/creep bounds |

At selection, recheck exact catalog identity and approved local folder. Ask the maintainer
once for correct files or an authorized source, including revision, format, official link,
purpose, rights uncertainty and blocked interface. Existing source links are consolidated
in D7's ledger; no new vendor availability or rights is asserted. Do not substitute,
invent dimensions, redraw a supposed vendor model or download anything to close a gap.
Independent desk work is complete without those future geometry approvals.
