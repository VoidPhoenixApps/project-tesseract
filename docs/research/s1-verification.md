# S1 — verification and delivery record

**2026-10-16 · Software-only research, not printer validation.**

## Authority and scope

Started from clean main `d8473d6b1e87667fdbc506f8437d1326337d3b19`, matching fetched
origin/main; branch `codex/s1-software-feasibility`. Origin and existing worktrees
inspected; unrelated Phase 1C worktree/branch preserved. Read issue #46, current
CHATGPT_INSTRUCTIONS/AGENTS, README, requirements, architecture, roadmap, contribution
rules, D6 firmware/scheduling/model, D7 integration, D8 assembly/motion and D9 support.
Shared workflow skill and engineering/development/review/knowledge/secrets/model
standards read at project-knowledge `147de4d979bba17120a4cc425983d590f85b6000`, matching
GitHub main. No Tesseract CURRENT_STATE exists there. Current Home Infrastructure
instructions read remotely. No cross-repository changes or synchronization performed.
AgentMemory queried once; unrelated results not used. No duplicate memory saved.

## Changed files

| File | Reason |
| --- | --- |
| [s1-study.md](s1-study.md) | Concise recommendation, eight modes, capability/decision tables, slicer strategy and next experiment |
| [s1-sources.md](s1-sources.md) | Pinned implementation evidence, release/license metadata and retrieval limitations |
| [s1-architecture.md](s1-architecture.md) | Editable Mermaid boundaries/state diagrams and proposed developer contracts |
| [s1_contract.py](s1_contract.py) | Original small metadata/epoch wrapper and visible synthetic lifecycle trace; reuses unchanged D6 |
| [test_s1_contract.py](test_s1_contract.py) | Nine offline acceptance/negative tests |
| [s1-results.json](s1-results.json) | Reproducible synthetic progress/state trace with occupied-conversion rejection |
| [s1-verification.md](s1-verification.md) | This evidence, limitations and handoff record |
| [research-first-plan.md](../research-first-plan.md) | Narrow navigation/status pointer, retaining detailed-CAD pause |

Requirements, architecture decisions, roadmap gates and previous research artifacts
are unchanged. No upstream code, reference CAD, firmware or third-party dependencies
were imported. All new code uses existing Python 3.9 standard library.

## Reproduction and actual evidence

From repository root:

```sh
python3 -B -m unittest discover -s docs/research -p 'test_*.py' -v
python3 -B -m unittest discover -s tests -v
python3 -B docs/research/s1_contract.py > /tmp/tesseract-s1-results.json
cmp docs/research/s1-results.json /tmp/tesseract-s1-results.json
git diff --check
git diff --cached --check
```

- Research suite: **132 tests passed**, including nine new S1 tests and 123 inherited
  tests. S1 trace reproduced byte-for-byte.
- New tests cover all eight mode counts, differing synthetic progress/height/layer/
  temperature metadata, late arrival, individual pause/resume/cancel, retained finished
  and cancelled occupancy, failed occupied conversion, successful empty-domain round
  trip with unaffected job progress, stale submission after S→M12→S, atomic metadata
  rejection, shared XYZ/heater resource conflicts, J exclusivity, obstructed park and
  transition route, global fault/reconnect/reset and stale observations.
- Self-review caught reset epoch invalidation after faults raised inside the inherited
  D6 model. Added Coordinator.reset and a negative stale-ticket regression. The first
  regression attempt correctly refused reset while evidence was still stale; the
  final test supplies fresh synthetic evidence before reset. No physical recovery
  claim follows from this test.

- Repository suite: **84 tests passed**; **216 total** across both suites.
- Local Markdown links, table columns, fenced blocks and final newlines checked;
  Python source parsed against Python 3.9 grammar. Mermaid diagrams inspected as
  source; no renderer execution claimed.
- Requirements, architecture, roadmap and D6 kernel compared against main: unchanged.
  Complete intended diff reviewed, including new files; working/staged whitespace
  checks passed before commit. No credential-like content found in intended files.

No test here executes Klipper, RRF, Moonraker, a slicer or real G-code.

## Independent read-only review

Separate AI reviewer inspected the stable report/code, issue acceptance criteria,
requirements and D6–D9 context, and then the verification record. It independently
ran nine S1 and 25 D6 tests, all passing, and spot-checked RRF's compiled two-system
limit and Prusa's project-plugin boundary. Final recommendation: **APPROVE for
research publication**, 0 Critical / 0 Important / 0 Minor remaining findings.
Overall confidence Medium; test confidence High within the synthetic scope.
Broader 132/84 suite results are primary-agent verification, not reviewer reruns.
This is not human merge approval or qualified engineering signoff.

## Limits and skipped work

The model checks supplied metadata, AABBs and resource sets, not their correctness
against a printer. No threaded race, crash persistence, distributed commit, buffer/stop
latency, heater dynamics, actual mesh transform, intermediate conversion or firmware
adapter is implemented. Runtime bugs and exact target-build semantics remain open.
The report's U/I/X/F/M classifications are sourced engineering judgments; green tests
do not independently prove them. Diagrams are editable conceptual text, not measured
CAD or simulated hardware. No external renderer was installed.

Firmware/slicer builds, installs, forks/clones, services, actual slicing, MCU connections,
physical motion/heating, purchases and detailed CAD were skipped because this task
explicitly excludes them. Dedicated Duet command-page extraction failed; aggregate
indexed documentation and pinned release source were used, with the gap retained in
[sources](s1-sources.md). No exact four-job RRF build or tested safe reconfiguration
implementation was found. Full-machine physical feasibility remains unresolved.

No final architecture or license adoption is requested. Independent AI review is for
research correctness; consequential adoption still requires qualified controls/
mechanical/electrical review and explicit maintainer decisions. After acceptance,
a separately authorized project-knowledge update could link this report and its
software integration gates; no existing Tesseract project record should be invented.
Home Infrastructure needs no duplicate engineering report. Neither repository changed.


## Publication and reporting

Research commit `ea03e87b5b94e5ec0aebf1278cf3626cd3169aca` published in
[Draft PR #47](https://github.com/VoidPhoenixApps/project-tesseract/pull/47), targeting
main and linked to issue #46. [Initial CI](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38867010363) passed. No merge performed. Final delivery-record commit changes
only this verification document; CI status is checked separately at handoff. Existing
CI runs the repository suite and whitespace checks, not the research suite.

Inspected 52 retained Discord reporting runs; none used the S1 milestone ID.
Dispatched `s1-software-feasibility-study` once with public fields and evidence category
`software`, explicitly limiting evidence to synthetic tests and source research.
[Run 38867044725](https://github.com/VoidPhoenixApps/project-tesseract/actions/runs/38867044725)
succeeded and acknowledged message `1560554108015083591`. The actual
[development-channel message](https://discord.com/channels/1558743337735954512/1558750555097145384/1560554108015083591)
was inspected through native Discord accessibility: accomplishment, recommendation,
132/84 tests, no firmware/slicer/hardware validation, remaining gaps, PR #47 and exact
report ID all matched. No duplicate/retry or secret retrieval occurred.
