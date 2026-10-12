# Phase 1B — precision docking, thermal expansion and packaging

**2026-10-12 · Engineering investigation for review, not architecture approval.** No manufactured assembly, physical measurements, heater operation, machine motion or engineering gate completion. The first target remains a two-bed docking and cross-seam proof. All rankings below select further investigations only.

Baseline: [Phase 1](../phase1/README.md), merged as [PR #7](https://github.com/VoidPhoenixApps/project-tesseract/pull/7), commit `7b734b0218b9589a030c1cd28d548159a2c02af5`, verified against GitHub main. Shared workflow and standards: project-knowledge `46ff107e35053b970915a3ca147f5513571f7be6`, verified against GitHub main. No Tesseract CURRENT_STATE record was found there. Current Home Infrastructure instructions were read through GitHub. Neither supporting repository was modified. AgentMemory was unavailable.

| Read | Purpose |
| --- | --- |
| [Docking interfaces](docking.md) | Six-DOF allocation, constraint equations, horizontal capture, preload and failures |
| [Thermal analysis](thermal.md) | Anchor comparisons, sheet uncertainty, gap feasibility and height effects |
| [Packaging](packaging.md) | Dimensioned envelopes, nested guides, locks, wiring, tug and configuration paths |
| [Two-bed rig and decisions](rig-and-decisions.md) | Replaceable cartridges, measurements, ranked shortlist, risks and human decisions |
| [Calculation source](analysis.py) / [generated results](results.md) | Standard-library analytical model and conservative rectangular sweeps |
| [Model checks](test_analysis.py) | Boundary, symmetry, constraint-rank and negative-control checks |
| [Sources and verification](verification.md) | References, applicability, checks, independent review and omissions |

## Findings that narrow the next experiment

1. **Investigate a cold-carrier/hot-plate hybrid with interchangeable guide-retained and planar-floating docking cartridges.** Start with guide-retained yaw as the simpler control; retain a 2+1 floating cartridge to test whether releasing guide yaw improves repeatability enough to justify its stiffness and fatigue burden. Neither corrects guide height errors automatically.
2. **An inward-corner thermal reference can preserve both joining directions in the uniform free-expansion model.** It must stay permanently assigned to each quadrant; no automatic anchor switching is assumed. A practical inset anchor gives residual normal growth, and a steel sheet that slips on an aluminum plate does not inherit the plate's anchor automatically. This is the leading thermal experiment, not a demonstrated mount.
3. **Fixed center anchors cannot keep a 0.10–0.30 mm seam across the entire 20–100 °C screening range on a stationary frame.** Growth varies by 0.33984 mm, wider than the proposed 0.20 mm gap window even before uncertainty. Increasing cold gap prevents contact but does not establish printability across that range. The window itself remains unapproved.
4. **Guide packages can plausibly occupy separate quadrant pockets, but the earlier 160 mm box is not a complete stage design.** A catalog-sized two-block example with 70 mm block separation needs 174.4 mm rail length for the screened stroke and margins. Reducing spacing to 50 mm fits the rail arithmetic within 160 mm, at increased moment-reaction demand. Motors, fasteners and floating stages remain unallocated in detail.
5. **The shared tug requires an explicit unobstructed lower plane and downward access to every pallet.** The model reserves this space; it does not prove a dog can pass through stacked stages. A blocked attachment path eliminates the screened tug implementation even if bed endpoint coordinates work.

No final bed mechanism, Z strategy, head architecture, electronics, firmware, material, supplier, CAD platform, reinforcement size or license is selected. Four individual nominal 180 × 180 mm heated beds and sheets, all layout modes, automatic horizontal conversion, printable-frame-first development, Ender 3-sized printed parts, separate imperial/metric interfaces, later 2020 edition and reproducible editable sources remain mandatory. Four-head cooperation remains stretch work. See the unchanged [requirements](../requirements.md).
