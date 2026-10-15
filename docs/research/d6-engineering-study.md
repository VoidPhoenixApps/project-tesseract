# D6 — electronics, firmware and independent-job scheduling

**2026-10-15, America/Chicago. Desktop research and synthetic software model only.**
No final electronics, firmware, mechanism, safety function, component or license is
selected. No hardware operation, configuration, import of firmware repositories or
reference CAD, purchase or cross-repository change is part of this work.

**Finding:** A publicly reproducible control architecture is plausible as a development
program, but no reviewed source establishes an off-the-shelf implementation of all eight
modes with four independent job lifecycles. Independent motion execution plus conservative
central admission deserves comparison with a centralized multi-queue implementation.
Neither repairs the unresolved D2 geometry or D3 support/selector mechanisms. The current
evidence cannot establish that the complete machine is implementable or reliable.

## Package and changed-file inventory

All additions are under `docs/research/`; parent research and requirements are preserved.

| File | Purpose |
| --- | --- |
| [Public summary](d6-public-summary.md) | Accessible conclusions, limits and contribution questions |
| [This study](d6-engineering-study.md) | Authority, comparison, dependencies and next experiments |
| [Firmware evidence](d6-firmware.md) | Documented capabilities versus missing job-control features |
| [Modes and supervisory states](d6-states.md) | Eight arrangements, states, ownership and guarded transitions |
| [Scheduling](d6-scheduling.md) | Geometry, conflicts, queue policy and model boundaries |
| [Channels and power](d6-electrical.md) | Conditional inventory and reproducible load sensitivity |
| [Safety requirements](d6-safety.md) | Stop distinctions, fault responses and review gates |
| [Editable diagrams](d6-diagrams.md) | Original Mermaid control, communication and transition diagrams |
| [Sources](d6-references.md) | Versions, primary references, limitations and component dependencies |
| [Model](d6_model.py) | Standard-library admission/state kernel and power arithmetic; no I/O to hardware |
| [Tests](test_d6_model.py) | Positive/negative synthetic fixtures and numerical regressions |
| [Results](d6-results.json) | Deterministic mode definitions and power/latency sensitivities |
| [Verification](d6-verification.md) | Actual checks, independent review and publication/reporting evidence |

## Authority and stack

Current GitHub main `952c2202bc001d1aff38fa7bce9a0b86410695d6` supplies AGENTS,
README, requirements, architecture, roadmap, contribution rules and research-first plan;
these files match the inspected D5 checkout. Clean tree and origin were verified before
branching. Current shared workflow, engineering, knowledge, secrets and review standards
were read at project-knowledge `147de4d979bba17120a4cc425983d590f85b6000`, matching
its remote main. No Tesseract project CURRENT_STATE exists there; none was invented.
Current Home Infrastructure instructions were read through GitHub. Cross-repository
synchronization was deliberately excluded by this task. AgentMemory was queried once;
returned records were unrelated and not used as evidence.

| Track | Open Draft PR | Inspected head |
| --- | --- | --- |
| D1 | [#25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25), targets main | `25eb8a745cf8c4ddc54d64a65159e26f756bbc93` |
| D2 | [#26](https://github.com/VoidPhoenixApps/project-tesseract/pull/26), targets D1 | `5957b80a5478e1cc669cbd7f81d71a5934326d63` |
| D3 | [#27](https://github.com/VoidPhoenixApps/project-tesseract/pull/27), targets D2 | `096ae806c08d437bf1c84c77d217cacdfd6f3231` |
| D4 | [#28](https://github.com/VoidPhoenixApps/project-tesseract/pull/28), targets D3 | `30367e326ae1eec1cfe62b7eb6c5eb1d30c9f7c5` |
| D5 | [#29](https://github.com/VoidPhoenixApps/project-tesseract/pull/29), targets D4 | `8c9321acedf9dda9b1cbbcba9f9bf3284a8b685d` |

D6 branch `codex/research-d6-controls-scheduling` starts from that exact D5 head and
must target `codex/research-d5-convertible-enclosure` as a Draft. D5's recorded AI
research review covers its package; its later reporting record does not imply human
approval. Live D5 had no GitHub review or comment. Preserve the entire parent stack;
no merge or parent modification is authorized.

## Requirements and inherited evidence

The unchanged [requirements](../requirements.md) remain mandatory targets: four nominal
180 × 180 mm heated beds and four individual sheets in every mode; automatic horizontal
conversion at a common fixed-height plane; all eight independent/paired/mixed/joined
arrangements; printable-first/Ender 3-sized printed parts; separately reproducible
imperial and metric reinforcement variants; later 2020 edition; removable tool-free
enclosure with both open and enclosed operation; editable sources and public reproduction.
Nominal dimensions do not establish usable volume. Four-head cooperation on one object
is a separate unproven stretch goal; baseline J uses one full-region head.

| Evidence | Control implication and retained limitation |
| --- | --- |
| [D1](d1-engineering-study.md) | Four independent progress coordinates in S; a shared axis or unified attached frame cannot provide them merely through more drivers |
| [D2](d2-mode-coverage.md) | Pair/full reach, entire parked structures and swept paths remain unproven; the hypothetical ±260 mm parks failed reach. D6 synthetic strips do not replace that negative result |
| [D3](d3-mode-constraints.md) | Separate position, load and transmission graphs; independent restraint and affected-domain closure required. A selector flag is not support evidence |
| [D4](d4-load-paths.md) | Shared-frame deflection can disturb an apparently unrelated job. Lock sensors need datums downstream of compliance/slip; motor counts are not surface metrology |
| [D5](d5-safety.md) | Ordinary open-air printing retains all modes; environmental-panel absence is not automatically a protective fault or interlock requirement. Hazard-specific assessment assigns necessary protection; distinguish panel handling, actual guard access and maintenance isolation |
| [Phase 1](../phase1/configuration-feasibility.md) | Rejected layout restrictions remain; queueing cannot make permanently unavailable required modes feasible |
| [Phase 1B](../phase1b/thermal.md) | Failed fixed-center-anchor gap interval remains. Four independently regulated temperatures can create differential seam motion |
| [Phase 1C](../phase1c/review.md) | Bounded CAD/checker evidence does not establish hot locks, capture, restraint or reliable sensors |

## Fair architecture comparison

A/B/C describe coordination placement, not specific boards. B may still have a host;
C specifically adds one authoritative admission/resource transaction layer. Independent
protective functions are a separate design obligation for all candidates.

| Candidate | Strength | Main burden / failure domain | Conditional research disposition |
| --- | --- | --- | --- |
| A centralized multi-queue firmware | One resource map and clock domain; easier coherent grouped motion and shared heater accounting | Must establish four interpreters/queues and independent lifecycle state; one planner/controller failure affects all groups; CPU/RAM/step-rate budget unknown | Retain RRF-like asynchronous execution as strongest documented queue precedent; four-job capability unproven |
| B separate region controllers | Each controller can own an ordinary single-job lifecycle; simple fixed S baseline; local clocks need not agree for permanently disjoint envelopes | Reconfiguring group ownership, crossing regions and bed-Z synchronization become difficult; split-brain ownership, shared power and fault propagation remain | Retain as a simpler fixed-partition baseline; region assignment alone fails both pair directions and J without added mechanisms/coordination |
| C independent executors plus central admission | One machine configuration/geometry authority with local buffered motion; can conservatively reserve disjoint volumes and stop scopes | Transaction epochs, acknowledgements, stale state, recovery and grouped-Z ownership need new engineering. Host failure and bus partition must not allow orphan execution | Retain for comparison, especially Z-A; do not assume distributed Z-E is solved by networked setpoints |
| One conventional active head / sequential queue | Least concurrent software; useful reference for joined-area execution | Fails simultaneous unrelated jobs | Reference only; not compliant substitute for S/R/C/M |
| Four isolated conventional printers | Strong reproducibility and failure isolation comparison | No automatic pairing or joined job; cannot meet complete brief | Reference only; no architecture selection |

No weighted score hides the missing geometry. If A can demonstrate four complete job
lifecycles without a maintained fork, its lower distributed-state burden could outweigh
C's modularity. If regions are mechanically independent and can keep whole-job swept
volumes disjoint, C avoids unnecessary microsecond synchronization of unrelated jobs.
Z-E/F may favor putting each connected lift group under one deterministic execution
authority, regardless of where independent-job admission runs.

## Prioritized decisions and experiments

1. **Firmware-only lifecycle contract experiment, subsequently authorized:** reproduce
four independent streams, different progress/temperatures, late job arrival, one pause,
one cancellation, and asymmetric completion in a pinned software-only harness. Compare
RRF queue limits with separate ordinary executors. Inspect resource release, pending
buffers, reconnect and barriers. This package does not run firmware or claim results.
2. **Mechanics/control interface contract:** establish candidate reach, whole-assembly
parks, stop envelopes, support graph and independently observable datums with D2–D5.
Reject an architecture that needs a shared moving resource continuously for unrelated
jobs. No detailed CAD until the existing research gate and explicit authorization.
3. **Group-Z timing/fault model:** compare one clock-domain lift group, mechanical
coupling and distributed followers under lost drive, latency and downstream slip.
Output maximum differential displacement with uncertainty, restraint energy and a
justified stop budget. No numeric safe skew limit currently exists.
4. **Power/interface inventory:** obtain exact proposed bed/hotend resistance/power,
driver supply demand, cable duty/flex data, board output ratings and ambient derating.
Compare staged startup with a supply sized for continuous worst-case demand. No purchase.
5. **Qualified review before implementation:** electrical distribution/protection,
controls/safety stop/restart independence, mechanical gravity/load paths and thermal
hazards. Require reviewed acceptance/abort limits, instruments/uncertainty and supervised
procedures before any energized or moving experiment. First physical proof remains
**two-bed docking and cross-seam printing**.

No durable knowledge repository edit is made. A later separately authorized project-knowledge
index/state entry could link D1–D6 and these unresolved gates; no existing project record
is available to update. Useful findings already live here, so no redundant memory save.
