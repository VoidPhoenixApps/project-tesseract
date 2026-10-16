# D7 — cross-system failure chains

[Overview](d7-integrated-study.md) · [evidence](d7-evidence.md).
These are research obligations and counterexamples, not an approved hazard assessment,
protective design or operating procedure. Severity, exposure, acceptable force/speed,
response time and residual risk require qualified review; no arbitrary risk score is used.

| Trigger → coupled mechanism → consequence | Relevant candidates/modes | Evidence and observable discriminator | Proposed containment to investigate / remaining dependency |
| --- | --- | --- | --- |
| Independent heater temperatures → unequal sheet/plate/frame growth → gap/step/adhesion drift at a locked seam | All candidates in R/C/M/J | Phase 1B .33984 mm center-anchor closure; corner reference reduces one normal term, not tangential mismatch or Z bow. Measure both ends, center crossing, full surface and cold-datum drift | Relieved hot mounts over retained cold supports; no stronger latch, bridge sheet or mid-print carrier repositioning as a cure. Requires actual laminate/friction/thermal evidence |
| Rigid cold tie + independently guided beds + datum error → closed elastic force loop → uplift/binding/nozzle error | E-tie/hybrid, F or C handoff, every paired mode | D3 guide mismatch and D4 negative-reaction example; observe support reactions and six-DOF pose over travel | Explicit released follower freedoms and positive load retention; must preserve moment support after release. A torque tree is not a six-DOF support proof |
| One group drive slips → relative bed step → joined print couples loads → remaining lift overload or collision | B/R, R/C/M/J | Downstream displacement and plane/skew observations, delay and worst stop mismatch; motor encoder can miss belt slip | Group fault domain must retain loads and inhibit unsafe continuation; if bounds cannot localize effect, broader stop. No timing/retention ratings established |
| Selector partially engages or loses power → torque path opens/bridges two outputs → falling platform or opposed drives | R J handoff; unused frame in partial modes | D3 point-path counterexample; continuous wrap/phase/tension plus independent support evidence at every state | Separate independently retained old/new support before unloading/engagement; positive selector remains comparison, not brake. Never rely solely on servo position or motor holding torque |
| Independent heights or finished tall part → low bridge/drop column sweeps across neighbor → collision despite reachable nozzle | H/B/R, especially C/M13/M24 and S | D2 structural clashes; D6 rejects only volumes actually supplied. Observe full swept structures, parks and routes, not nozzle rectangles | Route or architecture change; bounded scheduling may defer transition but cannot replace required independent jobs with permanent lockstep |
| Mirrored inward clearance gain → outward cable/filament/park growth → panel or frame conflict → fatigue or unreachable park | E overlay, all modes | D2 park260 stroke failure and 362 mm hypothetical required half-width; compare complete common/E assemblies with identical functional parts | Separate inward and outward budgets; determine actual stroke/bend/service paths. Removing environmental panels cannot be the workaround for ordinary enclosed operation |
| Longer perimeter arm + soft printed root + chamber warmth → sag/creep → group seam error and resonant coupling | H/B, all modes | D4 .112+.180 mm example; warm load/unload hysteresis, root rotation and frequency response needed | Deep truss/chord vs tube-node comparison with permanent bracing, both stock variants. No beam-only stiffness result validates joints or heat resistance |
| Panel retainer or thermal expansion disturbs primary frame → registration shift or falling panel | All modes/open-enclosed transition | D5 floating-retention and handling studies; measure force/deflection with panel present/absent | Environmental panel must not be required for primary stiffness. Assess handling separately; absence alone is not a protective fault. Genuine hazard-specific protective functions remain |
| Four heaters start + motor holding + enclosure derating → demand/connector temperature exceeds capacity → brownout and lost support/cooling | All, including apparently idle heated beds | D6 hypothetical 880 W peak vs 400 W typical; staged average 646 W is not instantaneous PWM bound | Actual rated/derated power budget, branch protection and fault-independent heater interruption. Falling-load protection must survive supply loss; no selected PSU/wiring |
| Heater output short or sensor detaches → software commands off but energy continues → thermal damage to frame/harness | All candidates and panel states | D5/D6 fault obligations; actual circuit fault analysis, independent sensing/interruption and thermal coast-down | Qualified electrical/thermal review; no controller software test establishes interruption of a shorted device. No active chamber heater approved |
| Job completes/cancels or communications reconnect → occupancy cleared or blind homing → sweep through retained object | Every transition, especially partial→J | D6 retains occupancy and latches fault; real start/end/homing macros and stale geometry still absent | Immutable toolpath/geometry certificate and explicit confirmed removal; no automatic restart from restored power, panel or lock state |
| Transition affects shared guide/support although bed endpoint unchanged → scheduler labels neighbor unaffected → live-job reference moves | R↔C and mixed orientation changes; all J conversions | D3 affected-group closure plus full support influence graph; inspect force paths and cable motion | Define affected by pose, support, reference and group, not XY delta. Only affected empty modules may convert at datum; retained jobs require verified isolation |
| Primary and backup restraint share printed root or heater supply → common failure defeats both → falling load despite two devices | All lifting candidates, service/stop | D4 common-mode warning; map anchors, thermal exposure and energy supplies | Independent failure-path analysis, fault load/impact evidence and maintenance support; E-stop is neither isolation nor automatic safe gravity state |

## Gate interaction and fault scope

A measured good cold dock cannot close the hot-seam gate; a stiff beam cannot close
printed-root creep; a clear endpoint cannot close the path gate; a valid scheduler
reservation cannot close actual geometry; a present panel cannot close a protective
function; and a sensor indicating engaged cannot establish positive load capacity.
Gates therefore form a conjunction, not an additive score that lets a strength cancel
a missing safety function. No shortlist candidate may trade away an unmet mandatory mode.

For group faults, initially assume the mechanical/thermal influence domain may be larger
than the logical job. Local stop is justified only after proving the unaffected job's
support, references, power and clearance remain bounded during detection/arrest. D6's
conservative machine-wide fault model is an algorithmic baseline, not a final E-stop
wiring design. Restart needs actual state and object knowledge plus deliberate reviewed
recovery; homing through an occupied volume is not a valid way to regain confidence.
