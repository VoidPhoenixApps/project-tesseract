# Proposed newcomer issues

**Drafts for maintainer review; none have been opened.** Recheck current issues, PRs and the active engineering investigation before assigning any task. Each block contains the complete suggested title, labels and body. All submissions follow [CONTRIBUTING](../../CONTRIBUTING.md); labels do not approve engineering results. Maintainers should confirm an available reviewer before applying `good first issue`.

## 1. Documentation navigation audit — beginner

```markdown
Title: Audit the newcomer reading path and explain five unfamiliar terms
Labels: documentation, good first issue

Start at https://github.com/VoidPhoenixApps/project-tesseract/blob/main/README.md and follow CONTRIBUTING.md, docs/requirements.md and docs/phase1/README.md.

Scope: report broken or confusing navigation and propose plain-language explanations for five terms already used (for example datum, registration, repeatability, seam step and thermal drift). Link each term to its existing technical context.

Deliverable: one small documentation PR with a before/after reading path and source-backed explanations. Preserve requirements and proposal/measurement distinctions.

Done when: every changed link resolves, explanations agree with source context, and a maintainer checks technical wording. Do not invent tolerances, change gates or imply hardware validation. No hardware work is required.
```

## 2. Layout diagram — beginner with technical wording review

```markdown
Title: Draw an editable overview of the required bed layouts
Labels: documentation, good first issue

Read https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/requirements.md and docs/phase1/configuration-feasibility.md before drawing.

Scope: one conceptual overview of separated, horizontal-pair, vertical-pair, mixed pair-plus-singles (both orientations), and fully joined arrangements. Reuse the study's conventions rather than proposing motion paths.

Deliverable: editable SVG or text-based diagram source with accessible text descriptions, four individually identified retained sheets, nominal 180 × 180 mm module labels and a clear “concept; not a validated mechanism or usable print area” caption.

Done when: every required arrangement is represented, labels match the requirements, sources/revisions and reproduction instructions are included, and a maintainer reviews it. Do not depict a selected frame, head arrangement or collision-free transition. No CAD or hardware is required.
```

## 3. Regional reinforcement sources — beginner research, specialist adoption

```markdown
Title: Collect supplier specifications for one imperial and one metric reinforcement candidate
Labels: documentation, good first issue

Read https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/requirements.md (reinforcement variants) and docs/phase1/preliminary-calculations.md. Ask the maintainer which material form is useful before starting.

Scope: collect two current purchasable listings, one US fractional-inch and one metric, for the agreed form. This is a source inventory, not a BOM or equivalence recommendation.

Deliverable: table of manufacturer/supplier links, access date, region, material grade, nominal and actual dimensions, OD/ID or cross-section, wall thickness where applicable, tolerances and available lengths. Mark unspecified fields unknown; distinguish pipe, tube and precision shaft dimensions.

Done when: each entry has a traceable specification and unavailable data is explicit. A specialist must assess fit, stiffness and suitability before adoption. Do not round dimensions into interchangeability, design sockets, buy stock or recommend substitution.
```

## 4. Docking evidence comparison — specialist review

```markdown
Title: Add a bounded evidence comparison for two docking interfaces
Labels: help wanted, engineering-review

Start from https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/phase1/docking-registration.md and coordinate with the active precision-docking investigation. Select one unanswered comparison with its maintainer; do not repeat the whole trade study.

Scope: compare two existing candidate interfaces using at least three primary sources. Explain which degrees of freedom are constrained, how locking/preload and thermal accommodation differ, and what the cited repeatability actually measures.

Deliverable: a short comparison with source revisions, units, operating conditions, contamination/wear considerations and a proposed way to discriminate between candidates on the two-bed rig.

Done when: carrier registration is distinguished from hot sheet/seam behavior, missing evidence is explicit and a mechanical reviewer checks applicability. No mechanism selection, fabricated measurements, construction or energized testing. Newcomers may help collect sources; engineering conclusions need relevant expertise.
```

## 5. Thermal source check — specialist review

```markdown
Title: Audit one thermal-expansion assumption in the Phase 1 calculations
Labels: help wanted, engineering-review

Read https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/phase1/preliminary-calculations.md and coordinate with its current contributor to choose one input rather than rewrite the study.

Scope: locate primary material data for the chosen expansion coefficient, including grade and temperature range. Reproduce the affected equation with explicit units and vary that input across its sourced range.

Deliverable: a small reproducible calculation and source note identifying assumptions, uncertainty and implications for what must be measured. Separate uniform expansion estimates from warping, gradients and interface constraints.

Done when: another reviewer can reproduce the numbers and a thermal/mechanical reviewer agrees that the source applies. Do not adopt operating limits or claim seam performance. This is desk research, not a heated experiment.
```

## 6. Printable-frame joint comparison — specialist review

```markdown
Title: Compare two printable-frame joint concepts against an existing load path
Labels: help wanted, engineering-review

Start at https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/phase1/motion-architectures.md and agree with the maintainer on one load path and two joint concepts to investigate.

Scope: a two-page comparison of stiffness, creep, fastening, assembly, service access and how each concept could accommodate separately generated imperial/metric interfaces. State assumed loads, materials, datums and print orientation rather than inventing final design values.

Deliverable: editable conceptual sketches and an evidence/gaps table. Identify how both concepts could respect the ordinary Ender 3 part envelope and printable-first sequence; explain what later measurement would be needed.

Done when: a structural reviewer checks assumptions and alternatives remain proposals. Do not select a topology, reinforcement size, allowable load or final frame; no simulation or sketch establishes strength. No physical testing is included.
```

## 7. Parametric toolchain sample — contributor with CAD experience

```markdown
Title: Demonstrate reproducible variants with two candidate CAD toolchains
Labels: help wanted

Read https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/architecture.md (CAD authoring) and CONTRIBUTING.md. Agree on a tiny nonstructural demonstration part and candidate tools with the maintainer before substantial work.

Scope: use the same synthetic parameters to evaluate two publicly reproducible candidate workflows. The part is a tool demonstration, not a printer component or a selected structural interface.

Deliverable: native editable parametric sources, tool/dependency versions, commands or steps, distinct variant identifiers and STEP plus relevant mesh exports. Include provenance/licenses for third-party content and limitations of editing, regeneration and export.

Done when: a reviewer can regenerate both variants without a paid/proprietary dependency or mesh scaling, and differences are documented. Do not select the project's CAD toolchain or present example dimensions as approved stock sizes. No physical fit claim is expected.
```

## 8. Failure-mode evidence — safety specialist review

```markdown
Title: Research one two-bed docking failure and its detection limits
Labels: help wanted, engineering-review

Read https://github.com/VoidPhoenixApps/project-tesseract/blob/main/docs/phase1/risks-and-decisions.md and docs/phase1/two-bed-proof-plan.md. Agree on one existing failure case, such as a false lock indication, without duplicating active safety work.

Scope: collect primary evidence describing how that failure can occur, what a sensor does and does not establish, and which fault/restart questions a future reviewed test plan must answer.

Deliverable: a short evidence table covering trigger, consequence, detection limits, candidate controls and unresolved questions. Link the existing risk instead of declaring a new approved safety architecture.

Done when: a qualified safety/mechanical/electrical reviewer, as appropriate, checks the claims and identifies remaining uncertainty. Literature work is not safety approval. No wiring changes, bypasses, powered tests, emergency-stop design adoption or unattended-readiness claims are authorized.
```
