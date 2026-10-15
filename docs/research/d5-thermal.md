# D5 — passive thermal and environmental sensitivity

[Equations and inputs](d5-calculations.md) · [results](d5-results.json) · [sources](d5-references.md).
Passive here means heat from beds, hotends, motors and other internal losses, **not** an
approved chamber heater. No temperature recipe, exhaust or filtration system selected.

## Heat sources, boundaries and nonuniformity

Use average net heat retained inside the studied volume, not the sum of nameplate heater
ratings. A possible bookkeeping model is `Q = sum(duty_i P_i retained_fraction_i) +
internal motor/driver losses + other internal losses`. Heater duty changes with environment;
external supplies and losses should not be counted as internal heat. Warmup and stuck-on
heater faults are separate load cases. No electrical power budget is established.

A deliberately hypothetical six-face 600 mm cube has area 2.16 m² and volume .216 m³.
This is an arithmetic specimen, not a proposed enclosure or a claim of compatibility with
D2's larger clear box. At 4 mm PC, inside/outside film coefficients 4/8 W/m²/K and assumed
exchange 0/5/20 m³/h, total conductance is 5.482/7.157/12.182 W/K, excluding additional
frame bridges. No flow rate is predicted from those assumptions or approved for emissions.

| Net internal heat W | Rise at 0 m³/h K | Rise at 5 m³/h K | Rise at 20 m³/h K |
| --- | --- | --- | --- |
| 100 | 18.24 | 13.97 | 8.21 |
| 300 | 54.73 | 41.92 | 24.63 |
| 600 | 109.46 | 83.84 | 49.25 |

These are steady **linear heat-balance outputs**, not attainable/safe chamber temperatures
or conservative upper bounds. At large temperature rise, fixed convection coefficients,
air density, heater duty and material properties cease to be credible; radiation and
leakage change. The high-rise rows deliberately expose the absence of a thermal guarantee.
They must not be used to rate the machine or authorize testing at those temperatures.
At an illustrative ambient 20–30 °C, add that ambient to a rise only within the model's
assumptions; ambient variation itself changes component margin.

At equal film assumptions and 5 m³/h exchange, the four example sheets give conductance
7.13–7.43 W/K despite very different conductivity. Surface films and leakage dominate this
particular thin-wall example. Thickness/insulation, wall area, frame bridges and openings
can change the ranking; replacing plastic with metal is not an assured chamber-cooling fix.
Surface radiation should eventually be modeled as `epsilon sigma A (Ts^4 - Tsur^4)` with
absolute temperatures, view factors and optical properties; transparent surfaces do not
necessarily have the same radiation exchange as opaque ones. No radiation bound is claimed.

## Transients and gradients

A lumped heat capacity of 10 kJ/K gives time constants 1824/1397/821 s for those exchanges.
At 300 W and 5 m³/h, the lumped rise after 30 minutes is 30.36 K versus steady 41.92 K.
Capacity is a sensitivity input, not air alone: air in the cube contributes only about
260 J/K using the stated air properties. Beds, panels and frame have separate temperatures
and heat capacities. Heating/cooling time scales cannot be inferred from a single air sensor.
For constant G, doubling capacity doubles the time constant; after heat removal the
lumped excess decays exponentially, but stored beds/hotends can stay hazardous much longer.

A separate two-zone steady example allocates 80/220 W to lower/upper nodes, each losing
4 W/K to ambient. Coupling 1/4/20 W/K yields upper-minus-lower differences
23.33/11.67/3.18 K. This preserves energy but is **not** a measured stratification pattern.
Heat plumes, fan flow, bed layout and door gaps may reverse or redistribute local gradients.
Corner, front/rear and member temperatures need their own future nodes/measurements.

Four independent heater recipes in S/R/C/M modes create asymmetric sources. Panels can
trap motor heat high in the frame while lower rails stay cooler. Enclosure conversion can
change seam drift during an existing print; do not assume it is harmless or automatically
recalibrate/move occupied beds. Review whether conversion must wait for completion/cooling.
Automatic bed rearrangement with panels installed remains a mandatory capability.

## Component and environment consequences

| Region | Plausible failure mechanism | Future evidence / unresolved choice |
| --- | --- | --- |
| Printed nodes and reinforcement sockets | Local radiant/motor heat reduces stiffness; clamp preload relaxes; uneven member growth shifts datums | Actual orientation/process/time/stress data; D4 HDT is not a continuous loaded-joint rating; compare thermal shielding/stand-off locations without selecting material |
| Motors, bearings and belts | Warm ambient reduces heat-rejection margin; grease, belt and winding limits differ | Exact parts, losses, case/winding/ambient ratings and sensor placement; no generic motor temperature limit |
| Drivers, PSU, connectors and wiring | Elevated inlet air and contact resistance accelerate heating; sealed electronics space may accumulate heat | Compare outside-chamber protected compartment versus thermally separated service spine; reviewed derating and fault behavior. Panels removed must not expose live parts |
| Magnets, clips, gaskets and grips | Loss of attraction, creep, adhesive degradation, seal set and unsafe touch surfaces | Actual local hot-spot temperature and material-specific cycle/cleaner evidence; no safe-touch threshold selected |
| Natural ventilation | Low inlet/high outlet can create buoyant flow; pressure/leaks, obstructions and room drafts determine rate | Openings trade thermal stability, access protection and emissions escape; flow and acoustic/comfort limits unmeasured |
| Seals and service openings | Better sealing can stabilize temperature but raise hot spots and complicate panel release | Replaceable compliant seals with retained thermal float; characterize leak paths and release forces hot/cold/dirty |

NIOSH's guide E1 treats printer/material combinations and exposure controls as requiring
assessment. A closed enclosure does not establish safe indoor air; opening it can release
accumulated emissions. Particles and gases need different control considerations, including
filter service, capture/leakage and safe discharge if a future exhaust is approved. No
exposure limit, purge time, HEPA-only VOC claim or safe unventilated operation is inferred.
Open-air printing still needs an emissions assessment. Ventilation and guarding openings
must be studied together; thermal convenience cannot justify reachable hazards.
