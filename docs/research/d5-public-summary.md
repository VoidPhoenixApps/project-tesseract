# D5 — can the enclosure come off by hand?

**Research only, 2026-10-15. No enclosure has been selected, built or validated.**

Project Tesseract must print with its environmental panels on or off. Those panels must
come off and go back on entirely by hand, without taking apart the frame, motion system,
electronics or heated beds. All eight bed arrangements must remain available in either
state, including automatic bed changes with panels installed.

Three concepts deserve further comparison: panels supported on a lower ledge with positive
hand fasteners; framed doors on removable hinges; and panels sliding out of captured edges
where there is enough extraction room. Magnets can help locate a panel, but they are not
assumed to be adequate safety restraints. Snap clips also need evidence of repeated use
and warm-temperature durability.

Polycarbonate, acrylic, tempered glass, metal and mixed transparent/opaque panels all have
tradeoffs. A clear panel can scratch, crack or expand; glass adds weight and vulnerable
edges; metal can conduct heat into handles and creates electrical-protection questions.
Manufacturer temperature and fire-test numbers do not certify a printer enclosure.

The calculations show why small details matter. A hypothetical 600 mm polycarbonate panel
warms and grows 1.56 mm at a 40 K temperature rise. That can jam a tightly captured edge.
Another example clears a panel while installed but blocks it when lifted for removal.
Neither example represents selected hardware or proves that a proposed mechanism works.

A passive enclosure can also trap enough heat to threaten printed joints, motors or
wiring. Our simple heat balances demonstrate sensitivity to leakage and uneven heating;
they do not establish actual chamber temperatures, safe ventilation or fire containment.
Active heating, exhaust, filtration and operating-temperature targets remain unresolved.

The largest open issue is protection with panels absent. The machine cannot depend on
removable walls for its primary stiffness, gravity support or sole essential guarding.
A panel-presence switch or firmware pause does not resolve that problem. Qualified
mechanical, electrical/thermal and safeguarding review is needed before adoption.

Read the [engineering study](d5-engineering-study.md), [comparisons](d5-materials.md),
[eight-mode matrix](d5-mode-clearance.md), [calculations](d5-calculations.md) and
[next investigations](d5-next-investigations.md). Challenge assumptions or bring better
source evidence in [GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions).
The first physical proof remains two-bed docking and cross-seam printing, under a
separately reviewed procedure. D1–D4's unresolved reach, support and thermal findings
remain intact; a larger enclosure cannot make an unreachable parked head reachable.
