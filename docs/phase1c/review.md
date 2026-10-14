# Independent desk review record

The review below covers the original concept implementation. It does **not**
constitute independent review or Fusion acceptance of the subsequent 2026-10-13
macOS runtime correction. See [verification](verification.md) for the observed
failures, the completed planned macOS matrix and the remaining engineering limits.
Historical test results below apply only to the source reviewed at that time.

## Completed matrix evidence review — 2026-10-13

The maintainer completed the planned macOS matrix. Direct inspection of local
reports corroborates the seven carrier passes; gap and release/return states;
pitch, bore, inset and B baseline values; and component sets for A,center,
A,inset, B,center and B,inset. Both negative tests are expected CHECK rejections
(carrier165 and X1/Y0); both restorations pass for 59 solids. The previously
unlisted carrier-restoration report `_hq6gs8v` was found and inspected alongside
the three supplied filenames. Exact outcomes, provenance and limitations are
in [verification](verification.md). Visual inspection and test continuity are
maintainer-reported, not independently executed by the agent.

Engineering review summary: the source now demonstrates a constrained editable
cold docking concept at the tested settings and configurations, including domain
and release-order guards and recovery. Missing edge constraints caused the
historical trapezoid; the successful corrected tests supersede that failure for
the exercised scope without erasing it. Independent review of the corrected CAD
scheme and contact/support/capture assumptions remains outstanding. No physical
docking, thermal/load evidence, full collision certification or independent
Windows verification is claimed. The full parameter space is not certified.

Finalization checks: all **47 automated tests passed (15.099 s)** using
`python3 -B -m unittest discover -s tests -v`. Static smoke validation passed;
that command does not execute Fusion. Changed Markdown local links/fences,
complete intended diff and working/staged whitespace checks passed. No source
or test files changed. CI is linked from Draft PR #18 after the documentation push.

This follow-up changes documentation only. No Fusion designs, source, tolerance,
logs, local configuration or other repositories were altered. Earlier pending
statements below are historical checkpoints. Draft PR #18 must not be merged
without explicit approval.

## Publication review — 2026-10-13

The maintainer explicitly authorized committing/pushing the intended Phase 1C
correction and updating existing Draft PR #18. Earlier no-publication statements
below describe the authorization state at those historical checkpoints. PR #18
must remain Draft; no merge is authorized. The complete local source/test/docs
diff retains the confirmed trapezoid failure, seven observed macOS CHECK results,
0.001 mm bounds tolerance and one-ULP boundary correction. No Fusion source
changes were needed for publication; the tested entry-point hash remains valid.
Registration examples now use a portable worktree placeholder. Local `.vscode`
and temporary diagnostic files are excluded. The next bounded test matrix is
in [verification](verification.md); all entries remain pending observed Fusion
results. No supporting-repository or cross-project knowledge update is required.

Publication checks: `python3 -B -m unittest discover -s tests -v` passed all
**47 tests (15.094 s)** on macOS. Static smoke checker, fixture compilation,
changed Markdown local links/fences and whitespace checks passed. One diagnostic
test assertion now checks the native Windows temp directory on Windows instead
of requiring `/tmp`; no CAD source changes or new runtime claims result. The
verified generator hash remains unchanged. CI is recorded on PR #18 after push.

## Carrier-resize runtime acceptance — 2026-10-13

The maintainer confirmed all requested checks passed. Direct review of seven
local reports confirms B,inset carrier 160→164→160→156→164→156→160 mm at gap=0.5
and zero X/Y travel: CHECK PASSED in each, 59 fully constrained healthy footprints,
no out-of-tolerance bounds, correct fixed-carrier center and passing volume/sweep
checks. [Verification](verification.md) records report filenames, hashes and scope.
The carrier-resize correction is runtime-verified for this sequence on macOS;
this is not independent engineering review, full parameter/variant acceptance,
physical validation or permission to publish. Repeating gap/release edits on
this corrected design remains outstanding. No Python changes in this follow-up;
the prior 47-test result remains applicable. Documentation checks passed.

## Full runtime evidence review — 2026-10-13

Read the maintainer's `/tmp/tesseract-phase1c-check-mm0alj_4.txt` directly.
The fixed carrier's lower-left point and all four driving evaluations are
correct, but the lower edge slopes from (18,38) to (182,36) mm. Upper vertices
remain at Y=200. Empty geometric constraints permit this trapezoid while all
four scalar dimensions remain satisfied. This confirms the source defect;
it is not a rigid Y translation, stale recompute or occurrence-context mismatch.
Six components fail bounds and all 59 footprints lack edge constraints. The
[verification record](verification.md) records the exact affected names and
observed dimensions without committing the local report. Actual carrier API
value also confirms the one-ULP conversion path in this run.

**47 repository tests passed (14.918 s)**, including 32 Phase 1C tests.
Python compilation/static smoke validation, Markdown local links/fences and
working/empty-index whitespace checks passed. Main remains clean.

Added a measured-vertex regression that distinguishes satisfying the old scalar
drivers from satisfying the corrected rectangle graph. No new generator edits
were necessary. The existing local four-edge constraint correction still awaits
maintainer execution in a separate unsaved document; the old timeline was not
modified. No publication or physical validation is authorized by this evidence.

## Earlier rectangle orientation correction — 2026-10-13 (before full report)

The new runtime observations are recorded in [verification](verification.md):
164 mm failed with correct dimensions but -2 mm Y displacement; 160 mm passed
all 59 checks while its footprint remained underconstrained. Identity transforms,
agreeing native/proxy boxes and unchanged successful recompute narrow the inquiry.

Source review found omitted horizontal/vertical rectangle-edge constraints,
which Autodesk's API sample adds explicitly. The correction adds those four
constraints, preserves all four driving location/size dimensions, and rejects
underconstrained generated footprints. This is a demonstrated missing design
constraint, not proof of the exact old solver trajectory or a corrected kernel
pass. Dimension-reference diagnostics enable examination of the still-missing
164 mm evaluated sketch/vertex evidence. All box footprints share this code.

Three new linear constraint tests exercise actual footprint helper calls with
API-shaped doubles: all variants and parts through carrier changes in both
directions without reseeding, gap/release/restoration, omitted orientations
(rank 4 instead of 8), and component/edge/axis error context. A fourth new test
ensures the user-reported -2 mm Y bounds still fail and dimension references are
reported. The equation test solves a fixed orientation branch; it is not Fusion
constraint inference, profile/extrusion regeneration or kernel validation.

The maintainer then reported message-box truncation. CHECK now writes a unique
local text file containing the complete result/traceback plus every expected
component's diagnostic snapshot, and shows a short result/path dialog. Two
additional tests cover distinct success/failure report files, all component
records, short dialogs and early failure logging. Test-created files are deleted
by the tests; actual maintainer reports are not removed or committed. The next
runtime step is an existing-design 164 mm CHECK followed by direct local file
inspection, not a request to transcribe the dialog.

Final local verification: **46 repository tests passed (14.724 s)**, including
31 Phase 1C tests. Python compilation/static smoke validation passed. Existing
one-ULP boundary and geometry tests remain green; the model SHA-256 remains
`2cf8d206ab5bd22210a62209283dd2d93d10fd06d8e3bf8c6122aeacc5cf4c18`.
Markdown local-link/fence checks and working/empty-index whitespace checks passed.
The main checkout remains clean. No test exercised Fusion's kernel.

No independent reviewer or Fusion run has accepted this correction. Existing
uncommitted fixes and `.vscode` are preserved. No commit, push, PR update,
existing-design mutation, save, supporting-repository edit or physical test.

## Earlier fixed-carrier bounds diagnostics — 2026-10-13 (historical)

The maintainer's latest 164 mm CHECK passed the range gate and failed the actual
body-bounds comparison for `Fixed_cold_carrier`. This is recorded as a failed
runtime check. There is insufficient evidence to identify stale geometry,
underconstraint, incorrect expression propagation, coordinate context, or a
bounding-box issue as the cause. No geometry repair or tolerance change is made.

Source/API review traced driving offsets and size expressions, the fixed Z
plane and extrusion height, identity occurrences, and native versus proxy
measurement. CHECK now captures actual/expected bounds and per-axis errors,
size/center, before/after recompute evidence, relevant parameter expressions,
native/proxy regular/tight boxes, sketch constraints/driving state and feature
health. See [verification](verification.md) for conditional interpretations and
the minimum two-run procedure in the existing design. Optional diagnostic
failures do not bypass validation or hide core actual/expected bounds.

Six new [diagnostic contract tests](../../tests/test_phase1c_diagnostics.py)
passed separately (1.695 s). Two initial failures were test-string expectations
for integer versus float Z formatting; these assertions were corrected without
changing the measured comparison. After adding sketch-to-component endpoint
coverage, all **40 repository tests passed (13.843 s)**, including the 25 Phase
1C tests and all previous one-ULP, parameter, geometry and reporting coverage.
API-shaped doubles exercise synthetic 160/164 states, stale/shifted geometry,
strict mismatch detection despite matching diagnostic boxes, failed diagnostic
reads, pre/post recompute, recompute failure and moved occurrences. They do not
establish any actual Fusion state or reproduce the maintainer's kernel failure.

Python/static smoke checker, Markdown links/fences, complete diff review and
working/empty-index whitespace checks passed. The one-ULP model file still has
SHA-256 `2cf8d206ab5bd22210a62209283dd2d93d10fd06d8e3bf8c6122aeacc5cf4c18`.
The diagnostic entry point now has SHA-256
`9322d19cbfeba17718aa9a1901278b90ff55011b58110e674b87caf1405c62cc`.
Earlier entry-point hashes below identify historical runs, not this diagnostic
revision. Existing uncommitted fixes and `.vscode` are preserved; main is clean.
No new independent review, successful Fusion check, physical validation,
commit/push, PR update, or supporting-repository change is claimed.

## Earlier carrier-boundary correction source checks — 2026-10-13 (historical)

The user subsequently confirmed B,inset generation (59 solids/reservations),
four 5 mm bores at 100 mm spacing, gap/restoration and release/reverse-docking
CHECKs, and rejection of invalid X-first travel on Fusion Personal for macOS.
Carrier 164 mm then failed the numeric domain gate. These observations supersede
the earlier pending status only for those checks; no numeric-fix runtime pass,
complete parameter matrix or physical evidence is recorded.

Author reproduction before correction: the new endpoint regression failed for
carrier 164, float_xy 0.8 and mount_bore 6 after representative multiplication
into cm and back to mm. Carrier became `164.00000000000003`. This confirms the
strict comparison defect; the original Fusion internal value remains unknown.
See [verification](verification.md) for the bounded one-step correction and limits.

Final source checks on existing Python 3.9.6: all **34 repository tests passed**
(11.916 s), including all **19 Phase 1C tests**. The four new numeric tests cover
all 17 parameter domains, exact limits, nearby valid values, one outward step,
two outward steps and 1e-9 violations, bad types/nonfinite values, normalized
carrier geometry in four variants, and unchanged sequence/transport rejection.
An earlier focused 19-test run also passed (12.072 s); the final full run includes
the subsequently expanded nearby-value and error-specific assertions.

Python compilation, existing smoke-test static checker, Markdown local links and
fenced blocks, complete diff review including previous local fixes, and working
and empty-index whitespace checks passed. Requirements, geometry definitions,
driving dimensions, unit extraction, release ordering and CHECK's downstream
validation are unchanged. The entry-point and manifest hashes below still match;
the new model hash is recorded in verification. The `.vscode` folder is untouched.

No new independent review, Fusion execution by Codex, Windows run, exports or
physical tests are claimed. The next required evidence is the user's CHECK in
the existing design at carrier 164 mm and restoration to 160 mm. No commit,
push, PR update or merge is authorized without explicit approval. No supporting
repository change is required for this implementation-specific correction.

## Earlier runtime-correction source checks — 2026-10-13 (historical)

Author checks on Forbidden Fruit using existing Python 3.9.6:

- All 15 Phase 1C tests passed (11.398 s); all 30 repository tests passed
  (11.306 s), retaining every original parameter/geometry test.
- Existing Fusion smoke-test static checker passed. Python compilation,
  manifest metadata, changed Markdown local links/fence balance, complete diff
  review (including the maintainer's changes), and `git diff --check` passed.
  `git diff --cached --check` passed with an empty index; nothing was staged.
- Read-only review found no changed requirements, geometry specification,
  architecture, hardware or supporting-repository files. The main checkout
  remains clean. Existing local `.vscode` content remains untracked and untouched.
- API contract test doubles check calls and injected failures only. Fusion's
  real solver, parameter regeneration, Windows runtime and exports have not
  been run by Codex. User-run macOS acceptance remains pending. The prior
  independent review does not cover this patch; no new independent review is
  claimed. No hardware tests were authorized or performed.

Uncommitted entry-point SHA-256 for the requested rerun:
`2f71165492a0248105523f83d6008f7d69f640745b4238ec96e0238647667e9d`.
Manifest SHA-256:
`c71f23e11af101a7df78d35433191c7992687d777a67e33ebd6915c961fb5424`.
Both accompany baseline `ed1c74a`; the unchanged commit alone does not identify
the corrected runtime source.

The durable failure/correction record belongs in this repository's
[verification document](verification.md). No new cross-project decision or
Tesseract project-knowledge record is needed for this local API correction.

## Original concept review (historical)

Scope: first Phase 1C source/analytical CAD concept, compared against current
requirements, Phase 1B studies and the shared independent-review standard.
An independent Codex subagent reviewed the generator, geometry specification,
manifest, tests, documentation and registration workflow without editing files.
This is an AI desk review, not competent-person physical safety sign-off.

**Disposition: APPROVE for the bounded Draft concept scope only.**
Critical findings: 0. Important findings: 0. Minor findings: 0.

The reviewer independently ran all nine Phase 1C tests (PASS, 20.808 seconds)
and `git diff --check` (PASS), and inspected contact/support geometry, release
sequence, dependencies, common mounts and negative controls. No Fusion execution,
export, force simulation or physical test was performed.

Initial review concerns and resolution:

- Finite rectangular contact faces and broad shoes do not physically implement
  ideal point-normal constraint equations automatically. The engineering record
  now explicitly distinguishes these envelopes from the rank model and requires
  contact curvature/compliance and retention development.
- Checking only tagged bodies could miss added obstructions. CHECK now rejects
  untagged top-level components, root bodies, nested additions and moved
  occurrences. It still is not a general topology or interference validator.

Assessment: requirements compliance yes within provisional scope; acceptance
yes for source/analytical concept, uncertain for Fusion behavior; test coverage
and overall confidence medium; security/authorization confidence high;
migration/data-integrity not applicable.

The review's most important limitation is B capture: the approximately 0.944 mm
sheet float/yaw envelope exceeds the 0.5 mm cold gap, even though the aligned
release sweep passes. Positive retention, force closure and fabrication
readiness are unresolved. No physical test or final architecture is approved.

## Author verification

Nine Phase 1C tests passed locally. The first full 24-test run had one unrelated
reporting-test error: the Windows sandbox denied creation/cleanup of its temporary
`event.json`. This was an environment failure, not a passing test; no reporting
source was changed. The same 24 tests passed outside that sandbox (20.468 seconds).
Markdown internal links, fenced blocks and `git diff --check` also passed.
The existing smoke-test static checker passed; its code/worktree was not changed.

Fusion execution, F3D/STEP export, actual fit, thermal testing and machinery
operation were deliberately not performed. Requirements and architecture remain
unchanged; root README adds only a navigation link to the bounded concept.
