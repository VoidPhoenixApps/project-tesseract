# D5 — safeguarding and fault-state register

**Research obligations, not an approved protective implementation or safe-use procedure.**
Qualified mechanical, electrical/thermal and controls/safety review is required before
physical adoption. Standards/public guidance in [S1–S5](d5-references.md) supply review
scope; no clause-level compliance, jurisdiction determination or certification is claimed.

## Open-air requirement versus protective function

Environmental panels may stabilize temperature and reduce drafts. Protective guards
prevent access/contact/ejection hazards and require their own evidence. A removable wall
cannot be both the sole essential guard and simply absent during unrestricted open-air
printing. Candidate resolutions, all unproven:

1. Permanent localized protection around drives/pinch points and electrical parts,
   leaving environmental panels independently removable. Assess head/bed reach and hot
   surfaces that local guards do not cover; open-air access must not remain hazardous.
2. A separately reviewed ventilated protective barrier or perimeter arrangement that
   stays effective in open-air mode. It must preserve all eight modes and practical
   service, not become an undocumented replacement enclosure or physical restriction.
3. Additional protective measures based on a complete risk assessment, with demonstrated
   stopping/access performance. Reduced speed or a warning alone is not credited as a
   solution; a mode that cannot perform required independent jobs fails compatibility.

If none can preserve protection and the required capabilities, escalate the conflict for
requirements/architecture review. Do not silently delete open-air printing or defeat an
interlock. Panel conversion can be limited to an established safe state; this does not
require panel removal for automatic bed configuration changes.

## Fault and service register

All rows remain open pending evidence. “Required behavior” is a proposed safety obligation
to review, not implemented logic. Response timing, stopping distance and risk reduction
requirements are unselected; a successful software test would not close these rows.

| ID / event | Hazard and affected state | Required behavior / possible controls to evaluate | Evidence before adoption |
| --- | --- | --- | --- |
| F1 panel removed/released during motion | Reach into head/gantry, pinch or hot zone; panel may fall inward | Protection remains effective in each operating mode; if protective function is lost, prevent hazardous continuation and restart. Assess guard locking if stop is slower than access | Measured total stop/access time, fault displacement, guard strength, intentional/accidental removal and independent-job effects |
| F2 one retainer/support fails | Falling sheet, sharp fragments, inward strike, exposed hazard | Positive retained support and secondary capture where justified; detect/inspect failed engagement; do not rely on magnetic attraction or equal load sharing | One-failure load/rotation analysis, edge retention, cyclic vibration and hot/dirty tests |
| F3 hotend/bed or grip accessible | Burns persist after heaters disabled; hot panel bends during handling | Protected hot zones, deliberate safe conversion state, residual-heat indication plus verified cooling procedure; review touch limits by material/contact duration | Surface/radiant temperature maps, uncertainty, cooldown curves and reachable areas; indication alone not credited as protection |
| F4 panel presence sensor stuck/spoofed | False closed state enables hazardous motion | Distinguish panel presence from full latch engagement; review diagnostics, defeat resistance, fault response and common causes | Open/short/stuck/misaligned/foreign-magnet cases, channel independence and demand tests |
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

| Strategy | Potential use | What prevents treating it as approved protection |
| --- | --- | --- |
| Ordinary microswitch, reed/Hall or optical presence sensor into controller | Convenience UI status, logging, recipe inhibit | Spoofing, obstruction and common controller faults; closed signal does not prove every latch captured. No safety credit assumed |
| Mechanically actuated protective interlock | Physical actuation can couple guard position to protective circuit | Mounting, actuator defeat, fault detection and complete safety function require review; no part/controller selected |
| Coded noncontact protective sensor | Can distinguish actuator identity and tolerate some alignment variation | Coding does not ensure retained panel or correct safety logic; evaluate fault coverage, reset and failure independence |
| Guard locking / monitored latch | Could prevent opening until hazardous motion has ceased | Power-loss behavior, escape/service release, heat remaining and lock-force proof; convenient hand conversion still required once safe |
| Separate protective control path with monitored outputs | Potential separation from printer scheduling | Required integrity, architecture, diagnostics, common-cause faults and validation unspecified; software-only monitoring is insufficient evidence |

Mandatory mechanical protection means keeping primary load restraints, electrical covers
and any necessary physical hazard barriers effective. A status LED, temperature display,
alert or convenient presence sensor is optional assistance unless a qualified design
assigns and validates a protective function. Emergency stop, isolation and normal pause
are distinct functions; none grants permission to reach a stored-energy hazard.
