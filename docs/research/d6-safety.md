# D6 — protective functions and fault-response requirements

**Proposals for qualified review, not an electrical design or certified safety system.**
No safety integrity level, performance level, stop category or numeric response time is
assigned. Ordinary printer firmware and the D6 Python model receive no independent
protective-function credit. [Sources](d6-references.md) and [D5](d5-safety.md) bound context.

## Distinct functions

| Function | Intended role | What it cannot establish |
| --- | --- | --- |
| Firmware monitoring | Detect temperature range/rate, communication or driver errors and request a defined stop | Independence from common controller/output/sensor failures |
| Operational pause/cancel | Controlled production stop, retain objects and resources, choose reviewed heat disposition | Emergency protection or safe access to hazardous energy |
| Emergency stop | Complementary protective response selected from actual hazards; stop hazardous motion/energy without creating worse gravity/thermal hazards | Routine guarding, maintenance isolation or automatic restart permission |
| Independent protective functions | Detect relevant faults and interrupt/control energy through reviewed independent paths; monitor final switching/retention where needed | Safety merely from adding a relay, watchdog or second processor |
| Maintenance isolation | Isolate energy, prevent reconnection, restrain gravity/stored energy, verify absence/cooldown before access | A UI service mode, software disable or open removable panel is insufficient |

HSE maintenance guidance explicitly includes isolation against reconnection and support
of parts that could fall. This is a useful engineering reference, not a determination
of jurisdiction or Tesseract compliance. Full applicable standards and qualified review
are still needed. Removing torque from Z may cause a drop; a brake upstream of a failed
belt may not retain the load. Analyze where restraint acts and what remains supported.

## Fault-response register

Responses are requirements to design and verify, not instructions for energizing equipment.
Fault scope is the complete mechanical, thermal and electrical influence domain. A local
job may continue only if independence is demonstrated; default uncertain scope is global.

| Fault | Required response / inhibited actions | Evidence and unresolved implementation |
| --- | --- | --- |
| Heater output stuck on | Independent energy interruption; latch, inhibit heating/restart, manage retained heat | Detect excess temperature/current despite command off; independent sensor/limiter and final switch failure analysis; no selected device |
| Temperature sensor open/short | Detect range/plausibility fault; remove affected heat authorization; expand scope for group/shared enclosure risk | Also test detached sensor and in-range stuck/bias faults; redundant observations must not share the same unexamined failure |
| Control communications lost | Inhibit new commands, expire authority and execute reviewed bounded local stop; retain occupancy and unknown position | Maximum delay includes watchdog, buffers, output action and mechanics; bus reconnect is not reset |
| Host/controller lockup | Independent watchdog/protective path and suitable local defaults | Fault injection across CPU stall, timer failure, frozen output and common power; firmware watchdog alone is insufficient |
| Brownout / restored power | Restrain gravity through loss; outputs boot inhibited; reject stale epochs; no automatic job resume or heating | Supply sequencing, output glitches, contactor dropout and brake timing under undervoltage; retained objects block blind homing |
| Driver fault / stalled axis / missed steps | Stop affected coupled motion domain; invalidate position; retain/support load | Motor encoder/step count can miss downstream slip; actual bed/head pose and seam skew need observations |
| Structural/position lock fails | No transfer/reconfiguration/start; if running, protective response with independent support | Lock command or switch alone does not prove engagement, strength, preload or datum; prove sensor mounting and diagnostic coverage |
| Selector partly engaged / two owners | Inhibit torque transfer until supported, phase/engagement established; prevent fighting drives | D3 handoff and downstream restraint, not just an exclusive software lock |
| Emergency stop | Hazard-based stop and energy handling, latched; deliberate reset does not restart | Response under every mode, load, single relevant fault and loss of power; retaining gravity may require independent mechanical means |
| Guard/service access or panel removal | Stop/inhibit access-affected hazards; establish maintenance isolation as applicable | Both open-air and enclosed modes need a valid safeguarding concept; never bypass protection to satisfy open-air requirement |
| Overtemperature in electronics / fan loss | Remove relevant heat/motion authorization while preserving required support/cooling | Local sensor locations, driver/connector/printed-joint temperatures, fan diagnostics, thermal inertia and D5 limits |
| Sensor stale/contradictory/unavailable | Treat state unknown, reject admission/transition, latch running-state fault as appropriate | Timestamps, wiring faults, clock resets, spoofed/replayed data and disagreement; software truth value is no physical evidence |
| Job cancel / barrier failure | Clear no physical occupancy until actual stop/removal; bounded handling of waiting peers | Independent lifecycle semantics and queued/executed distinction; no indefinite hazardous wait |
| Scheduler wrong / geometry changed | Independent reviewed protective measures remain effective; revoke stale plan and inhibit | Input hashing/versioning, parser coverage, uncertainty and configuration epoch; software collision model cannot be sole protection |

## Required verification before adopting protective functions

Qualified electrical, controls/safety and mechanical reviewers must establish a hazard
assessment, safe state per fault and mode, required risk reduction, independence/common
cause analysis, maximum allowed response/skew/temperature, and diagnostic coverage.
Specify measured acceptance limits with uncertainty, test revisions/conditions, supervision
and abort criteria before testing. Evaluate reset, recovery, restart and service with
objects present, not only an empty cold machine. Include loss of power mid-handoff,
failed downstream transmission, welded heater switch and failed support indication.

The current task performs none of that physical verification. No protective function,
unattended readiness, legal compliance or safety certification is claimed.
