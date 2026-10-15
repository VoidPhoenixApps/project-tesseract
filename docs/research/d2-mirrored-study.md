# D2 — mirrored A/B packaging versus common orientation

[Report](d2-engineering-study.md) · [code](d2_geometry.py) · [diagrams](d2-diagrams.md).
The maintainer's concept is preserved exactly. Type A at H1; its left/right mirror B
at H2; H3 is B rotated 180°; H4 is A rotated 180°. Nozzle corners face inward at home,
bulk faces outward. These orientations remain fixed during travel. There is no rotary
axis, and a head crossing the center does not turn to face it.

About each nozzle, `Q1=(+X,+Y)`, `Q2=(−X,+Y)`, `Q3=(+X,−Y)`, `Q4=(−X,−Y)`.
Translation is separate. A reflection is a **design relationship**, not a manufacturing
instruction to mirror a purchased rotor, extruder gearing or connector.

## Equal-envelope experiment

Both comparisons use the same synthetic A body: X=−50..8, Y=−8..50, Z=10..70 mm.
The mirrored case applies Q1–Q4. The conventional case uses Q1 for all four. Component
volumes, nozzle reference and carriage strokes are otherwise equal; no chosen product
is represented. Hotend, probe, carriage, cable and filament reservations are separate
boxes in the model, so body-only gains are not mistaken for complete-machine gains.

For H1/H2 at equal Y/Z with nozzles separated by d along X, body separation needs:

- Mirrored: `d > 8 + 8 + c = 18 mm` for illustrative reserve c=2.
- Common orientation: `d > 8 + 50 + c = 60 mm`.

The same 42 mm body-only difference applies to the north/south home seam using the
specified Y extents. At d=20 with c=0, the mirrored bodies do not intersect while common
orientation bodies do. This test is exact for the boxes, not real hotend clearance.
Sweep outward extent 35/50/65, inward 5/8/15 and c=0/2/5: 27 combinations in JSON.
Savings equal `outward − inward`; benefit disappears if the assembled extents become
symmetric and can reverse if inward protrusions dominate. Different Z levels can remove
body overlap, but cannot be assumed for unrelated jobs which may also share a layer.

At the right boundary, H2's body extends 50 mm beyond its nozzle instead of 8 mm: the
same 42 mm becomes an **outer frame penalty**. With cable and filament reservations,
the current hypothetical outward extent is 80 mm. A nozzle parked at 260 requires a
frame inner half-width of at least 362 mm including 2 mm reserve and 20 mm frame/panel
allocation; current 320 fails. This lower bound includes one outward extent, not proof
that the complete corner park or its route fits. The common-orientation family still
needs its left/top bulk reservations; this is not a claim it wins total machine size. The park260 example also fails
carriage reach: it requires ±280 against ±240 stroke limits. Enlarging the enclosure
alone cannot repair that failure.

Fixed nozzle-to-carriage offset in A coordinates is (20,−20,−50) mm. J nozzle bounds
±175 require H1 carriage X=−195..155 and Y=−155..195 at Z=50 for nozzle Z=0.
H2 uses X=−155..195; mirroring shifts the required carriage region rather than magically
increasing its stroke. Nominal carriage-center range ±240 is a sensitivity; real rail
end blocks, belts and housings reduce usable travel.

## Can there be only two assemblies?

Possible as a design hypothesis; not demonstrated. Diagonal rotation is a proper rigid
rotation and preserves a given assembled head. Left/right reflection generally requires
new original mounts/ducts while using ordinary unmirrored purchased parts. A two-head-type
BOM must distinguish complete head assemblies from any four different carriage adapters,
umbilicals or perimeter mounts; counting the latter outside the BOM can hide complexity.

| Interface | What would establish benefit / two-type reuse | What could refute it |
| --- | --- | --- |
| Nozzle/carriage and rail/belt | Dimensioned nozzle datum and complete mount transform; diagonal fastener/belt clamp congruence | Carriage block or belt path requires extra handed mounts; offset causes bending or loses reach |
| Extruder/fans/ducts | Exact assembled outer envelope for both types, including motor, lever, connector and duct mouth | Mirroring housing cannot mirror a purchased extruder; outward lever/service operation occupies parking zone |
| Probe and sensors | Probe sample positions reachable on each required sheet, cable exit and deployed/retracted geometry known | Nozzle reaches seam while probe is over gap/off sheet or sensor mount collides |
| Filament | Same entry direction in each local frame, exact feed tube and filament bend limits and spool route | Rotated head points feed into frame/another chain; guide loop needs a third/fourth assembly or excessive friction |
| Cable/strain relief | Connectors and anchors permit rotation with validated full XYZ bending and no twist | Cable route consumes park or crosses a lower bridge, with strain relief absent from nominal box |
| Cooling | Same fan unit mounted with correct inlet/outlet and independently tested mirrored ducts | Reflecting a drawing reverses assumed flow/rotor handedness; nearby panel blocks intake or produces asymmetric cooling |
| Service | Nozzle wrench, heater withdrawal, extruder opening and fan removal envelopes clear with power/motion isolated | Head has an accessible static pose but tools or extracted components cross parked gantries; panel removal insufficient |

Minimum evidence request: exact manufacturer components/revisions and permitted models,
assembled A/B envelope including all operating/service states, carriage interfaces,
nozzle/probe/connector datums, chain and filament routes, equivalent conventional layout,
and measured cooling/access trials later. Do not download models or fabricate interfaces
at this research stage. [Catalog](d2-references.md) identifies the missing dependencies.

**Conclusion:** a supportable *conditional geometric* advantage exists at home seams.
There is no supportable whole-machine advantage or demonstrated two-assembly implementation
yet. Preserve the concept in the next comparison; do not use it to dismiss conventional
heads or to claim that central beam interference has been solved.
