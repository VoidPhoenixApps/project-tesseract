# Phase 1C — cold two-bed docking CAD concept

**Status: reviewable source and analytical envelope checks, not fabrication-ready.**
The maintainer reports successful B,inset generation and default bore inspection
on macOS, plus gap/release/docking CHECKs and rejection of invalid X-first travel.
The rectangle-edge correction now passed the maintainer's B,inset carrier sequence
160→164→160→156→164→156→160 mm. Seven local CHECK reports confirm all 59 footprints
fully constrained, matching bounds/volumes and passing nominal box sweeps.
See [verification](verification.md) for the earlier failure, exact evidence and
limits. The planned macOS CHECK matrix is now complete, including gap/release,
mounting, anchor/contact, all four variants and expected negative rejections.
See verification for report-inspected versus maintainer-observed evidence. Full
parameter combinations, exports, independent Windows execution, physical docking,
thermal/load validation and full collision certification remain unverified.
No engineering gate or physical test is approved.

The [generator](../../cad/fusion/TesseractDockingFixture/TesseractDockingFixture.py)
builds a new unsaved parametric assembly for **one selected cartridge and one
selected thermal reservation**. Run separately for `A,center`, `A,inset`,
`B,center`, and `B,inset` to compare. Each has exactly two nominal 180 x 180 mm
retained surface envelopes: a fixed reference and a horizontally moving bed.
The registered `.worktrees/fusion-smoke-test` and its script remain untouched.

## Review package

- [Engineering comparison, constraints, load paths and risks](engineering.md)
- [Parameter domain, datums, dependencies and component inventory](parameters.md)
- [Reproduction, static checks and interactive acceptance](verification.md)
- [Independent desk review](review.md)
- [Pure Python geometry specification](../../cad/fusion/TesseractDockingFixture/fixture_model.py)
- [Source and analytic tests](../../tests/test_phase1c_fixture.py)

The baseline is GitHub `main` at `2d5ca1497ffbd929e09a386d21eccb20d2b1f8ba`,
especially [Phase 1B docking](../phase1b/docking.md),
[thermal analysis](../phase1b/thermal.md),
[fixture recommendations](../phase1b/rig-and-decisions.md), and the
[Phase 1 all-mode path study](../phase1/configuration-feasibility.md).
Those studies' quantitative physical acceptance limits remain proposals.

## Scope decisions for this drawing only

- A **laboratory reference base envelope** isolates the docking question. It is
  not a printable-frame design or a purchased plate. Printed candidate nodes,
  carriers and mount plate are individually screened against a provisional
  200 x 200 x 180 mm budget, not certified Ender 3 fit or stiffness.
- Two stacked **idealized X/Y guide envelopes** maintain support at one fixed
  height. They do not select production transport, rails, bearings or actuators.
- A: one X contact and one Y contact; yaw passes through three rigid coupling
  keys to the guides. B: two separated X contacts and one Y contact; three
  sliding shoes retain vertical support while allowing planar slip. B's guards
  limit escape, but its centering/hold-down is only reserved, not engineered.
- Three noncollinear plate-height support envelopes remain separate from
  center/inset anchor and radial-relief reservations. No heater is modeled.
- Contacts are flat pad **envelopes**, not a finished exact-constraint contact
  shape. Real conformal faces add moment constraints; pad crown, compliance,
  friction, contact stress and mounting need development before fabrication.

This scope supersedes none of the [requirements](../requirements.md). In
particular it neither solves nor removes four-bed layouts, independent retained
sheets, printable-first development, separate imperial/metric interfaces, the
later 2020 edition, or the unproven cooperative-printing stretch track.

## Toolchain and licensing boundary

Fusion is still a preferred candidate, not an adopted public toolchain. Native
Fusion parameter/feature history is generated from editable Python; no mesh-only
source is used. The kernel-independent box specification/tests are a starting
point for a future FreeCAD/build123d backend, **not an implemented non-proprietary
CAD reproduction workflow**. That backend must reproduce bores, dependencies,
component structure and checks before claiming the requirement satisfied.

Project licensing is undecided. The installed Fusion Personal entitlement does
not itself establish suitability for company/commercial work; this task makes
no licensing decision. No software, parts or services were installed or bought.

## Next experiments, in order

1. Run the four CAD variants and the parameter/check matrix in
   [verification](verification.md). Resolve kernel/API and geometry failures.
2. Desk-design B capture, centering, retention and preload sequencing, including
   finite yaw near the seam, real contact curvature and an interference/force
   model. Draw adjustments, fasteners and tool access from actual component data.
3. Prepare a **separately reviewed cold test proposal** for A/B repeatability,
   preload hysteresis and support deflection with measured representative loads.
   Before any operation: hazard assessment, limits, uncertainty, supervision,
   abort rules, restrained energy and competent mechanical review are required.
4. Only after independent authorization and cold evidence, propose center versus
   inset thermal-support experiments, then cross-seam work. Neither is authorized
   by this CAD package; the four-bed central junction remains a separate test.

After review/merge, any cross-project knowledge promotion should link to this
package and its limits. There is no Tesseract `CURRENT_STATE.md` in the inspected
project-knowledge checkout; none was invented. Home Infrastructure's POTUS
development record separately needs the user-reported Fusion installation and
smoke-test evidence. Supporting repositories were not changed. AgentMemory was
unavailable; current repository sources were used.
