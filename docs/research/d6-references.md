# D6 — primary-source ledger and unresolved dependencies

**Accessed 2026-10-15, America/Chicago.** Rolling pages may change. Repository/release
identities were queried from GitHub without importing or redistributing firmware source.
No cited subsystem proves the Tesseract machine. Feature summaries below identify scope;
engineering deductions are explicitly D6 proposals in the linked study.

## Firmware and controls sources

| ID / primary source | Revision / retrieved evidence | Applicability and limitation |
| --- | --- | --- |
| K1 [Klipper releases](https://www.klipper3d.org/Releases.html) | Latest listed release 0.13.0, 2025-04-11; upstream master observed `9cb99754c035b90206ef0a02660f674fc9517e9b`, committed 2026-10-13 | Rolling configuration/developer docs may include post-release features; no claim all current features are in 0.13.0. GitHub releases/latest returned 404; official release page used |
| K2 [Code overview](https://www.klipper3d.org/Code_Overview.html) | Rolling developer page, accessed date above; host move flow, clocks and timed MCU queues | Basis for separating coordinated step execution from independent job lifecycle; no four-job implementation tested |
| K3 [Configuration reference](https://www.klipper3d.org/Config_Reference.html) | Rolling sections dual_carriage, generic_cartesian, heaters, verify_heater | Carriage and thermal facilities, not a complete multi-job scheduler or independent safety system |
| K4 [Multi-MCU homing](https://www.klipper3d.org/Multi_MCU_Homing.html) | Rolling page; latency/overshoot and same-axis MCU restrictions | A specific homing protocol, not a collision/protective response bound |
| K5 [MCU commands](https://www.klipper3d.org/MCU_Commands.html) and [FAQ](https://www.klipper3d.org/FAQ.html) | Rolling pages; output defaults, refresh/clock mechanisms | Firmware monitoring cannot switch off a physically shorted power output |
| R1 [RRF 3.7.0 release](https://github.com/Duet3D/RepRapFirmware/releases/tag/3.7.0) | Published 2026-10-08; tag commit `d5749c55a061136e856e9cde191f8020a94d5aa6`; described as first stable 3.7 release | Current baseline for future experiment; release says Duet 2 is no longer supported. No installation performed |
| R2 [G-code dictionary](https://docs.duet3d.com/User_manual/Reference/Gcodes/M586) | Current indexed full dictionary supplied M595–M599, M606, M959 descriptions; accessed date above | Queue count is build-dependent; collision and timeout primitives have narrow scope |
| R3 [M596](https://docs.duet3d.com/User_manual/Reference/Gcodes/M596), [M606](https://docs.duet3d.com/User_manual/Reference/Gcodes/M606) | Canonical command links resolve, but browser text extraction empty; descriptions checked in R2 | No claim that independent file readers supply independently managed job lifecycle |
| R4 [RRF changelog](https://github.com/Duet3D/RepRapFirmware/wiki/Changelog-RRF-3.x) | Context7 returned version-labeled 3.6.4/preparation entries involving pause/axis release and synchronization fixes | Regression-test prompts, not proof those bugs persist in 3.7.0; indexed historical text is not current release authority |
| L1 [LinuxCNC code notes](https://linuxcnc.org/docs/html/code/code-notes.html) | Rolling architecture documentation; task/interpreter, motion and IO layers | Custom-control reference; no native four-printer lifecycle claim |
| L2 [LinuxCNC v2.9.10](https://github.com/LinuxCNC/linuxcnc/releases/tag/v2.9.10) | Published 2026-07-03; separate latest API entry named v2.10.0-pre2, published 2026-09-28 | Use stable 2.9 reference for comparison; do not confuse a release name containing pre2 with a verified stable target |

Context7 was consulted for firmware documentation; its RRF result mixed historical
version entries and is treated as a discovery aid. Current release identity and primary
command descriptions govern. The attempted generic Duet Multiple_motion_systems URL was
not retrievable, and the wiki variant redirected to the wiki home. Dedicated M597/M599/
M959 extraction also failed; their text was available in R2. Record these retrieval gaps
rather than claiming the dedicated guide was read. No exhaustive target-build source
audit or firmware runtime experiment was performed; maximum usable queues and independent
lifecycle semantics remain open.

## Electrical and safety references

| ID / source | Revision / scope | Use and limitation |
| --- | --- | --- |
| E1 [Mean Well LRS-600 manufacturer specification](https://www.meanwell.com/Upload/PDF/LRS-600/LRS-600-SPEC.PDF) | Current PDF retrieved through indexed text; exact printed revision not established | Example of output rating, inrush and derating information required; no supply selected, no curve value adopted |
| E2 [Duet 3 wiring guide](https://docs.duet3d.com/en/How_to_guides/Wiring_your_Duet_3) | Rolling manufacturer documentation | Candidate board-specific wiring/rating reference for later selection; no wiring design copied or approved |
| S1 [HSE maintenance guidance](https://www.hse.gov.uk/work-equipment-machinery/maintenance.htm) | Current public guidance; isolation and stored-energy/support discussion | Engineering reference for maintenance distinctions; not local legal advice or compliance assessment |
| S2 [HSE L22 guidance](https://www.hse.gov.uk/pubns/priced/l22.pdf) | Public work-equipment guidance, fourth edition 2014 | Stop and emergency-stop discussion supports distinction from routine operation; not a complete applicable standards review |
| S3 [Inherited D5 source ledger](d5-references.md) | Includes machinery guarding/interlock standard catalog references and retrieval limits | Full normative standards not acquired; no certified design or prescribed performance level inferred |

Power numbers, channel counts, latency examples and synthetic geometry are authored
hypothetical assumptions in [electrical study](d6-electrical.md) and [model contract](d6-scheduling.md),
not values extracted from E1/E2. Source revisions must be rechecked when actual parts,
firmware builds and protective functions are proposed.

## Dependency and reproducibility register

| Missing dependency | Why it matters / next evidence | Current disposition |
| --- | --- | --- |
| Exact bed/heater/hotend part and revision | Resistance tolerance, temperature/power ratings, insulation, sensor attachment and replaceability | No final selection; all numerical loads hypothetical |
| Motor/driver/board interfaces | Supply demand, step-rate limits, thermal derating, IO and queue capacity, faults and documentation | No board shortlist promoted to design; manufacturer specifications required |
| Locks, selectors, brakes, restraints | Load ratings, fail states, engagement diagnostics, timing and downstream support | D3 mechanisms remain unresolved; no part or sensor assumed sufficient |
| Protective devices / interlocks | Qualified risk allocation, switching ratings, diagnostics, independence and restart design | No certified safety path or chosen stop category |
| Whole-machine geometry / sensor datums | Swept volumes, reachable parks, uncertainty and thermal/mechanical influence | D2–D5 still unresolved; test strips are not substitutes |
| Firmware build and host/executor contract | Four-job lifecycle, group-Z ownership, resource release, loss/reconnect and reproducible builds | Current primary docs support investigation, not complete solution |
| Public reproduction / third-party rights | Firmware and board dependencies, toolchains, CAD rights and compatible distribution terms | No paid runtime selected or required by model; third-party dependencies need rights audit before import/distribution; Tesseract license remains undecided |

No purchased-part interface CAD is created, so no reference-model request blocks this
D6 package. Future CAD must use exact manufacturer part/revision, approved model folder
and provenance catalog. If absent/uncertain, request the maintainer's correct STEP/native
file or approval for a source, with geometry purpose and rights/accuracy uncertainty.
No invented dimensions, substitute vendor models, bulk downloads or firmware repository
redistribution occurred. The Python model is original, dependency-light and locally
reproducible; that is not a license grant for the currently unlicensed repository.
