# Project Tesseract

Project Tesseract is an early engineering concept for a reconfigurable multi-bed RepRap 3D printer: one machine intended to operate as four smaller printers, paired or mixed regions, or one larger printer. Its mechanics should give it a distinctive identity, with editable design data and reproducible community builds.

**Development status:** Early feasibility stage, with a published mechanical trade study for review. No CAD, mechanism, firmware, or prototype has been validated. The features below are design targets, not working capabilities.

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

The [Phase 1 mechanical trade study](docs/phase1/README.md) is available for critique; its rankings remain proposals. The first physical proof remains **two-bed docking and cross-seam printing**. Measure registration, seam gap, thermal drift, adhesion, and repeatability through dock/undock cycles before scaling to four beds. Thermal, electrical, moving machinery, heater wiring, collision avoidance, and emergency-stop behavior require reviewed evidence; a drawing or successful simulation alone does not validate a mechanism.

## Why this is an interesting engineering problem

Moving a bed is only the start: separate heated surfaces must return to a repeatable common plane, accommodate thermal expansion, and support a first layer across their seams. Locks, transport, sheet behavior, cable routing and printable-frame stiffness all interact. A convincing result needs measurements through repeated docking cycles, including failures.

The printable-first RepRap approach makes reproducibility part of the challenge: builders should eventually be able to make the printed parts on an ordinary Ender 3 and use documented local reinforcement stock. Imperial and metric interfaces must each work without mesh scaling, socket reaming or improvised shims.

## Follow, discuss, contribute

- **Follow progress:** star this repository to bookmark it and use GitHub Watch to choose notifications. Reviewed work and evidence live here.
- **Discuss ideas:** use [GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions). Questions and evidence-backed challenges to assumptions are welcome.
- **Contribute:** start with [the contributor guide](CONTRIBUTING.md), check [open issues](https://github.com/VoidPhoenixApps/project-tesseract/issues) and current PRs, and agree on a small scope before substantial work.
- **Discord:** [join Project Tesseract](https://discord.gg/45NYXMxKHg), start in `#welcome`, and discuss the first challenge in `#bed-docking`. The public invite was verified on 2026-10-12; [Community activation and newcomer testing remain pending](docs/community/activation.md).

You can help today with source checks, documentation, bounded research and reviewable calculations. Engineering proposals need specialist review; nobody needs to promise a complete printer to contribute.

## Documentation

| Document | Purpose |
| --- | --- |
| [Requirements](docs/requirements.md) | Complete approved brief, provenance, mandatory targets, preferences, and stretch goals |
| [Architecture](docs/architecture.md) | Candidate systems, constraints, tradeoffs, and unresolved decisions |
| [Roadmap](docs/roadmap.md) | Development phases and measurable engineering gates |
| [Contributing](CONTRIBUTING.md) | Contribution process, reproducible evidence, and review expectations |
| [Community preparation](docs/community/README.md) | Issue drafts, discussion and outreach drafts, and owner setup actions |
| [Discord reporting](docs/discord-reporting.md) | Automated development updates, setup, security boundaries and recovery |
| [Agent instructions](AGENTS.md) | AI engineering standards and repository workflow |
| [ChatGPT Project instructions](CHATGPT_INSTRUCTIONS.md) | Durable ChatGPT-specific rules; intended target for the short Project settings pointer |

The [original approved brief](https://github.com/VoidPhoenixApps/home-infrastructure/blob/75f40a677e00407e40b0995504476f473c4c23f7/3d-printing/reconfigurable-quad-bed-printer-concept.md) remains the historical source baseline. [Home Infrastructure](https://github.com/VoidPhoenixApps/home-infrastructure/blob/main/3d-printing/reconfigurable-quad-bed-printer-concept.md) now points to this repository as the maintained engineering authority. This is an original future printer, separate from Fireball, Enderwire, the existing Voron V2.4 plan, and the 1980s bowling-alley printer concept.

## Development and participation

There is no selected CAD environment, printer build command, firmware target or hardware BOM yet. Reporting automation has isolated software tests; it does not validate printer hardware. Begin with the requirements and contribution guide; propose bounded trade studies and test plans before detailed machine design or parts selection. Record failed experiments and rejected alternatives alongside successful results.

## Open-source intent and licensing

The project is intended to become fully open source, including hardware, software, and documentation. **Licensing remains undecided, and this repository is not currently distributed under a selected open-source license.** License selection and third-party compatibility require review. Third-party kits and assembled products are welcome in principle as a future ecosystem goal; this statement is not a license grant or a manufacturer endorsement.
