# Project Tesseract requirements

## Status and provenance

**Status:** Approved concept requirements ported for foundation review; no CAD, mechanism, firmware, or prototype has been validated. Planned features are not implemented capabilities.

The source is the [approved design brief captured 2026-10-10](https://github.com/VoidPhoenixApps/home-infrastructure/blob/75f40a677e00407e40b0995504476f473c4c23f7/3d-printing/reconfigurable-quad-bed-printer-concept.md), verified against GitHub `main` on 2026-10-11. The user subsequently selected **Project Tesseract** and this repository. The source's placeholder name and future repository-selection wording are superseded by that instruction. Its engineering requirements remain intact below.

The project intends to become fully open source. **Licensing is undecided; the repository is not currently distributed under a selected open-source license.** Commercial kits are an intended future permission, not an existing license grant.

## Requirement classification

- **Mandatory targets:** The four-bed geometry, horizontal automatic reconfiguration, fixed-height common reconfiguration plane, retained individual sheets, all listed layout capabilities, printable-first sequence, Ender 3 part envelope, both reinforcement standards, future 2020 edition, editable sources, reproducibility, and engineering gates are requirements. They are not promises of demonstrated feasibility. Infeasibility requires a documented requirement review rather than silently dropping a mode.
- **Preferences and proposed approaches:** Wording such as “prefer,” “investigate,” “candidate,” “may,” and “where practicable” retains its original qualification. Frame topology, motion systems, sensing, CAD tools, and software suggestions are not selections.
- **Stretch goal:** Four heads cooperating on one large print is separate from independent concurrent jobs and is not a baseline release gate.
- **Unknowns:** Usable build extent, tolerances, performance limits, exact stock sizes, architecture, electronics, CAD toolchain, budget, and license remain unresolved. Define measurable limits in reviewed test plans before claiming validation.

[Architecture](architecture.md) tracks candidate approaches and decisions; the [roadmap](roadmap.md) stages the evidence gates. Changes to approved requirements must identify the source clause, rationale, evidence, and review outcome.

## Vision

Create a mechanically distinctive printer immediately recognizable as its own design—not "another Voron-inspired printer." It should be simultaneously capable of being **one large printer or four smaller printers**, with the possibility of cooperative heads on one large part. The mechanism, not just cosmetic panels, should make it visually and functionally unique.

Embrace the original RepRap ethos: anyone should be able to build, inspect, modify, repair, improve, redistribute, or commercially kit the design. Make the process and design data available, not only exported STLs.

## Established product requirements / preferences

### Four modular beds; no manual conversion

- Four nominal **180 x 180 mm** heated bed modules, initially arranged as a 2 x 2 array.
- Four **individual build sheets remain installed** for all operating modes. No requirement for the user to replace them with a single larger sheet when combining beds.
- Nominal joined footprint: **360 x 360 mm** before any effective-area losses due to joins, mechanical margins, and travel limits. Do not promise an exact usable 360 mm build area without engineering verification.
- Bed modules **automatically reposition horizontally** as needed. They maintain a **common fixed-height build plane** through reconfiguration; vertical lifting/lowering as a reconfiguration method is not desired. Final Z-axis printing architecture is undecided.
- Beds must be able to join by rows or columns as well as all four together: a permanently diagonal-only separation mechanism is unacceptable.
- User prefers **press Print -> machine plans/configures itself**, not manual bed arrangements or changing sheets. Automatic configuration should respect already-running jobs and require empty/clear modules when rearrangement is needed.
- A **small visible line/mark on the underside of prints across sheet seams is acceptable**. Reliable adhesion, first-layer behavior, leveling, and safe nozzle transit across seams remain requirements.

### Intended layouts and printing modes

These are target behaviors subject to mechanical and software feasibility:

| Arrangement | Nominal joined regions / use |
| --- | --- |
| Four separated | 4 independent 180 x 180 mm print jobs |
| Two vertical pairs | 2 independent 180 x 360 mm regions |
| Two horizontal pairs | 2 independent 360 x 180 mm regions |
| Mixed pair + singles | One 180 x 360 or 360 x 180 region plus two 180 x 180 mm regions |
| All four joined | One nominal 360 x 360 mm region |

One, two, three, or four concurrently active jobs may be desirable depending on arrangement. Region size refers to **nominal bed geometry**, not yet validated printable extents.

**Stretch goal:** Four heads cooperatively contribute to a single large print, not just separate independent prints. A single head covering the entire joined bed is another candidate strategy; neither has been selected or proven. Do not assume an off-the-shelf slicer or Klipper configuration already supports collision-free multi-head cooperative printing.

### Two build variants, designed as one family

**Version 1 — printable/RepRap edition (design first):**

- Print every component that *reasonably and safely* can be printed, including a novel modular structural frame.
- **Every printed part must fit on an ordinary Ender 3 build plate**; precise allowable footprint, margins, print orientation, and material requirements to be established in CAD/test fixtures.
- Large structural members may consist of printable segments with mechanically sound joints.
- Investigate **internal metal reinforcement**, including Prusa-style smooth steel guide rods/linear shafts, threaded rods, or steel tube. Those are candidate structural members, not yet selected parts; size, stiffness, stress, fastening, thermal behavior, and load paths must be assessed.
- Printed structure should exploit printable trusses/lattices/topology and geometry—not copy a square aluminum-extrusion cage in plastic.
- Standard manufactured items such as bearings, motors, fasteners, electronics, heaters, and precision motion hardware are allowed where printing them would compromise function or safety.

### Imperial and metric reinforced-part variants (required)

For **every printed part or assembly that interfaces with structural metal stock** (for example steel tubing, smooth rods, threaded rods, or other reinforcement), provide **two maintained build options**:

1. **Imperial / US stock:** Parts and assembly instructions designed to fit commonly obtainable US fractional-inch metal stock.
2. **Metric / international stock:** Corresponding parts and instructions designed for commonly obtainable metric metal stock.

Requirements:

- Use a **single parameterized design family**, but generate **separately labeled, ready-to-print part variants** (and relevant STEP/STL/3MF outputs) for each stock standard. Builders must not need to edit CAD, scale STL meshes, hand-ream structural sockets, or invent shims merely to use their local standard.
- Specify actual purchasable material forms and **nominal versus actual dimensions**, including OD/ID or cross-section, wall thickness/gauge, length, material grade, and tolerances. In particular, **nominal pipe sizes are not necessarily real outer diameters**; do not equate pipe, tube, and precision shaft sizing.
- Dimension CAD interfaces to the selected stock's **actual measured or standardized physical size** with validated clearance/interference and fastening strategy; do not assume fractional-inch and rounded metric equivalents are interchangeable.
- Preserve mounting datums and the wider machine interfaces across both options wherever practical, while adapting sockets, joints, fastening, and reinforcement geometry appropriately.
- Publish distinct **BOMs, cut lists, assembly notes, parts naming, and version identifiers** so builders cannot accidentally mix incompatible reinforcement and printed joints.
- Verify fit, strength, stiffness, heat/creep behavior, and manufacturability for **both** standards before labeling either version released; validate any strength-critical substitutions and do not assume equal performance from superficially similar stock.
- The **Ender 3 printable-part envelope** applies to both standards.

**No rod, tube, or pipe size has been chosen yet.** Select actual regionally available profiles during the trade study; not all imperial and metric choices need to have identical nominal diameters, only proven compatible functional performance.

**Version 2 — 2020 aluminum-extrusion edition (adapt after printable version):**

- Use 2020 extrusion for the main frame; print most remaining mechanical parts.
- Preserve motion, bed modules, control architecture, and mechanical interfaces with the printed edition where practicable.
- Adapt joints/bracing and revalidate structural performance; an extrusion frame is **not** automatically a drop-in replacement for a printed truss.
- Prefer parts/common interfaces that enable upgrading a printed-frame machine to extrusion without replacing all costly components.

Both variants are intended to provide the **same core print capabilities**; no essential operating mode should be reserved only for extrusion without an explicit design review.

### Standard, readily available component policy

**Approved design requirement (2026-10-13):** Wherever reasonably possible, select standardized, readily available **off-the-shelf components** rather than unusual, proprietary, one-off, discontinued, or single-source parts. This applies to the proof rigs and both eventual printer editions, including motion hardware, bearings, belts, motors, fasteners, structural stock, sensors, connectors, power and control components.

- Prefer established, interchangeable specifications and parts that builders can readily source from multiple independent suppliers; consider regional availability, especially US/imperial and international/metric options.
- Evaluate sourcing, lifecycle/replacement availability, cost, documentation, serviceability, safety suitability, and practical substitutions during component trade studies and BOM reviews. A common part is not automatically mechanically or electrically suitable.
- Purpose-designed **3D-printed components** are expected in this RepRap design. Custom fabricated or unusual purchased components are exceptions only when needed to meet a documented functional, safety, or performance requirement that practical standard alternatives cannot satisfy.
- For each exception, document the reason, standard alternatives evaluated and rejected, manufacturability or procurement route, replacement/repair plan, and any supplier or availability risk before adoption.
- BOMs should identify actual specifications, compatible alternatives where validated, and sourcing constraints. Do not silently substitute superficially similar components; safety-critical and load-bearing replacements require the relevant verification.
- Do not let sourcing preference silently eliminate an approved mechanical capability or compromise safety; surface unavoidable conflicts for explicit design review.

### Open-hardware / community commitment

- Publish **native/editable parametric CAD source**, assemblies, editable manufacturing data, dimensioned drawings where needed, and STEP exports; publish STL/3MF print files as derivatives, not the sole source.
- Publish firmware, host software, configuration-planning logic, electronics/schematics/wiring, assembly and calibration procedures, complete BOM, tested sourcing alternatives, maintenance, and known limitations.
- Commercial kits and assembled products by third parties are **permitted in principle**. Favor readily obtainable parts, serviceability, and no unnecessary vendor lock-in; keep BOM workable for self-sourcing or curated kits.
- Open development history, tradeoffs, prototype failures, tests, and community contributions.
- License **not yet chosen**. Consider an appropriate open-hardware license (e.g. CERN-OHL family) plus compatible software/documentation licenses and check third-party component licenses; do **not** assert CERN-OHL-S was selected.
- User enjoys the LDO, Fabreeko, and Siboor approach to third-party Voron kits as an ecosystem example; **no partnership or manufacturer endorsement exists**.

## Design exploration directions (not settled architecture)

- Frame: distinctive triangulated/space-frame, reinforced printed trusses, or other load-appropriate, printable architecture; not merely an enclosure disguising a conventional cube printer.
- Bed positioning: motorized sliding mechanisms with controlled X/Y changes, repeatable mechanical locating/locking, thermal-expansion accommodations, heater-flex management, alignment sensing, and bed registration.
- Toolheads: candidate options include shared motion architecture, separately moving heads with overlapping reachable regions, or modular head systems. Requirement is to avoid collisions and support the planned modes, not to preselect CoreXY, multiple gantries, or robot arms.
- Software: supervisory configuration planner from incoming job geometry and queue constraints; verify position/lock states and surface status before print. Existing slicer object metadata and Klipper facilities may be useful inputs, **but do not imply they automatically solve reconfiguration, concurrent independent jobs, or cooperative multi-head paths**.
- Build-sheet sensing: optional automatic verification of sheet presence/identity if needed; no manual swap between modes.
- Useful reference machines to study: Elegoo OrangeStorm Giga and Voron Phoenix for segmented large print surfaces. Their fixed segmented beds do **not** establish feasibility of repeatedly docking moving heated plates.
- CAD implementation candidates: FreeCAD and/or build123d with Codex, with source-controlled parameterization and reproducible generation; Fusion can be used for investigation, but public reproduction should not depend on a paid/proprietary design tool.

## Hard engineering gates before claiming a workable design

1. **Bed seam proof:** Repeatable X/Y/Z register of two moving heated 180 mm surfaces; thermal drift, seam gap and adhesion; demonstrate a test object spanning the seam after repeated dock/undock cycles.
2. **Bed mechanism:** Confirm constrained motion reaches separated, paired, mixed and joined positions without interference; verify positive locks and detection, cable strain relief, heat-safe routing, and homing.
3. **Structural stiffness:** Calculate and measure deflection, torsion, vibration, creep, joint strength, and dimensional drift for printed/reinforced frame and extrusion variant.
4. **Head workspace:** Confirm actual reachable volumes, parking, collision envelopes, service access, toolhead coordination, and any real-time control requirements.
5. **Safety:** Enforce no motion while a person services the machine, no automatic repositioning into a printed object, safe heater control, E-stop/stop-state behavior, failed-sensor/failed-lock interlocks, wiring thermal limits, fault recovery, and supervised validation before unattended use.
6. **Software:** Safe scheduling/configuration that knows actual print footprints, not just four rectangles on a UI; reject impossible/unsafe jobs. Cooperative large-part printing is separately verified, not assumed.
7. **Reproducibility:** Demonstrate that somebody with an ordinary Ender 3 and documented off-the-shelf materials can print the complete printable-part set, assemble, calibrate, and maintain a working machine.

## Development approach / immediate next steps

1. **Preserve requirements first** (this document), avoiding premature printer styling, naming, CAD or parts orders.
2. Ask Codex for an **architecture trade study**, not a fully invented or prematurely finalized machine: bed motion/docking concepts, independent-vs-shared printhead reach, printed-frame load paths, kinematic constraints, and documented feasibility risks.
3. Begin with the **printable frame architecture** and Ender 3-compatible part envelope; maintain replaceable frame interfaces for the future 2020 version.
4. Build a **two-bed docking and seam test rig** as first mechanical proof, with precision measurements before scaling to four.
5. Compare concepts, revise requirements based on evidence, then create a native editable CAD assembly and staged BOM.
6. Only later choose motion electronics, firmware integration details, part suppliers, prototype budget, and licensing.

**Unresolved decisions:** Four-head versus shared-carriage mechanical approach; whether all heads can traverse entire joined area; joined-bed toolpath partitioning; exact bed travel and locking geometry; printer Z motion; materials/diameters of reinforcement; overall outer dimensions; speed/temperature goals; exact licensing; visual language. The current project name is Project Tesseract; the source brief predates that name.

## Relationship to existing work

This is an **unbuilt future printer design**, not a modification to Fireball, Enderwire, the existing no-compromises Voron V2.4 plan, or the 1980s bowling-alley printer concept. Do not conflate them or record candidate parts as currently owned/installed hardware.

Project Tesseract is the dedicated design repository selected for this foundation. The original Home Infrastructure brief remains the approved source baseline while this port is under review. Authority/link updates in Home Infrastructure and project-knowledge are deferred to a separate reviewed change; this PR does not silently complete that handoff.
