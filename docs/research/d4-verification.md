# D4 — verification and review record

**2026-10-14, America/Chicago.** Desk analysis only. Completed checks and independent read-only
review for preliminary research publication; no physical validation.

## Scope and source state

Clean D3 checkout at `096ae806c08d437bf1c84c77d217cacdfd6f3231`; origin verified as
VoidPhoenixApps/project-tesseract. Fetched only this repository. D1/D2/D3 live states
and ancestry matched the requested open Draft stack. Dedicated branch
`codex/research-d4-structural-frame` targets D3's branch. All additions are under
`docs/research/`; requirements, parent evidence, main and supporting repositories preserved.
[Study index](d4-engineering-study.md) enumerates every added file and its purpose.

## Checks

- `python3 -B -m unittest discover -s docs/research -p 'test_d*.py' -v`: **55 passed** (15 D4, 40 inherited D1–D3).
- `python3 -B -m unittest discover -s docs/phase1b -v`: **11 passed**.
- `python3 -B -m unittest discover -s tests -v`: **63 passed**. These reporting tests do not validate hardware.
- Total: **129 tests passed**. D4 JSON regeneration from outside the repository was byte-identical and matched the parsed generated object.
- Both added Python files parsed using Python 3.9 grammar. Standard library only; inherited D2/D3 imports remain explicit.
- All 11 added Markdown files checked for internal file/heading links, table structure, balanced fences, H1 and final newline. Requirements, eight-mode coverage, classification and cross-document consistency reviewed.
- Complete staged change reviewed, including generated numeric results; working and staged `git diff --check` passed. Explicitly staged only the 14 package paths.

The initial D4 reproduction test exposed Python tuple versus JSON list comparison for
inherited reaction output; serialization was already byte-identical. Results were
normalized to JSON-native lists rather than suppressing equality. No mechanical result changed.

No external Markdown renderer/linter was run; the editable text diagrams were inspected
as source. No CAD fit/envelope checks, full-system FEA, physical measurements or hardware
safety tests were performed: geometry, selected parts, reviewed test procedures and
operating limits are absent, and this task authorizes desk research only. Source gaps,
including an unavailable norelem PDF and missing stock tolerances, remain in the ledger.

## Independent review

A separate read-only reviewer inspected all 14 files, requirements and inherited context,
checked analytical relations, spot-checked manufacturer sources and independently ran
all 55 research tests. The reviewer did not run the Phase 1B or reporting suites; those
were run by the author. This is an AI engineering desk review, not professional certification.

Initial disposition: **REQUEST CHANGES**, one Important finding. Shallow soft-joint
V-truss examples extrapolated deflection to 75–80% of rise, invalidating small-displacement
geometry even in a case without Euler exceedance. The correction preserves those negative
results, adds explicit geometric-validity and Euler-demand flags, documents possible
geometric softening/snap-through, and adds a regression distinguishing these warnings.
The 10% rise warning is a caution diagnostic, not an engineering acceptance limit.

Independent re-review: **APPROVE for preliminary research publication**, conditional on
completion of this verification record (now completed). No Critical, Important or Minor
findings remain open. Research scope and architecture-neutrality accepted; arithmetic
confidence high, overall confidence medium, physical-prediction confidence low. No final
architecture, material, operating envelope or physical test is approved by this review.

## Boundaries and durable context

No detailed CAD, fabrication files, hardware tests, energization, motion, firmware,
purchases, component adoption, license decision or cross-repository edits. Simplified
beam/truss/spring results are not full-machine FEA or mechanism validation. Whole-system
clearance, creep, strength, dynamics and safety remain unresolved; see [risk register](d4-risks.md).

After review/merge, separately authorized project-knowledge work could link this package
and its unresolved status; no existing Tesseract project record exists to update. No
memory save needed: useful results are recorded in this repository. Qualified mechanical,
electrical/thermal and controls/safety review remains necessary before adoption or
operation; first hardware proof remains two-bed docking and cross-seam printing.
