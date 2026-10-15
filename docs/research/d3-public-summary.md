# D3 — what holds the beds while their drives change?

**Research findings, not a working printer or a chosen design.**
[Full study](d3-engineering-study.md) · [calculations](d3-calculations.md) ·
[conceptual diagrams](d3-diagrams.md).

Two paired prints may be at different heights. One rigid frame carrying all four beds
cannot give those pairs independent vertical movement. It could help in the fully joined
mode, but partial modes would still need their own lifts and a safely detached frame.
Splitting the secondary frame into sections is another idea, not a feature already solved.

The simpler comparison is four bed lifts with measured alignment and independent support
against falling. Mechanical links could help keep a joined surface aligned, but linking
four already rigid guides can make them fight each other. The proposed central cross
must distinguish locating a bed, carrying its weight, and transmitting drive torque.
It cannot automatically keep four separate hot sheets flat or stop their expansion.

We preserved both versions of the proposed selector. Moving idlers to reroute a belt
changes its length, tension and tooth engagement during the switch. Keeping separate
belts installed and selecting a torque path avoids that changing geometry, but still
needs unloaded alignment, positive engagement and separate gravity restraint. Neither
is demonstrated. A small mathematical example shows why equal belt lengths at the two
endpoints do not prove the belt stays tensioned between them.

The new calculations also show why equal quarter-loads are a poor assumption, why an
off-center object may lift a support contact, and why a delayed catch can see much more
than the static bed weight. Those numbers are deliberately labeled assumptions, not
hardware ratings or passing test results. Earlier unfavorable thermal results remain intact.

Next, compare complete support/constraint paths, study a fully specified selector path,
and combine seam error with the unresolved toolhead/gantry clearances from D2. Qualified
mechanical, electrical/thermal and controls review is still required. No hardware was
operated or bought, and no architecture, component, CAD toolchain or license was selected.
The first physical proof remains separately reviewed two-bed docking and cross-seam printing.

Source-backed critique is welcome in [GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions).
