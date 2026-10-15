# D6 — eight-mode control matrix and supervisory states

Bed IDs: **1 NW, 2 NE, 3 SW, 4 SE**; X right, Y north, Z up, millimetres.
D3's common horizontal reconfiguration datum is Z=0; printing Z is a separate coordinate.
Head IDs below are illustrative assignment obligations, not validated D2 reach.

## Eight arrangements

| Mode | Independently scheduled groups / streams | Active / parked heads | Z and temperature ownership |
| --- | --- | --- | --- |
| S | 1 / 2 / 3 / 4: four streams | Four active, no unused head | Four independent print-Z coordinates, bed recipes and nozzle recipes |
| R | 12 / 34: two streams | Two row-capable active; two complete structures parked | Two unrelated Z coordinates; each pair one coherent surface recipe, four separate bed heater loops |
| C | 13 / 24: two streams | Two column-capable active; two parked | Two unrelated Z coordinates; column coupling and thermal gradients checked separately |
| M12 | 12 / 3 / 4: three streams | Row-pair head plus two singles; one parked | Pair Z plus independent 3 and 4; three job recipes |
| M34 | 34 / 1 / 2: three streams | Opposite row pair plus singles; one parked | Pair Z plus independent 1 and 2; reflected routes checked |
| M13 | 13 / 2 / 4: three streams | Left column pair plus singles; one parked | Pair Z plus independent 2 and 4; no shared row drive |
| M24 | 24 / 1 / 3: three streams | Right column pair plus singles; one parked | Pair Z plus independent 1 and 3; no assumed reflected clearance |
| J | 1234: one stream | One full-region head, three parked | One print-Z coordinate and coherent four-surface recipe; four heater/sensor loops remain |

All active streams may have different speeds, layer heights, temperatures, progress
and completion times. Within a joined group, mutually incompatible temperature recipes
must be rejected; per-sheet regulation can correct local conditions but does not prove
seam stability. Compatible material/thermal limits remain unknown. Z-A assigns Z to each
active head/gantry; Z-E assigns one trajectory owner per connected bed group. Z-F keeps
partial-mode group lifts and detaches/retains its unified frame until an empty J handoff.
A unified frame permanently attached in partial modes fails the required independence.

Four-head cooperation on a joined object is excluded. Homing/calibration for a new job
must fit a reserved full path without moving an occupied bed or changing a shared datum,
mesh, support or axis of an unrelated job. If that cannot be shown, defer the new job.
Full-region J requires exclusive ownership of all four beds, its full sweep, one selected
head, and the parks/approach paths of every unused head.

## Proposed state vocabulary

| Entity | States / evidence carried |
| --- | --- |
| Machine | BOOT_INHIBITED, READY, RECONFIGURING, SERVICE_ISOLATED, FAULT_LATCHED; observed configuration epoch, environmental/recipe status separate from assessed protective-function status, communication health, power budget |
| Bed | UNAVAILABLE/UNKNOWN, EMPTY_READY, RESERVED, PRINTING, FINISHED_OCCUPIED, COOLING_OCCUPIED; retained sheet presence/readiness, pose, datum/mesh revision, temperature, support and lock observations |
| Head | UNKNOWN, PARKED_CONFIRMED, RESERVED, PRINTING, PAUSED_HELD, FAULTED; full gantry/harness envelope, homing status, nozzle temperature and local frame transform |
| Group | DISJOINT_SUPPORTED, PREPARING, DATUM_SUPPORTED, DOCKING, LOCK_CHECK, GROUP_READY, ACTIVE, DECOUPLING, FAULT_SUPPORTED_UNKNOWN; distinct position/load/transmission graphs and exactly one printing-Z authority |
| Job | QUEUED, ADMISSION_BLOCKED, RESERVED, RUNNING, PAUSED, CANCELLED_OCCUPIED, FINISHED_OCCUPIED, FAULTED; immutable geometry, resources, temperatures, progress and disposition |

These are **proposed states**, not a hardware design. A software flag never proves a
physical lock, sheet or safe support. Evidence needs identity, timestamp, validity,
source, disagreement detection and a defined maximum age. Absence/contradiction is
unknown, not “last known safe.” Sheet sensing technology is undecided; reliable surface
readiness is necessary even if achieved by a reviewed alternative to automatic sensing.

Environmental-panel status is distinct from protective-guard status and maintenance
isolation. All eight modes remain available for ordinary open-air printing. Panel absence
alone does not enter FAULT_LATCHED or require an interlock. Recipe constraints and
panel-handling conditions need their own justification; neither turns environmental
status into a protective observation. An actual protective fault, unsupported load or
unsafe restart remains inhibiting regardless of enclosure state.

The unchanged synthetic model's `Evidence.guard_permitted` represents an injected
assertion about any **assessed protective access conditions**, not environmental-panel
presence. It does not prescribe a guard or sensor and supplies no physical evidence.
No panel-presence input or hardware interlock is implemented by this correction.

## Transition contract

| From → to | Preconditions and ordered obligations | On missing evidence |
| --- | --- | --- |
| BOOT_INHIBITED → READY | Outputs remain inhibited; establish real configuration/support, sheets, position, assessed protective-function status and thermal state; explicit enable | Stay inhibited; no automatic homing into existing objects |
| QUEUED → RUNNING | Validate geometry/recipe; atomically reserve group, head, sweeps, Z and power; confirm evidence and local start acknowledgement | Queue with reason; no partial reservation or speculative motion |
| RUNNING → PAUSED → RUNNING | Stop within owned envelope; retain beds, objects, support and heat budget; recheck evidence before resume | Fault if stop/position uncertain; never silently free resources |
| RUNNING/PAUSED → CANCELLED_OCCUPIED | Controlled stop and reviewed heater disposition; keep object occupancy and reservations until removal | Fault uncertain stop, preserve conservative occupancy |
| RUNNING → FINISHED_OCCUPIED → EMPTY_READY | End acknowledgement, cooldown, safe access/isolation where required, removal and sheet/volume readiness evidence | Finished does not mean empty; blocked paths remain blocked |
| S → pair/mixed → R/C | Compute affected pose/support/drive/reference closure; all affected beds empty; independent supports and restraints established; empty modules at common datum before horizontal movement; reserve complete route; position then structural/drive engagement checks; group calibration; commit new epoch | Reject route or latch fault if underway; preserve unaffected job states only with demonstrated mechanical/thermal isolation |
| Pair/J → split | Same empty-domain and route gates; support loads independently before releasing links/selectors; horizontal undocking at datum; verify separate supports, datums and unused-drive isolation before commit | No release based solely on a command acknowledgement |
| Any → FAULT_LATCHED | Inhibit new starts/reconfiguration; execute separately reviewed protective response over influence domain; retain occupancy/uncertain pose | No automatic restart after reconnect, power return or sensor recovery |
| FAULT_LATCHED → recovery/READY | Human acknowledgement, cause correction, support/assessed-protection/temperature and position evidence; review object obstruction before any re-home; re-admit explicitly | Reset alone cannot enable motion or resume a buffered job |
| Environmental panel conversion → same operational state unless assessed conditions require a stop | Verify reviewed panel/hand paths, thermal handling and any explicitly assigned protective function; panel absence alone does not alter motion authority | Defer unsafe handling; invoke a protective response only for an actual assessed protective loss, not mere environmental-panel absence |
| Actual protective access event → assessed stop/inhibit state | Apply the justified function response and scope; restore evidence and deliberate restart readiness | Never bypass necessary protection or treat closing a guard as restart authorization |
| Safe stopped → SERVICE_ISOLATED | Independent maintenance isolation, stored-energy restraint and verified cooldown/access procedure | UI service flag is not isolation |

Changing group membership affects the entire old and new connected group, including
support/torque links whose endpoint XY does not move. S↔M12 can leave 3/4 active only
with proven isolation and a clear route; R↔C normally affects all beds; any transition
to a unified J support affects all four. The model implements only an atomic abstract
transition with injected evidence. It does not simulate physical lock sequencing, all
56 paths, selector travel, load transfer or sensing. The complete transition contract
above remains unimplemented engineering work.
