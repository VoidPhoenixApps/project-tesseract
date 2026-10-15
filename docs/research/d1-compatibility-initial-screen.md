# D1 — preliminary mode × XY × Z architecture compatibility screen

**Date:** 2026-10-14. **Status:** Initial desk research for public challenge; **unreviewed**, **not an architecture selection**, and **not physical validation**. All entries are conditional functional screens, not measured clearances, tolerances, stability, safety, or build volumes.

## Follow-up audit and expanded package

The [first comparative investigation](d1-engineering-study.md) extends this initial
screen with all-mode integrated candidates, [equations and reproducible calculations](d1-calculations.md),
[editable conceptual diagrams](d1-diagrams.md), a [failure-mode study](d1-failure-study.md)
and [verified sources and limitations](d1-verification.md).

**Audit correction:** The Z-C/Z-F partial-mode B entries below apply to the restricted
single-gantry/locked-bed or unified-frame-only forms. Retaining independently grouped
bed lifts can supply partial modes, conditionally, with E-like synchronization and
support obligations. The expanded report supersedes any broader impossibility reading;
these initial deductions remain visible as the reasoning being challenged.

## Purpose, inputs, and evidence classes

This is the first bounded result of the [research-first plan](../research-first-plan.md). It screens all five mandatory layout families before more detailed CAD. The approved [requirements](../requirements.md) govern. The [toolhead/Z concept backlog](../concepts/toolhead-z-motion-exploration.md) contains XY-A–E and Z-A–F, but these labels describe ideas at different levels of abstraction.

| Evidence | Classification | Finding relevant to this screen | Limitation |
| --- | --- | --- | --- |
| [Requirements](../requirements.md), [roadmap](../roadmap.md) | Approved targets and proposed gates | Four nominal 180 × 180 mm beds and four retained sheets; automatic horizontal reconfiguration at common reference plane; singles, both pair orientations, mixed and joined; independent work; printable-first, both stock standards, later 2020 edition and removable enclosure | No physical configuration proven |
| [Phase 1](../phase1/README.md) and [configuration feasibility](../phase1/configuration-feasibility.md) | Analytical trade study | Independent XY carriers were prioritized as an investigation baseline; compact shared-row travel and uniform mechanisms exhibited mode restrictions | Candidate geometric envelopes and assumptions, not full-machine layout |
| [Phase 1B](../phase1b/README.md) and [thermal analysis](../phase1b/thermal.md) | Analytical negative/conditional results | Fixed center anchors failed the screened 0.10–0.30 mm seam-gap range across 20–100 °C; free expansion varied by 0.33984 mm under stated assumptions; inward-corner referencing is worth testing | Not hot physical measurements or an approved acceptance window |
| [Phase 1C](../phase1c/README.md) and [verification](../phase1c/verification.md) | Parametric concept and software/maintainer checks | Two-bed cold docking fixture A/B geometry and selected bounded checks exist; a corrected geometry checker and retained failures are recorded | Neither structural fit nor hot docking, active Z, four-bed integration, or physical testing is validated |
| [XY/Z exploration](../concepts/toolhead-z-motion-exploration.md) | Maintainer concept proposals | Independent XY options, Z-A–F, two-type mirrored-head packaging and belt-switched secondary Z frame were captured | No detailed carriage, drive, load path, control or quantified sweep |
| Manufacturer/firmware references below | External examples of subsystem functions | Segment heating, tool changing, multiple carriages and precision guides have precedent | None demonstrate automatic reconfigurable heated-bed docking, independent quad-head concurrency, or switchable multi-bed Z |

## Five mandatory mode families — functional obligations

These are functional questions independent of specific rails, screws, motors or controllers. 'Z groups' means independently progressing print-height coordinate systems; a joined group also needs physical seam alignment and load support.

| Mode key | Bed grouping | Potential simultaneous job progress | Z-group requirement if printing Z is bed-side | Head reach requirement |
| --- | --- | --- | --- | --- |
| S — singles | 1 + 1 + 1 + 1 | Four unrelated jobs | Four independent groups | Four concurrently useful local workspaces |
| R — row pairs | 2 + 2, side-by-side in rows | Two unrelated seam-spanning jobs | Two independent groups | Two heads/path systems each spanning a horizontal seam |
| C — column pairs | 2 + 2, top-to-bottom in columns | Two unrelated seam-spanning jobs | Two independent groups | Two heads/path systems each spanning a vertical seam |
| M — mixed | 2 + 1 + 1 | Three unrelated jobs | Three independent groups | One pair-spanning head plus two single-region heads without collisions |
| J — joined | 4 | One seam-spanning job | One joined group or suitable head/gantry-side Z | At least one demonstrably full-region toolpath, independently of cooperative four-head printing |

All rearrangement must occur at the required common fixed-height horizontal reconfiguration datum with affected modules clear and safe. These group counts are **logical control requirements**, not proof that a mechanical linkage can implement them. The 360 mm and 180 mm labels are nominal module sums, not validated nozzle reach or usable volume.

## XY-side screen

Key: **P** = function conceptually provided, subject to geometric and safety proof; **R** = critical capability remains unresolved in the proposed architecture; **N/A** = not a standalone XY mechanism. Neither P nor R is a measured pass.

| XY | Idea | S | R | C | M | J | Main reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | Four local independent XY gantries | P | R | R | R | R | Four local nozzles do not automatically reach either neighboring bed, much less the whole joined area; parked gantries and tall finished objects can obstruct travel |
| B | Shared framework with four genuinely independently driven XY heads | R | R | R | R | R | Structural sharing is not itself independent two-axis kinematics; route conflicts, carriage ordering and central intersection remain open |
| C | Four local independent heads plus a fifth full-region head | P | R | R | R | R | The fifth head is a plausible joined-job path, but **two simultaneous pair-spanning jobs** still need two independently progressing pair-capable heads; parking and 3D envelope remain unknown |
| D | Shared/reconfigurable gantry, modular heads or overlapping reach | R | R | R | R | R | Toolchanging/one shared active gantry alone cannot deliver simultaneous independent jobs; variant needs independent path specification |
| E | Mirrored A/B toolhead orientation (1=4, 2=3 by 180° rotation) | N/A | N/A | N/A | N/A | N/A | **Packaging overlay on A–D**, not an alternative motion topology; evaluate on each physical gantry/rail candidate |

**XY-E preservation:** Two nominally distinct assemblies (A and mirrored B), reused diagonally. The nozzle faces the interior corner, while extruder bulk faces outward. Confirm actual rotation/reuse with mounts, ducts, filament path, fan flow, probe, cables and complete 3D swept clearances. None of the XY alternatives may depend on unproven four-head cooperation to deliver baseline J.

## Z-side mode compatibility

Key: **P** = functionally plausible in the named idea but unverified; **R** = concept needs specified supporting mechanism, controls and proof; **B** = **not supported as presently described** for independent jobs in this mode; redesign can create another candidate. XY head reach and safety remain separate gates in every row.

| Z | Printing-Z concept | S | R | C | M | J | Reason and required discrimination |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | Independently moving head/gantry-side Z, nominally stationary beds | P | P | P | P | P | In principle independent head Z can track unrelated jobs; joined reach, multi-gantry crossing, head stiffness and parking not supplied |
| B | Four independently lifted beds | P | R | R | R | R | Independent motors alone do not ensure seam step, angular consistency, load transfer or fault-safe synchronization for a joined print; a linked/monitored subgroup becomes an E-like variant |
| C | Individual bed Z for singles, one moving gantry Z for joined | P | B | B | B | P | As written a **single shared** joined gantry Z does not provide two independently advancing paired prints or 2+1+1; additional separate gantry Z groups fundamentally change the proposal |
| D | Common gantry Z plus individual short-stroke head Z | R | R | R | R | P | Unrelated jobs can diverge in accumulated height beyond finite head stroke; quantify maximum divergence, service travel and available build height |
| E | Selectively coupled/coordinated bed Z groups | P | R | R | R | R | Row and column pair selection, 2+1+1 grouping, group reference, positive support, heat-induced binding, safe drive fault response and phase/load sharing all unproved |
| F | Individually belted lifts with belt-switched secondary joined lifting frame/cross | P | B | B | B | R | **One permanently unified four-bed secondary frame** does not supply two independent pairs or mixed groups; selective frame sections or alternate paired mode must be specified. For J, switching, support and indexing remain unproved |

**Important:** B denotes insufficiency of the architecture **as described**, not a theorem that no revised implementation is possible. Modes must work with unrelated Z progress; a pause/restart assumption must not silently replace independent printing. Z-F's literal belt-redirection idea and a separate positive-clutch alternative are both retained for research, with different transmission/failure paths.

## Cross-product XY × Z risk index

Each cell lists the highest-priority unclosed **functional gate** for the combined candidate, not a compatibility verdict. Read alongside both mode tables; every combination remains **unvalidated**. This keeps the complete A–E × A–F cross without treating XY-E as if it contains motors/rails.

| XY \ Z | Z-A | Z-B | Z-C | Z-D | Z-E | Z-F |
| --- | --- | --- | --- | --- | --- | --- |
| XY-A: local gantries | H | H+G | H+P | H+T | H+G | H+P |
| XY-B: common rails, independent heads | H+I | H+I+G | H+I+P | H+I+T | H+I+G | H+I+P |
| XY-C: local + full-region fifth | H2 | H2+G | H2+P | H2+T | H2+G | H2+P |
| XY-D: shared/reconfigurable | H+I | H+I+G | H+I+P | H+I+T | H+I+G | H+I+P |
| XY-E: rotated mirrored A/B packaging | Overlay | Overlay | Overlay | Overlay | Overlay | Overlay |

Gate codes: **H** = prove pair/full nozzle reachable sets, parked swept collision-free volume; **H2** = prove at least two independently usable seam-spanning heads in pair modes notwithstanding a fifth full-region head; **I** = prove truly independently driven XY motion and unrelated job progress; **G** = demonstrate group registration, support and Z synchronization/coupling for 2+2, 2+1+1 and 4; **P** = provide a genuinely independent partial-mode Z strategy beyond a single large-mode gantry/frame; **T** = show sufficient independent Z range at maximum permitted job height divergence. **Overlay** = evaluate flipped/mirrored toolheads on each candidate, including their nozzle-centered swept 3D volumes.

## Early deductions worth challenging

1. **XY-E is an orientation constraint, not a fifth complete transport architecture.** It can improve inward nozzle access while still leaving the transport/carriage reach problem open. Any matrix that treats it as a substitute for XY-A–D risks comparing unlike things.
2. **Z-F has a partial-mode functional gap in its current single-frame form.** Its joined mode might be worth a bounded comparison, but a sectional/selectable solution must show both pair orientations and mixed-group drive/load ownership without mechanically overconstraining docked beds.
3. **Z-C also has a partial-mode gap if it means only one shared moving gantry.** No amount of single-object joined coverage proves two independently advancing paired objects can be printed at once.
4. **XY-C solves only part of the coverage question by adding a fifth head.** It does not solve multiple simultaneous paired jobs unless at least two active head systems cover their respective pair spans.
5. **Precise cold registration is not adequate hot seam validation.** The Phase 1B negative thermal result should stay visible. A central cross on a cold frame may index carriers but must not become an assumed hard constraint on all heated sheet edges.
6. **Unverified simultaneous-motion firmware behavior is not a mechanism.** State transitions, sensing, active-object protection, collision envelopes, missed steps, drive disengagement and power loss need separate review.

## External primary references (read as precedents, not validation of Tesseract)

- [Klipper configuration reference](https://www.klipper3d.org/Config_Reference.html): multi-extruder, dual-carriage and additional motion sections exist; these do not establish native coordination for this four-independent-job, reconfigurable-bed design.
- [Prusa XL+ manufacturer description](https://www.prusa3d.com/product/original-prusa-xl/): toolchanger and segmented *fixed* heatbed demonstrate a different way to distribute heaters and tools; they do not demonstrate moving bed docking or four independent XY heads.
- [ELEGOO OrangeStorm Giga manufacturer specifications](https://us.elegoo.com/products/orangestorm-giga): four separately heated plates and optional multiple nozzles demonstrate segmentation and multi-nozzle arrangements, not automatic moving-bed reconfiguration. Manufacturer claims are not independent performance evidence.
- [HIWIN linear guideway installation resources](https://hiwin.com/resources/installation-instructions/): guide mounting/parallelism require controlled datums and alignment; automatic cross-coupled support cannot assume nominal rail alignment.
- Existing [Phase 1 references](../phase1/references.md) and [Phase 1B sources](../phase1b/verification.md) remain the quantitative provenance for earlier local screening assumptions.

## Next reproducible research package — not CAD authorization

1. Draw editable, clearly conceptual top-view and side-view mode diagrams for at least XY-A/Z-A, XY-C/Z-A, XY-A/Z-E, and XY-A/Z-F, including both pair orientations, one mixed mode, tool parking and maximum object heights.
2. Determine full nozzle XY *reachable sets*, 3D swept envelopes and required parking/clearance margins from traceable bounds. Do not use nominal 180 × 180 sheet area as actual reachable area.
3. Make Z-E and Z-F selector/load-state diagrams with explicit safe, disconnected, engaged and fault states for S/R/C/M/J, including phase, belt tension, load support and power loss. Review the Z-F cross indexing constraint/thermal relief separately.
4. Parameterize head offsets, Z bed+part masses, guide skew, frame compliance and the sheet seam gap/step error budgets. Reference the Phase 1B inputs; propose ranges and measurement methods without inventing pass limits.
5. Invite external critique before narrowing options. A revised matrix must record rejected variants and why; CAD can resume only after the documented research review, with specific maintainer authorization.

**Verification status:** Documentation-only desktop screen based on public/current repository records and cited external source descriptions. No physical tests, thermal measurements, purchased component selections, CAD runs or independent review performed for this D1 note. Model feasibility, support for concurrency, dimensions, budgets, source-model rights and firmware integration are unresolved.
