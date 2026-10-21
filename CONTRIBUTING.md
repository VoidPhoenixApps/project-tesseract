# Contributing to Project Tesseract

Project Tesseract is at the documentation and feasibility stage. No CAD or prototype has been validated. Start with the [newcomer reading path in the README](README.md#newcomer-reading-path), then use this guide to choose a bounded contribution. Contributions should help test the [requirements](docs/requirements.md), compare [architecture candidates](docs/architecture.md), or produce evidence for the [roadmap](docs/roadmap.md).

## Find a useful starting point

You do not need a workshop or a finished design. Pick a small question, check [open issues](https://github.com/VoidPhoenixApps/project-tesseract/issues) and [PRs](https://github.com/VoidPhoenixApps/project-tesseract/pulls), and say what you plan to investigate before duplicating someone else's work. The [Phase 1 study](docs/phase1/README.md) is a proposal to examine, not a settled architecture.

| Contribution | Useful submission today |
| --- | --- |
| Documentation or diagrams | One confusing passage or a clearly labeled conceptual diagram, with source links and editable source |
| Research | A bounded comparison using primary sources, revisions/access dates, applicability and limitations |
| Calculations | Equations, units, assumptions, parameter ranges, uncertainty and reproducible working; distinguish estimates from measurements |
| CAD proposals | A small interface or illustrative concept, native editable parametric source, tool versions and regeneration steps; label it unvalidated and do not assume a chosen toolchain |
| Test plans | A question, proposed measurement method, uncertainty, acceptance limits, hazards, supervision and abort criteria; a plan does not authorize testing |
| Mechanical critique | The exact assumption, why it may fail, supporting evidence, alternatives and what observation could resolve the disagreement |

[Proposed newcomer tasks](docs/community/issue-drafts.md) distinguish beginner documentation/source work from specialist engineering work. The navigation/glossary and conceptual-layout tasks are published as [issue #13](https://github.com/VoidPhoenixApps/project-tesseract/issues/13) and [issue #14](https://github.com/VoidPhoenixApps/project-tesseract/issues/14), with owner review confirmed. The other six remain drafts awaiting triage. Comment before starting to avoid overlapping work.

## Propose an idea or challenge an assumption

Use [Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions) for exploratory questions. Use the [existing issue templates](https://github.com/VoidPhoenixApps/project-tesseract/issues/new/choose) for a bounded engineering proposal, documentation problem, bug, or completed experiment report. For a test plan, use Engineering Proposal and clearly label all results as not performed.

Link the requirement and exact document revision/section you are questioning. Separate approved targets from proposed mechanisms; describe a counterexample or source, its limits, and an alternative. Challenging a mandatory target is welcome as a request for requirement review, never as permission to silently remove it. Critique the claim, treat people respectfully, and retain negative or inconclusive evidence.

GitHub owns durable decisions and evidence. [Join Project Tesseract on Discord](https://discord.gg/45NYXMxKHg) for conversation and progress; start in `#welcome` and use `#bed-docking` for the first engineering challenge. [Access verification and remaining setup limits](docs/community/activation.md) are recorded separately. Bring useful discussion conclusions back to a linked issue or PR.

## Open your first Draft PR

1. Fork the repository if you lack write access, and create a focused branch from current `main`. If another task uses your checkout, use a separate clean worktree.
2. Keep the change small, link the issue/discussion, and follow the workflow and verification rules below.
3. Push your branch to your fork or authorized repository. In GitHub, compare it against `VoidPhoenixApps/project-tesseract:main`, choose **Create draft pull request**, and use the PR template.
4. State what is ready for feedback, what has not been tested, and which decisions remain open. Draft status invites review; it does not approve a design.
5. A maintainer reviews scope and evidence; consequential architecture and safety changes require risk-appropriate independent review. Resolve findings and obtain human approval before merge. Record accepted decisions in their owning documents; preserve rejected alternatives and their rationale.

## Licensing status

The project intends to become fully open source, but no hardware, software, or documentation license has been selected. This repository is not currently distributed under a selected open-source license. Do not assume the planned openness or future commercial-kit ecosystem already grants a license. Identify authorship and third-party source/license information in contributions; resolve licensing and compatibility through review before adopting dependencies or release terms.

## Contributor workflow

1. Read the requirements and current repository state. For substantial work, identify the source requirement, uncertainty or failure being addressed and propose a bounded scope with acceptance criteria.
2. Check Git status and origin, preserve local work, and begin from a clean, current `main`. Create a dedicated feature branch; do not commit directly to `main` or rewrite shared history. Agents also follow [AGENTS.md](AGENTS.md).
3. For design changes, compare alternatives and document assumptions, load paths, constraints, risks and verification plans before treating a proposal as selected. Mechanical architecture, electronics, CAD toolchain and licensing require review.
4. Make focused changes with editable source and update the relevant documentation. Preserve failed experiments and rejected alternatives; link superseding conclusions to prior evidence.
5. Review the full diff, check scope, and perform the appropriate verification below. Stage only intended files and make focused commits.
6. Open a PR against `main` describing the problem, changed behavior/design, requirement coverage, evidence, limitations and open decisions. Use a Draft PR while review or evidence remains outstanding. Identify affected imperial/metric variants and frame editions.
7. Address findings and obtain human approval before merge. Safety-critical and consequential architecture changes need risk-appropriate independent review. Passing automated checks alone does not prove design intent or safety.

Do not modify linked source repositories merely to reconcile this repository's PR. Identify needed authority/context updates for separately authorized work after review.

## Engineering contribution standards

Start physical feasibility with two-bed docking and cross-seam printing before scaling to the complete machine. The printable-frame edition comes first; every printed part must fit an ordinary Ender 3. State the tested print envelope, orientation, margins and material/process settings rather than assuming a printer's nominal size establishes fit.

Maintain imperial and metric structural reinforcement options as separately labeled outputs from one parameterized family. Supply actual stock dimensions and tolerances, material grade, OD/ID or cross-section, wall thickness, cut lengths, fastening and fit details. Include separate BOMs, cut lists, naming/version identifiers and assembly notes; do not require builders to scale meshes or improvise adapters. Validate both standards, including strength-critical substitutions. The future 2020 edition must retain core capabilities and receive its own structural verification.

Use native editable parametric source and reproducible generation steps, with tool/dependency versions and parameters recorded when a toolchain is selected. Provide STEP and relevant STL/3MF derivatives alongside source, plus assemblies, drawings, wiring/schematics, configuration and manufacturing information appropriate to the change. Avoid proprietary or export-only dependencies that prevent public reproduction. No CAD toolchain is mandated yet.

Treat region dimensions as nominal until measured. Protect all required independent, paired, mixed and fully combined configurations; do not silently remove difficult modes. Keep four-head cooperative printing labeled as an unproven stretch goal distinct from independent concurrent jobs.

## Safety-critical work and experiment records

Thermal, electrical, moving machinery, heater wiring, collision avoidance and emergency-stop changes need reviewed hazards, controls and measurable evidence. A documentation or software contribution does not authorize an unsafe physical trial. Before energized/moving tests, agree on safe conditions, supervision, abort criteria and pass/fail thresholds. Prevent service motion and movement into existing objects; test fault and recovery paths as well as successful operation. Validate under supervision before making unattended-use claims.

For each experiment, record:

- Question, relevant requirements, hypothesis and alternatives.
- Design/source revision, stock variant, materials, equipment, software and operating conditions.
- Procedure, acceptance limits, cycle/sample counts, calibrated measurement method and uncertainty.
- Raw results, photos/logs as useful, repeatability and comparison with the agreed limits.
- Failures, unexpected behavior, limitations, tradeoffs, conclusion and next action.

Retain negative and inconclusive evidence. Clearly label simulation, calculation, bench testing and machine testing; one does not stand in for another. Reassess relevant tests when parts, material, stock, wiring or control behavior change.

## Verification and PR handoff

For documentation changes, check requirement preservation and classification, cross-document consistency, Markdown headings/tables/fences, internal links and intended file scope. Run `git diff --check` and, after staging, `git diff --cached --check`. Review new files as well as tracked-file diffs.

For future design/software changes, run the applicable reproducible generation, parameter/variant, dimensional, build, test and safety-evidence checks. Document exact commands or procedures, results and skipped checks with reasons. There is no printer build or CAD-generation pipeline. For reporting automation, run `python3 -m unittest discover -s tests -v`; its isolated CI and mocked software tests do not establish hardware validation. See [Discord reporting](docs/discord-reporting.md) for the integration trust boundaries and activation procedure.

The PR should enumerate changed files, cite requirements and evidence, explain unresolved choices, identify unavailable references, and state which durable context needs a separate source-repository update. Never include credentials or secret values in files, logs, examples or PR descriptions.
