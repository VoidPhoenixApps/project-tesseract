# D3 — mode, support and constraint matrix

[Report](d3-engineering-study.md) · [transition/fault obligations](d3-failure-study.md).
Bed IDs match D1/D2: 1 NW, 2 NE, 3 SW, 4 SE; X right, Y north, Z up.
P=positional registration; L=gravity/moment support; T=drive transmission.
`Li` means each bed's own load path including independent gravity restraint;
`Lij` means an **optional, unvalidated** load-bearing cold link, not an edge clamp.
`Dg` means one group motion reference, potentially commanding several monitored motors.
An edge listed for P or T does not automatically exist for L.

## Eight explicit printing states

Every row supports **all four beds**, whether jobs are active or not. Each retained
sheet/plate remains on its own thermally relieved supports. The primary matrix uses
independent local supports, with optional hybrid ties shown explicitly. Scalar heights
describe progression only; roll/pitch and surface deformation remain measured quantities.

| Mode / groups | Independent Z progression and motion owners | P registration | L support / engaged load joints | T selection and secondary platform | Verified state required before printing |
| --- | --- | --- | --- | --- | --- |
| S: 1 / 2 / 3 / 4 | 4: D1,D2,D3,D4 | Four separate cold station datums | L1,L2,L3,L4; inter-bed load links open | Independent transmissions; common platform detached and independently retained clear | Four positions/planes, local restraint and station lock states; all cross-group links open |
| R: 12 / 34 | 2: D12,D34, unrelated heights | Each pair registered; no hard 12→34 datum closure | All Li retained; hybrid L12,L34 engaged if adopted | Independent pair paths 12 and 34; platform isolated | Both pair locks/pose and each lift observed; no cross-row structural/torque link |
| C: 13 / 24 | 2: D13,D24, unrelated heights | Column datums, not rotated row assumptions | All Li; optional L13,L24 | Independent column paths; platform isolated | Both column locks/pose, four restraints; row links open and column guide compatibility |
| M12: 12 / 3 / 4 | 3: D12,D3,D4 | Pair 12 and two independent stations | All Li; optional L12 only | Pair plus two singles, platform isolated | Pair support/phase, singles undisturbed; 13,24,34 links open |
| M34: 34 / 1 / 2 | 3: D34,D1,D2 | Pair 34 and two independent stations | All Li; optional L34 only | Pair plus two singles, platform isolated | Mirror placement separately checked; 12,13,24 links open |
| M13: 13 / 2 / 4 | 3: D13,D2,D4 | Pair 13 and two independent stations | All Li; optional L13 only | Column pair plus singles, platform isolated | 12,24,34 links open; left-pair guide/cable route verified |
| M24: 24 / 1 / 3 | 3: D24,D1,D3 | Pair 24 and two independent stations | All Li; optional L24 only | Column pair plus singles, platform isolated | 12,13,34 links open; right-pair guide/cable route verified |
| J: 1234 | 1: D1234, or stationary locked beds and gantry G | Four cold carriers; released-slave tree or independent datums, no forced four-edge loop | Baseline all Li; hybrid links need six-DOF analysis. Secondary variant: all four transfer to retained platform locks and independent platform restraint | Baseline group drives; mechanically coupled example T12,T13,T34 forms tree. Secondary selects platform only after handoff. Gantry variant holds beds structurally | All sheets/planes and center crossing, selected ownership, positive load locks, unused-drive isolation and entire parked-head structures |

For the baseline, P locks locate each carrier **within its moving Z assembly**, so they
do not pin printing Z to a stationary frame. For a mechanically linked alternative,
specify the corresponding released follower freedoms; do not layer both constraint sets.
Independent lifts remain responsible for moment support in the baseline: a torque link
does not allow deleting their bearings. Hybrid tie load redistribution is indeterminate
without stiffness data. Secondary-frame J must explicitly release/float incompatible
local-guide constraints or demonstrate compatibility and load sharing; disconnected
motor torque does not disconnect a guide.

## Secondary frame interpretation across modes

| Platform condition | S | R/C | All four M placements | J |
| --- | --- | --- | --- | --- |
| Single rigid frame remains attached to every bed | Fails four heights | Fails two heights | Fails three heights | One height coordinate, conditional support/selector |
| Unified frame detached in partial modes, independent group lifts retained | Conditional | Conditional with both group orientations | Conditional with each isolated single | Transfer and selected lift remain unresolved |
| Two permanent row sections | Could not supply four independent heights alone | R conditional; C fails while rows remain rigid | Fails any grouping that requires splitting a row | Conditional after joining sections |
| Four selectable sections | Unresolved guide/support topology | Unresolved orthogonal coupling | Unresolved sectional support/clearance | Unresolved joint compliance and closure |

These are DOF exclusions, not whole-machine feasibility. Section count alone does not
establish stable supports or accessible joints. D1's `h_i=g+b_i` still applies: for a
stationary gantry, independently descending bed groups provide independent progress;
with beds all locked, one common gantry supplies only one progress coordinate.

## Dock/decouple changes and unaffected beds

| Requested transition | Affected clear modules / ownership changes | Unaffected jobs protected |
| --- | --- | --- |
| S ↔ M12 / M34 / M13 / M24 | Only nominated pair, if route allows; two local references become one group or reverse; add/remove its P and optional L/T links while supported | Other two local lifts retain position, support, cables and reference; no movement or load transfer into their structures |
| M12 or M34 ↔ R | Only the other row if existing pair pose/load stays unchanged; add/remove second row group | Existing row pair may continue only with a verified independent path and unchanged support geometry |
| M13 or M24 ↔ C | Only other column under same condition | Existing column pair may continue with verified isolation |
| R ↔ C, row mixed ↔ column mixed | Any bed whose pose, group, load path or reference changes is affected; usually all four | Do not relabel a bed unaffected merely because its XY endpoint matches. Changed connected groups must be empty |
| Any partial arrangement ↔ J | All four for unified platform or changed all-bed group; all clear, at datum before horizontal conversion | No occupied module is exempt from J's changed load/constraint domain |
| Any arrangement → S | Every split/moved group clear; unaffected singles only if pose/support path truly unchanged | Finished objects still count as occupied; no assumed clearance from queue status |

Use the [generic handoff states](d3-failure-study.md) for each affected group. No complete
56-directed-transition trajectory proof is claimed. D2's final poses and synthetic
sweeps cannot certify the added guides, cross or selector. Reject transitions obstructed
by active/finished objects; do not indefinitely pause jobs during otherwise claimed
independent printing to hide a structural inability.
