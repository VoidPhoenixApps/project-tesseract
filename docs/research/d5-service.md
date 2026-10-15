# D5 — installation, removal and service access

This is an access analysis, **not an executable machine-service procedure**. No hardware
exists with established safe states. [Safety](d5-safety.md) owns isolation and fault needs.
Tool-free conversion does not itself establish safe handling during active printing or
while hot. Assess conversion hazards separately; panel absence does not itself require
service isolation, an interlock or a protective fault. Ordinary open-air printing retains
all required modes; maintenance still requires reviewed energy isolation.

## Path definitions and counterexample

Analyze panel solid, edge frame, grips, hand envelopes, release levers and any retained
keepers as a moving assembly. Include the reverse installation path, seating tolerance,
visibility and final engagement check. Installed clearance is necessary but insufficient.
Use swept volume `union(P(q))` over the entire path; evaluate uncertain panel bow and
relative frame growth, not only corner snapshots. A turning panel requires rotation-aware
geometry; endpoint AABBs do not bound a rotating plate.

The reproducible abstract example has panel X −300..300, Y 320..324, Z 0..600 mm and
an overhead lip X −310..310, Y 310..350, Z 615..630 mm. It is clear at rest. Lifting
40 mm then moving outward 100 mm intersects the lip. Moving outward first and then
lifting clears **that one obstacle**, including the reverse path. A captured hook might
forbid outward-first release, so this alternative is not automatically a mechanism fix.
Hands, grip projection, cables, rotation and floor access are absent from the example.

| Mechanism | Removal and reverse installation | Failure to check / potential improvement |
| --- | --- | --- |
| Supported lift-out | Support panel, release positive retainers, disengage capture in permitted direction, lift/carry to storage; reverse and verify every capture | Required lift height blocked by gantry/brace/roof; fingers trapped at bottom. Compare outward-releasing support or smaller cassettes without removing primary structure |
| Removable hinge | Release closure, open through prescribed swing, support weight, release anti-lift feature, withdraw hinge/pin by hand, carry away | Hinge release hidden by door, panel falling from last pin, cable tug or insufficient room to lift. Refit must visibly engage every hinge before loading |
| Slide-in edge | Release captive hand end stop, translate completely out with sustained support, reverse without gouging gasket | Full panel-length clearance unavailable, slot packed with debris, hot panel jams. A split face may shorten travel but adds leak/retention joints |
| Captive knobs / quarter-turn | Supported panel while all catches released; reverse with aligned grip and gasket stack | Last fastener takes entire load; glove/finger access blocked; retainer feels tight while hook misses. Visible state plus positive engagement inspection |
| Roof cassette | Two accessible grip locations and independent support during release; clear overhead filament and beams in both directions | Overhead handling, hot sheet and falling debris; no lifting over occupied machine. Consider smaller independent roof sections as an unselected alternative |

No hose, spool, chain anchor, electronics enclosure or bed cable may require dismantling
to remove an environmental panel. Compare fixed service spines and removable split seals
around permanent penetrations. A panel-mounted exhaust fitting would create a later
conversion dependency; exhaust is not selected, and hand-disconnect alone would not prove
safe emissions control. Keep emergency-stop and isolation access visible in both states.

## Task access matrix

| Task | Access needed after safe state established | Evidence still missing |
| --- | --- | --- |
| Routine cleaning | View and reach ledges/tracks, floor debris and all bed seams without disturbing registration | Reach/grip envelope, dust trapping, cleaner/material compatibility, cooled-surface evidence |
| Calibration | Sight and instrument placement at four sheets, lock witnesses and frame/head datums | Instrument size, all eight layouts, no dependence on a removable brace or panel datum |
| Wiring inspection | Permanent covered electrical compartment, strain reliefs and routing on both sides of flex points | Safe isolation/absence-of-voltage procedure, bend/abrasion limits, inspection lighting; transparency is not sufficient access |
| Component replacement | Complete extraction route for head/rail/bed carrier and access to both ends of fasteners | Assembly sequence and independently supported service condition; distinguish authorized maintenance disassembly from panel conversion |
| Belt/selector/lock service | Access to adjust/inspect without loading another live lift; support stored gravity loads first | Reviewed service restraints, no remote restart, failure recovery and compatible tools |
| Repeated conversion/storage | Hand-only seating, secure retention, manageable grip and storage footprint; protected sheet edges | User hand-size/reach study, hot/cold force distributions, cycle life, drop hazards and orientation markings |

Service may need tools **after** conversion; that does not permit tools for panel
installation/removal. Component replacement may involve disassembly under an approved
maintenance plan; reaching the service opening by removing panels must not dismantle
primary systems. A convenient access door is not evidence that a rail can be extracted.

Compare large versus segmented panels explicitly: fewer joints/leaks versus lower mass,
shorter removal sweep and easier replacement. No selected cassette size or single-person
mass limit exists. Maintain inspection criteria for cracks, loose inserts, deformed clips,
fretted tracks, seized knobs, damaged seals and missing retainers before further use.
