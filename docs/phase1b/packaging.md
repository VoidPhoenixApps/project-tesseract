# Mechanical packaging and transition screening

**Dimensioned conceptual envelopes only.** The [model](analysis.py) checks conservative axis-aligned boxes and continuous axis-segment sweeps. It is not CAD, a detailed collision-checked assembly, head/object collision planning or manufactured fit evidence. All dimensions are mm. No CAD toolchain is selected.

## Coordinates and reserved bands

Use the Phase 1 frame: X right, Y up, sheet top Z=0; A NW, B NE, C SW, D SE never exchange quadrants. To compare directly with Phase 1, retain **g=0.20 only as a cold geometric scenario**, b=180, q=(b+g)/2=90.10, separated center magnitude s=130 and axis stroke d=39.90. Thermal admissibility is assessed separately in [thermal analysis](thermal.md); the clearance model does not approve this gap.

```text
TOP at J, cold nominal sheets (not to scale)
             180         0.20        180
         +-------------+      +-------------+
         | A   160 K   |      | B   160 K   |
         |   carrier  |      |   carrier  |   Y up
         |       a *  |      |  * a       |   X right
         +-------------+      +-------------+
                         +                    central cross
         +-------------+      +-------------+
         |       a *  |      |  * a       |   a = inset thermal anchor
         | C          |      |          D |   10 from inward X/Y edges
         +-------------+      +-------------+
 Each carrier side inset 10 from plate; opposed K faces gap 20.20.
 No latch, cable, sheet tab or anchor body may occupy the central cross.

SIDE, suggested reservations (Z in mm; thicknesses are budgets)
     0  separate sheet / plate stack
    -8  heater, insulation, support and cable-termination band
   -35  cold carrier / dock / optional float band (20 high)
   -55  upper X guide + intermediate structure (25 high)
   -80  lower Y guide + base structure (25 high)
  -105  clear lower tug band starts
  -145  tug band ends; fixed bracing below or outside its swept region
```

This revises the earlier provisional -35 to -95 mechanism budget to -35 to -105 **for this scenario**, with an optional further 40 mm tug band. It is not evidence those depths suffice. A 14 mm guide in a 25 mm band leaves 11 mm for structure, screw heads, running clearance and tolerances; the 20 mm float/dock band has no verified flexure geometry. Heat isolation, stiffness and assembly access may require substantially more depth.

| Envelope / feature | Proposed dimension or rule | Status and failure trigger |
| --- | --- | --- |
| Sheets / plates | 180 square at Z≈0; no inward tabs | Actual stack and hot outline unknown; four retained sheets mandatory |
| Cold carrier | 160 square, centered on module | J face clearance 20.20; c=10 noncontact allowance leaves 10.20 total reserve |
| Guide foundation reservation | Per quadrant x,y magnitudes from q-80=10.10 to s+80=210 | Includes union over travel; no cross-center rails at the same band |
| Sheet sweep | Per quadrant magnitudes q-90=0.10 to s+90=220 | Cold only; thermal edge excursions added separately |
| Dock blocks | Conceptual 15×20×20 blocks inset within carrier projection | Must coexist with guides/float; not fitted parts. Actuator retracts within pocket |
| Plate supports | Example local (-60,-60),(60,-60),(0,60) | 120 baseline, triangle area 7200 mm²; central corners lie outside support triangle |
| Inset anchor | Local (±80,±80), signs toward center | Separate in-plane reference, not a fourth rigid height support; thermal/mechanical bridge to carrier required |
| Cable exits | Outer quadrant corner, no inner seam loop | Independent XY loop ends and connectors require geometry and bend-radius qualification |
| External cable corridor | Example 80 mm depth beyond |X|=230 or |Y|=230, routed per quadrant | Assumes R=30, bundle D=10, allowance=10: 2R+D+allowance=80; not cable rating |
| Service space | Outward withdrawal of empty cold module; removable external panel | Tool/connector reach and removal sequence unmodeled; service may lift after isolation, never during conversion |

The external-corridor scenario reaches ±310, or 620 mm overall on axes using both sides, before guards and service reach. At I the cold sheet perimeter reaches ±220; a 10 mm stand-off separates the corridor. Its cable connection must span from moving module to corridor through a protected outer route; the 80 mm corridor width alone does not prove that connection fits. Two-axis motion requires nested single-axis loops or a qualified multidirectional loop; bending a planar chain sideways is not a solution. In J a module exit can be 39.9 mm farther inward on each axis. Include all intermediate loop shapes, strain relief, connectors, sag and thermal rating. No universal R or cycle life is assumed; [igus guidance](verification.md) motivates checking the selected cable's dynamic minimum radius.

## Independent XY carriers

Load path: plate → three supports → cold carrier/float → X bearings → intermediate plate → Y bearings → stationary reinforced frame. Guide moments and serial compliance add; top-plane height cannot be inferred from motor step resolution. A short single wide rail can save transverse space but must resist roll and moments; dual rails increase stiffness potential and alignment demands.

For two blocks on a rail, along-axis center spacing S, block length Lb, stroke d and end reserve m at each end, require `Lrail >= S+Lb+d+2m`. A manufacturer's catalog example [THK SRS12WMUU(GK)](verification.md) has Lb=44.5, width 40, assembled height 14; these dimensions establish an example scale, not a part selection or load qualification.

At d=39.9, m=10: S=50/60/70 gives minimum rail lengths **154.4/164.4/174.4 mm**. A rail centered at the travel midpoint (110.05 in each quadrant coordinate) does not follow the bed center. With S=50, it spans 32.85–187.25, within the reserved 10.10–210 quadrant foundation. The moving carrier occupies 10.10–170.10 at J and 50–210 at I. A 174.4 rail can still fit the larger fixed foundation reservation, but cannot simply be called a 160 mm moving package. A moving upper rail's *swept* rectangle must include its motion on the lower axis.

Two parallel 40 mm blocks on rail centers separated transversely by 80 occupy 120 mm, leaving 40 mm across a 160 mm carrier for margins and other hardware. Two longitudinal blocks at S=50 have only 5.5 mm between their 44.5 mm bodies; lubrication/tool clearance is unverified. Mounting holes, actual offered rail lengths, end seals, bolt head access and cable fittings can increase the package. No catalog load or life claim is imported.

Reducing support/bearing span increases force: a 2 N·m moment requires a reaction couple 40 N across 50 mm, versus 28.57 N across 70 mm. Weight, acceleration, cable pull and latch offsets combine with that moment. Printed foundations need short reinforced force loops and adjustable metal datum surfaces where justified; rail alignment cannot rely on as-printed holes. Qualify both imperial and metric frame interfaces from actual stock, separate generated variants and measured stiffness. No new stock size is specified here.

### Locks at every necessary station

Each module uses four combinations of coordinate magnitudes `(q,q),(q,s),(s,q),(s,s)`. One fixed 2+1 cartridge at J cannot lock all modes. Candidate station design: four discrete frame-referenced datum nests with retracting local fingers, or independently selectable X/Y datum surfaces whose yaw ownership is audited. Provide seated/locked observation at I and all paired/mixed endpoints as well as J. Intermediate transport needs controlled support and a reviewed power-loss hold state.

Fixed protruding stops would block travel between stations. Inactive fingers must withdraw entirely from the module sweep without changing bed Z; active fingers extend only after coarse positioning and clearance verification. Station hardware must remain within its own quadrant and avoid rails in the same band. This is a significant unresolved packaging detail, not included in the rectangle checks. A transport brake can hold a pallet but does not establish the same precision as a datum nest. No automatic leap from J-only accuracy to every-mode accuracy is permitted.

## Shared tug challenger

Keep the same passive supported XY carriers and station locks. Reserve a common lower XY tug plane at -145≤Z≤-105, with no frame crossmember, motor, cable loop or hanging fastener in its swept region. An illustrative tug body 60×60 moving between module-centered capture points x,y∈[-130,130] sweeps within [-160,160]². Body top proposed Z=-115 leaves 10 mm to the -105 plane; this is a nominal clearance, not a stop-distance allowance.

Every pallet needs a dog attachment reachable from this plane. A stem projected down through two crossing rail layers is **not automatically possible**. Either demonstrate a continuously clear aperture across full XY travel or provide an offset bracket whose complete sweep remains inside that pallet's reserved quadrant. That bracket transmits tug force with a larger bending moment. The horizontal dog must engage without lifting, without becoming a conflicting precision datum when docked, and without passing through a neighbor's loop. No stem/aperture solution is supplied by this box model; tug feasibility is therefore conditional and less mature than independent drives.

Sequence proposal: tug clear → align to empty carrier → horizontal capture → observe capture → release only that carrier's park lock → move one axis segment → seat and lock → observe seats and lock → unload dog → release dog. If capture or seating is ambiguous, stop with gravity support and appropriate retained restraint; no blind retry or increased tug force. Tug failure may strand access to every module even though local locks hold. Frame deflection during tug travel can disturb a running bed despite no geometric contact.

## Every required layout and occupied-region protection

The model enumerates I, H, V, MH-top, MH-bottom, MV-left, MV-right and J. In each quadrant, coordinates lie independently between magnitudes q and s. For an empty machine any pair of these eight modes can be connected by single-module, single-axis segments; each segment's swept AABB is checked against every stationary module. No sampling gaps are hidden between endpoints: the union of an axis-translated rectangle is its exact swept rectangle. This is a conservative solid-box check, with different sheet and carrier layers. A negative-control 190 mm carrier is expected to collide at J.

At every point, opposing quadrant centers have separation at least 2q=180.20 in at least one axis. Thus cold sheets have at least 0.20 separation in that axis and 160 mm carriers at least 20.20. This certificate covers the stated boxes, not an assertion of omnidirectional Euclidean clearance at arbitrary protrusions. The model reserves c=10 mm between carrier boxes; actual uncertainty, overshoot/stopping distance, float motion and thermal excursion must fit the remaining allowance. Near sheet seams, c=10 is inappropriate; the separate thermal/print gap budget controls.

Freeze occupied modules' coordinates, locks, support state, temperature recipe and object volumes. A transition is rejected if it changes any occupied module coordinate. Examples: I→MH-top can preserve busy C and D; I→MV-left cannot preserve busy A or C; J cannot split while a joined object exists. A busy joined region is treated as all its member beds occupied. The check demonstrates coordinate preservation only. It excludes objects overhanging their bed, toolhead motion, purge structures, cable excursion, vibration, thermal disturbance and braking failures. These require subsequent integrated swept-volume and disturbance evidence before concurrent conversion is allowed.

There is no normal service access through the 0.20 central cross. Locate fasteners, wiring disconnects and latch release access toward the perimeter or from below after isolation. A module removal operation must not require pulling on a busy neighbor's heater leads or releasing its support. Support-triangle corner overhang, a corner anchor bridge, retracted station stops and a tug stem all compete under the same 180 mm plate: a dimensioned assembly must resolve them before detailed feasibility is claimed.
