# D6 — conditional channels, power and distribution study

**No motor, heater, board, PSU, voltage, wire gauge, fuse or protective circuit selected.**
[Source ledger](d6-references.md) · [fault requirements](d6-safety.md).

## Parameterized channel inventory

Let H=4 physical heads; x=2 XY drive channels/head as an illustrative Cartesian/CoreXY
case; e=1 extruder/head; z_h=1–3 Z drivers/head in Z-A; z_b=1–3 local Z drivers/bed in
Z-E/F. These are sensitivity counts, not chosen mechanisms. Let r=number of horizontal
reconfiguration drives; s=powered selector channels; b=restraint/brake outputs;
l=position/structural lock outputs; f=secondary-frame lift drivers. A pneumatic/solenoid
actuator uses a suitable output/valve rather than a stepper channel. Multi-motor axes
may need multiple independent drivers even though they share one logical coordinate.

| Channel class | Z-A head/gantry Z | Z-E grouped bed Z | Z-F retained group lifts plus secondary frame |
| --- | --- | --- | --- |
| XY drivers, illustrative | 4x = 8 | 8 | 8 |
| Extruder drivers | 4e = 4 | 4 | 4 |
| Printing-Z drivers installed | 4z_h = 4–12 | 4z_b = 4–12 for retained local drives; mechanical master variants need their own inventory | 4z_b + f; never delete local partial-mode lifts merely because J has one frame |
| Illustrative motion subtotal | 16–24 | 16–24 | 16–24 + f |
| Reconfiguration motor drivers | +r | +r | +r; frame parking/selector drives counted separately if motorized |
| Selectors / brakes / locks | s + b + l suitable outputs, possibly zero selectors | s + b + l; distinct engagement and load restraint | s + b + l plus secondary support/retention and handoff feedback |
| Heater outputs | Four bed + four nozzle = 8 | 8 | 8; fewer active heads do not remove installed circuits |
| Primary temperature inputs | At least 8 for those independent loops | 8 | 8 |
| Additional monitoring | Independent overtemperature/current/ambient channels per reviewed fault architecture, count unresolved | Same; group differential/surface observations added | Same plus platform/handoff observations |
| Head fans | Up to 4 hotend cooling + 4 part cooling = 8 outputs if independently controlled | Same | Same |
| Other fans | Electronics/PSU/optional extraction cooling, count and power unresolved | Same | Same |
| Position / homing | Illustratively 8 XY + 4 Z home observations; extra limits/independent motor leveling increase count | 8 XY + 4z_b or other measured plane scheme; not necessarily one pin per observation | Z-E plus frame reference and retained-park feedback |
| Bed transport / docking | r reference observations plus 4 bed pose/readiness records; at least one sheet-readiness assessment per bed | Same, plus independent group plane/tilt and slip observations | Same plus load-transfer and unused-drive isolation |
| Lock feedback | Separate positional versus structural engagement observations at each implemented joint; channel count depends on diagnostic design | Same; drive selection is a third distinct state | Same; old/new support confirmation during handoff |
| Guards / stop / isolation | Guarded access zones, emergency-stop inputs, output feedback, reset and isolation indication per safety review; no single-input sufficiency claim | Same | Same |

Counts describe installed channels, not simultaneous axis DOF: group progress is 4/2/3/1
for S/R-or-C/M/J. Even if two mechanically linked lifts share one master motor, each
bed still needs guide/load support and downstream condition evidence. Conversely,
multiple drivers sharing one trajectory do not create multiple independently scheduled
jobs. Three non-collinear surface observations can describe a plane in an ideal model;
thermal bow and local sheet slip need more than that ideal plane fit.

As a deliberately hypothetical example with one Z driver per head/bed, r=4 and f=2:
Z-A and Z-E have 20 motion drivers including extruders and reconfiguration; Z-F has 22.
Selectors, brakes and locks remain **additional** outputs, not zero by omission. These
counts cannot select a board without step-rate, current, heat, I/O and bus-load evidence.

| Control placement | Board/link budgeting obligation |
| --- | --- |
| Centralized | One coordinator plus enough driver/heater/I/O capacity, possibly expansion boards; count channels by exact ratings and firmware limits rather than one large-board assumption |
| Distributed | Illustratively four region executors plus shared-resource authority; shared supply and protection remain. A shared host for four instances creates a common failure domain |
| Hybrid | Logical admission service plus independent executors and separately reviewed protective functions; roles may share or separate hardware only after failure analysis |

CAN/CAN-FD expansion, USB/serial and Ethernet are possible communication classes, not
interchangeable protocols. Check termination, isolation, cable lengths/flex, bus loading,
priority, clock synchronization, recovery and address/version management. Ordinary
network commands are not an independent protective stop circuit. No board count is final.
Prefer documented replaceable drivers, sensors and common connectors with explicit
ratings and public configuration/build support; current market availability still
requires exact manufacturer/distributor evidence at future component selection.

## Power sensitivities

All numerical inputs below are **hypothetical**, not selected heater specifications or
measurements. Four beds at P_b, four nozzles at P_n; assumed aggregate driver DC demand
P_m=120 W (includes all enabled motion/holding), auxiliaries P_a=40 W, optional future
accessory P_x=0 W. No active chamber heater approved. Bed typical duty d_b=.35; nozzle
duty d_n=.30. Actual duty depends on temperature, enclosure, airflow and material.

`P_peak = 4 P_b + 4 P_n + P_m + P_a + P_x`

`P_typical = 4 d_b P_b + 4 d_n P_n + P_m + P_a + P_x`

`I_DC = P_peak / V_DC`; `P_AC_real = P_peak / efficiency`.

| Assumed bed W each | Nozzle W each | Concurrent peak DC W | Typical DC W | Peak at hypothetical 24 V A |
| --- | --- | --- | --- | --- |
| 80 | 60 | 720 | 344 | 30.00 |
| 120 | 60 | 880 | 400 | 36.67 |
| 180 | 60 | 1120 | 484 | 46.67 |

At 90% assumed efficiency, the middle case needs 977.78 W real AC input at its peak;
this is **not** branch-circuit sizing. Power factor, inrush, supply tolerance, leakage,
startup, derating, continuous-load rules and other circuit loads need separate review.
At 48 V the same assumed wattage halves bus current, but requires compatible actual
heaters/drivers/protection; this arithmetic does not approve 48 V. Motor winding current
is not DC supply current: chopper operation, torque/speed, losses, holding and regeneration
must be considered. Exact demand and transient voltage remain unknown.

Staged startup example: one 120 W bed at full power while three hold at assumed .35 duty,
all four 60 W nozzles at full power and 160 W fixed load gives **646 W**, compared with
880 W concurrent startup. This is an average holding assumption: asynchronous PWM peaks
can still coincide. A real bounded power scheduler must enforce instantaneous aggregate
allocation, preserve temperature quality and detect failure; simply delaying start times
is not a protective current limit. In a cold enclosure all beds may demand full power
longer, and duty assumptions cease to apply. Do not accept a job using average load when
its reserved concurrent peak exceeds capacity.

For a hypothetical derated DC capacity C=1000 W, peak headroom for the rows is 280/120/−120 W.
That capacity is an input, not a selected supply. Manufacturer LRS-600 documentation is
only a technical example that rated output, inrush, operating conditions and temperature
/line-voltage derating differ; its ratings are not adopted for this machine. A fuse
protecting wiring does not implement job power allocation or detect all heater failures.

## Electrical design questions before component selection

- Classify supply isolation and accessible conductive parts; establish protective-earth
  bonding where required, including continuity across removable parts and flex joints.
  Do not assume plastic structure eliminates bonding or that DC negative is protective earth.
- Split heater branches with coordinated protective devices sized to actual wire,
  connector, switching-device and fault-current limits; protect shared feeders as well.
  Define independent heater energy interruption for a welded/shorted output.
- Separate mains, heater-current, motor and low-level sensor routes; plan strain relief,
  flex-rated wire, bend radius, abrasion/pinch protection, service loops and connectors
  for the full XYZ/reconfiguration sweep. No wire gauge or connector rating invented.
- Review contact temperature, bundled-conductor and enclosed-compartment derating,
  switching transients, backfeed between supplies, stored charge and motor regeneration.
  Keep accessible service areas segregated from energized terminals.
- Document conductor identities, board revisions, protective devices, disconnects,
  grounding and replacement limits in a later wiring/BOM package. Required qualified
  electrical/controls review precedes construction or protective-function implementation.
