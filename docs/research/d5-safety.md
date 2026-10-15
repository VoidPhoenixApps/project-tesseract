# D5 — safeguarding and fault-state register

**Research obligations, not an approved protective implementation or safe-use procedure.**
Qualified mechanical, electrical/thermal and controls/safety review is required before
physical adoption. Standards/public guidance in [S1–S5](d5-references.md) supply review
scope; no clause-level compliance, jurisdiction determination or certification is claimed.

## Open-air requirement versus protective function

The maintainer intends ordinary open-air RepRap printing with environmental panels
removed, retaining all eight required modes. Panels primarily control thermal/environmental
conditions. Installing one does not make it a protective guard; its absence does not by
itself require an interlock, create a protective fault or prohibit printing. Tool-free
installation/removal without dismantling primary systems remains mandatory.

Accessible belts, moving heads and hot surfaces do not automatically mandate full
guarding. Existing open-frame printers are relevant precedent, not evidence that every
Tesseract hazard is acceptable. A documented hazard-specific risk assessment must identify
exposure, severity, likelihood, operating conditions and residual risk, then justify the
necessary protective functions. Barriers, sensors and interlocks remain candidates where
that assessment supports them; none is selected by this study. Assess inherently safer
geometry, force/speed limits, localized protection and information for use as appropriate;
no measure is automatically sufficient or categorically excluded without its risk basis.

| Activity | Interpretation / evidence needed |
| --- | --- |
| Ordinary open-air printing | Preserve all required modes and independent jobs. Assess ordinary accessible motion and hot surfaces without presuming a perimeter guard or zero residual risk |
| Automatic docking/reconfiguration | Separately assess closing bed gaps, locks, unexpected motion, flexing heater wires and occupied neighbors; retain fixed-datum horizontal motion and supported load transfer |
| Environmental-panel removal/reinstallation | Assess hand/panel paths, falling or hot panels and interference with motion. Define conversion conditions from those hazards; removal is not automatically service isolation or a protective fault |
| Access through an actual protective guard | Where risk assessment assigns a protective function, define its access response, sensing/interlocking and stopping requirements. Do not bypass that function for open-air operation |
| Maintenance/service | Prevent motion and unexpected restart; isolate relevant energy and independently restrain gravity/stored energy before service. A panel opening or software pause is not isolation |

Electrical covers, necessary load restraints and justified heater/fault protections must
remain effective in either enclosure state. In particular, assess falling Z loads,
transmission disengagement, insufficient restraint, exposed terminals and heater faults;
ordinary printer precedent does not resolve these Tesseract-specific mechanisms.

If a proposed environmental panel is also assigned an essential protective function,
record that assignment explicitly and provide a reviewed means of retaining the function
in open-air mode. Do not silently delete open-air capability or defeat a necessary
interlock. Panel conversion may require a reviewed stopped/cooled condition because of
its handling or access hazards; that does not prohibit ordinary open-air printing or
require panel removal for automatic bed configuration changes.

## Fault and service register

All rows remain open pending evidence. “Required behavior” is a proposed safety obligation
to review, not implemented logic. Response timing, stopping distance and risk reduction
requirements are unselected; a successful software test would not close these rows.

| ID / event | Hazard and affected state | Required behavior / possible controls to evaluate | Evidence before adoption |
| --- | --- | --- | --- |
| F1 environmental panel removed/released | Handling may introduce a falling panel, hot grip or collision with motion; absence alone is not a protective fault | Assess conversion paths and conditions separately from ordinary open-air printing. No automatic interlock requirement; preserve every mode and necessary protection | Panel/hand sweep, retention, temperature and handling assessment; justify any stopped/cooled conversion condition |
| F1a actual protective guard opened / protective function lost | Access to a specifically assessed hazard, including a dual-role panel only if explicitly assigned that function | Prevent hazardous continuation/restart as required by the assessed function; consider interlocking or guard locking where justified. Preserve equivalent protection in open-air mode | Documented function assignment, access/stop performance, fault response and guard strength; no protective credit from panel presence alone |
| F2 one retainer/support fails | Falling sheet, sharp fragments, inward strike, exposed hazard | Positive retained support and secondary capture where justified; detect/inspect failed engagement; do not rely on magnetic attraction or equal load sharing | One-failure load/rotation analysis, edge retention, cyclic vibration and hot/dirty tests |
| F3 hotend/bed or grip accessible | Burns persist after heaters disabled; hot panel bends during handling | Assess contact exposure and justify measures for each surface/task, including localized protection where needed, handling conditions, residual-heat information and cooling procedure; no blanket hot-zone guarding mandate | Surface/radiant temperature maps, contact duration, uncertainty, cooldown and reachable areas; evidence that the combined measures adequately reduce the identified risk |
| F4 presence/access sensor stuck/spoofed | Incorrect environmental status, or lost protection only where an assessed protective function depends on the sensor | Separate environmental/recipe status from protective status; presence does not prove latch engagement. Diagnostics and fault response follow the assigned function | Open/short/stuck/misaligned/foreign-magnet cases; independence and demand tests where protection is assigned; no universal panel-sensor requirement |
| F5 service with unintended restart | Remote queue, homing or recovery starts while hand/tool inside | Isolation against restart, verified energy state and independent gravity support; maintenance is not a firmware pause | Reviewed isolation procedure, stored energy inventory and verification; all command sources considered |
| F6 heater/sensor fault | Stuck-on switching, detached sensor or misleading air reading overheats structure | Review independent overtemperature/heater-energy interruption and fault latching; chamber sensor cannot substitute for heater fault protection | Fault injection plan, thermal runaway and sensor-placement analysis, qualified electrical/thermal review |
| F7 mains/DC wiring fault | Shock, fire, metal panel energization, abraded wire or hot connector | Fixed protected terminals/compartment, strain relief, bonding where applicable, overcurrent/thermal protection; do not remove these with wall | Wiring design, component ratings/derating, fault-current/bonding review and inspected routing in every pose |
| F8 E-stop | Stopping hazard may release gravity restraint or leave hot components | Defined safe stop by energy domain; maintain necessary passive support and protective functions. E-stop not isolation and not a fire-containment promise | Failure of supply/drive, restraint independence, residual heat, reset without restart and accessible controls in both states |
| F9 power loss/brownout | Lift/platform drops, panel unlocks, cooling stops | Retain gravity loads independently of drive torque; assess power-to-lock/unlock consequences and controlled access | D3/D4 support-loss analysis, guard state, restart state and thermal coast-down evidence |
| F10 interrupted operation/recovery | Unknown panel/lock/bed state, object collision on homing | No automatic motion merely on power restoration or latch closure; verify actual state, affected objects and deliberate restart readiness | Recovery scenarios across eight modes, failed references and occupied beds; no unsafe automatic reconfiguration |
| F11 jammed/hot/distorted panel | Excessive pull causes drop, sudden release or frame disturbance | No forceful release into hazards; support and safe cooldown/isolation before recovery; maintainable capture | Hot/cold/dirty force and displacement distributions, wear inspection and replacement criteria |
| F12 stored energy during service | Gravity bed/platform, tensioned belts/springs, capacitors, hot plates | Identify, isolate, dissipate or independently restrain each energy source before access; wall never a restraint | Service load path, verified support, discharge/cooldown and access procedure |
| F13 emissions/sealing failure | Particle/gas exposure, accumulation released when opened; hot spots | Review emissions controls for both panel states and each material recipe; no unventilated/unattended claim | Capture/leakage and exposure assessment, future filter/exhaust selection/replacement review |
| F14 thermal drift/creep | Panel jams or pops; joint relaxation changes head/bed alignment | Floating retained interfaces, independent frame integrity and warm inspection criteria | Time/temperature/load evidence for actual printed joints, seals, magnets and all variants |

## Interlock and status-sensing alternatives

These alternatives apply only where the hazard assessment or a separately defined
operational need justifies them. Environmental-panel absence alone selects none of them.

| Strategy | Potential use | What prevents treating it as approved protection |
| --- | --- | --- |
| Ordinary microswitch, reed/Hall or optical presence sensor into controller | Convenience UI status, logging, recipe inhibit | Spoofing, obstruction and common controller faults; closed signal does not prove every latch captured. No safety credit assumed |
| Mechanically actuated protective interlock | Physical actuation can couple guard position to protective circuit | Mounting, actuator defeat, fault detection and complete safety function require review; no part/controller selected |
| Coded noncontact protective sensor | Can distinguish actuator identity and tolerate some alignment variation | Coding does not ensure retained panel or correct safety logic; evaluate fault coverage, reset and failure independence |
| Guard locking / monitored latch | Could prevent opening until hazardous motion has ceased | Power-loss behavior, escape/service release, heat remaining and lock-force proof; convenient hand conversion still required once safe |
| Separate protective control path with monitored outputs | Potential separation from printer scheduling | Required integrity, architecture, diagnostics, common-cause faults and validation unspecified; software-only monitoring is insufficient evidence |

Necessary protection means keeping primary load restraints, electrical covers
and hazard-assessment-justified protective functions effective in both panel states.
A status LED, temperature display, alert or convenient presence sensor is optional assistance unless a qualified design
assigns and validates a protective function. Emergency stop, isolation and normal pause
are distinct functions; none grants permission to reach a stored-energy hazard.
