# Contributing to Project Tesseract

Project Tesseract is at the documentation and feasibility stage. No CAD or prototype has been validated. Contributions should help test the [requirements](docs/requirements.md), compare [architecture candidates](docs/architecture.md), or produce evidence for the [roadmap](docs/roadmap.md).

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

For future design/software changes, run the applicable reproducible generation, parameter/variant, dimensional, build, test and safety-evidence checks. Document exact commands or procedures, results and skipped checks with reasons. This foundation has no executable build, CAD generation, test runner or CI to run; documentation verification does not establish hardware validation.

The PR should enumerate changed files, cite requirements and evidence, explain unresolved choices, identify unavailable references, and state which durable context needs a separate source-repository update. Never include credentials or secret values in files, logs, examples or PR descriptions.
