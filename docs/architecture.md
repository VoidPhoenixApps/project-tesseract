# Project Tesseract architecture exploration

**Status:** Candidate architectures only. No final mechanical architecture, electronics system, firmware integration, CAD toolchain, or license is selected. No CAD or prototype has been validated.

The [requirements](requirements.md) preserve the approved brief. This document organizes its exploration directions and proposes comparison criteria; it does not approve a design. The [roadmap](roadmap.md) defines the evidence needed to advance.

The [urgent toolhead/printing-Z exploration backlog](concepts/toolhead-z-motion-exploration.md) captures the 2026-10-14 multi-independent-head, moving-bed/moving-gantry/dual-Z, and automatically coupled bed-Z concepts for integrated trade study. **All remain unreviewed candidates**, not choices or approved requirements.

The [Phase 1 mechanical trade study](phase1/README.md) compares bed transport, six-degree-of-freedom docking, configuration paths, preliminary thermal/structural estimates and a proposed two-bed proof plan. Its rankings and numerical test criteria are proposals for review; no architecture is selected and no engineering gate has passed.

## Constraints for every candidate

The [Phase 1B investigation](phase1b/README.md) extends the Phase 1 baseline with precision-interface constraints, thermal-anchor comparisons, packaging envelopes and two-bed cartridge recommendations. Its analytical conclusions remain conditional; final architecture and physical-test approval are still open.

- Four nominal 180 × 180 mm heated modules must support separated, row-paired, column-paired, mixed, and fully joined layouts. A permanently diagonal-only mechanism is unacceptable.
- Reconfiguration is automatic and horizontal, with a common fixed-height build plane and four retained individual sheets. This does not select the printing Z mechanism.
- Nominal region sizes do not establish reachable or printable areas. Measure sheet margins, seam losses, travel limits, and tool access.
- Preserve running jobs, require empty/clear modules for rearrangement, and check actual object footprints and collision envelopes.
- Develop the printable frame first. Every printed part, including imperial and metric variants, must fit an ordinary Ender 3 with verified orientation and process margins.
- Use one parametric reinforcement family with separately labeled, ready-to-print imperial and metric outputs, BOMs, cut lists, and validated physical interfaces. Do not substitute rounded dimensions or assume equivalent performance.
- Plan replaceable interfaces for the later 2020 frame and the same core printing capabilities across editions; structural equivalence requires testing.
- Support [convertible, removable enclosure panels](requirements.md#convertible-removable-enclosure) for enclosed and open-air printing in both structural editions and both imperial/metric reinforced-frame variants, preserving all required layouts, motion envelopes, service access and operating capabilities.

## Candidate systems and trade studies

The following are proposed study directions, not selected components or proven solutions.

| Subsystem | Candidates from the brief | Questions and evidence needed |
| --- | --- | --- |
| Printable frame | Triangulated/space-frame geometry, reinforced printed trusses, load-appropriate lattices | Compare load paths, joint behavior, stiffness, torsion, vibration, printability, heat/creep, and service access. Avoid merely copying an extrusion cube in plastic. |
| Reinforcement | Smooth steel rods/linear shafts, threaded rods, steel tube or other reviewed stock | Compare regional availability, actual dimensions, grade, mass, fastening, stress, thermal behavior, and cost. Prove both imperial and metric interfaces rather than scaling meshes. No stock size is chosen. |
| Bed reconfiguration | Motorized horizontal sliding with controlled X/Y travel and repeatable locating/locking | Compare reachable layouts, constrained degrees of freedom, lock detection, homing, thermal expansion, registration, heater-flex routing, and interference. Travel geometry and actuator arrangement remain open. |
| Toolhead motion | Shared motion, separately moving heads with overlapping reach, modular head systems | Map actual workspace, parking, service access, collision envelopes, concurrent-job capability, and control timing. Do not preselect CoreXY, multiple gantries, or robot arms. |
| Joined-region coverage | Single head covering the joined region; multiple heads partitioning work | Prove coverage and seam transit. Four-head cooperation on one object is a separately gated stretch goal, not assumed slicer behavior. |
| Supervision | Job-geometry and queue-aware configuration planner | Determine safe configurations, verify position/lock/surface state, protect running jobs, and reject impossible jobs. Slicer metadata and Klipper facilities are possible inputs, not complete solutions. |
| Sheet verification | Optional sheet-presence/identity sensing | Assess whether sensing is needed and how surface readiness can be established reliably. Retaining four sheets and avoiding manual swaps remain mandatory regardless of sensing choice. |
| CAD authoring | **Fusion 360 is the maintainer's strong preference if feasible**; FreeCAD and build123d remain full alternatives or potential reproducible companions | Compare native editable design history, assemblies, parameterization, reproducible imperial/metric variants, STEP and other interchange, source/version-control workflows, collaboration and license restrictions (including personal and commercial contributors). Demonstrate a usable public reproduction path that does not require a paid/proprietary tool. Fusion is preferred, **not yet selected**. |
| Convertible enclosure | Removable-panel materials and attachment methods to compare; no mounting or material solution selected | From the beginning, compare structural interfaces, thermal expansion, ventilation, chamber monitoring, fire safety, electronics temperature limits, moving-part protection, ready availability and practical service access. Demonstrate mandatory tool-free panel installation/removal and configuration changes entirely by hand, without structural disassembly or dismantling the primary frame, motion, electronics or heated-bed mechanisms. Verify secure retention during normal operation and convenient removal/reinstallation; keep the attachment mechanism open for evaluation. |
| Future frame | 2020 aluminum extrusion with adapted joints/bracing | Reuse costly components and interfaces where practical, then revalidate loads and modes; it is not automatically a drop-in replacement. |

Elegoo OrangeStorm Giga and Voron Phoenix are reference machines identified by the brief for studying segmented surfaces. Fixed segmented beds do not prove that moving heated beds can repeatedly dock. Reference names imply neither adopted architecture nor endorsement.

## Proposed interface records

Before detailed integration, propose and review records for bed mounting datums, the common build plane, docking/lock state, frame attachments, reinforcement variant identity, head workspace, heater/sensor connections, and supervisory state. Include coordinate conventions, units, tolerances, thermal assumptions, failure states, and version compatibility. These records are a documentation approach, not a prescribed controller or bus.

The frame interfaces should accommodate imperial/metric joints and later extrusion while preserving common datums where practical. Record any necessary divergence explicitly, including effects on calibration and interchangeability.

## Safety-critical design review

Thermal control, electrical protection, moving machinery, flexing heater wiring, collision avoidance, and emergency-stop behavior are safety-critical. Before energizing or moving a prototype, review hazards, test conditions, controls, and pass/fail limits appropriate to that prototype. Electrical and thermal ratings, wire routing/strain relief, travel and pinch envelopes, and stop behavior need calculations and physical evidence.

The design must prevent motion during servicing and repositioning into printed objects. Define and test failed-sensor and failed-lock responses, heater faults, stop states, fault recovery, and safe restart. The exact protective circuits, controller, interlocks, and emergency-stop implementation remain decisions for review; a software stop command alone is not evidence of an adequate emergency-stop system. Validation must be supervised before any unattended-use claim.

Retain raw measurements, conditions, instrument limitations, failures, and repeatability results. Analysis and simulation support testing but do not replace proof of a physical mechanism. Gate procedures and evidence requirements are in the roadmap.

## Open decision register

Every item below is **unresolved**. A proposal must compare alternatives, cite requirements, state assumptions and risks, supply evidence, and record a maintainer-reviewed decision before it becomes the baseline.

| Decision | Evidence or review needed |
| --- | --- |
| Bed travel, docking and lock geometry | Two-bed registration/seam proof, layout reach, locking and fault tests |
| Shared-carriage versus multi-head mechanics | Workspace, concurrency, parking and collision study |
| Whether all heads can traverse the entire joined area | Measured or modeled reach followed by physical verification |
| Joined-bed path partitioning | Scheduling and seam strategy; separate cooperative-printing feasibility work |
| Printing Z motion | Load path, precision, bed-plane compatibility and collision review |
| Printed-frame topology and reinforcement profiles | Structural comparison, regional stock specifications, both variant tests |
| Ender 3 envelope, materials and orientations | Verified usable print volume, margins, process constraints and printed fixtures |
| Enclosure implementation and chamber conditions | Trade study of panel materials, mounting and interfaces across both editions and reinforced-stock variants; enclosed/open-air capability and access evidence. Active heating, filtration, exhaust, temperature targets and additional safety measures require separate decisions; enclosure support does not approve active chamber heating. |
| Outer dimensions and usable print volumes | Full travel/clearance study and measured prototype limits |
| Speed, acceleration, temperature and material targets | Reviewed operating envelope and acceptance limits before performance claims |
| Electronics, power system and firmware integration | Channel/timing needs, heater loads, wiring, interlocks and fault response review |
| CAD toolchain and reproducible export process | Editable-source and variant-generation demonstration |
| Suppliers and prototype budget | Staged BOM with tested alternatives and explicit purchasing review |
| Hardware/software/documentation licenses | Compatibility and third-party license review; no license selected |
| Visual language | Functional/mechanical identity consistent with the printable-first design |

Project Tesseract is the selected project name for this foundation. That resolves the source brief's placeholder name only; it does not resolve machine styling or architecture.

## Decision and experiment preservation

Keep reviewed decisions and experiment records in version control as work begins. Include the source revision, alternatives considered, rejected options and reasons, constraints, measurements, uncertainty, and next action. Preserve failures; supersede an earlier conclusion with a linked correction rather than deleting the evidence. Do not record proposed or candidate parts as purchased, installed, or validated hardware.
