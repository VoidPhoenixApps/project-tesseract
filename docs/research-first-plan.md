# Research-first architecture phase — public plan

**Recorded:** 2026-10-14. **Maintainer direction:** Prioritize research and comparison of **all current Project Tesseract architecture concepts before undertaking further detailed CAD development**. This work is deferred until the maintainer has time. The community should be able to see the research, alternatives, evidence and reasoning, not just a finished CAD outcome.

**Status:** Planning direction, not completed research or an approved mechanism. Nothing here selects hardware, software, CAD, printer configuration, numerical acceptance limits, or a license. Existing Phase 1/1B/1C source, evidence and unfinished work must be retained; do not silently discard earlier CAD or rewrite its conclusions. No physical work is authorized by this plan.

## Why the order changes

Independent toolhead movement, Z ownership, coupled/selected lifts, bed docking and registration, frame compliance and safety are coupled decisions. More fixture or printer CAD now could prematurely embody one architecture and hide contradictions with the required separated, paired, mixed and fully joined configurations.

Use existing [requirements](requirements.md), [architecture](architecture.md), [roadmap](roadmap.md), [Phase 1](phase1/README.md), [Phase 1B](phase1b/README.md), [Phase 1C](phase1c/README.md) and [detailed toolhead/Z concept backlog](concepts/toolhead-z-motion-exploration.md) as the starting evidence. These records vary in evidence strength and do **not** establish a validated printer.

## Scope to research before new detailed CAD

| Track | Questions to answer and public output |
| --- | --- |
| Bed travel and mode changes | Compare independent XY carriers, row mechanisms and other viable transport paths; demonstrate feasible and infeasible arrangements/transition sequences for all five required layouts in conceptual kinematic diagrams |
| Registration, docking and seams | Study 6-DOF constraints, hot/cold references, thermal expansion, four-sheet seams, load transfer, horizontal-only docking and repeatability; preserve the quantitative negative results and assumptions from Phase 1/1B |
| Printing Z | Compare gantry/head Z, individual bed Z, dual-Z handoff, short-stroke hybrid head Z, automatically coupled bed Z and servo/belt-switched secondary lift; explain mode-specific actuation, positive support, homing, failure modes and intermediate pair/mixed modes |
| Toolhead XY and packaging | Compare independent gantries, shared motion rails with truly independent carriers, four local plus full-region head, modular systems and the precise mirrored A/B/B/A toolhead orientation; evaluate true nozzle reach, full swept collision envelopes, parked heads and unrelated Z progress |
| Structural systems | Compare printable-frame load paths, stiffness/creep/vibration, Ender 3 print envelope, actually sourceable imperial/metric reinforcement stock and later 2020 adaptation; avoid assuming dimensional interchangeability |
| Convertible enclosure | Study tool-free panel interfaces, frame/heat/motion clearances, removal/service paths, passive chamber environment, ventilation and thermal/electrical risks; no active chamber heating is approved |
| Motion electronics, firmware and scheduling | Assess independently scheduled jobs, coupled-group state transitions, sensors/locks, safe reconfiguration, heating/power, fail-safe behavior and controller feasibility without assuming an existing slicer or Klipper solves coordination |
| Reproducibility and manufacturability | Evaluate standard/obtainable components, serviceability, accurate sourcing, BOM complexity, editable parametric sources and a publicly reproducible CAD path without requiring paid/proprietary tools |

**Scope guard:** Four nominal 180 × 180 mm modules with retained individual build sheets, automatic horizontal rearrangement at a common fixed-height reconfiguration plane, all separated/paired/mixed/joined modes, printable-first and both reinforcement standards, later 2020 edition and removable enclosure remain approved targets. Four-head cooperation on one large object remains an **unproven separate stretch goal**, not a prerequisite for baseline joined-area coverage.

## Future Codex CAD reference-parts library (planning only)

**Stage A implementation (2026-10-15; pending PR review):** The [reference-parts catalog and workflow](../cad/reference-parts/README.md) now contain 34 candidates across 13 categories, a schema, validation and one explicitly authorized local Adafruit STEP sample. The maintainer selected the sibling library on Forbidden Fruit; read access and file/hash checks are recorded in [Stage A verification](../cad/reference-parts/verification.md). CAD import/dimension checks remain pending. All other models are link-only. This supersedes the library-only planning status below; it does not authorize detailed printer CAD, hardware selection, additional downloads or physical work. The heading is retained for existing links.

### Historical library proposal — 2026-10-14

The following proposal records the original alternatives and gates. Its uncreated-folder and planning-only statements describe that earlier state; use the Stage A workflow above for current library operations. Rights, missing-model and engineering safeguards continue to apply.

**Maintainer preference (2026-10-14):** When detailed CAD resumes, make it easier for Codex to reuse legitimate, accurate third-party CAD models of standard purchased parts rather than recreating every motor, bearing, pulley, hotend, sensor, rail and fastener. Evaluate local downloads on **Forbidden Fruit** first and a reproducible approach usable on POTUS and by community contributors. This is a **proposed workflow**, not an established library, completed installation, vendor choice or authorization for bulk downloads.

**Proposed two-layer architecture:**

1. **Local vetted models:** Consider a dedicated sibling reference folder such as `~/Development Projects/tesseract-cad-library/` on Forbidden Fruit; this example path is **not created or verified**. Maintain a corresponding explicitly configured read-only Codex project source folder, **in addition to** the existing required `project-tesseract` Primary and `project-knowledge` additional source. Verify that the actual local Codex session can list/reference models; adding a folder path alone is not proof of CAD import or GUI control. The alternative of a clearly gitignored `local-cad-references/` under the project should be compared for sandbox practicality, with safeguards against accidental commits.
2. **Public provenance/catalog in Tesseract GitHub:** Track part category, manufacturer, exact manufacturer/part number, source URL, publication/access date and revision, candidate geometry and material, units/coordinate axes, model format, file hash where legitimately obtained, dimensional/tolerance confidence, use permissions (local Codex reference, derivatives, public redistribution, automation), and download/recovery instructions. Keep source identities and permitted reproduction instructions accessible to collaborators even when original files cannot be redistributed.

**Format guidance:** Prefer STEP (`.step`/`.stp`) for portable solid reference geometry and retain native editable manufacturer CAD if available and legitimately usable. Keep reference geometry separate from **Tesseract-authored editable parametric parts**, which still need independently reproducible source. STL-only mesh geometry is a last-resort clearance reference, not authoritative precision or a substitute for editable engineering CAD. PDF drawings/datasheets can be more trustworthy than simplified vendor models for fits and tolerances.

**License/rights gate:** Public download availability does **not** establish permission to redistribute the CAD asset or insert it into openly shared assemblies. Review the current source terms for each library/vendor before local AI-agent processing, automated retrieval, derivative design use, repository distribution or commercial redistribution; record the reviewed permission and source. A provider such as McMaster-Carr has materially restrictive CAD-model terms; **do not bulk ingest, copy into GitHub, redistribute or claim AI-use permission without a specific acceptable rights basis**. For sources with unclear rights, record the link/specifications without sharing or automatically downloading the file. Never scrape sites against their terms. Project Tesseract's eventual open-source licensing remains undecided.

**Proposed workflow on resume:** First audit any files already legitimately owned/available; choose a small sample of reviewed and genuinely relevant parts; inspect manufacturer drawings and actual stock standards (metric/imperial are not interchangeable); download **only after rights review and authorization**; fingerprint and catalog files; test read access and a reproducible one-part STEP import/placement through the chosen CAD tool; compare imported geometry with authoritative dimensions; record an exact rebuild procedure and any platform-specific differences. Do not claim an AI can reliably understand CAD geometry merely because it can read binary filenames. Geometry inspection/manipulation still needs a suitable CAD engine or reviewed automation.

### Missing manufacturer-model rule for future CAD tasks

**Maintainer direction (2026-10-14):** Codex should **ask for a missing purchased-part CAD model instead of redesigning a component merely because that model is unavailable locally**. Absence from the reference folder is a missing dependency, **not a reason to alter the part choice, fabricate dimensions or quietly invent an equivalent**.

For each task that needs a purchased component's geometry:

1. Check the approved local reference folder **and** the GitHub provenance catalog for the **exact selected manufacturer and part/revision**, including expected units and model format. If the component has not been selected, keep that as an unresolved sourcing decision rather than inventing a choice.
2. If the needed model is missing, incompatible, unverifiable or restricted, **pause only dependent detailed CAD work** and ask the maintainer for the model or authorization to obtain an acceptable version. The request should name the exact part or proposed part options, needed format (preferably STEP), official source link when established, intended use, reason geometry is needed, rights/availability uncertainty, and what work is blocked.
3. Give the maintainer a short actionable **missing-model list**, rather than repeatedly asking one part at a time if several dependencies are known. Accept a legitimately supplied file or a reviewed source; catalog its part/revision, source, permission, hash and geometry checks before CAD use.
4. Never silently substitute another motor/rail/fastener/hotend, approximate unverified physical interfaces, reverse-engineer a proprietary model or redraw an off-the-shelf part as a fake manufacturer model to keep work moving. A conservative **explicitly labeled non-fabrication clearance placeholder** may be proposed **only with maintainer authorization** and traceable source dimensions; it must not be promoted to a fit-validated model.
5. Continue unrelated documentation, calculations, approved original printed-part design or other unblocked work where safe. Report missing geometry and its design impact at handoff. Do **not** download, redistribute or ingest rights-restricted models without appropriate permission and task authorization.

This rule applies when preparing future CAD work. The separately authorized Stage A sample is documented above; the rule itself does not authorize additional downloads, reconfiguration or detailed printer CAD during the research-first pause.

**Storage and portability:** Keep protected source assets out of public Git where redistribution is not allowed. Publish approved-redistribution files only after their rights are confirmed, using sensible size/version controls. Ensure Forbidden Fruit and POTUS access are verified separately, with machine-local details recorded in **Home Infrastructure**, not duplicated as unverified device state in Tesseract. Do not assume Codex Cloud, local Codex Desktop, Fusion 360, FreeCAD or build123d have identical file-system, licensing, import or automation capabilities.

**Deliverables for later:** (a) approved reference folder and Codex read-only verification on each intended machine; (b) traceable catalog/manifest with rights flags, sources and hashes; (c) one sample cross-platform part import and envelope/dimension audit; (d) reproducible assembly workflow with usable fallback when a vendor model is unavailable/restricted. These are preparatory research/library tasks, **not permission to resume detailed architecture CAD**.

## Work sequence when research resumes

1. **Inventory and evidence map:** Link existing calculations, negative findings, concept notes and unresolved assumptions. Mark each item as requirement, hypothesis, analytical result, independent review or measured evidence. Do not redo work that is already reproducible unless checking a discrepancy.
2. **Public architecture matrix:** Make one traceable matrix crossing XY-A–E with Z-A–F against the five mandatory layout types. Separate mechanically impossible combinations from plausible-but-unproven ones. Identify active-object protection, collision and load-transfer constraints.
3. **Bounded research per candidate:** Use dated primary references, clear mechanisms, source/license information, parameterized estimates, loading/DOF diagrams and explicit uncertainty. Report both strong and weak arguments, not just a favored layout.
4. **Integrated comparisons:** Rank a small shortlist against all targets, safety/complexity/reproducibility and failure cases. Include simpler baselines. Record eliminated candidates, circumstances where rankings change, and serious dissent.
5. **Review before CAD continuation:** Request suitable independent mechanical/electrical/safety critique. Publish open questions and measurable test proposals. The maintainer reviews the trade study before authorizing further detailed architecture CAD. After review, resume **bounded** CAD needed to discriminate remaining candidates rather than committing to a full-machine model.
6. **Physical evidence remains subsequent:** The first physical proof is still the reviewed two-bed docking and cross-seam rig. Require reviewed hazards, explicit acceptance/abort criteria, measurement uncertainty, supervision and recorded failures before operating any prototype.

### What the public should see

Every completed research track should have a **readable public summary** in GitHub (with a stable link), plus its underlying source citations and reproducible calculations/figures where useful:

- Plain-English question, why it matters to builders and the required printing modes.
- Clear **labeled diagrams** (top/side views, mechanism and motion/clearance sketches), with editable source when created; conceptual art never presented as proof.
- Side-by-side alternatives showing advantages, liabilities, sourceable components, likely failure points and what remains unknown.
- Actual references, revisions/dates, assumptions, units, numerical sensitivity/ranges and code or formulas sufficient for reproduction.
- Decision and verification status: proposed, screened out with rationale, unresolved, independently reviewed or physically measured. Preserve failed or inconclusive approaches.
- An invitation to challenge assumptions or contribute better evidence through [GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions); keep reviewed conclusions in GitHub, using Discord for conversation and meaningful factual updates.

Do **not** describe publication, a PR, an animation or successful software checks as evidence that a mechanical design works. Publish milestones only when meaningful; the established Discord reporting workflow is not a mandate to announce every exploratory note.

## Exit condition for the research-first pause

New detailed printer/fixture CAD should resume only after a reviewed research package identifies:
- Requirements traceability for every mandatory mode and the current constraints/risks.
- A reasoned short list of *integrated* bed/head/Z/structure approaches, with showstoppers and uncertainties called out.
- Preliminary reproducible estimates for thermal drift, seam registration, lift loads, swept head coverage, collisions and safety-related faults appropriate to the proposed CAD scope.
- A prioritized list of narrow CAD experiments needed to resolve remaining uncertainty, plus the evidence each experiment must produce.

These are **planning/review criteria**, not assertions that research has been performed or physical engineering gates passed. The maintainer can authorize a specific exception, such as preserving, diagnosing or finishing an existing narrow CAD/evidence artifact, without treating it as approval for a new mechanical architecture.

**Resumption prompt:** Start at the existing concept backlog and Phase 1/1B/1C evidence. Produce the public mode × XY × Z compatibility matrix and an evidence inventory first. No new detailed CAD or hardware actions until the maintainer explicitly requests them.
