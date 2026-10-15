# D4 — Ender 3 segmentation, structural joints and materials

**Feasibility study only.** Every printed first-edition part must fit an ordinary
Ender 3 in each stock variant. Creality lists 220 × 220 × 250 mm for Ender-3 Pro
[P4](d4-references.md); this is a nominal reference, not a chosen usable envelope.
Brims, clips, purge regions, supports, shrinkage, orientation and calibrated travel must
be included. A tilted bounding box is not proof of a printable, strong structural part.

## Segmentation and joint study

| Approach | Load transfer and alignment | Orientation, replacement and calibration | Principal limitation |
| --- | --- | --- | --- |
| Repeating triangulated cells | Put splits at axial nodes where possible; align strut centerlines through joint reaction center. Out-of-plane brace closes spatial load path | Print long loaded fibers largely in layer plane; provide access to both fastener ends and external datum pads | Node eccentricity creates bending; printed butt joints cannot inherit continuous-beam EI |
| Continuous rods/tubes through short printed webs | Chords carry axial tension/compression; webs transfer shear between chords and prevent local buckling only if laterally stiff | Split clamp webs can be replaced without withdrawing all stock; end anchor and brace remain accessible | No perfect composite action assumed; slip or loose web increases effective buckling length |
| Overlapping splice / double-sided gusset | Separate locators establish assembly datum; fasteners and broad bearing faces carry load with defined preload | Stagger chord splices, avoid peel across layers, use replacement access from clear service side | More parts/stack tolerances; lap eccentricity and hole bearing need checks |
| Scarf/key joint with retained fasteners | Large contact area and key can register parts; bolts retain separation | Split along supportable faces, avoid unsupported socket roofs and trapped nuts; inspect mating faces | Geometry does not guarantee contact or load distribution; fit and wear unmeasured |
| Printed node with metal sleeve/load spreader | Sleeve can bypass polymer under bolt compression; retained socket transfers axial/shear/torque by explicitly designed surfaces | Accessible through-bolt and captive replaceable nut compared with heat-set inserts; identify assembly direction | Sleeve fit, insert pullout, socket splitting and tube crushing still need evidence |

A hypothetical 600 mm member divided into four 150 mm cells illustrates length only.
Tabs, node width, brim and height may exceed the ordinary Ender envelope; no part-fit
claim is made. A future automated envelope check must include all print accessories and
both stock variants at their worst orientation. Splits placed in highly loaded cantilever
roots need special justification; smaller parts are not automatically a better frame.

Candidate assembly process: datum jig establishes rail planes and diagonals; locate
nodes without forcing rods into bowed sockets; seat retained contacts; apply reviewed
preload sequence; measure alignment unloaded and loaded; lock adjustment; recheck after
temperature/time cycling. This is a proposed process, not an executable test procedure.
Provide removable covers, visible retention indicators and access to inspect wear,
loose nuts and datum contamination. Replacement must not require removing a loaded
support without independent service restraint.

## Polymer comparison under possible enclosure conditions

The table compares research candidates, not chamber ratings. ASA and PC values are
supplier specimen results, not Ender-printed joint properties. Plausible **sensitivity
conditions** of 20/40/60 °C local node temperature would be useful to compare later;
none is an approved ambient, chamber or continuous-use target. Radiant bed heating and
motor heat can make a node hotter than chamber air.

| Material family | Evidence / reason to compare | Limitation and reproducibility question |
| --- | --- | --- |
| PLA | Readily printed; useful room-temperature geometric control [P3](d4-references.md) | Thermal deformation/creep must be characterized; no enclosure structural approval inferred from printability |
| PETG | Prusa describes relatively easy printing and toughness [P3](d4-references.md) | Long-duration clamp preload and warm-node stiffness unknown; ductility does not establish dimensional stability |
| ASA / ABS | ASA TDS v1.1 lists flexural modulus 2.0/1.9 GPa by specimen direction and HDT 93 °C at .45 MPa, 86 °C at 1.8 MPa [P1](d4-references.md) | HDT is a short standardized deflection test, not allowable service temperature. Warp/process dependence and layer peel matter; ABS is a separate formulation requiring its own data |
| PC blend | TDS v1.1 lists HDT 113/93 °C at .45/1.8 MPa [P2](d4-references.md) | Printing process demands may exceed an ordinary unmodified Ender's capabilities. A higher HDT does not prove creep resistance, joint fit or safe reproduction |
| Filled polymers | Compare if directional stiffness helps and an accessible process exists [P3](d4-references.md) | Fiber direction, moisture, abrasion, interlayer strength and print capability need formulation-specific evidence; cannot apply unfilled data or assume chopped fiber is continuous reinforcement |

Maintain distinction between fitting the bed and printing reliably on the ordinary
machine. No nozzle, enclosure modification or material purchase is authorized. A material
that requires an unavailable process may fail reproducibility even if its coupon is stiff.

For sensitivity, use `E_eff(t,T,orientation,stress)` rather than a constant lifetime
modulus. Reducing 2 GPa to .5 GPa in the abstract truss multiplies the **member** compliance
by four, but total compliance also includes joint springs. This is deliberately a range,
not a sourced creep law. No time-to-failure or retained preload is predicted.

Bolt preload passing through polymer can relax; then friction-only load transfer may
slip. Compare metal compression sleeves, broad bearing area, positive axial shoulders
and replaceable nuts. Inserts save access on one side but add pullout/rotation and
thermal-installation uncertainties. Do not compensate for creep by an arbitrary torque
increase. Small slip at a root creates nozzle error amplified by reach. Measure future
joint rotational stiffness, hysteresis and retained clamp force at temperature and time;
strength, fatigue and accidental overtorque require separate evaluation.
