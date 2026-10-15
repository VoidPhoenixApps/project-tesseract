# D6 — firmware capability and architecture evidence

[Source ledger and revisions](d6-references.md). **Capability research, not tested integration.**
No firmware was installed, built, cloned, configured or connected to a machine.

## Documented capabilities and limits

| System / evidence scope | Documented capability | What D6 must not infer |
| --- | --- | --- |
| Klipper rolling documentation, pinned upstream identity in ledger | Host look-ahead generates timed step commands; MCU clocks are mapped to print time. Multiple MCUs expand execution and I/O | Extra MCUs, extruders and per-stepper queues do not establish four independent G-code/job lifecycles. A custom host fork or multiple instances would need separate investigation |
| Klipper dual-carriage / generic-carriage configuration | Carriage assignment and copy/mirror facilities; configurable kinematics | Copies/mirrors of one trajectory are not four unrelated objects at unrelated heights/speeds; do not claim all possible custom configurations impossible |
| RepRapFirmware current 3.7.0; commands introduced from 3.5 | M596 selects asynchronous queues (typically two, build-dependent); M606 forks readers of a stored job; M598 is a barrier | These features are meaningful concurrency evidence, but not proof of four separately submitted/cancelled/restarted jobs. Queue count and lifecycle isolation require target-build tests |
| RRF collision primitives | M597 axis-separation constraints; M599 tool-reference keepouts | Neither is evidence of complete 3D gantry, harness, object or transition collision checking |
| LinuxCNC 2.9-series architecture reference | Task/interpreter, motion planner and HAL provide extensible control layers | Independent joints beneath kinematics are not independent print-job interpreters; multi-printer scheduling and heater integration remain development work |

Klipper's documented normal move flow reaches one ToolHead look-ahead path, with scheduled
MCU execution. That supports a centralized coordinated printer and provides extension
points, but a four-job supervisor must also isolate parser modes, origins, extrusion,
mesh compensation, pause state and error handling. Four processes cannot safely command
the same MCU/axis without an explicit ownership and transport design. Source-backed
absence of a complete recipe here is **not** a proof that extension is impossible.

RRF is the closest documented centralized concurrency precedent in this comparison.
Its queue primitives merit a bounded experiment; a forked input file should not be
advertised as independently arriving jobs. The source ledger records retrieval gaps
and version-specific regressions to retest rather than assuming a historical bug still
exists. No exact controller memory/queue configuration is selected.

LinuxCNC is a credible custom-controller reference when low-level integration dominates.
It would add printer-specific lifecycle and heater work, so it is not automatically
simpler than ordinary printer executors. No paid/proprietary runtime is assumed;
board interfaces, real-time platform and downstream licensing still require review.

## Time, buffers and failure boundaries

| Concern | Required comparison / evidence before adoption |
| --- | --- |
| Timebases | A single execution domain can schedule grouped axes against one time reference. B/C independent clocks are acceptable only for truly disjoint reserved envelopes; shared bed-Z requires a bounded synchronization/error argument |
| Buffered commands | Track accepted versus executed sequence numbers and stop acknowledgement. Host send completion and commanded position are not measured motion completion. Cancelling a UI job cannot free space occupied by buffered moves |
| Clock/communication uncertainty | Include clock offset/drift, transport jitter, host scheduling, retries, queue depth, missed heartbeats and power-loss detection. No unbounded TCP/USB/CAN round trip may be assumed suitable for coupled-Z safety |
| Buffer starvation | Stop/hold policy must respect gravity restraint and coordinated group response; do not let one lift exhaust its queue while others continue. Deeper buffering improves continuity but may increase cancellation latency |
| Barrier/deadlock | A barrier waiting for a cancelled/disconnected stream needs defined fault disposition; never wait indefinitely while continuing shared hazardous motion |
| Controller failure | Local output defaults and watchdogs reduce some failures; shared supply, host, bus or sensor faults defeat simplistic isolation. Fault the complete mechanical influence domain; conservative fallback is machine-wide inhibit |
| Extensibility | Version pinning, reproducible builds, public tests, documented adapters and upstream compatibility must be evaluated. A private patch or unavailable OEM specification cannot become an invisible dependency |

Klipper documents multi-MCU homing communication checks over 25 ms, with predictable
low latency needed and same-axis multiple steppers constrained to one MCU for this
feature. At 10 mm/s, 25 ms corresponds to 0.25 mm travel; it is not a Tesseract safe
stop bound. The illustrative `v*t` output in D6 excludes braking, compliance and gravity.
For a real stop, a first screening relation is `d = v*T_detect+transport+actuation +
v²/(2*a_stop) + uncertainty`, valid only where that deceleration is physically available.
Vertical load support needs its own analysis.

Ordinary heater watchdogs do not interrupt a shorted output device. RRF 3.7 M959 documents
expansion connection supervision and heater-off behavior after lost synchronization;
its default timeout is 10 s and configurable minimum is 3 s. Such protocol behavior
cannot establish collision-stop or gravity-restraint response times. Reconnect must not
restore Tesseract motion/heating authority automatically.

## Minimum proposed executor contract

Each job needs a unique ID, configuration epoch, coordinate/mesh revision, resource
set, swept-volume revision, temperature recipe, allowed power envelope and immutable
input hash. Executor replies must identify epoch, job, accepted sequence, executed
sequence, current health and timestamp; a duplicate command must not execute twice.
Prepare all resource reservations before commit; abort an incomplete prepare without
motion. On uncertain commit/acknowledgement, retain reservations and inhibit rather
than resend an ambiguous start. Local executors need a bounded authorization lifetime
with a reviewed stopping strategy before expiry; revocation is not instantaneous.

After disconnect, reject stale epochs and require fresh position/support evidence,
review of remaining objects, explicit reset and a new admission. Global re-homing or
re-calibration cannot be smuggled into an individual job's start macro while another
job occupies the shared sweep. These are proposed requirements; the D6 model does not
implement a distributed transaction protocol or parse G-code.
