# Stage D — qualification and next sample request

**2026-10-15, Forbidden Fruit; [issue #37](https://github.com/VoidPhoenixApps/project-tesseract/issues/37).** Stage C merged in [PR #36](https://github.com/VoidPhoenixApps/project-tesseract/pull/36), commit `8da69d945fc562c4cbd09f9cee2b080a807dc2eb`, at 2026-10-15 17:21:59 UTC. This stage prepares decisions and offline tooling; it does not approve retrieval or resume printer CAD.

## Readiness audit

The reproducible [45-record matrix and source revision register](READINESS.md) derives from the catalog without schema changes. The axes deliberately overlap:

| Axis | Result | Meaning |
| --- | --- | --- |
| Source | 15 listed, 13 portal-unconfigured, 17 not-located | 28 URLs do not mean 28 exact ready-to-download solids. Listed sources can be packages or landing pages |
| Download rights | 3 allowed, 3 conditional, 39 unknown | Catalog readings, not new legal conclusions or maintainer authorization |
| Local AI / public redistribution rights, each | 3 allowed, 1 conditional, 41 unknown | All five dimensions remain separately visible; cloud upload/training remain outside this scope |
| Retrieval authorization | 1 approved (#4884), 44 not-requested | Only the existing Feather may be held locally |
| Inspection triage | 1 authorized local record, 2 promising requests, 42 unresolved inspection-rights records | The two are Pico and #1253; no command downloads anything |
| Source revision | 5 exact commit pins, 40 needing source-version review | A commit pin is not physical revision accuracy; Pico's documentation pin is not a model-byte pin |
| Physical revision | 39 unknown; 6 named | Named: ESP32 V4, Nucleo C04, SKR V3.0, Octopus V1.0, Duet 1.02, BLTouch V3.1. None has inspected matching local geometry |
| Geometry | 1 partial dimension check; 44 documentation-only | Feather still has finished-hole, later-board and physical-fit gaps; none is fully fit-qualified |

Rights blockers include Noctua's conditional reference use and unresolved AI/redistribution, Duet's conditional hardware terms, and BTT's unestablished hardware grant. Unknown does not mean prohibited. No portal-wide AI or cloud permission is inferred. See [Stage C](stage-c-verification.md) and [Fusion library rights](fusion-library-research.md) for the evidence rather than repeating vendor research.

Revision/geometry blockers apply independently of rights: STEPPERONLINE's conflicting body length; LDO's suffix/drawing discrepancies; HIWIN's incomplete configuration; the Feather's physical revision and finished-hole limits. The matrix keeps every record's revision and confidence visible; `--id ... --json` includes its full geometry checks, rights evidence and notes. No free-text keyword heuristic declares a model suitable for interface design.

## Next sample recommendation and consolidated approval packet

**Recommend Adafruit #1253 first for a bounded local workflow exercise.** It adds shaft/bore, axial flange and set-screw inspection to the board-based Feather exercise, using a smaller, pinned STEP. The product is **no longer stocked by Adafruit**; this recommendation is not a future BOM choice or procurement endorsement. Pico is the fallback for a second board/import comparison, with weaker byte-level revision provenance until approved retrieval.

### Adafruit #1253 — preferred

- Exact identity: Adafruit SKU **1253**, aluminum GT2 pulley, 36 teeth, nominal 5 mm bore, for 6 mm belt. Underlying OEM and physical manufacturing revision are unknown.
- Official [product listing](https://www.adafruit.com/product/1253), checked 2026-10-15, supplies nominal 17 mm height and 25 mm outer diameter and says “No longer stocked.” No drawing tolerance or supplied-lot mapping was established.
- Exact proposed file: [`1253 Aluminum Timing Pulley.step`](https://github.com/adafruit/Adafruit_CAD_Parts/blob/c128bceb1f96b6ea8b68f250bda986ba85da24ea/1253%20Aluminum%20Timing%20Pulley/1253%20Aluminum%20Timing%20Pulley.step), at commit `c128bceb1f96b6ea8b68f250bda986ba85da24ea` (current head when checked). Git tree metadata gives **472,468 bytes**, blob **`b6128259281cdeb578b4422d11da41a6ec9e4868`**. These are upstream metadata, not locally verified bytes/SHA-256. The folder also lists `.f3d`; it is not included in the proposed retrieval.
- Rights: [pinned root MIT license](https://github.com/adafruit/Adafruit_CAD_Parts/blob/c128bceb1f96b6ea8b68f250bda986ba85da24ea/LICENSE), copyright Adafruit Industries 2016. Complete recursive tree (`truncated=false`) lists only STEP/F3D in this folder; no folder-specific override found. All five catalog actions remain recorded as allowed under that repository grant, with copyright/permission notice preservation. Local automated inspection is an inference from broad use rights, not a model-training clause.
- Request: approve **only this STEP and its pinned LICENSE** for storage under `belts-pulleys/adafruit/1253/<commit>/` in the approved sibling library and local numerical inspection in an already available authorized engine. Compute SHA-256, byte count and Git blob identity before import; preserve original bytes and notice.
- Verification purpose: native units/axes, solid count, bore axis and diameter, axial height, flange envelope, tooth count where represented, and set-screw geometry/clearance. Compare source nominal values; log omitted/simplified threads or teeth explicitly. Do not derive fit tolerances, belt contact accuracy, shaft retention strength or physical capability from nominal dimensions.
- Limits: no public model redistribution, cloud upload, supplier-library insertion, derivative printer design, hardware purchase, software installation or physical test is included. No SHA-256 or internal model revision is invented before authorized retrieval.

### Raspberry Pi Pico — optional alternative, not a second automatic download

- Exact identity: **Raspberry Pi Pico, RP2040, non-wireless, without headers**, not Pico H/W/WH or Pico 2. Physical revision remains unknown.
- Official [non-wireless Pico resource section](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#non-wireless_pico) links [STEP resource RP-008311-DS](https://pip.raspberrypi.com/documents/RP-008311-DS). A **HEAD-only** request on 2026-10-15 returned HTTP 302 to [`RP-008311-DS-1-Pico-R3-step.zip`](https://pip-assets.raspberrypi.com/categories/610-raspberry-pi-pico/documents/RP-008311-DS-1-Pico-R3-step.zip). No archive/model body was retrieved. `DS-1` and `R3` are filename labels, not verified internal revisions or a current shipped-board mapping. Archive members, STEP header, hash and solid count remain unknown.
- Source provenance: the exact resource and grant are also in [official documentation at `ddea98e…`](https://github.com/raspberrypi/documentation/blob/ddea98e98dafe9419feb4fd82710c2fbdef7dc44/documentation/asciidoc/microcontrollers/pico-series/about_pico.adoc). This pins the documentation, not the mutable linked asset.
- Rights: the Pico/Pico H section grants broad use, copying, modification and distribution for any purpose, with or without fee, with warranty disclaimers. It supplies no named SPDX license/version; do not relabel it MIT or transfer it to other Pi products. Local automated inspection is inferred from this broad design-resource grant; check any bundled asset terms after approval and stop on conflicts.
- Optional request: approve that **single STEP ZIP resource**, inspect its member list safely, and retain only the exact no-header Pico STEP plus applicable bundled notice in the local library. If it contains a different variant, unexpected assets, unsafe paths or conflicting terms, stop rather than substitute/extract everything. Record original archive and selected-member hashes locally after approval; no Allegro/Fritzing package is requested.
- Purpose: board outline/thickness, mounting-hole layout, USB shell and connector envelope, native orientation and repeat-import portability. Internal model identity, drawing correspondence, tolerances, mated USB clearance and physical fit remain unverified. Same no-upload/no-design/no-install limits as #1253.

The maintainer can authorize **#1253 only**, **Pico only**, or neither. Approval of one does not authorize the other or future revisions. This packet is prepared, not approval granted; catalog authorization fields remain unchanged.

## Most useful supplier questions — not sent

1. **STEPPERONLINE 17HS08-1004S:** ask the existing Stage C question for a dated current drawing/change notice and supplied-lot-to-STEP mapping explaining **20 ±1 mm versus 21.5 mm** body length, plus the five CAD-use permissions. This is a concrete, narrow discrepancy with direct mount/envelope consequences and an already listed STEP. Repeated searching of the same inaccessible PDF would add little.
2. **BTT SKR MINI E3 V3.0:** ask the Stage C asset-specific rights question for the pinned STEP, separately from firmware/PCB rights. One board is a bounded first rights inquiry; request all five dimensions and any cloud restrictions. A clear reply would establish whether this candidate can even enter the local workflow, without choosing Tesseract electronics.

Defer LDO's exact VRN/linear-motor correction questions until that candidate is needed; their existing evidence/questions remain authoritative. Defer HIWIN outreach until application requirements define a real rail/block configuration; there is no exact assembly to ask for yet. Neither priority authorizes contact, model retrieval or hardware selection. Use the complete [Stage C request table](stage-c-verification.md#consolidated-information-requests--prepared-not-sent) if outreach is separately authorized.

## Verification and handoff scope

Started from clean synchronized `main` at `8da69d9`; existing branches and separate docking-fixture worktree preserved. Shared project-knowledge at `147de4d979bba17120a4cc425983d590f85b6000` matched GitHub. No Tesseract `CURRENT_STATE.md` exists there. Current Home Infrastructure instructions and Forbidden Fruit records were consulted. AgentMemory queried once; no relevant continuity returned.

[PR #19](https://github.com/VoidPhoenixApps/project-tesseract/pull/19) proposes a standard-parts requirement in AGENTS/instructions/requirements. This stage does not modify those files, adopt its unmerged requirement, or change that PR. Its sourcing concern reinforces why the discontinued pulley is only a workflow exercise.

Actual checks: catalog/schema and generated-index validation passed; existing local Feather size/hash/Git blob and license checks passed (2,443,088 bytes, unchanged SHA-256); readiness-report freshness passed; all **84 repository unit tests passed**, including eight new triage tests. The two-candidate request CLI produced a consolidated packet. Catalog invariants preserve identity, physical revision, permissions, authorization, local asset and geometry fields for all 45 records. Changed Markdown relative file links/fence balance and Python syntax (including the proposed FreeCAD snippet) passed. Complete diff, requirement coverage/classification and cross-document consistency were reviewed; unstaged whitespace check passed. Staged whitespace/publication checks and CI results are recorded in the Draft PR. The only available local CAD bytes remain the existing Feather. No new CAD downloaded, no CAD engine installed, no independent geometry import, no contact/purchase/hardware action or existing design edit occurred. [FreeCAD procedure](freecad-inspection-plan.md) is proposed and unexecuted.

All approved requirements, research-first pause, native-source/reproducibility targets and undecided machine/toolchain/license choices remain unchanged. Independent review and human merge approval are still required for this Draft. No cross-project change is required: Tesseract owns these findings. If installation or persistent library attachment/backup is later approved, its actual machine configuration belongs in Home Infrastructure. Neither Home Infrastructure nor project-knowledge was changed; no redundant memory was saved.

## Changed files

| File | Reason |
| --- | --- |
| `scripts/reference_parts_triage.py` | Offline search, multi-axis audit, local hash checks and consolidated requests |
| `tests/test_reference_parts_triage.py` | Eight tests including rights/authorization, missing/corrupt assets, identity misses and CLI guards |
| `scripts/check_reference_parts.py` | Derive index confidence from actual catalog evidence instead of stale import-pending text |
| `cad/reference-parts/catalog.json` | Exact Pico resource/revision uncertainty and pulley metadata/availability |
| `cad/reference-parts/INDEX.md` | Regenerated Pico link and Feather confidence |
| `cad/reference-parts/READINESS.md` | Generated classification of all 45 records and source revisions |
| `cad/reference-parts/README.md` | Tool usage, bounded expansion and Stage D navigation |
| `cad/reference-parts/stage-c-verification.md` | Preserve historical handoff while recording merged status |
| `cad/reference-parts/stage-d-qualification.md` | Evidence, approval packet, supplier priorities and completion scope |
| `cad/reference-parts/freecad-inspection-plan.md` | Proposed repeatable second-engine procedure and explicit execution gate |
| `docs/research-first-plan.md` | Current Stage C/Stage D status without lifting research-first pause |
