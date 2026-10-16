# S1 — software feasibility before forks

**2026-10-16 · Research and offline software tests only · [issue #46](https://github.com/VoidPhoenixApps/project-tesseract/issues/46).**

Investigate a **standalone coordinator with ordinary executors first**. No baseline
requirement yet demonstrates a need to fork a slicer. Four isolated Klipper instances
are a credible starting point for independent jobs, conditional on exclusive physical
resources. They are not a demonstrated solution for dynamically grouped bed-Z. Keep
RRF as a serious grouped-motion comparator, but its inspected 3.7.0 source has **two**
motion systems and shared print lifecycle state, not four independent uploaded jobs.
A Klipper fork should follow a reproduced integration failure, not precede it.

This is a feasible software investigation program, **not proof of a feasible printer**.
No controller, Z scheme, toolchain or license is selected. Detailed machine CAD remains
paused; the first physical proof remains reviewed two-bed docking and cross-seam printing.

Read [sources and licenses](s1-sources.md), [architecture and interfaces](s1-architecture.md),
[verification and limits](s1-verification.md), and the [offline trace](s1-results.json).
Source IDs below refer to the pinned ledger; classifications are engineering inferences
from those sources unless explicitly labeled tested.

## Required arrangements and slicing route

Beds: 1 NW, 2 NE, 3 SW, 4 SE; X east, Y north, Z up, mm. Reconfiguration is horizontal
at the common fixed-height datum; printing Z remains a separate ownership problem.
Four nominal 180 × 180 mm heated beds and **four individual sheets** persist in every row.
Nominal dimensions below are profile families, not approved usable areas.

| Mode | Independent region jobs | Profile families per job; nominal XY | Main integration obligation |
| --- | --- | --- | --- |
| S | 1 / 2 / 3 / 4 — four | Four single-region 180 × 180 | Four independent XYZ/extrusion states and recipes |
| R | 12 / 34 — two | Two horizontal 360 × 180 | Two unrelated seam-spanning trajectories and Z owners |
| C | 13 / 24 — two | Two vertical 180 × 360 | Column reach and ownership; rotating a row profile alone is insufficient |
| M12 | 12 / 3 / 4 — three | Horizontal pair + two singles | Protect lower singles during empty upper-pair conversion |
| M34 | 34 / 1 / 2 — three | Horizontal pair + two singles | Reflected physical route needs separate evidence |
| M13 | 13 / 2 / 4 — three | Vertical pair + two singles | Protect right singles and their supports |
| M24 | 24 / 1 / 3 — three | Vertical pair + two singles | Protect left singles and their supports |
| J | 1234 — one | Joined region, nominal 360 × 360 | One full-region head, three retained parked assemblies, all bed resources exclusive |

Ordinary profiles can describe one stationary logical region's printable polygon,
height limits, nozzle/material, speeds and supported G-code dialect. Separate region
exports permit different layer heights, temperatures and completion times. The
coordinator chooses a permitted mode and calibrated region profile, then assigns each
file to an executor. Usable polygons must come from actual reach/clearance and seam
measurements; no ready-to-print machine profiles are justified yet.

A conventional J file need not know there are four sheets: one continuous calibrated
coordinate surface is a candidate. Firmware/adapter maps its origin and mesh to the
single nozzle, while one thermal owner manages four heater/sensor loops. G-code must
not reset unrelated offsets or globally home/disable heaters. A mesh cannot repair a
physical gap, unstable seam step, sheet slip, missing reach or differential lift fault.
One joined toolpath therefore does not demonstrate cross-seam print quality.

## Capability decision table

**U** upstream building block; **I** integrable outside firmware in principle;
**X** extension/semantics uncertain; **F** firmware modification candidate;
**M** mechanically constrained. None of these means Tesseract runtime-tested.
K = ordinary single Klipper; K×4 = coordinator + isolated instances; KF = targeted
shared-scheduler Klipper modification; RRF = one 3.7.0 build + coordinator.

| Required behavior | K | K×4 | KF | RRF | Slicer / host responsibility |
| --- | --- | --- | --- | --- | --- |
| Four independent S interpreters/jobs | F: K2 has one normal state/file | U processes + I admission; M isolated resources | F separate file/parser/planner/lifecycle contexts | F beyond two compiled systems; X independent files | I four ordinary exports; virtual beds are not execution queues |
| Two R/C and three mixed jobs | F for unrelated simultaneous lifecycles | I/M per region; grouped resource handoff X | F/M shared scheduler still needs independent DOFs | U two async queues; X two independent lifecycles; F three | I two/three region exports; preserve all four mixed cases |
| J single-head toolpath | U ordinary single job; M full reach | I select one executor; M/X group ownership | U trajectory + F group integration | U one queue; M grouping | U conventional single-region slice; I mapping/recipe |
| Independent progress and late arrival | One job's U progress; another file cannot start concurrently | U per-process status + I admission | F separate progress/input state | X file readers progress independently but stored print lifecycle shared | I immutable per-job files and metadata; no global layer barrier |
| Independent XYZ, extrusion modes, offsets and mesh | U one context; multiple axes do not isolate contexts | U per instance; I transforms; M no shared axes | F namespaces and independent look-ahead/compensation | U movement states/tools; X full mesh/modal isolation per unrelated job | I bind calibration and dialect per region; unsupported commands rejected |
| Bed/nozzle temperatures | U loops; I protected one-owner recipes | I global thermal owner or exclusive per-instance outputs | F/X resource-scoped heater commands | U tool/heater facilities; I ownership | I each group coherent recipe; four regulated bed loops retained |
| Coordinated group Z / shared axes | U one trajectory domain; X changing groups | X/F if groups cross fixed executor/MCU boundaries | F common timebase and arbitration | U async/resource primitives; X exact grouping/build | M shared permanent axis cannot supply unrelated coordinates; host timestamps do not synchronize lifts |
| Individual pause/cancel/finish | U one job; not four | U per instance + I safe park/retained objects | F isolate buffers, pause, park and cancellation | X shared pause/print state; do not credit M606 with job isolation | I preserve occupied volumes and reservations; queue pause is not print pause |
| Protected reconfiguration | I planner; X resource reassignment | I affected-domain planning; X no generic hot MCU transfer | F only where scheduler/ownership cannot be extended | I planning + X axis/resource release semantics | I require empty affected beds, routes, support/lock/datum evidence |
| Lost MCU/link or controller fault | U shutdown facilities; M physical stop/retention | I conservative global inhibit; X bounded distributed stop | F/X coordinated fault scopes | U fault facilities; X group stop/recovery semantics | I persist occupancy; acknowledgements are not measured stops |
| Power recovery / restart | X no full Tesseract recovery contract | I boot inhibited; X safe resumption | F/X replay and state reconciliation | U power-fail features on supported hardware; X multi-job recovery | I no automatic restart; re-establish position, supports, sheets and objects |
| Full-head clearance and occupied objects in every mode | I admission; M actual geometry absent | I global reservations; M absent envelopes | I/F planner integration; M geometry | U limited separation/keepout; I full swept-volume check | X geometry certification not provided by slicer model bounds |

K2/K3/M1 support the Klipper columns; R1–R3 support RRF; P1–P3/O1–O2 support
slicer columns. The KF column is a **work estimate**, not an existing fork capability.

## When changes belong where

| Approach | What it buys | Smallest missing work / boundary | Disposition |
| --- | --- | --- | --- |
| Vanilla single Klipper | Established one-job kinematics, heaters, multiple MCUs/carriages | Extra MCUs and copy/mirror trajectories do not create independent job state. Macros saving/restoring state do not add concurrent planners | Useful one-region/J executor, not complete S/R/C/M baseline |
| Coordinator + ordinary Klipper instances | Existing independent file, progress and pause/cancel domains | Global admission, objects, transforms, thermal ownership, fault aggregation; MCU/axis handoff and grouped Z remain hard | First investigation, especially H independent-head-Z candidate; not selection of H |
| Klipper extras / upstream extension | Add commands/status, narrowly scoped transforms or interlocks | Internal APIs/version coupling; cannot assume extra virtual_sdcard names isolate gcode_move, toolhead, mesh and pause state | Try bounded extension before core fork when a measured gap is localized |
| Targeted Klipper fork | Potential shared resource scheduler and common clock with independent jobs | Separate parser/modal/extrusion/mesh/file state, planning queues, pause/cancel/fault namespaces and axis arbitration; large regression surface | Only after isolated-executor spike exposes an unavoidable boundary; host-side changes may suffice, MCU fork not automatically required |
| RRF + coordinator | Existing asynchronous movement selection, barriers, axis allocation and limited collision primitives | Two-system compile limit; File2-only reader duplication and shared lifecycle. Four-system work is not a one-constant change | Compare two-queue integration; no-go as a proven four-job drop-in. Multiple RRF controllers are another isolated-executor option with the same group-handoff problem |
| Slicer profile / postprocessor / coordinator | Region shape, ordinary paths, metadata, dispatch | G-code semantic validation and protected start/end/pause routines; versioned exports and independent recipes | Baseline route; no demonstrated engine-fork requirement |
| Slicer engine modification | Potential seam-aware deposition planning or cooperative partitioning | Only needed if new path generation cannot be expressed with ordinary regions or a correct external planner | No-go now; four-head cooperation on one object remains separate unproven stretch work |

RRF's M598 barrier is useful for coordinated phases; inserting a barrier every layer
would violate unrelated job progress. M597 separation checks and M599 tool-reference
keepouts cannot certify whole gantry/harness/finished-object safety. M606 forks the
same stored input; a coordinator may investigate channel streaming or host-managed
lifecycles, but neither proves independent cancellation, buffering or four queues.

## Slicer extension evidence and limits

PrusaSlicer 3.0 alpha12 is the current inspected 3.0 prerelease, superseding the issue's
alpha11 lead. Its multi-bed architecture supports different printer configurations
within a project. This is useful authoring UX, not physical bed recombination or a
multi-job firmware controller. Its Lua API is currently a limited project plugin API,
not a documented general toolpath scheduler. CLI slicing, exported files, external
postprocessing and host-upload adapters are more appropriate integration seams (P1–P3).
Do not assume 2.x scripts/profile schemas work unchanged after the 3.0 refactor.

OrcaSlicer 2.4.2 has per-plate print/config/result objects, printable/excluded regions
and external postprocessing (O2). It also exposes parallel-printhead count settings
(up to four, mentioning OrangeStorm Giga). That is meaningful upstream support to
inspect, but no evidence here establishes unrelated heights, late arrivals or
individual job cancellation through those settings. Start with separate projects or
exports for heterogeneous profiles; do not assume every machine setting can vary per
plate. Existing CLI/config definitions deserve a version-specific export trial, not
an invented stable plugin API. Neither slicer's sequential-object collision checks
replace the coordinator's complete machine swept-volume contract.

No baseline slicer-engine change is identified. A Tesseract upload UI might need an
upstream print-host adapter or GUI extension; that differs from changing slicing.
Seam-specific extrusion/support/infill optimization or cooperative multi-head path
partitioning could require new planning algorithms. A postprocessor is acceptable
only if it preserves extrusion, timing, arcs, coordinate modes and all safety-relevant
paths; regex offsets alone are insufficient. An external planner may still avoid a
fork even for stretch work. No such planner is implemented here.

## Next experiment and decision gates

**Smallest useful next integration:** after separate approval for upstream checkout/
build/runtime, run two ordinary Klipper executors against isolated simulated/debug
MCU outputs, with no physical I/O. Use two different conventional files with unrelated
layer heights and extrusion modes. Start B late, pause/cancel A, then demonstrate B
continues. Capture exact versions, accepted/executed command evidence, shutdown scope,
and distinct file/modal/mesh/heater ownership. Expand to four only after this boundary
passes; passing two does not establish four or resource reassignment.

In the same bounded comparison, use an explicitly async-enabled RRF 3.7.0 software
test target if available (otherwise report unavailable, do not attach hardware).
Exercise queue selection, forked-reader behavior, one blocked/heating stream, M598,
pause/cancel and stream failure. Demonstrate whether an independently arriving file
can be managed without disrupting the other. Retain the two-system limit as a failed
four-job criterion until actual generalized implementation evidence exists. DSF/SBC
and standalone execution must be tested separately if both are candidates.

The decisive second step is an **empty affected-domain S→M12→S ownership handoff**
while jobs on 3/4 continue: no shared MCU reset, no stale command acceptance, no loss
of unrelated calibration/heaters, no ambiguous start replay. H tests bed thermal/
configuration changes with stationary print beds; B also needs one coherent pair-Z
trajectory and fault domain. If this cannot be built with exclusive existing executors,
compare a narrow extension and a shared-scheduler fork against RRF development cost.
Do not select electronics merely to make a premature software topology work.

Acceptance records must separate file-reader progress from motion completion, test
lost acknowledgements and retained occupied objects, and use generated normalized
command traces to compare profile output. Actual PrusaSlicer alpha12 and Orca 2.4.2
export tests should cover all eight arrangements and J seam-spanning paths, including
start/end macros. None of those runtime/export trials was performed in S1.

E1 still owes complete head reach/parks, low/tall/finished-object clearances and shared
XY influence; E2 owes H/B full-stroke support, group-Z error/stop bounds, downstream
restraint/observation and continuously supported conversion. Without these, resource
partitions and fault domains remain assumptions. See [D7](d7-integrated-study.md),
[D8](d8-motion-contract.md), [D9](d9-contract.md) and [D6](d6-scheduling.md).

All requirements remain intact, including printable-first development, Ender 3 part
fit, distinct reproducible imperial/metric reinforcement interfaces, later 2020 edition,
editable parametric sources and both open/enclosed operation with tool-free removable
panels. Panel absence alone is not a protective fault. No physical tests, purchases,
firmware changes, services or new upstream repositories are authorized by this study.
