# D1 — failure modes, support and recovery

**Preliminary hazard identification, not a reviewed hazard assessment or permission
to operate hardware.** [Study](d1-engineering-study.md) / [diagrams](d1-diagrams.md).
Severity/frequency scores and acceptance limits are deliberately unassigned: no component
reliability, stored-energy envelope or validated protective system exists.

A **bed-position lock** retains registration, a **structural load-bearing joint** carries
specified forces/moments, and a **drive-transmission coupling** transfers actuator torque.
A device may fulfill several functions only after each is sized and verified separately.
Neither “locked” nor “servo at target” establishes all three. Motor holding torque is not
passive fall protection; screw self-locking and a clutch's holding behavior need evidence.

| Initiating fault / affected concepts | Consequence | Proposed prevention/detection, still requiring design review | Required stop/recovery evidence |
| --- | --- | --- | --- |
| Half-engaged/misphased coupling, E/F | Tooth damage, slip, step in seam, asymmetric lift | Supported unloaded alignment; positive retained engagement; direct engagement sensing plus actual output-position plausibility; inhibit torque on disagreement | Hold group through independent restraint, isolate failed path; recover only after support and phase established; no blind retry |
| Belt slack/skip/break or F switch power loss | Local or whole frame drops; hot part/nozzle collision | Restraint independent of switched/broken belt; tension/engagement design; output/carrier monitoring rather than only motor encoder | Measure stopping/catch displacement and impact at worst payload and direction; preserve support in every intermediate selector state |
| One motor stalls/loses steps, B/E/F partial | Bed skew tears seam-spanning part or overloads guides | Measure relative carrier plane/height with enough independent observations for tilt; bound skew rate and detection latency | Stop all mechanically joined supports coherently without increasing skew; restrain gravity; inspect part/support before rehome |
| Common gantry/trim failure, A/C/D | Head drops, strikes tall object or runs out of trim | Independent gravity retention where needed, travel/range supervision and entire beam envelope | Stop affected collision domain, not just extruder; verify coordinate validity and clearance before any restart |
| Rigid guide/cross mismatch or thermal binding, E/F/C | Internal load, warp, step changes, lost travel | Exact-constraint review, suitable compliant/relieved freedoms, thermal map and reaction/load checks; current rise alone cannot identify cause | Inhibit further driving into bind; keep gravity restrained; do not force disengagement of a loaded jam |
| Position lock seated but no structural support, all | Misleading ready state, bed tips or settles under print | Separate sensing/verification of P/L/T functions; eccentric-load analysis and retention against uplift | Prove support with intended force/moment envelope; no motion based solely on latch switch |
| Unexpectedly occupied bed or stale job map, all | Reconfiguration into existing object, head/bed collision | Trusted occupancy reconciliation beyond queue metadata; inspect actual state, sheets and detached parts; reserve full swept obstacles | Reject affected transition; preserve unaffected active jobs where independent isolation is proven; uncertainty cannot default to empty |
| Parked head/beam or unequal-height object omitted, all | Nozzle/body/gantry collision during print or recovery | Full 3D geometry plus stopping/uncertainty clearance; dynamic object volumes transformed with bed Z; parked structures included | Fault-injection trajectory review; no generic lift/rehome unless swept recovery path is clear |
| Encoder/endstop/lock sensor stuck, disconnected, false positive | Unsafe state accepted; delayed loss of support detection | Plausibility, independent observations and failure diagnostics; sensing motor motion alone misses downstream failure | Demonstrate fail response to each sensor fault and common supply/communications loss; no safety-integrity rating claimed |
| Heater wire fatigue, pinch, strain-relief failure, bed motion | Short, open thermistor, uncontrolled heating, exposed conductor | Independently reviewed power/protection, cable temperature/current/bend ratings and full XYZ routing; strain relief and service isolation | Test reviewed heater fault response and power isolation; retain needed cooling if justified; no electrical ratings selected |
| Emergency stop / loss of power, all | Active brake torque/cooling disappears; falling load or thermal hazard persists | Define energy-specific safe state: prevent hazardous motion, retain gravity, isolate heater energy through reviewed means; avoid relying solely on firmware | Verify stop latency/distance, restraint and restart interlock under worst load/temperature; power return does not authorize motion/heating |
| Maintenance with stored gravity/belt energy, all | Crush/pinch while drive or joint removed | Positive service supports, energy isolation and verification; removable panels cannot serve as assumed structural supports | Competent service procedure and access review; never remove a loaded coupling or treat a software pause as isolation |

## Support invariant and fault tree

At every transition state, each carrier must have a defined path capable of carrying
its gravity and moment loads to ground, including one relevant failure of the candidate
transfer mechanism. This is a **design objective**, not a single-fault safety claim.
Quantitative force capacities and the necessary independence/redundancy are unresolved.

```text
 Uncontrolled bed lowering
   OR: belt/shaft/support failure without independent restraint
   OR: old path released before new path carries load
   OR: false engagement accepted + gravity restraint released
   OR: two incompatible paths bind, then one releases abruptly
   OR: power loss defeats both active drive and active-only restraint
```

For J a common frame reduces some differential-motion terms but introduces common
support failure and torsional compliance. For R/C/M, faults within a mechanically
connected group require coordinated arrest; sharing a gantry/rail/power domain can
force a wider stop. Preserving independent printing does not justify allowing hazardous
motion after a fault. Conversely, routinely pausing other jobs to compensate for an
inadequate mechanism is not evidence of required independent job progression.

## State and sensing obligations before later testing

Record actual carrier position/tilt, group membership, P/L/T state, motion ownership,
occupied volume, bed temperature state, restraint state and valid reference status.
A rebooted controller cannot reconstruct those facts solely from the last command.
After an ambiguous fault, keep support, isolate hazardous energy, inspect actual
mechanical state and choose a collision-free recovery procedure. Rehoming a tilted
bed carrying a joined part may itself destroy the part or mechanism; recovery may
require supervised removal under a reviewed safe procedure.

A future procedure must set measurable limits for seam step/tilt, lift deflection,
engagement, belt tension/wrap, restraint holding/impact, temperature, stopping distance
and sensor latency, together with uncertainty and abort conditions. The illustrative
numbers in [calculations](d1-calculations.md) do not supply those limits. Qualified
mechanical, thermal/electrical and controls/safety review remains required before
adoption or operation. The first physical proof remains the separately authorized
two-bed docking and cross-seam rig, not a switched four-bed prototype.
