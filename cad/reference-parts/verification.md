# Stage A verification — 2026-10-15

Historical evidence for merged PR #32. [Stage B verification](stage-b-verification.md) supersedes the import limitation and records subsequent catalog growth; the observations below describe Stage A.

Evidence category: **documentation and software/file checks**, not geometry or physical testing. [Scope/workflow](README.md); [issue #31](https://github.com/VoidPhoenixApps/project-tesseract/issues/31). Draft implementation requires maintainer review; no engineering gate is claimed passed.

## Authority and scope audit

- Clean `main` matched freshly fetched `origin/main` before branch `codex/reference-parts-stage-a` was created. Existing Fusion sources and worktrees were preserved. Open PRs #17 and #19 were inspected for overlap; neither was incorporated or changed.
- Read current repository instructions, requirements, architecture, roadmap, research-first plan, contributing and Discord reporting rules; read current Home Infrastructure instructions and local Codex setup standard through GitHub.
- Shared workflow, engineering, knowledge, secrets, tooling/model and independent-review standards read from project-knowledge commit `147de4d979bba17120a4cc425983d590f85b6000`; GitHub `main` matched. No Tesseract `CURRENT_STATE.md` exists in that checkout. No source repositories changed.
- AgentMemory queried once; returned unrelated context, so no task decisions were drawn from it. No redundant memory was saved.
- No manufacturer CAD files were found in the repository CAD area. Existing Fusion Python sources/manifests remain intact. The sibling reference library did not exist before this task; no broad scan of personal files was performed.
- Initial project-local-cache proposal was superseded by the maintainer's explicit sibling-folder authorization. Only the sibling library was created. The project-local alternative is ignored defensively.

## Coverage

| Category | Candidates |
| --- | ---: |
| SBCs | 4 |
| MCUs | 4 |
| Controller boards | 3 |
| Motors | 2 |
| Linear rails/carriages | 4 |
| Bearings | 1 |
| Structural components | 3 |
| Belts/pulleys | 2 |
| Extruders/hotends | 2 |
| Sensors | 1 |
| Fans | 3 |
| Electrical hardware | 3 |
| Fasteners | 2 |
| **Total** | **34** |

These are sourced candidate identities; unresolved physical revisions/configuration suffixes remain explicit. Several records have only documentation or an unconfigured manufacturer portal. They are **not 34 verified CAD models**. Manufacturer alternatives appear across controller boards, MCUs, structural components, hotend/extruder and fan categories. More motor/rail/bearing alternatives, reinforcement stock and probes remain next-batch work.

## Authorized sample and actual access

Library root on Forbidden Fruit: `/Users/todd/Development Projects/tesseract-cad-library/`. All 13 category directories exist. Local Codex list/read access was demonstrated by file reads and hashing. Persistent additional-source configuration, POTUS access and cloud access remain unverified.

| Property | Observed evidence |
| --- | --- |
| Part | Adafruit Feather RP2040, product #4884 |
| Source revision | `c128bceb1f96b6ea8b68f250bda986ba85da24ea` in official `adafruit/Adafruit_CAD_Parts` |
| Model bytes | 2,443,088 |
| SHA-256 | `de85fb7f6644cdea17808208d888e64264d691573da8cd0fee808e2fd44d477f` |
| Git blob SHA-1 | `6b6c10b83c8e2648b036c741208101c5511affd6`, matched GitHub API metadata |
| License | Pinned root MIT, Adafruit Industries; 1,076 bytes; no folder-specific override in inspected source directory |
| License SHA-256 | `f60436644e066301d4c2e8f1f0674a157b1f60e4fd5586717b99dde255cc18cd` |
| STEP structure | Exchange start/end, HEADER, DATA, two ENDSEC markers, 50,481 entity definitions |
| Schema / units | AP214 AUTOMOTIVE_DESIGN; one SI millimetre declaration |
| Source header | Timestamp 2021-05-10; model label rev C v2, **not** confirmed purchased PCB revision |
| Import / dimensions / physical fit | **Not performed** |

One CAD asset and its license were downloaded. No other CAD models or archives were downloaded, and no third-party model is in Git. MIT permissions and maintainer authorization were checked before retrieval. Hash/marker checks establish bytes and basic structure, not full STEP syntax, topology, correct units throughout an assembly or dimensions.

## Checks and limits

- `python3 scripts/check_reference_parts.py`: schema/completeness, normalized duplicate identities, category coverage, source URL syntax, permissions/authorization, safe relative asset paths, generated index and public file/index checks pass.
- `python3 scripts/check_reference_parts.py --library '/Users/todd/Development Projects/tesseract-cad-library'`: both hashes, byte size, upstream Git blob identity and STEP structural markers pass; filesystem access verified.
- `python3 -m unittest discover -s tests -v`: **76 tests pass**, including 13 new catalog tests. Reporting tests are mocked; existing CAD software tests do not validate hardware.
- Markdown relative targets/anchors, headings, table structure and code fences checked; full changed/new-file diff reviewed. Requirements, architecture, roadmap and existing Fusion sources are unchanged. All bed/mode/stock/enclosure targets and the research-first priority remain intact.
- `git diff --check` and `git diff --cached --check`: run before commit. CI workflow repeats offline catalog checks and focused negative tests without secrets, model downloads or library access.
- Import limitation: no `FreeCAD`/`freecad`/`FreeCADCmd` executable on PATH, no FreeCAD app in `/Applications`, and `FreeCAD`, `cadquery`, `OCP` unavailable to the checked Python. Fusion app exists under the user's Applications directory, but a usable reproducible import automation route was not established. No engine installed, GUI import claimed, geometry measurements fabricated or original design opened/modified. Record an actual engine/version and import/dimension evidence in a later authorized session.
- Physical tests, electrical checks and full machine builds are outside this task and were not performed. No formal independent engineering review is claimed; maintain Draft status for review.

### Source-link checks

Official product/document pages and GitHub tree metadata were examined with web tools/GitHub API. A bounded HEAD-only check of 28 unique documentation URLs returned 9 HTTP 200 responses, 15 HTTP 403 responses, two HTTP 429 responses, one timeout and one 404. No CAD download was attempted by this check. A HEAD failure is not proof a page is dead; no access restrictions were bypassed and no blind retry loop was used.

The stale HIWIN regional PDF (404) was replaced by the [live manufacturer dimensional table](https://www.hiwin.de/en/Products/Linear-guideways/Blocks/Miniature-guides/MGN-HIRES-series/c/4500); all four recorded size dimensions were rechecked there. The US catalog endpoint returned HTTP 200 but exceeded the web reader's size limit, so no claim of reading that full PDF is made. The preliminary 80/20 1010 entry was replaced with the separately verified [1010-S product](https://8020.net/1010-s.html), including its 12-inch stock option. Neither was selected for the printer.

403 responses affected 80/20, OMRON, Adafruit product pages, STEPPERONLINE, Raspberry Pi, SUNON and WAGO; their metadata was available through web/indexed manufacturer sources. Noctua returned 429 to HEAD but its product/download and CAD terms pages were readable through the web reader. ST timed out on HEAD; its product page/design-package revisions were read through the web reader. Thus **not every external link was directly reachability-verified**. Catalog URL syntax passes; recheck source content, revision and rights before future retrieval.

The STEPPERONLINE [older 17HS08-1004S drawing](https://www.omc-stepperonline.com/download/17HS08-1004S.pdf) specifies a 20 mm body; the current [17HS19-2004S1 product page](https://www.omc-stepperonline.com/nema-17-bipolar-59ncm-84oz-in-2a-42x48mm-4-wires-w-1m-cable-connector-17hs19-2004s1) links the 17HS08-1004S with a 21.5 mm title. This is an unresolved revision conflict, not permission to choose one envelope. Source date, drawing revision and a matched model must be resolved before designing an interface.

## Files changed and purpose

| Path | Purpose |
| --- | --- |
| `.gitignore` | Ignore optional project-local reference cache |
| `AGENTS.md` | Point future CAD sessions to implemented catalog/workflow |
| `README.md` | Discoverable library entry point |
| `docs/research-first-plan.md` | Mark library-only Stage A progress while retaining historical proposal and CAD pause |
| `cad/reference-parts/catalog.json` | 34 source/rights/geometry records and one local asset fingerprint |
| `cad/reference-parts/catalog.schema.json` | Machine-readable required-field/type contract |
| `cad/reference-parts/INDEX.md` | Generated readable category index |
| `cad/reference-parts/README.md` | Storage comparison, permissions, contribution, source configuration, reproduction and missing-model procedure |
| `cad/reference-parts/verification.md` | Evidence, limitations and handoff |
| `scripts/check_reference_parts.py` | Offline validator, publication guard, local hash/structure audit and index generator |
| `tests/test_reference_parts.py` | Negative/positive validation and boundary checks |
| `.github/workflows/reference-parts.yml` | Isolated offline CI validation |

Outside Git, created the authorized sibling category folders, a local `README.txt`, and the single pinned sample/`LICENSE.txt` pair. No Home Infrastructure or project-knowledge edits occurred.

## Remaining decisions and durable handoff

No component, reinforcement stock, electronics architecture, final CAD toolchain or Tesseract license has been selected. Rights on most assets, complete order configurations, source revisions and dimensional verification remain open; see the [workflow's next batch](README.md#next-batch). Public redistribution is forbidden by this task even for the MIT sample.

After maintainer review, separately authorized Home Infrastructure work should record the actual library root, verified access, manual source-folder configuration result and backup/recovery procedure under its workstation/local Codex setup records. Project-knowledge has no Tesseract project record to update; if a shared reference-library standard is adopted later, its shared workflow/tooling standard should link here instead of duplicating the catalog. No such updates are claimed.
