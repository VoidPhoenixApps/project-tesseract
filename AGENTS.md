# Project Tesseract agent instructions

## Scope and authority

This repository contains the engineering foundation for a future reconfigurable quad-bed RepRap printer. No CAD, mechanism, firmware, or prototype has been validated. Keep claims consistent with that state until measured evidence and review establish otherwise.

1. Follow the newest explicit user instruction.
2. Read [README.md](README.md), [requirements](docs/requirements.md), [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), and [contribution rules](CONTRIBUTING.md) relevant to the task; inspect actual repository state before editing.
3. Consult the [shared development workflow skill](https://github.com/VoidPhoenixApps/project-knowledge/blob/main/.agents/skills/voidphoenix-development-workflow/SKILL.md) and applicable engineering, knowledge, secrets, and independent-review standards in the sibling `project-knowledge` checkout or its GitHub repository. Read a project `CURRENT_STATE.md` first when one exists there. Do not invent a missing project record.
4. The [original approved brief](https://github.com/VoidPhoenixApps/home-infrastructure/blob/75f40a677e00407e40b0995504476f473c4c23f7/3d-printing/reconfigurable-quad-bed-printer-concept.md) remains the historical source baseline; [Home Infrastructure](https://github.com/VoidPhoenixApps/home-infrastructure/blob/main/3d-printing/reconfigurable-quad-bed-printer-concept.md) now links to this repository as the maintained engineering authority. Consult current [Home Infrastructure instructions](https://github.com/VoidPhoenixApps/home-infrastructure/blob/main/CHATGPT_INSTRUCTIONS.md) before work involving household machines, printers or infrastructure.
5. Project-knowledge owns durable cross-project standards and project context it records; this repository owns actual design/implementation artifacts and evidence. Surface conflicts rather than silently overriding either source. Current GitHub documents and measured evidence outrank memory or chat recollection.

When AgentMemory is available, retrieve relevant continuity once at the start of substantial work. Avoid repeated unrelated searches; report unavailability without blocking authoritative source work. Save only useful durable context not already adequately recorded in repositories.

## Model selection

Follow the [shared model-selection policy](https://github.com/VoidPhoenixApps/project-knowledge/blob/main/System/CODEX_MODEL_SELECTION.md): Astra Light is the normal baseline; recommend Astra Medium for difficult engineering analysis, architecture, debugging, or review, with a brief reason near the start. Reserve higher settings for unusual difficulty. Default does not imply automatic escalation; model/session selection is user-controlled. Never reduce safety, correctness, or verification to save usage.

## Engineering requirements

Preserve the complete requirements document. In particular, retain four nominal 180 × 180 mm heated beds, automatic horizontal reconfiguration at a common fixed-height plane, four individual sheets in every mode, all independent/paired/mixed/combined layouts, printable-frame-first development, Ender 3-compatible printed parts, distinct imperial/metric reinforcement variants, a later 2020 edition, editable parametric sources, and reproducible builds. Four-head cooperation on one object remains an unproven stretch goal. The first physical proof is two-bed docking and cross-seam printing.

Distinguish mandatory targets, preferences, proposed approaches, unknowns, and stretch goals. Do not silently pick a final mechanical architecture, electronics system, CAD toolchain, reinforcement stock, or license. Present alternatives and evidence for review. A bounded rig component choice does not select the final machine. Do not promise exact usable build area from nominal bed dimensions.

Prefer the smallest change that satisfies the task. Preserve working artifacts and source history. Keep units, datums, tolerances, materials, variant identifiers and operating conditions explicit. Check actual purchasable stock sizes; imperial and rounded metric values are not interchangeable. Keep both variants reproducible without builder CAD edits, mesh scaling, socket reaming, or improvised shims.

## Safety and evidence

Treat thermal systems, electricity, moving machinery, heater wiring, collision avoidance, and emergency-stop behavior as safety-critical. Require risk-appropriate independent review before adopting consequential architecture or safety changes. Do not energize hardware, run moving-machine tests, purchase components, or alter physical systems merely because documentation work is authorized.

Before physical testing, require a reviewed hazard assessment, safe test procedure, measurable acceptance limits, measurement uncertainty, abort criteria, and supervision appropriate to the experiment. Prevent motion during service and reconfiguration into printed objects. Verify heater controls, locks/sensors, cable strain relief and thermal limits, emergency-stop states, fault recovery, and restart behavior. Do not bypass protections to make a test pass or claim unattended readiness before supervised validation.

A render, CAD assembly, simulation, calculation, or successful software check does not by itself validate a mechanism. Record raw measurements, revisions, conditions, repeatability, failures and limits. Never fabricate passing tests or treat nominal dimensions as measured capability.

## Source and documentation standards

- Keep native editable parametric CAD, assemblies, manufacturing sources and reproducible generation instructions. STEP and STL/3MF are useful derivatives; meshes alone are insufficient. Public reproduction must not require a paid/proprietary tool.
- Update the narrowest document that owns a changed fact. Keep requirements, architecture decisions, roadmap state, BOMs, wiring, build/calibration instructions and known limitations consistent as those artifacts are introduced.
- Preserve rejected approaches, tradeoffs and failed experiments with their rationale and evidence. Supersede conclusions explicitly instead of erasing failed results.
- Cite source revisions and distinguish proposals from owned/installed/validated hardware. Do not conflate this project with other household printer builds.
- The project intends to become fully open source, but licensing is undecided. Do not add a license, imply an existing open-source grant, or select CERN-OHL-S without review. Track third-party sources and license compatibility.
- Never commit credentials, keys, tokens, private authentication material, or secret values. Record only non-secret configuration and secret-location references where necessary.

## GitHub workflow and verification

Inspect Git status, branch and origin first. Start from a clean, current base; preserve unexpected local work and report divergence. Do not auto-stash, reset, clean, force-push or overwrite another contributor's work to bypass a guard. Respect the user's repository scope; do not run cross-repository synchronization when source repositories must remain unchanged.

Use a dedicated feature branch and focused commits, then a pull request against `main`. Follow an explicitly requested branch name; otherwise use a descriptive `codex/` prefix. Review the complete diff and stage explicit intended paths. Push only authorized, reviewed changes. Keep requested Draft PRs in draft and do not merge without explicit human approval.

Run checks appropriate to the artifacts. For documentation, review requirement coverage, classification, cross-document consistency, Markdown structure, internal links, scope, and `git diff --check` (including the staged diff before commit). For future CAD/software, add reproducible generation, fit/envelope, simulation and software checks as applicable; physical claims still need physical evidence. No CAD toolchain or printer build system is established. Discord reporting has isolated Python tests and CI; these do not validate printer hardware.

Report every changed file, reasons, checks actually performed, skipped checks and why, unresolved decisions, unavailable sources and remaining risks. Identify required durable knowledge updates without claiming they were made. Keep Home Infrastructure and project-knowledge changes separate when the task excludes them.

## Automatic Discord development reporting

Follow [Discord reporting](docs/discord-reporting.md). Once the reviewed integration is active on `main` and its channel-scoped secrets are authorized, automatically dispatch meaningful public project updates without asking for repeated approval. Report completed design milestones, approved decisions, measured experiments, confirmed significant failures/blockers and important task/phase completions. This rule directs reporting during active Codex work; it does not create a background agent.

Each update must state what was accomplished, why it matters, actual verification and its limits, unresolved work, and a relevant GitHub link. Label concepts, simulations, software checks and physical tests accurately. No untested design is validated. Never include secrets, private information or unsupported safety/release claims. GitHub remains authoritative.

Use `gh workflow run discord-reporting.yml --ref main --json` with public JSON input as documented. Use a stable milestone ID, inspect previous runs to avoid duplicates, and avoid routine chatter, every commit, or a redundant summary of an automatic merge announcement. Dispatch acceptance is not delivery: inspect the run and the actual Discord message. Do not blindly retry ambiguous failures or bypass missing authorization; report the blocker. Do not read or request webhook secret values for ordinary reporting.
