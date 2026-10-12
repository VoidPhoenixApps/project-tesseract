# Sources, requirement coverage and verification

**Evidence labels:** equations and box sweeps are analytical screening. Unit tests verify model behavior, not printer performance. Original diagrams are editable Markdown text; no third-party image, CAD or code is incorporated. Licensing remains undecided.

## Technical references

Primary sources inspected 2026-10-12. These establish principles or explicitly labeled example inputs, not a qualified Tesseract component choice.

| Source | Applicability and limit |
| --- | --- |
| Slocum, *Kinematic couplings: A review of design principles and applications*, IJMTM 50 (2010), 310–327, DOI 10.1016/j.ijmachtools.2009.10.006; [MIT author manuscript](https://web.mit.edu/2.70/Reading%20Materials/Kinematic%20coupling%20review%20article.pdf), especially exact constraints pp. 2–3 | Contact constraint count, preload, compliance and friction. Does not validate these horizontal mechanisms; no published coupling repeatability transferred to this project |
| [Carr Lane diamond-pin reference](https://www.carrlane.com/product/locating-pins/locating-pins/round-diamond-pins/diamond-pins) | Relieved secondary locating principle; ordinary vertical pin insertion is not an admissible conversion method |
| [Kaiser 6061 sheet/coil/plate data](https://online.kaiseraluminum.com/depot/PublicProductInformation/Document/1015/Kaiser_Aluminum_6061_Sheet_Coil_and_Plate.pdf), Rev. 05/06, pp. 1–2 | Typical E=68.3 GPa and alpha=23.6e-6/K over 20–100 °C. No plate alloy, residual stress, sheet laminate or service temperature is established |
| [THK master-guide installation reference](https://www.thk.com/us/en/products/lm_guide/maintenance/0001/) | Engineered guide datum/assembly practice; does not supply a tolerance for printed foundations |
| [THK SRS12WMUU(GK) catalog record](https://store-na.thk.com/Catalog/linear-motion/linear-motion-guide/srs12wmuu-block), part record 202K12011000000 | Example body 44.5×40 mm, assembled height 14 mm. Only dimensional scale used; rail length, moments, fastener/tool envelope, preload, pricing and regional availability are not qualified |
| [igus cable-carrier filling/design guidance](https://www.igus.com/cable-carriers/resources/energy-chains-designing-filing-com) | Bend-radius, separation and strain-relief considerations. R=30 mm in this study is hypothetical, not an igus rating or selected cable |
| [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297), 1994 | Combined/expanded uncertainty and transparent reporting. No calibration or measured uncertainty budget exists for this rig |

Free-expansion, contact-Jacobian, gap-interval and rectangular-sweep derivations are stated in the study so they can be challenged without a proprietary tool. Bow is a free strip-curvature sensitivity, not a referenced laminate solution. Generic steel alpha=12e-6/K is explicitly a sensitivity assumption. No new reinforcement profile is specified; prior stock alternatives remain unselected and require actual sourcing/tolerance verification before CAD.

## Requirement-preservation audit

| Obligation | Location / treatment |
| --- | --- |
| Four nominal 180 mm heated modules and separate sheets | Thermal model includes independent temperatures and sheet/slip uncertainty; no bridge sheet or exact usable-area promise |
| Automatic horizontal fixed-height conversion | Dock entry/release has no vertical landing; continuous gravity support; guide height/tilt error retained as unresolved |
| I, H, V, both mixed orientations and J | Eight states including mirrored mixed pairs; all directed box transitions and occupied-coordinate rejection checks |
| Preserve running jobs and clear moving beds | Packaging occupancy rule plus explicit unmodeled object/head/thermal/vibration constraints; no active-bed thermal repositioning |
| Printable reinforced frame first, Ender 3 fit | Rig transfer requires representative printed nodes, actual usable print envelope and load/heat measurements |
| Separate imperial and metric stock interfaces | No rounded-stock substitution; separately generated/qualified future interfaces and sourcing remain required |
| Later 2020 edition | Core capabilities unchanged; separate structural qualification required |
| Editable parametric sources and reproducibility | Plain-text equations, original diagrams and standard-library source; native parametric CAD still required later, no CAD platform selected |
| First two-bed seam proof / staged safety gates | Rig recommendations preserve cold → supervised heat → seam printing; no operation authorized |
| Architecture, electronics, firmware, materials, suppliers, license undecided | Recommendations rank investigations only; decision table requires human review |
| Four-head cooperation remains stretch | No cooperative-head capability assumed or implemented |
| Preserve prior analysis/rejections | Phase 1 retained; only a follow-up link added; narrowed conclusions explicitly identify assumptions |

## Reproduction

From the repository root with Python 3.9+ and no third-party dependencies:

```sh
python docs/phase1b/analysis.py --write
python -B -m unittest discover -s docs/phase1b -p test_analysis.py -v
python -B -m unittest discover -s tests -v
git diff --check
git diff --cached --check
```

`--write` regenerates only `docs/phase1b/results.md`. Without it, results print to stdout. The model defaults and functions are editable parameters, not a selected printer build system. This Windows session used the bundled Python runtime supplied by Codex; no dependencies were installed.

## Checks performed

- Analytical model executed and generated tables inspected: ambient/equal/differential cases, both orientations, anchor inset limits, four-corner geometry, rail arithmetic and known negative-gap cases.
- Eleven model checks passed: temperature exchange/rotation, zero-rise limit, center/inset limiting cases, common translation, four-corner symmetry, lost-yaw constraint rank, redundant guide yaw, all 64 directed mode pairs per screened layer, oversized-carrier and mid-path collision counterexamples, occupied-region rejection, invalid inputs and generated-output agreement.
- Existing reporting regression suite: all 15 mocked tests passed. Process-local TMP/TEMP/TMPDIR used the repository directory to avoid sandbox temporary-directory restrictions. Reporting implementation is unchanged.
- Markdown check: all nine changed/new Markdown files have existing local link targets, balanced code fences and document titles; tables and terminology reviewed. Requirements, roadmap and root README are byte-for-byte unchanged against the baseline. Unstaged whitespace check passed.

## Independent desk review

A separate read-only reviewer inspected the actual Phase 1B files, tracked diff, task acceptance criteria, Phase 1 baseline, requirements and shared review rubric without receiving the author's self-review. Recommendation: **APPROVE for this bounded documentation/analytical study**, with **0 Critical, 0 Important, 0 Minor** findings. Overall confidence Medium; analytical test coverage confidence High; requirement/architecture compliance Yes. PR/reporting completion was outside this engineering review.

The reviewer independently ran all 11 model checks, recalculated center/inset full-range closure (0.33984/0.03776 mm) and preload reactions (16.67/33.33 N), and exhaustively checked occupied-module subsets across all 64 directed mode pairs. Kaiser material inputs and THK dimensional examples were independently corroborated against their primary sources. Highest remaining risks: actual sheet/plate thermal behavior and unresolved assembled packaging. Neither the review nor the calculations approve hardware operation; qualified mechanical/electrical/safety review remains necessary.

During work another session created `.worktrees/community-onboarding` and switched the shared checkout to main. The author restored the Phase 1B branch, preserved the unrelated worktree and limited staging to this study's explicit paths. No supporting-repository changes were made.

Not performed: physical metrology, detailed assembled collision checking, plate/laminate finite-element or thermal-field simulation, contact stress sizing, flexure fatigue, head/object swept volumes, actual cable fit, qualified safety sign-off, purchases, fabrication, energized tests or printing. These are unresolved engineering work requiring drawings, measurements and authorization. The source-reference review cannot establish a safe prototype.

Final commit/PR/CI and Discord delivery evidence belong in the Draft PR handoff. Supporting repositories were read only; durable follow-up is identified in [rig decisions](rig-and-decisions.md). AgentMemory was unavailable.
