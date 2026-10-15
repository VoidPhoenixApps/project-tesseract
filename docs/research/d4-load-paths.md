# D4 — eight-mode support and constraint study

[Study](d4-engineering-study.md) · [diagrams](d4-diagrams.md) · [D3 ownership](d3-mode-constraints.md).
Coordinates: X east, Y north, Z up; 1 NW, 2 NE, 3 SW, 4 SE.
`F` is the global frame and its supported foundation, `Ui` the complete guided lift and
independent restraint, `Bi` cold carrier, `Hi` hot plate and retained individual sheet.
All four beds carry gravity in every mode, including inactive beds.

Three distinct edge types: **P** positional registration, **L** structural load support,
**T** torque transmission. Sharing an endpoint does not combine these functions.
For each bed, baseline L graph is `Hi → Bi → Ui → F → feet/foundation`. Each Ui must
carry gravity, horizontal forces and moments, not merely supply Z actuation.
P baseline locates Bi within its moving assembly; it does not pin printing Z to F.
Hot-plate mounts release thermal in-plane growth. Baseline T uses monitored local
actuators; optional T trees below represent selectable mechanical transmission only.

## Explicit configuration graphs

Every row includes all four baseline L paths. Listed P trees are **alternatives** to
fully frame-referenced location, with conflicting follower freedoms released. Listed L
ties are optional additions with proven compatibility required; they are not assumed
rigid. A tree prevents one scalar closure loop but does not prove spatial six-DOF rank.

| Mode | Progress groups | P alternative tree edges | Optional L ties / load domain | Optional T tree | Shared platform |
| --- | --- | --- | --- | --- | --- |
| S | 1 / 2 / 3 / 4 | None; four local datums | None; four independent Ui | None between lifts | Detached, independently retained clear |
| R | 12 / 34 | 12 and 34 | B1↔B2; B3↔B4; no tie between rows | 12, 34, separately selected | Detached; one rigid attached platform fails two progress coordinates |
| C | 13 / 24 | 13 and 24 | B1↔B3; B2↔B4; column roots differ from rows | 13, 24 | Detached; permanent row subframes fail this grouping |
| M12 | 12 / 3 / 4 | 12 only | B1↔B2; U3/U4 remain independent | 12 only | Detached; frame disturbance into 3/4 remains possible |
| M34 | 34 / 1 / 2 | 34 only | B3↔B4; U1/U2 remain independent | 34 only | Detached; mirror service and cable routing separately |
| M13 | 13 / 2 / 4 | 13 only | B1↔B3; U2/U4 remain independent | 13 only | Detached; left-side frame torsion and access |
| M24 | 24 / 1 / 3 | 24 only | B2↔B4; U1/U3 remain independent | 24 only | Detached; right-side frame torsion and access |
| J | 1234 | 12,13,34 illustrative released tree | All Ui retained; optional B1↔B2, B1↔B3, B3↔B4 | 12,13,34 selected tree | Alternative handoff: Hi→Bi→platform locks→guided platform/restraint→F; release incompatible Ui constraints |

[Generated graph records](d4-results.json) contain the eight partitions and distinct
P/L/T labels. These are topology assertions and tests of bookkeeping, not automatically
solved spatial constraint graphs. In J, each optional edge has its own load and release
specification; no fourth stiff edge closes a loop by accident. One full-region head is
assumed only as a coverage requirement, not as established D2 feasibility.

## Force entry and support ownership

| Subsystem | Force entry / structural return | Constraint and packaging consequence |
| --- | --- | --- |
| Four independent bed Z stages | Gravity, lift acceleration and guide overturning couples enter separate towers/base rails through Ui; restraint loads need independent return paths | Stationary full-height guides cannot follow sideways-docking carriers by assumption. Either guides travel with transport or reviewed support handoff is required |
| Coupled Z carriages | Same individual returns plus optional ties redistribute differential force and moment | Shared trajectory does not remove guide parallelism. Stronger links increase mismatch forces; release a specific follower translation/rotation without losing lateral stability or gravity restraint |
| Central cross/T indexing | P forces enter a cold datum spine; if L is also intended, arm bending, root torsion and retained support reactions enter F | A literal T lacks a fourth arm; fourth bed needs another support. Cross arms must clear horizontal travel, sheets, heater leads and locks. It cannot rigidly impose a common printing height on partial modes |
| Secondary lift | Platform weight plus four beds reaches its guide/actuator/independent restraint and F | Handoff at fixed datum must preserve support during engagement, release incompatible local guides and isolate unused torque. A parked platform still has mass and a restraint requirement |
| Independent XY gantries | Head and carriage inertia into rail seats, belt anchors, bridge ends, frame towers | Four forces can reinforce rather than cancel; opposing forces can create a couple even if net force vanishes. Local rail-seat twist causes alignment error |
| Perimeter cantilevers | Head gravity at long reach creates root moment; transverse acceleration creates bending/torsion | Root stiffness dominates as arm length grows. External roots/braces compete with park and hand-removable-panel space |
| Stacked bridges | Gravity and acceleration enter several elevations of side towers; descending columns add eccentric moments | Separation of bridge planes does not clear columns or objects. High force-entry elevation increases overturning and base reaction differences |
| Parked heads, cables, filament | Park brackets retain full assemblies; cable drag/spool feed forces enter moving head and fixed anchors | Nozzle-only park analysis insufficient. Reserve all cable bend envelopes; do not hang tensioned feed paths from removable panels |
| Bed horizontal transport/docking | Motor reaction, stops and latch preload enter base rails/datum spine | Local docking impulse may disturb a busy neighbor through F; structural independence is not guaranteed by separate actuators |
| Acceleration/vibration | `F=ma`; eccentric `M=F e`; gravity moments coexist | Compare coherent four-head excitation, unequal phases, reversal, braking and lost-restraint transients; no acceleration rating established |

A support polygon must contain the resultant for compression-only contacts. For an
illustrative 100 N load, 240 mm support spacing and 150 mm eccentricity, reactions are
-12.5 and 112.5 N: a negative reaction means loss of contact unless a rated hold-down
exists. It is not a passing capacity result. Asymmetric print mass and parked heads
also change whole-machine foot reactions; footprint and tip-over margin remain unknown.

## Independent ownership versus hybrid structural links

Independent supports avoid a closed structural link between beds; differential elastic
motion remains. Hybrid ties can reduce that difference, but convert guide/datum error
into force. The [two-coordinate spring model](d4-calculations.md) reduces a 0.020 mm
load-induced difference to 0.00667 mm; adding a hypothetical 0.200 mm support mismatch
requires a negative 33.3 N reaction. A real gravity-only contact would open and the
linear solution would cease to apply. This is a reason to model contact, not a cure
through greater preload.

For future spatial audit, list each guide/contact normal and lever arm, retained versus
unilateral contact, released freedoms, compliance and independent restraint. Evaluate
constraint rank, positive reactions and stiffness together across the whole stroke.
Thermally expanding links and unequal guide spacing add incompatibility even when
rank is nominally six. No rail tolerance or permitted mounting error is selected.

When U2 loses support, a retained hybrid link could transfer its load to U1: the scalar
example demands 60 N at U1 and 40 N in the link. It does not prove rotational stability,
link capacity, fault independence or dynamic arrest. Without the link, that coordinate
is unsupported. A link sharing the failed node/fastener is not an independent backup.

## Transitions and unaffected jobs

Apply D3's [transition obligations](d3-failure-study.md). Before a support path is released,
verify the receiving restraint, compatible pose and positive load engagement. Disabling
a motor does not release its guide. No vertical bed landing is introduced as horizontal
conversion. Only clear affected groups may return to the common reconfiguration datum.

For mixed states, loads, references, cables and stiffness of occupied singles must remain
within future reviewed disturbance limits while another group docks. All-bed J handoff
changes the common support domain and requires all affected beds clear. Graph isolation
does not authorize 56 directed transition paths; full spatial sweeps remain absent.
Neither extra stiffness nor stopping all jobs indefinitely establishes independent jobs.
