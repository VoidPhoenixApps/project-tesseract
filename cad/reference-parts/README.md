# Off-the-shelf reference parts library — Stages A/B/C/D

This is a reusable **candidate catalog**, not a Tesseract BOM or a component selection. It supports future research without resuming detailed printer CAD. The Feather sample has a partial reference-dimension check; no mechanism, electrical system or physical fit has been validated. [Stage B issue #33](https://github.com/VoidPhoenixApps/project-tesseract/issues/33) continues merged Stage A (#31 / PR #32).

Start with the [readable index](INDEX.md), [machine-readable catalog](catalog.json), [schema](catalog.schema.json), and [Stage A record](verification.md) and [Stage B verification](stage-b-verification.md). [Stage C findings](stage-c-verification.md) and [Fusion library research](fusion-library-research.md) record source/revision resolution, remaining requests and future workflows. Stage B merged in [PR #34](https://github.com/VoidPhoenixApps/project-tesseract/pull/34). There are 45 candidates in 13 categories. Only the Adafruit Feather RP2040 (#4884) sample is authorized for local download; all other models remain link-only, even where a permissive license is recorded.

Stage C merged in [PR #36](https://github.com/VoidPhoenixApps/project-tesseract/pull/36). Start Stage D with the [readiness matrix](READINESS.md), [sample approval packet and supplier priorities](stage-d-qualification.md), and [proposed FreeCAD procedure](freecad-inspection-plan.md).

## Storage decision and actual access

The maintainer explicitly authorized the sibling library on 2026-10-15:

```text
/Users/todd/Development Projects/tesseract-cad-library/
```

| Option | Benefits | Costs / safeguards | Outcome |
| --- | --- | --- | --- |
| Sibling library | Reusable across checkouts; separates third-party files from public Git; survives branch changes | Needs explicit per-machine source configuration and separate backup; relative catalog paths need a supplied root | Selected following explicit maintainer authorization |
| Project-local `local-cad-references/` | Convenient within an existing project filesystem boundary | Easier to accidentally stage; checkout-specific; ignored files are not backed up by Git | Considered initially; not created. Exact root path is ignored and forced tracking is rejected by validation |

All 13 category directories were created in the sibling library. Current Codex filesystem read access was verified by reading the sample and license, checking sizes and hashes. This does **not** prove that the folder is configured as a persistent Codex project source, nor that POTUS or a cloud session can access it. No workstation settings or other repositories were modified.

Layout: `<category>/<manufacturer-slug>/<part-slug>/<source-revision>/<original-or-described-filename>`. The sample directory uses the immutable upstream commit, not an invented physical revision. Catalog asset paths are relative to the library root, never machine-specific absolute paths.

### Manual Codex source configuration

Open the local Project Tesseract project's menu, choose **Edit project**, inspect the current sources, and use **Add folder** only if missing to add `/Users/todd/Development Projects/tesseract-cad-library/` as an **additional source folder**. Treat model bytes as read-only references; attaching a folder does not itself enforce read-only filesystem access. Keep `/Users/todd/Development Projects/project-tesseract` **Primary** and `/Users/todd/Development Projects/project-knowledge` as the existing additional source. Do not replace either source. This follows [official local-project guidance](https://learn.chatgpt.com/docs/projects#use-local-projects-for-folders-and-codebases); the installed configuration UI remains unverified because Computer Use refused access to the Codex app. Inspect existing sources before adding a duplicate; no settings were changed. In a new session, explicitly list the folder and hash the sample to verify access.

Repeat configuration and access verification separately on POTUS using its actual local path. Cloud sessions need separately authorized file availability; never upload the library merely to make it accessible. Follow the [local setup standard](https://github.com/VoidPhoenixApps/home-infrastructure/blob/main/standards/codex-local-project-setup.md). The sibling directory is outside Git backup; arrange its recovery/backup policy separately in Home Infrastructure when authorized. Approved assets can be recovered from pinned sources and verified against catalog hashes.

## What a catalog record means

All records require exact manufacturer or vendor identity, model/part number, variant, revision, source/date, formats, geometry confidence and five separate permissions. `unknown`, an empty format/check list, or `null` asset/model URL explicitly records missing evidence; it is not permission or a verified zero dimension. Vendor SKUs whose OEM is undisclosed are labeled in notes. A product-family drawing is not proof of a particular physical board revision.

- `listed`: a manufacturer source offers the model/design resource. It may be a landing page or native PCB package rather than a solid model. Inspect `formats` and notes.
- `portal-unconfigured`: a legitimate manufacturer portal is known, but the exact downloadable configuration/model has not been established. HIWIN carriage size codes still need preload, accuracy, seals and matching rail specification; extrusion lengths/machining must be resolved where unknown.
- `not-located`: documentation exists but no trustworthy exact model has been located. Do not invent a URL or use a generic model.
- `documentation-only`: no model bytes inspected. Dimensions are published nominal source facts, not measurements or fabrication acceptance limits.
- `file-checked`: bytes, identity and structural checks only. Even `dimension-checked` would mean comparison with a drawing, not physical validation.

A source access date records when the cited metadata/documentation was examined. It does not mean the linked model was downloaded. `source_revision` is distinct from the physical part revision. Undated live pages need rechecking. Availability is a candidate sourcing indication, not confirmed local stock, price, affordability or a purchasing recommendation. The first batch favors common interface families and documents industrial alternatives; it is not a comparative procurement study.

The STEP sample was imported in installed Fusion without saving. Native axes, PCB outline, hole centers and assembly envelope are recorded in [Stage B evidence](stage-b-verification.md). Hole diameters differ between pairs; Stage C traces this to 2.50 mm plated-pad drills and 2.54 mm plain holes in both original and later PCB sources. Finished-hole tolerances, physical revision and connector mating clearances remain unresolved. Do not translate/rotate/scale it silently. The catalog contains no claimed fit tolerance.

## Rights and authorization gates

`download`, `local_ai_processing`, `derivative_use`, `public_redistribution`, and `commercial_reuse` each have an independent status, evidence link and note. `allowed` is a scoped reading of the recorded grant, not legal advice or a grant of patents/trademarks. `conditional` needs conditions resolved for the intended use. Unknown/prohibited rights block the corresponding action. A manufacturer download button does not grant redistribution or AI use. An MIT grant in a firmware directory does not license adjacent hardware CAD.

Maintainer authorization is a separate gate. **Only #4884 is approved in this batch.** Broad license permissions do not authorize additional downloads. No public third-party models are permitted by this Stage A workflow, even where upstream redistribution is licensed. The validator checks public-library file types/content and the Git index, including text STEP, binary data, LFS pointers and forced tracking of the optional local cache. It is an accidental-publication safeguard, not a universal classifier of disguised copyrighted data; review every staged file. Existing Tesseract-authored Fusion sources remain untouched.

The Adafruit model is in its official CAD repository at commit `c128bceb1f96b6ea8b68f250bda986ba85da24ea`. The pinned root MIT license and directory listing were read before download; no folder-specific override was present. Preserve the copyright and permission notice with copies. Local CAD inspection is inferred from the broad unrestricted-use grant, not from an AI-specific clause; no training or cloud upload is authorized.

Other notable limits:

- Raspberry Pi Pico's official design-resource grant is broad, but download authorization is still absent. Do not generalize that grant to Pi SBCs.
- Noctua permits reference/integration uses with exclusions for product reproduction and performance simulation; modified impeller geometry is unsuitable for airflow analysis. AI processing and redistribution remain unresolved.
- Duet3D native board CAD has CERN-OHL-S v2-or-later plus additional attribution/logo terms. Compatibility needs review. This does not select a Tesseract license.
- BTT hardware-model rights were not established by nearby firmware licenses. Other vendors' links remain held for rights/configuration review.
- Do not source substitute models from McMaster-Carr or other restricted libraries without specific rights review and authorization.

## Adding candidates and assets

1. Search by manufacturer, exact part number, variant and physical revision before adding a record. Keep dimensional variants separate; imperial stock is not a rounded metric equivalent. Resolve duplicate identity and supplier/OEM ambiguity.
2. Read a current official product/drawing source. Record publication/revision where exposed, access date, relevant dimensions with units, provenance, uncertainty, and exact asset link or an explicitly unresolved portal. Never claim a generic motor/rail model represents an exact part.
3. Review asset-specific rights before retrieval or processing. Link terms and explain each permission separately. Ask for consolidated maintainer approval for a bounded sample; collect correct files when rights or geometry cannot be established. Do not bulk clone/download CAD repositories.
4. After approval, retrieve only identified files into the local category/manufacturer/part/revision folder. Preserve the original bytes and license. Compute SHA-256, record the precise source revision and file size, and match available upstream identity metadata. Never overwrite an existing asset; a new upstream revision gets a new directory and retained history.
5. With an available approved CAD engine, import **one part** without saving into an existing design. Record engine/version/import options, file units and native axes/origin, solid count, import errors, bounding box and transform. Compare specific mounting-hole diameters/spacing, datums and connector/shaft envelopes with the matching drawing. Record expected/observed values, units, tolerances and discrepancy handling; overall bounds may include connectors and are not PCB dimensions. Preserve the original reference separately from any permitted derivative.
6. No compatible engine: run file/hash checks and explicitly leave import, placement and dimensions pending. Do not install tools or generate precision stand-ins to bypass the dependency.
7. Update `catalog.json`, regenerate the index, run checks, inspect the complete diff/index and open a focused Draft PR. Third-party CAD stays local. Do not infer a new hardware approval from catalog inclusion.

The JSON Schema is the required-field/type contract. The standard-library validator evaluates the exact subset of JSON Schema used here and fails on unsupported keywords; extending the schema requires extending/testing the validator. Semantic checks additionally enforce duplicate identity, rights basis, safe local paths and authorization. Keep changes to both reviewable.

## Reproduce checks

Run from the repository root with Python 3.9 or later. Offline CI does not access the sibling library or retrieve external models.

```sh
python3 scripts/check_reference_parts.py --write-index
python3 scripts/check_reference_parts.py
python3 -m unittest discover -s tests -v
```

For the explicitly authorized local sample:

```sh
python3 scripts/check_reference_parts.py --library '/Users/todd/Development Projects/tesseract-cad-library'
```

Recovery source for the one approved asset (retrieve only after verifying the catalog approval applies to your session and environment):

```text
https://raw.githubusercontent.com/adafruit/Adafruit_CAD_Parts/c128bceb1f96b6ea8b68f250bda986ba85da24ea/4884%20Feather%20RP2040/4884%20Feather%20RP2040.step
https://raw.githubusercontent.com/adafruit/Adafruit_CAD_Parts/c128bceb1f96b6ea8b68f250bda986ba85da24ea/LICENSE
```

Use the paths, byte size, STEP hash and license hash in the catalog; do not replace them with a checksum from a newer download. The validation command reads existing files only and never executes CAD scripts or downloads anything.

## Future Codex sessions: missing-model request

Before designing around **every purchased component**, check this catalog and the approved local library for the exact selected manufacturer/part/revision. Check source, rights, units, native frame and geometry evidence. If missing, restricted, ambiguous or unusable, pause only dependent CAD and send one consolidated list:

| Exact manufacturer / part / revision | Needed format and source | Geometry purpose | Missing evidence / permission | Blocked work |
| --- | --- | --- | --- | --- |
| Actual selected identity, not a guessed substitute | Prefer STEP plus applicable native source; link official source if established | Holes, datums, shaft, connector or clearance envelope | State exact gaps and request correct file or approved source | Name dependent interface/task |

Never fabricate a vendor model, substitute a purchased part silently, or invent precision geometry. A labeled preliminary non-fabrication envelope needs explicit maintainer approval and traceable dimensions. Continue unrelated safe work. No catalog entry selects the machine's hardware, final CAD toolchain, electronics or license. The research-first priority and two-bed docking/cross-seam first physical proof remain unchanged.

## Offline triage and consolidated requests

Use the standard-library helper before adding a candidate or requesting files. Search results identify possible existing records; confirm the full manufacturer, part, variant and physical revision before reuse. No command downloads, uploads, changes permissions or opens CAD.

```sh
python3 scripts/reference_parts_triage.py --query "Adafruit 1253" --json
python3 scripts/reference_parts_triage.py --id adafruit-4884-feather-rp2040 --library '/Users/todd/Development Projects/tesseract-cad-library' --json
python3 scripts/reference_parts_triage.py --id adafruit-1253-gt2-36-teeth-5mm-bore --id raspberry-pi-pico-rp2040-without-headers --requests --purpose "Compare bore/board interfaces and import portability" --blocked-work "Next local sample inspection"
python3 scripts/reference_parts_triage.py --check-report
```

Repeat `--id` for a consolidated request. An unknown exact ID is reported as missing without inventing a source or substituting a near match; normal lookups fail with nonzero exit status. Requests include all five rights statuses/evidence, source revision, purpose and dependent work. For different purposes, generate separate groups and combine them for review. No local record means no cataloged file, not proof that no unregistered file exists anywhere. `--library` hashes only recorded approved assets and fails on absent/corrupt bytes; it does not crawl or adopt other files. `--json` preserves the full source notes and geometry evidence.

After metadata changes, regenerate with `python3 scripts/reference_parts_triage.py --write-report`, then run `--check-report` and the existing validator. CI unit tests check both generated reports. Expand only for a named research/interface need: search existing identities, resolve exact variants and source/rights gaps, add a small link-only batch with evidence, and request one useful sample at a time. Do not fill category quotas or model commercial parts already cataloged.

## Next batch

Resolve the Feather finished-hole tolerances/physical revision and later-board clearances, corrected STEPPERONLINE and LDO drawings, BTT hardware-model permissions and a fully configured HIWIN rail/carriage assembly. Refine stock grade/tolerances, rod length/end machining, probe stroke and Gates bore/drive configuration. Stage B added eleven link-only candidates; see its evidence for source errors and blocked work. Growth remains incremental and independent of Tesseract hardware selection. Request separate approval before any additional model download; no purchase, hardware test or detailed printer CAD is authorized by this backlog.
