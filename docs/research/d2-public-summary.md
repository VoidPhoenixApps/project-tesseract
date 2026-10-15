# Can four Tesseract heads reach every bed arrangement?

D2 investigated all eight arrangements: four singles, both two-pair directions, each
of the four pair-plus-singles placements, and one fully joined region. It compared
local gantries, extended gantries, shared rails, a fifth full-region head, reconfigurable
mechanisms, and the proposed mirrored A/B heads.

**We have not yet established a four-head layout that clears every required motion.**
A nozzle can reach a point while its bridge hits another print. Stacking bridges can
avoid one collision while leaving a descending head column in another bridge's way.
Parking must make room for the entire machine, cables and filament, not just its nozzle.

Some simpler arrangements fail clear requirements. Four quadrant-only heads cannot
print across the seams. Adding one full-region fifth head still cannot run two separate
paired jobs at once. Two independently driven X carriages on one Y beam are not two
fully independent XY printers. A conventional toolchanger supplies one active path.

The mirrored A/B idea remains worth investigating. With the same hypothetical body
sizes, it reduces the space needed between inward-facing heads. The tradeoff is more
space needed toward the outer frame and parking bays. We have not verified that two
complete assembly types can provide all the required mounting, cooling, probe, cable,
filament and service arrangements.

The package includes reproducible Python geometry checks, continuous collision tests,
parameter sweeps, editable conceptual drawings and a manufacturer-reference/missing-model
catalog. All non-required machine dimensions are labeled assumptions. Software checks
are **not physical validation**, and no purchased part or architecture was selected.

Next, compare perimeter cantilevers, bridges with explicitly routed head columns, and
automatic workspace reconfiguration using complete envelopes and qualified engineering
review. The first physical proof remains two-bed docking and seam printing. Four sheets,
all required modes and the printable-first approach remain intact.

See the [engineering report](d2-engineering-study.md) and [verification record](d2-verification.md).
Contribute exact source-backed component geometry or challenge a specific assumption in
[GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions).
D2 builds on [Draft PR #25](https://github.com/VoidPhoenixApps/project-tesseract/pull/25);
it does not approve D1 or bypass its unresolved findings.
