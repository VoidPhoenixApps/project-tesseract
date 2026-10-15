# D1 — sources, scope and verification record

**Study date:** 2026-10-14, America/Chicago. [Report](d1-engineering-study.md).
External sources below were retrieved during this investigation; retrieval verifies
what the source says, not the machine performance it advertises. No third-party CAD,
images or code were downloaded into or redistributed with this package.

## Repository authority and prior evidence

- Current GitHub `main` was fetched and matched local main at
  `952c2202bc001d1aff38fa7bce9a0b86410695d6`. Read CHATGPT_INSTRUCTIONS, AGENTS,
  README, requirements, architecture, roadmap, contribution rules, research-first plan
  and toolhead/Z backlog at that baseline.
- Existing Draft #25 head was `81c5b44952d0814f53c943fbc6173241886816a3` on
  `codex/research-d1-compatibility-screen`, already containing current main. Started
  clean, continued that branch without rebasing, overwriting or duplicating the PR.
- Shared workflow and engineering, knowledge, secrets, model and independent-review
  standards read from sibling project-knowledge at
  `147de4d979bba17120a4cc425983d590f85b6000`, confirmed current GitHub main.
  No Tesseract CURRENT_STATE/project record was found; none invented.
- Current Home Infrastructure instructions retrieved via GitHub; main resolved to
  `963185a4d528884473a28a87ef81ffb0d1e59dd4`. Both supporting repositories remained
  read-only; cross-repository synchronization was intentionally excluded.
- AgentMemory queried once; returned unrelated summaries, not used as evidence.
  No duplicate research memory was saved.
- [Phase 1 equations](../phase1/preliminary-calculations.md) and
  [references](../phase1/references.md): ideal thermal/structural/drive assumptions.
  [Phase 1B](../phase1b/README.md), calculation source, results and verification:
  retained thermal negative findings, constraint and rectangular-sweep limitations.
  [Phase 1C](../phase1c/README.md), review and targeted verification: retained CAD
  checker failures/recovery, not physical registration, strength or heat validation.
  No prior files/results were rewritten or historical failed experiments removed.

## External primary references and precise limits

All access dates below are **2026-10-14 America/Chicago**. “Undated” means no publication
revision was established from the retrieved page; search crawl dates are not publication
dates. These are links for research, not approved component-model sources.

| ID | Source / publication or revision | Supporting claim inspected | Limits / applicability |
| --- | --- | --- | --- |
| R1 | [ELEGOO OrangeStorm Giga](https://us.elegoo.com/products/orangestorm-giga), undated live page; [quad package](https://uk.elegoo.com/products/pre-order-orangestorm-giga-quad-printhead-upgrade-package), undated | Manufacturer describes four separately heated platforms and additional X-axis heads printing copies of the same model | Segmented heat and duplicate printing precedent, not arbitrary four-job XY/Z independence or moving-bed docking; not independent performance tests |
| R2 | [Prusa XL/XL+ live product page](https://www.prusa3d.com/product/original-prusa-xl/), undated current XL+ content | Toolchanging and 16 individually controlled heat tiles | Fixed segmentation and sequential tool selection do not establish retained-sheet reconfigurable beds or independent simultaneous jobs; marketing claims of eliminating warp are not adopted |
| R3 | [Kaiser 6061 sheet/coil/plate data](https://online.kaiseraluminum.com/depot/PublicProductInformation/Document/1015/Kaiser_Aluminum_6061_Sheet_Coil_and_Plate.pdf), Rev. 05/06, printed pp. 1–2 | Typical E=68.3 GPa, density 2.70 Mg/m³, alpha=23.6e-6/K at 20–100 °C | Independently rechecked against primary data in this pass; not selected alloy/temper, actual plate flatness or laminate properties |
| R4 | [Gates PowerGrip drive design manual](https://www.gates.com/content/dam/documents-library/catalogs/powergrip-gt3-drive-design-manual-en.pdf), revision not established; printed p.171 and sections on idlers/engagement | Low tension can permit tooth jump; linear-motion use requires allowable working-tension and sprocket-fatigue analysis rather than ordinary rotational selection alone | Supports investigating path/tension/wrap; does not demonstrate belt switching under load or authorize a belt size |
| R5 | [Miki Pulley 546 tooth-clutch catalog excerpt](https://www.mikipulley.de/wp-content/uploads/2025/08/546_Catalog_2021.pdf), filename identifies 2021; printed pp.118–120, document revision unconfirmed | Positive tooth engagement; full/single-position variants and tooth-shape distinctions | Shows selectable torque transmission precedent only; no chosen clutch, engagement speed, holding safety or scaled printed-dog capacity inferred |
| R6 | [mayr vertical-axis braking overview](https://www.mayr.com/en/industries/vertical-axes~517), undated | Manufacturer distinguishes gravity-loaded axis braking and linear/rotary brake options | Supports separate restraint investigation; no selected brake, stop rating, safety integrity level or Tesseract certification |
| R7 | [Slocum kinematic coupling review, MIT manuscript](https://web.mit.edu/2.70/Reading%20Materials/Kinematic%20coupling%20review%20article.pdf), manuscript header 2009; journal 2010, DOI 10.1016/j.ijmachtools.2009.10.006 | Six-DOF exact constraint, contact stiffness and preload design | Principles for cold-carrier registration; no published repeatability transferred to hot horizontal docking. Manuscript rights are not a license for this project |
| R8 | [THK master-guide/combined-use reference](https://www.thk.com/us/en/products/lm_guide/maintenance/0001/), undated | Guide matching/reference surfaces and joint deflection/misalignment concerns | Datum and assembly discipline; not a selected guide, printed-frame tolerance or automatic docking solution |
| R9 | [Voron mechanical assembly](https://docs.vorondesign.com/build/mechanical/), undated; [official Voron-2 repository](https://github.com/VoronDesign/Voron-2), live Voron2.4 branch | Documentation explicitly discusses belted V2 Z and allowing joint movement during quad gantry adjustment; repository identifies official design and license | Open-source belted-lift precedent, not selectable lift paths or independent four-bed Z; no files imported and no license adoption |
| R10 | [Klipper configuration reference](https://www.klipper3d.org/Config_Reference.html#dual_carriage), undated live documentation | Dual-carriage section describes activation, copy/mirror modes and carriage proximity checking; multi-stepper Z commands act in concert | Relevant motion/interlock concepts, not proof of four asynchronous XY jobs or sensed bed synchronization; no firmware/controller selected |
| R11 | [Duet3D G-code reference](https://docs.duet3d.com/User_manual/Reference/Gcodes/M586), live dictionary, M584/M598/M606 sections; listed version qualifications 3.5+ where stated | Additional axes, synchronization of motion systems, and asynchronous input-stream handling are documented with firmware/configuration qualifications | Independent-motion software precedent only; axis/queue/resource limits and four-job integration not established. No firmware implementation in this task |

**Voron Phoenix gap:** Searched the official Voron site and organization plus Phoenix
references. The [official landing page](https://vorondesign.com/) was accessible but
supplied no Phoenix technical specification. A discovered
[2026 video lead](https://www.youtube.com/watch?v=3cfrMXQwZfU) could not be retrieved
(browser tool returned an internal error). Forum/search discussion was not used to
assert released architecture, exact dimensions, IDEX capability or release status.
Phoenix remains a useful follow-up reference, **not verified technical evidence in
this pass**. Voron-2 evidence is explicitly separate and does not stand in for Phoenix.

No direct source in this pass establishes a commercially supported literal timing-belt
rerouting lift. This is a research gap, not proof that none exists. Vendor geometry,
ratings, rights and regional availability remain unchecked because no exact purchased
parts were selected. Before later interface CAD, consult the approved model catalog
and ask for missing approved files/sources as required by AGENTS; no invented geometry
or bulk model downloads are an acceptable substitute.

## Coverage and verification

| Requested scope | Where covered / limit |
| --- | --- |
| Five families including both mixed orientations | Report mode/group table, eight explicit states including mirrored mixed placements |
| XY-A through XY-E and Z-A through Z-F | Initial full cross-product index plus audited integrated candidates and all-six Z comparison; B/D topology unresolved explicitly |
| Mirrored A/B relationship | Diagrams preserve 1/4 Type A by 180°, 2/3 Type B by 180°, A/B mirror counterparts; interchangeability not claimed |
| Literal belt versus clutch | Separate report discussion, power diagrams, support state/fault study |
| Independent job progress and single-head J | Group coordinates and relative-Z equations; no reliance on cooperative stretch printing |
| Calculations | Mass, torque, force/advantage, seam/tilt/compliance, thermal growth, backlash, lost motion/power and synthetic 3D swept boxes |
| Actual head reach and 3D machine collision | Unresolved without approved actual geometry; equations and counterexamples only, no fictional fit claim |
| Safety | Separate P/L/T functions; sensor, gravity, heater, occupancy, stop and recovery obligations; no approved test procedure |
| Other mandatory requirements | Requirements unchanged: four sheets, horizontal fixed-datum conversion, printable-first/Ender 3, distinct stock variants, later 2020, tool-free enclosure and reproducible sources; no selection or waiver |

Completed local checks:

- `python3 -B -m unittest discover -s docs/research -p test_d1_analysis.py -v`: six tests passed (energy balance, stroke counterexamples, seam/phase arithmetic, mid-path/height collisions, historical thermal reconciliation and invalid inputs).
- `python3 -B -m unittest discover -s docs/phase1b -p test_analysis.py -v`: 11 tests passed, preserving negative thermal/constraint/occupancy cases.
- `python3 -B -m unittest discover -s tests -v`: 63 existing repository tests passed; these are software/API-double/evidence/reporting checks, not hardware tests.
- Regenerated D1 JSON compared exactly with the committed result; both new Python files parsed under Python 3.9 syntax rules.
- All six research Markdown documents checked for local links/anchors, balanced fences, table column counts, titles and trailing newlines. Conceptual text diagrams reviewed for group/axis labeling and two-type rotation relationships. No external Markdown renderer/linter was run; plain text diagrams require no renderer.
- Full intended package reviewed including new files; requirements and non-research artifacts unchanged. Unstaged and staged whitespace checks passed before commit.

## Independent desk review

A separate read-only AI reviewer inspected all nine artifacts against the request,
requirements and shared rubric, reran all six D1 tests, reproduced the JSON and checked
whitespace. Initial result: **APPROVE WITH MINOR CHANGES**, 0 Critical, 0 Important,
1 Minor. The finding was an ambiguous J rating combining Z-F literal switching with the
positive-selector variant. It was corrected by separating the two rows: literal J=U,
positive selector J=C, with E-like partial-mode obligations retained in both.
The reviewer rechecked the correction and exact XY-E diagram, confirmed resolution,
and updated the recommendation to **APPROVE for research documentation**, with
0 Critical, 0 Important and 0 Minor outstanding findings.

Reviewer confidence was Medium; acceptance was for the expressly permitted first
investigation, not a working machine or permission to proceed to detailed CAD. The
reviewer did not independently retrieve external references. Highest remaining risk:
every shortlisted architecture depends on unproven extended XY reach and gantry packaging.
Qualified mechanical/electrical/safety review and explicit human approval remain required.
Final publication/CI/Discord evidence belongs in Draft PR #25's handoff.
No detailed CAD, manufacturing files, hardware operation, purchases, firmware changes,
physical measurements or qualified safety validation were performed. Actual part costs,
supplier suitability, sensing/stop architecture, assembly geometry and thermal gradients
remain unresolved. This is a first investigation, not completion of all D1 engineering.

Durable knowledge: after review, a separately authorized project-knowledge entry could
link to this package and its status, especially relative-Z/grouping constraints and the
pending physical proof. No existing Tesseract project record was found to update, and
neither supporting repository was changed. Research notes are already owned here.
