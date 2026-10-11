# Project Tesseract

Project Tesseract is an early engineering concept for a reconfigurable multi-bed RepRap 3D printer: one machine intended to operate as four smaller printers, paired or mixed regions, or one larger printer. Its mechanics should give it a distinctive identity, with editable design data and reproducible community builds.

**Development status:** Documentation foundation and feasibility planning only. No CAD, mechanism, firmware, or prototype has been validated. The features below are design targets, not working capabilities.

## Goals and planned features

- Four nominal **180 × 180 mm heated bed modules** in an initial 2 × 2 array.
- Automatic horizontal reconfiguration into independent, row-paired, column-paired, mixed pair-plus-singles, and fully joined layouts, maintaining a common fixed-height build plane during reconfiguration. Printing Z motion remains undecided.
- Four individual build sheets retained in every mode, without swapping in one large sheet. The joined footprint is nominally **360 × 360 mm**; usable print extents must be measured.
- Job-aware configuration that protects running prints, requires clear modules for rearrangement, and prevents collisions.
- A printable-frame edition first, with every printed part fitting an ordinary Ender 3; separate ready-to-print imperial and metric structural reinforcement variants from one parametric design family.
- A later **2020 aluminum-extrusion edition**, preserving core capabilities and common interfaces where practical.
- Native editable parametric CAD, derivative manufacturing files, firmware/software, wiring documentation, BOMs, calibration, maintenance, and reproducible build instructions.

Four-head cooperative printing on a single large part is an **unproven stretch goal**. It is distinct from running independent jobs. No final mechanical architecture, electronics system, CAD toolchain, or license has been selected.

## First engineering milestone

Start with an architecture trade study and a **two-bed docking and cross-seam printing proof**. Measure registration, seam gap, thermal drift, adhesion, and repeatability through dock/undock cycles before scaling to four beds. Thermal, electrical, moving machinery, heater wiring, collision avoidance, and emergency-stop behavior require reviewed evidence; a drawing or successful simulation alone does not validate a mechanism.

## Documentation

| Document | Purpose |
| --- | --- |
| [Requirements](docs/requirements.md) | Complete approved brief, provenance, mandatory targets, preferences, and stretch goals |
| [Architecture](docs/architecture.md) | Candidate systems, constraints, tradeoffs, and unresolved decisions |
| [Roadmap](docs/roadmap.md) | Development phases and measurable engineering gates |
| [Contributing](CONTRIBUTING.md) | Contribution process, reproducible evidence, and review expectations |
| [Agent instructions](AGENTS.md) | AI engineering standards and repository workflow |

The [original approved brief](https://github.com/VoidPhoenixApps/home-infrastructure/blob/75f40a677e00407e40b0995504476f473c4c23f7/3d-printing/reconfigurable-quad-bed-printer-concept.md) is the source baseline for this foundation. Cross-repository authority/link updates will follow separately after review. This is an original future printer, separate from Fireball, Enderwire, the existing Voron V2.4 plan, and the 1980s bowling-alley printer concept.

## Development and participation

There is no selected CAD environment, build command, firmware target, test runner, or hardware BOM yet. Begin with the requirements and contribution guide; propose bounded trade studies and test plans before detailed machine design or parts selection. Record failed experiments and rejected alternatives alongside successful results.

## Open-source intent and licensing

The project is intended to become fully open source, including hardware, software, and documentation. **Licensing remains undecided, and this repository is not currently distributed under a selected open-source license.** License selection and third-party compatibility require review. Third-party kits and assembled products are welcome in principle as a future ecosystem goal; this statement is not a license grant or a manufacturer endorsement.
