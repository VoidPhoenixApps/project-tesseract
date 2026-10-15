# D4 — risks and negative results

Preliminary desk register, **not an approved hazard assessment**. No probability,
severity score, structural rating or operating limit is assigned. [D1](d1-failure-study.md),
[D2](d2-engineering-study.md), [D3](d3-failure-study.md) and Phase 1B/1C failures persist.

| ID | Failure or negative evidence | Consequence / research response |
| --- | --- | --- |
| F1 | Soft printed root dominates a stiff tube; example .18 mm joint versus .112 mm member motion | Member-only rankings mislead. Obtain measured rotational stiffness, hysteresis and preload retention before choosing topology |
| F2 | Shallow printed V-truss amplifies load to 304 N per bar; degraded-E/K=2 Euler reference about 178 N | Soft-joint cases also extrapolate sag to 75–80% of rise, outside linear geometry even without Euler exceedance; geometric softening/snap-through is unmodeled. Linear small-deflection solution does not describe stable operation. Increase depth/bracing or revise member; no safety factor/capacity established |
| F3 | Rigid hybrid with .2 mm hypothetical datum mismatch gives -33.3 N reaction | Unilateral contact opens or a hold-down is loaded; guide binding/servo fighting possible. Specify freedoms and contact model, not simply larger motors |
| F4 | One independent support lost with no tie has singular vertical model | Unsupported bed/head. Separate passive restraint and common-mode root/node failures require review; tied static case does not prove dynamic arrest |
| F5 | One brace missing/slack, especially tension-only diagonal under reversed load | Frame may become a mechanism; analyze three-dimensional restraint and reversed loads with panels absent |
| F6 | Printed joint preload relaxes or tube clamp ovalizes | Rail alignment/bed plane drift, slip or fracture. Compare sleeves/load spreaders/positive capture and thermal-time testing |
| F7 | Four independent actuators share elastic frame | Docking or acceleration disturbs an occupied neighboring job. Derive cross-compliance and a reviewed disturbance allocation |
| F8 | Cross/T treated as P, L and T without separate design | Missing fourth support, eccentric uplift, forced guide loops or unsupported handoff. Audit independent edge functions and six-DOF contact behavior |
| F9 | Unified secondary platform attached in R/C/mixed modes | Insufficient independent progress coordinates; **rejected interpretation**, unchanged from D3 |
| F10 | Braces or panel latches occupy head/bed/cable paths | D2 collision failures remain unresolved. Full geometry and transition/park/access sweeps needed; no mode may be silently removed |
| F11 | Imperial stock rounded to metric or alloy/tolerance guessed | Fit, wall strength and stiffness not reproducible. Distinct ready-to-print interfaces and supplier specification packets required |
| F12 | HDT treated as long-term chamber rating; local node hotter than air | Creep or loss of restraint despite apparently acceptable chamber temperature. No material/temperature approved; measure actual thermal fields and joint behavior later |
| F13 | Removable panels supply shear bracing or electrical protection | Open-air conversion changes stability or exposes electrical hazards. Permanent independent structure/protection must remain |
| F14 | Stiff frame credited with fixing hot-sheet seam | Phase 1B empty gap window, bow/slip and Phase 1C capture/retention issues survive. Preserve separate local registration research |
| F15 | Reinforcement/chords cut or assembled without controlled datums | Cumulative angular error forces rails to bend during tightening; use explicit cut/alignment/inspection method for both variants |
| F16 | Lumped frequencies treated as resonant-speed limits | Unknown damping, moving modes and control coupling invalidate performance claims; modal model and supervised measurements needed later |

No CAD, models, fabrication, firmware, hardware tests, purchases, license selection or
cross-repository edits were performed for D4. Manufacturer CAD rights remain unresolved;
public download availability is not permission for redistribution or AI processing.

Before any physical test, require qualified risk-appropriate review of hazards, safe
procedure, measurable acceptance limits, uncertainty, abort criteria and supervision.
Gravity/service restraint, heater controls, wire strain relief, locks/sensors, electrical
protection, stop/restart behavior and collisions need evidence. First hardware proof
remains the separately reviewed two-bed docking and cross-seam experiment.
