# D7 — integrated evidence inventory

All repository paths below were inspected at the clean synchronized baseline
[`8b2512035560350863a27fd7fb99af2366ffed2c`](https://github.com/VoidPhoenixApps/project-tesseract/tree/8b2512035560350863a27fd7fb99af2366ffed2c),
which includes library Stages A–D and D1–D6. Relative links are convenient current-tree
links; use that immutable tree for the exact D7 input revision. D7 does not revise
old result files. Earlier reports' references to then-open stacked Drafts are historical;
they are not claims that those PRs remain open today.

Evidence types: **R** approved requirement; **P** concept/proposal; **A** analytical
calculation; **S** software or synthetic geometry/model check; **I** independent AI
review of stated scope; **M** physical measurement. I is not qualified engineering
certification. No M evidence validating hot docking or an integrated printer was found.
Manufacturer sources recorded in D1–D6 are external documentation, not Tesseract tests.

| Source / evidence type | Established result and valid scope | Negative/correction preserved and remaining gap |
| --- | --- | --- |
| [Requirements](../requirements.md), architecture, roadmap; R/P | Approved targets and staged evidence gates, not demonstrated operating envelope | No size/speed/temperature/seam/height acceptance limits established; all mandatory modes retained |
| [Phase 1 configurations](../phase1/configuration-feasibility.md), [equations](../phase1/preliminary-calculations.md), [verification](../phase1/verification.md); A/P | Independent horizontal carriers worth investigating; ideal expansion/drive/structure estimates | Compact shared-row/uniform topology restrictions; vertical landing and diagonal-only conversion do not meet targets. Simplified geometry omits machine structures |
| [Phase 1B docking](../phase1b/docking.md), [thermal](../phase1b/thermal.md), [results](../phase1b/results.md); A/S | Center anchors close a 180 mm aluminum seam by .33984 mm over 20–100 °C in uniform free-growth model (alpha 23.6e-6/K). Proposed .10–.30 mm gap window cannot contain that range | Negative gap means contact/model breakdown, not physical interpenetration. Window unapproved. Inset 10 mm gives .03776 mm closure, but sheet slip, bow, adhesion and gradients unbounded |
| Same Phase 1B; A/S | Permanent quadrant assignment permits inward-corner references for both seam directions in ideal model; B floating carrier has six independent constraints | Supersedes earlier corner-mode-conflict suggestion. Adding retained guide yaw gives seven equations/rank six: redundant constraint. Positive reactions, preload, wear and hold-down remain unknown |
| [Phase 1C source/record](../phase1c/README.md), [verification](../phase1c/verification.md), [review](../phase1c/review.md); S/I | Bounded cold fixture parameter/checker and selected maintainer-observed CAD runtime evidence, not physical fit | Retains solver/API failures, floating-point endpoint fix and stale geometry/Z-datum corrections. Rank/bounds/volume checks do not prove capture, force closure or hot seam; existing worktree not touched |
| [D1 equations](d1-calculations.md), [study](d1-engineering-study.md), [verification](d1-verification.md); A/S/I | Relative height h=g+b; head-trim interval test; mass/torque/tilt and free-fall sensitivities | Z-C/F partial-mode blanket exclusion corrected for retained grouped lifts. 90 mm × tan(.05°)=.07854 mm is illustrative; no tolerance or measured tilt |
| [D2 reach](d2-mode-coverage.md), [study](d2-engineering-study.md), [mirroring](d2-mirrored-study.md), [verification](d2-verification.md); A/S/I | Eight final-mode reach assignments in synthetic model; injective matching prevents counting one global head twice | Local-only and single-toolchanger failures; nonpassing bridges fail arbitrary column jobs; low bridges/descending columns collide with synthetic objects/structures. No all-mode actual sweep proof |
| Same D2; A/S | Body-only mirrored separation 18 vs 60 mm under stated 2 mm reserve; outward envelope pays same 42 mm | Hypothetical park260 needs carriage280 against limit240; enlarged enclosure alone cannot fix stroke. Neither park220 at limit nor box nonintersection proves approach/return route |
| [D3 modes](d3-mode-constraints.md), [selector](d3-selector-study.md), [calculations](d3-calculations.md), [verification](d3-verification.md); A/S/I | Separate P/L/T graphs; group support needs; equal selector endpoint length can hide 3.96078 mm middle loss in point-path example | No finite pulley geometry or servo sizing. Equal phase cannot fix lead mismatch. Unified attached frame fails partial independent heights; isolated frame plus retained lifts is distinct |
| [D4 calculations](d4-calculations.md), [stock](d4-reinforcement.md), [verification](d4-verification.md); A/S/I + supplier documentation | Hypothetical tube arm member .112 mm plus root .180 mm illustrates joint dominance; distinct US/metric catalog profiles and unresolved tolerances recorded | Stiff tie with .2 mm datum mismatch produces a negative gravity-only reaction; shallow truss examples exceed linear/Euler assumptions. Not stable measured deflections or selected stock |
| [D5 study](d5-engineering-study.md), [thermal](d5-thermal.md), [safety](d5-safety.md), [verification](d5-verification.md); A/S/I | Thermal/panel sensitivities and eight-mode access obligations, no safe chamber rating | Integrated-review correction separates ordinary panel absence from protective guard access and maintenance. Tool-free panel is neither primary brace nor automatic safety interlock |
| [D6 states](d6-states.md), [scheduling](d6-scheduling.md), [electrical](d6-electrical.md), [verification](d6-verification.md); A/S/I | Synthetic resource admission, stale-state rejection, persistent occupancy, park conflict tests and peak-power arithmetic | Tests use supplied strips/volumes, not D2 machine geometry. Review caught omitted park-to-park/obstacle checks; retained correction. No production queue, real-time stop, firmware or electrical protection implemented |
| [Library catalog](../../cad/reference-parts/catalog.json), [readiness](../../cad/reference-parts/READINESS.md), [Stage D](../../cad/reference-parts/stage-d-qualification.md); documentation/S | 45 candidates/13 categories, 1 retrieval authorization, 44 documentation-only geometry records; offline rights/revision triage | A source URL or commit pin does not qualify physical geometry. Feather partial dimensions are not full fit qualification or useful printer architecture proof; all other CAD remains link-only |

## Provenance and uncertainty policy

D7 reproduces inherited analytical outputs rather than fitting new numerical thresholds.
The source ledgers in [D2](d2-references.md), [D3](d3-references.md),
[D4](d4-references.md), [D5](d5-references.md) and [D6](d6-references.md) retain exact
primary URLs, access dates and source limitations. Their catalog/rating/firmware
statements are attributed to those recorded revisions; D7 does not claim fresh stock,
pricing, current firmware support or legal permission. No new vendor models were fetched.

The material and mathematical models are conditional: uniform homogeneous expansion,
linear elastic beams/springs, ideal constraint rank and supplied conservative volumes.
Model-form uncertainty dominates their printed decimal precision. Undefined sheet slip,
creep, stop distance, contact/friction and hot warpage cannot be assigned zero or given
invented probability distributions. For a future measured quantity x with reviewed
limit L and expanded uncertainty U, the test plan must specify a decision rule (for
example an upper-bound gate x+U≤L); this example is not an approved limit or uncertainty
coverage factor. Record calibration, temperature, load, cycles, outliers and failed runs.

Independent AI reviews in earlier verification records concern desk artifacts and
software corrections. No qualified mechanical/electrical acceptance or human approval
of an integrated architecture follows from those records or the D7 review.
