# D7 — interpretation of the integrated matrix

[Overview](d7-integrated-study.md) · [all 1,536 cells](d7-matrix.md) · [source](d7_matrix.py).
This is an evidence-gated screen, not a numerical feasibility score. X means
**unsupported-as-proposed**, K **conditional**, U **unresolved**, D
**conceivable-at-DOF-only**. No class means validated. A K does not outrank D as a
whole-machine recommendation: it records a more explicit conditional subsystem contract.

## Coordinates, assignments and common obligations

X east, Y north, Z up; 1 NW, 2 NE, 3 SW, 4 SE. Reconfiguration occurs horizontally
at the common fixed datum z=0; printing Z is separate. Four nominal 180 × 180 mm
modules and their separate sheets remain in all modes. Nominal area is not usable area.
[D2's eight assignments](d2-mode-coverage.md) supply candidate head ownership:

| Mode | Groups / job-height owners | Candidate active heads | Full inactive assemblies to park | Required single-head reach |
| --- | --- | --- | --- | --- |
| S | 1 / 2 / 3 / 4; four | H1,H2,H3,H4 | None; service/escape still needed | Four local regions |
| R | 12 / 34; two | H1,H3 | H2,H4 | Two complete X-seam regions |
| C | 13 / 24; two | H1,H2 | H3,H4 | Two complete Y-seam regions |
| M12 | 12 / 3 / 4; three | H1,H3,H4 | H2 | Top X pair and two lower singles |
| M34 | 34 / 1 / 2; three | H3,H1,H2 | H4 | Bottom X pair and two upper singles |
| M13 | 13 / 2 / 4; three | H1,H2,H4 | H3 | Left Y pair and two right singles |
| M24 | 24 / 1 / 3; three | H2,H1,H3 | H4 | Right Y pair and two left singles |
| J | 1234; one | H1 | H2,H3,H4 | One path across both seams and center |

These are assignments for extended four-head candidates, not promises about A0.
C0 uses H5 for the mixed pair/J; its unused locals AND their structures must park.
C+ must establish an injective assignment with at least two pair-capable heads in
both R and C. The fifth head needs its own relative Z/control allocation. B/D may
require different assignments: changing labels cannot overcome shared coordinates.

Every row of the generated matrix incorporates the following open contracts. Reading
only its letter without these contracts loses the actual compatibility conditions.

| Gate | Obligation for every nonexcluded cell | Present evidence / missing evidence |
| --- | --- | --- |
| G1 hot docking | Cold-carrier P locators, continuous vertical support, relieved hot-plate mounts, all sheets retained; capture/release entirely horizontal at datum | Phase 1B thermal/constraint negatives; Phase 1C bounded cold geometry. Hot surface maps, friction, capture, preload and repeatability absent |
| G2 Z and restraint | One independent relative-height owner per job group; all four beds supported even when idle; separate positional P, load L and transmission T graphs | D3 group matrix; no qualified positive restraints, fault loads or stable intermediate handoff proven |
| G3 reach and parking | Complete head/beam/column/cable/probe sweeps, approach/departure, tall active AND finished objects, both panel states, uncertainty and stopping reserve | D2 synthetic clashes and unreachable parks; actual models absent. E adds H1=A, H2=mirror-X(A), H3=R180(B), H4=R180(A), fixed during travel; no purchased part is reflected |
| G4 frame | Printed joints/chords carry all reactions without panels; imperial/metric ready-to-print variants, Ender 3 segmentation and later independently revalidated 2020 edition | D4 member/spring sensitivities; joint creep, modes, load transfer and real tolerances unknown |
| G5 environment/protection | Tool-free panel fit/removal paths and all modes open/enclosed; hazard-specific protection survives either state | D5 corrected interpretation: panel absence alone is no interlock/fault. No thermal envelope, guard selection or certification established |
| G6 controls/power | Exclusive head/XY/Z/support/park/transition ownership, heater setpoint ownership, concurrent peak allocation, observed lock/plane state and bounded fault response | D6 synthetic kernel only; no firmware lifecycle, independent heater cutoff, wiring or restraint implementation |
| G7 conversion | Every bed whose group, load path, reference or pose changes is affected and empty; preserve occupied neighbors' reference/support and swept volume | D3 transition table and D6 abstract rejection logic; 56 directed distinct-mode routes not proven, nor every transient support state |

## What the profiles mean, and counterexamples

The profile names deliberately refine [D1](d1-engineering-study.md),
[D2](d2-engineering-study.md) and [D3](d3-engineering-study.md); they do not rename
requirements. They distinguish a repair from the restricted proposal it repairs.

| Profile | Why its classifications differ / counterexample | What could change the finding |
| --- | --- | --- |
| A0 | Four strict local machines can run S; no one nozzle traverses a joined region. X in every other mode | Extend actual travel and remove inner supports: becomes A+, not an A0 pass |
| A+bridge | D2 independent moving bridges have reach-only matches but overlap tall neighboring objects; all U | Whole-structure routes and full independent height range, not simply higher nozzle parks |
| A+cant / B3 | Independent serial stages can describe eight XY coordinates; no specified physical sweep or stiffness establishes them. D only | Exact envelope/loads, guide roots, fully retractable parks; shared static frame still transmits disturbances |
| B0 | B0 is explicitly four X carriages on ONE translating Y member: all active heads share one Y coordinate, excluding every multi-job mode. One J head remains U; changing printing Z cannot add missing Y | Two independently translated beams with two carriages each can express two R jobs at the coordinate level, but not four arbitrary S jobs; assess their ordering/parking separately under B1/B2. Four independently moving stages produce B1/B2/B3, not B0 |
| B1 | Full-width nonpassing bridges enforce Y order. R has separated Y lanes conditionally; S, C and every mixed mode contain independently moving jobs with overlapping Y ranges, so X. J has one active bridge: U pending whole-bridge end parking and route proof, not excluded by concurrency | Bypass/stack/automatic layout change explicitly creates a new variant. Endpoint reach is not independence |
| B2 | High fixed bridge levels avoid some beam crossings but descending columns pass lower bridge planes; D2 found conflicts. All U | Concrete column route, aperture or bypass with clearance over entire paths; no assumption that Z-E removes columns |
| C0 | Four strict locals plus one H5 supply at most ONE concurrent pair path; R/C X. Mixed and J U due to fifth beam/local structures | Pair-capable locals make C+; a fifth tool on the same active gantry is not a fifth independent machine |
| C+ | Extension from D2; ownership plausible but actual geometry missing: D | Both orthogonal pair assignments and fifth/local Z ownership, with no unsupported sharing |
| D0 / D+ | One active toolchanger D0 fails all concurrent modes; J U. D+ may reconfigure independent stages but has no supported transformation mechanism: U throughout | Retained joints/locks, calibration, unaffected-job isolation and full transformation paths |
| E-only / E overlay | E-only has no XY topology: U unless Z already excludes the mode. Every A–D profile with E retains its topology status plus G3 | D2's body-only 42 mm inward gain also increases outward envelope by 42 mm; actual probe/cable/duct routes may erase benefit |
| Z-A | Independent full-stroke head/gantry Z conditionally supplies each job's height; stationary bed supports still need positive restraint | Full relative stroke/clearance and gantry fall retention; a shared-Z XY structure needs independent slides or changes variant |
| Z-B-raw | Independent bed lifts support S conditionally; group plane/drive/support behavior unspecified: U for seams | Adding measured group synchronization produces E-sync; equal step commands alone do not |
| Z-C0 / C-group | C0 retains S lifts but locks partial-mode beds under one gantry: R/C/M X. C-group keeps E-like partial lifts and locks J beds to rated stationary supports | Conditional C-group corrects the overly broad initial D1 exclusion. Both mechanisms, unused-drive isolation and handoff must exist |
| Z-D-trim | For unrestricted job histories beyond usable trim, S/R/C/M X; one J height conditional | D1 interval intersection: ±10 mm trim cannot absorb 21 mm job divergence. This is not a proposed machine limit; long full-range slides approach Z-A. A restricted-height experiment remains possible, not full requirement coverage |
| Z-E-sync / drive | E-sync retains independent local supports and measures group surfaces; E-drive phases lift inputs, retains local guides/restraints and releases unused drive torque | Actual downstream displacement/tilt, lead mismatch, stop skew and retention evidence; torque linkage is not gravity support |
| Z-E-tie / hybrid | E-tie specifies compatible released freedoms and force sharing; hybrid adds monitored followers. Conditional, not a four-guide rigid-loop endorsement | The unrelieved rigid-link version is rejected by D3/D4; a stronger tie may increase binding and contact uplift |
| Z-F0 reroute / clutch | S independent lifts and J platform, without partial grouped lifts: R/C/M X. Rerouting J U; positive selector J conditional with independent support | Adding E-like partial lifts changes to F-group. A clutch is neither a brake nor load-support proof |
| Z-F-group reroute / clutch | Partial modes retain E-sync lifts and isolated, independently retained secondary frame. J differs by transmission uncertainty | Both need rated load transfer and release/compatibility of local guides; disconnecting motor torque does not disconnect a guide |
| Z-F-attached / row / section | Attached frame: only one height; permanent row sections: only R/J. Four selectable sections U: section count does not establish support | Splitting/reconnecting sections with continuously retained support creates a specified alternative; no implicit vertical landing allowed |

K is used only for an explicitly stated conditional functional contract. U is retained
where the documented geometry already has unresolved interference or mechanism gaps;
D marks an independent-axis proposal with no such resolved geometry. The conjunction
is intentionally conservative, but cannot detect every new XY/Z interaction. For
example, replacing A+bridge's moving Z with bed Z changes the structural arrangement;
its U remains U until that new arrangement has a concrete study. No cell borrows a
clearance result from a mechanically different variant.

## Shared resource and support interpretation

For Z-A, job group g owns head Z(g); beds retain individual stationary load paths Li.
For E-sync each bed keeps its guided Li and independent downstream restraint, while
one group trajectory Dg commands its member lifts. E-drive changes T, not Li.
E-tie/hybrid add only specified cold Lij ties (12/34 for R, 13/24 for C, the one
pair edge for each M); incompatible guide freedoms must be released. J may use a
three-edge **torque** tree 12,13,34; this does not prescribe its load-support graph.
F-group uses that same partial-mode contract; only empty J transfers all four to a
separately restrained platform. C-group instead transfers J to stationary rated
supports. The original [D3 P/L/T table](d3-mode-constraints.md) governs details.

[D6's channel inventory](d6-electrical.md) remains conditional: four-head Cartesian
examples use 8 XY + 4 extruder + 4–12 printing-Z drivers, before transport, locks,
brakes and selectors. C variants have a fifth head and must add its actual axes,
extruder, heater, fan and observation channels; do not reuse the four-head subtotal.
F retains partial-mode lifts and adds platform channels. No board/firmware capacity
is established. Job counts 4/2/3/1 are not physical driver counts.

Whole-job reservations must include shared moving members and structural influence,
not merely bed numbers. A queue may defer an unsafe reconfiguration until affected
beds are empty; it may not serialize all printing and call it four independent jobs.
A completed/cancelled object remains occupied until confirmed removed. Surface heating
and frame elasticity can couple jobs even where the ownership graph is disjoint.
