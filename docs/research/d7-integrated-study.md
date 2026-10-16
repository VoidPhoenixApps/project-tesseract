# D7 — integrated architecture research and evidence-gated shortlist

**2026-10-15, America/Chicago. Research proposal for [issue #39](https://github.com/VoidPhoenixApps/project-tesseract/issues/39); no final architecture selected or physical capability validated.**

The best next investigation is a comparison between independent head Z and monitored
bed-group Z using perimeter XY stages. A third candidate retains automatically
reconfigurable stages and a secondary joined frame to test whether their extra
mechanisms earn their complexity. None has demonstrated full-machine clearance,
hot seam behavior or fault-safe load retention. Detailed printer CAD remains paused.

The central conflict is the combination of **two independent seam-spanning jobs at
unrelated heights**, plus three independent jobs in mixed modes. Local machines
cannot reach across seams; one extra global head cannot print two paired jobs at
once; and full-width bridges that cannot pass cannot supply arbitrary column jobs.
Adding enough motors does not resolve those conflicts. Conversely, the early blanket
exclusion of Z-C/Z-F partial modes was too broad: retaining independent grouped lifts
can express them, with additional support and control obligations.

## Read the evidence

| Artifact | Purpose |
| --- | --- |
| [Evidence inventory](d7-evidence.md) | Pinned source state, established desk results, preserved failures and physical gaps |
| [Compatibility contracts](d7-compatibility.md) | Eight modes, assignments, support/ownership and named counterexamples |
| [Full matrix](d7-matrix.md) | 12 XY × 16 Z variants × eight arrangements; E overlay explicitly factored |
| [Failure chains](d7-failure-chains.md) | Coupled mechanical, thermal, electrical, panel and scheduling failure paths |
| [Concept diagrams](d7-diagrams.md) | Editable top/side and support sketches; no dimensioned geometry |
| [Future experiment and model queue](d7-experiments.md) | Discriminating evidence, exact catalog dependencies and stop gates |
| [Consolidated catalog request appendix](d7-model-requests.md) | Offline Stage D request output; no download or approval |
| [Verification](d7-verification.md) | Actual checks, review disposition, file inventory and limits |

## Shortlist for investigation, not adoption

All candidates retain the Phase 1 independent horizontal-carrier research baseline
and compare Phase 1B relieved cold-carrier docking. That is a study assumption, not
selection of a transport mechanism or latch. All share four individual heated sheets,
fixed-height horizontal reconfiguration and G1–G7 in the compatibility contract.
Prefer no unnecessary hot-edge constraints; inward-corner anchoring remains a
comparison against center anchoring, not a solved seam design.

| Candidate | Integrated mechanism and greatest merit | Killer unresolved issue / dissent | Complexity and reproducibility burden | Evidence that could reverse its priority |
| --- | --- | --- | --- | --- |
| H: A+cant + Z-A, common vs E heads | Four perimeter serial XY stages with independent full-range head Z; locally supported stationary beds avoid joined-bed lift synchronization | Long arms/slides may be too compliant or obstruct neighboring tall parts. D2 has no actual clear sweep. Stationary seams still drift thermally | Four independent XYZ systems, gantry fall restraint, long harnesses and stiff roots. Compare D4 deep printed truss/metal chords versus tube-and-node permanent bracing; both stock standards need separate interfaces | Exact swept models or root compliance could eliminate H before detailed CAD. Lower bed-lift error than cantilever nozzle error could favor B |
| B: A+cant/B3 + Z-E-sync; E-hybrid as a bounded alternative | Independent local bed supports remain in every mode; one group trajectory with measured actual surfaces; no secondary-frame selector | Bed XY transport must carry full Z guides or transfer support; differential lift motion can spoil seam or break a joined object. Bed Z does not remove XY collision | Similar installed axis count to H, greater moving bed/part mass, XYZ heater flex, surface/skew observations and downstream restraint. Same printed frame alternatives, separately assessed at enclosed temperature | Measured joint/support compliance, fault-stop skew and harness routing may make head Z preferable. Hybrid only survives if added tie lowers error without guide binding/uplift |
| R: D+ + Z-F-group-clutch, compared with literal rerouting and C-group | Automatically relocated/retracted stages could avoid fixed bridge ordering; retained partial lifts preserve every grouping, J platform might reduce differential Z | Neither transformation nor continuously supported handoff is defined. D3's rerouting example loses intermediate belt path demand; positive selection still needs phase and support | Highest joints, locks, sensors, calibration and retained unused structures. Custom selectors/restraints lack exact catalog entries; frame and wiring crowding severe. C-group comparator exchanges J platform for stationary bed locks plus gantry Z | A concrete no-selector C-group or H/B geometry meeting requirements would remove much justification. R earns priority only with an observable clearance/alignment benefit exceeding its extra fault burden |
| L: A0 + Z-A fixed local-region control | Four conventional independent local machines establish simpler ownership and modular service | Fails automatic region combination, both paired directions, every mixed pair and J. Explicitly not compliant and not a fallback requirement change | Fewer shared moving structures; still requires a printable-first frame, both stock variants, protection and open/enclosed assessment | Useful only as control for local stiffness, independent-job logic and cost drivers; cannot win the full requirement comparison without becoming A+ |

For H/B compare mirrored E against common orientation with equal complete component
volumes. D2's synthetic inward body clearance gain is balanced by outward park space;
no two-type BOM or whole-machine benefit is established. R may also use E, but
orientation does not supply passing lanes or independent coordinates. C+ remains a
**reserve comparator**: two pair-capable locals plus a fifth global head could work
at the ownership level, but adds an independent machine before solving four-head
structure. B2's fixed overhead stack remains a challenger only with a concrete
route for descending columns past lower bridges.

There is no defensible numerical ranking or price estimate without actual masses,
strokes, joint stiffness, guide options and a BOM. Catalog categories show possible
supply routes, not obtainable exact assemblies. Only one unrelated electronics
sample is authorized locally. A higher motor count could still produce fewer risky
handoffs; a clever shared transmission could increase maintenance and calibration.

## What is established and what would unlock CAD

Established desk findings include the center-anchor thermal-window contradiction,
axis/ownership exclusions, synthetic collision counterexamples, guide-loop and
joint-compliance sensitivities, and conservative scheduler rejection behavior.
These results justify rejecting specific assumptions; they do not establish a
working integrated candidate. No D7 physical measurements were taken, and no prior
physical seam or prototype validation is recorded in the reviewed sources.

The next decision is a bounded geometry/measurement plan, not a final architecture.
Before resuming even narrowed detailed CAD: maintainer acceptance of this comparative
research; independent mechanical and electrical/controls review of proposed obligations;
a specific experiment scope with explicit unknowns and acceptance criteria; exact
component identities, rights and approved reference geometry for its interfaces;
and a reproducible public toolchain path. Before any physical work, additionally
require reviewed hazards, limits, uncertainty, supervision and abort/recovery procedures.
The first physical proof remains **two-bed docking and cross-seam printing**; the
queue does not authorize execution or put a full machine ahead of that proof.

## Requirement coverage and open decisions

[Requirements](../requirements.md) remain unchanged in full. The matrix preserves
S/R/C/M12/M34/M13/M24/J, 4/2/3/1 independent progress owners and a candidate single-head
J route. Four-head cooperation on one object stays a separate unproven stretch goal.
Four nominal 180 × 180 mm modules retain four sheets; usable area, height and
performance limits remain unknown. No vertical reconfiguration, manual sheet swap,
or forced serialization is credited as satisfying the targets.

The printable/reinforced edition comes first; every printed component must fit an
ordinary Ender 3 with later reviewed margins/orientation. Distinct actual imperial
and metric stock require ready-to-print labeled outputs, BOMs/cut lists and validated
interfaces without scaling, builder CAD edits, reaming or improvised shims. The later
2020 edition must retain the same core capabilities and receive separate verification.
Tool-free removable environmental panels must preserve every mode open or enclosed,
without structural disassembly; they are not assumed protective guards. Native editable
sources and public reproducibility remain mandatory. Final architecture, stock,
components, electronics/firmware, CAD toolchain, operating limits and license remain open.
No existing open-source grant, safety certification or unattended readiness is implied.

Community contributors can challenge one matrix cell by naming the exact variant,
mode, source assumption and counterexample or corrected mechanism. Useful evidence
includes a full path/support graph, a reproducible calculation or a rights-qualified
model source; attractive renders alone cannot close a gate. Submit through
[Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions) or issue #39.
