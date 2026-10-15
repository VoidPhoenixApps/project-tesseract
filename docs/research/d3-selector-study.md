# D3 — belt rerouting versus positive torque selection

[Report](d3-engineering-study.md) · [power/load diagrams](d3-diagrams.md) ·
[equations and reproducible counterexample](d3-calculations.md).
These are competing interpretations. No servo, motor, belt, clutch or actuator is selected.
Neither is a proven gravity support or an approved transfer procedure.

## Original: servo moves idlers/pulleys to reroute the belt

The belt leaves one transmission route and enters another. A real study needs pulley
centers, pitch radii, finite tangent segments, contact arcs, flange clearances and the
moving selector trajectory. Total pitch-line length is
`L(q)=Σ tangent_length(q)+Σ radius_j*wrap_angle_j(q)`, including the tensioner.
Evaluate every continuous branch and contact-topology change throughout selector q.
At a loss of contact the assumed formula changes; sparse endpoint samples cannot prove
minimum wrap/tension. A tensioner must accommodate length **and** maintain the required
force throughout travel, lift position, temperature and wear. A spring tensioner can
also introduce position compliance and oscillation. No constant-length geometry is specified.

The zero-radius mathematical counterexample in the code moves a point from (0,-20)
to (0,+20) mm between fixed endpoints (-100,0),(100,0). Equal endpoint length 203.96078
mm hides a middle length of 200 mm. Without take-up or elastic changes the belt loses
3.96078 mm of path demand at mid-travel. This is **not** proposed component geometry,
a vendor stand-in, or proof that every possible rerouting mechanism fails. It disproves
the inference that equal endpoint lengths suffice. At imposed uniform 50 N tension,
virtual work gives selector reaction `T*dL/dq`: magnitude 19.6116 N at either endpoint,
zero at the middle, reversing direction across it. Real wraps/friction/tooth engagement
add forces and hysteresis; this does not size a servo or include its lever ratio.

Pitch `p` and tooth count `N` imply nominal engaged teeth `N*wrap/(2π)`. Full contact,
entry/exit load sharing and actual manufacturer ratings still matter. Switching must
align the tooth phase modulo pitch without dragging a loaded carrier. A pulley passing
through a belt loop may encounter flanges; axial rerouting introduces tracking and edge
wear. Reverse bending, small idlers, debris and repeated engagement add fatigue unknowns.
No retrieved primary source demonstrates this literal Tesseract switching sequence.

## Alternative: dedicated tensioned belts, positive selector

The input selects one installed output path with a positively engaged dog/tooth clutch
or equivalent; both belts retain their paths. A neutral position is not a supported
load state by itself. Separate brakes/catches/locks must retain loads including the
unused frame. Unless a fully analyzed synchronizing topology is proposed, inhibit both
outputs being torque-connected at once: a momentary bridge can drive two unequal-height
systems against each other. Loss of selector power must not automatically release load
restraint or leave partial teeth carrying gravity.

For a proposed stop-and-unload sequence, immobilize loads independently, remove torque
from the engagement interface, align shafts without moving the supported beds, verify
full mechanical engagement/retention and only then restore drive ownership. Even a
multi-position tooth clutch has discrete mesh positions; “full position” is not arbitrary
continuous phase acceptance. The Miki catalog distinguishes full/single-position and
directional tooth forms [E2](d3-references.md). It does not establish a selected unit's
power-loss behavior, holding capability or permissible engagement speed here.

Output displacement from phase error is `travel_per_rev*phase/360`; at hypothetical
40 mm/rev, 1° output error is 0.11111 mm. An upstream 3:1 reduction does not reduce
backlash added **after** the reduction. Separate upstream and output 1° errors total
0.14815 mm in that example. Engagement can seat on a different flank under load reversal;
calibration at zero load is not loaded seam accuracy. Positive transmission does not
remove belt elasticity, bearing play or unequal local lift ratios.

## Comparison and evidence gates

| Question | Literal rerouting | Positive selector |
| --- | --- | --- |
| Belt length/tension | Entire path changes; take-up, branch changes and intermediate wrap unresolved | Path fixed in each transmission, but torque transfer and tension changes still load shafts/bearings |
| Phase and engagement | Belt teeth must enter target sprocket, with wrap and flange clearance | Teeth/dogs must align and seat fully; disconnected outputs may drift unless restrained |
| Switching force | Geometric tension reaction plus friction, bending, tracking and tooth forces | Spring/preload/axial engagement force plus tooth friction; torque can prevent release |
| Backlash and seam | Reseating, tooth jump and tensioner compliance | Clutch backlash, wrong index, shaft torsion and retained belt elasticity |
| Wear/service | Repeated path changes and reverse bends; inspect tooth roots/edges/idlers | Tooth impact, fretting and engagement depth; inspect clutch and bearings |
| Power loss mid-switch | Slack or partial wrap can remove lift torque | Neutral/partial engagement can remove lift torque; electromagnetic engagement may need power |
| Structural support | Independent load retention throughout; belt is not sole safety backup | Same; clutch is not a brake, brake upstream of a broken belt does not catch the carrier |
| Partial-mode independence | Requires independent group drives with unified frame detached | Identical requirement; selecting torque does not add frame degrees of freedom |
| Present ranking | Weakest specified transmission concept: continuous path and engagement unproven | Preferred *comparison* if a secondary frame is retained; fewer varying belt-geometry conditions |

Gates' manual (copyright 2014) requires separate backup for belt-based lifting and
addresses idlers, engagement and linear-drive working tension [E1](d3-references.md).
It supplies no approval for this mechanism. Standstill, unloaded engagement is a proposed
research restriction here, not a universal catalog requirement or a proven safe procedure.
Both alternatives must outperform the simpler no-selector baseline before adoption.
