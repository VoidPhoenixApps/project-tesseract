# D6 — scheduling, geometry and conflict study

[State contract](d6-states.md) · [model](d6_model.py) · [tests](test_d6_model.py).
**Proposed operational software only; not an independent protective controller.**

## Admission and scheduling alternatives

| Approach | Benefit | Cost / limitation |
| --- | --- | --- |
| Fixed regions, one ordinary queue each | Simplest independent progress; conservative ownership | Does not express dynamic pairs/J without a separate reconfiguration mechanism and planner |
| Whole-job resource and swept-volume reservation | Independence without exact cross-job timing; atomic allocation avoids resource hold-and-wait | Overconservative near shared corridors; full future toolpaths and parking envelopes needed |
| Time-window shared-space scheduling | Could admit paths whose envelopes overlap at different times | Clock/stop uncertainty, pause behavior, online replanning and lost communications become collision-critical; may serialize mandatory independent motion |
| Global layer barriers / lockstep | Simple synchronized demos | Reject as a baseline solution: unrelated heights, layers, speeds and completion must remain possible |

The D6 reference kernel uses whole-job reservation to expose feasibility conflicts.
It admits **supplied geometry**, not inferred nominal rectangles. A future preprocessing
stage must parse supported G-code dialects or equivalent toolpaths, resolve coordinate
modes/offsets, extrusion, arcs, transforms, meshes and start/end/pause macros, and bind
the result to an immutable hash. Unknown commands or post-admission edits invalidate the
certificate. Slicer thumbnails and a bounding box of model triangles alone are insufficient.

Represent the object (including brim, raft, support and expected growth) as a union of
conservative 3D volumes. Add nozzle, extruder, gantry, descending columns, belts, harnesses,
probe and park/approach/departure swept volumes, expanded by position/geometry/stop
uncertainty. Bed-side Z transforms the **entire attached object**; a head's reported Z
alone cannot locate it. Test in one declared machine frame at every relevant configuration.
The union-of-AABBs kernel treats contact as conflict and can distinguish separated Z
volumes; it is not a mesh intersection engine, dynamic sweep generator or proof that
those input volumes cover a real mechanism. Real geometry and uncertainty are missing.

## Resource rules and unresolved scheduling conflicts

Exclusive resources include a head, bed group, any shared XY member, printing-Z authority,
selector, structural/load-transfer domain, required park and transition corridor.
Thermal capacity and electrical budget are bounded shared resources; a physical heater
still has one setpoint owner. Ordinary communications bandwidth can be shared only within
a measured deadline budget. Structural/thermal influence can couple jobs even without
an obvious shared motor. Resource maps must come from D2–D5 mechanics, not UI bed labels.

| Conflict | Proposed handling | Model coverage |
| --- | --- | --- |
| Two jobs want the same bed/head/lift | Atomic all-or-nothing admission; retain existing reservation | Tested, including explicit shared-Z and shared-beam resources |
| A holds lift 1 waiting for 2; B holds 2 waiting for 1 | Acquire all resources atomically under one authority; never allocate incrementally | Counterexample tested; failed batch acquires nothing |
| Finished/cancelled object obstructs new work | Keep occupancy and conservative sweeps until confirmed safe removal | Tested; no automatic clearing on completion |
| New job needs occupied neighbor's homing sweep | Defer/reject; never home the whole machine from an individual start macro | Geometric rejection kernel only; homing path generation unimplemented |
| Paused job blocks urgent work | Preserve it; explicit cancellation/removal may eventually release resources | Pause/cancel and continued unrelated progress tested |
| Unreachable/occupied park | Reject; no guessed high-Z escape or nozzle-only parking | Missing/unreachable/colliding park and park-to-park tests |
| Shared frame/drive across otherwise separate beds | Same exclusive resource or invalidate independence; no schedule can create missing DOF | Shared-resource rejection tested; actual resource discovery absent |
| Stale/failed sensor, disconnect, lost position | Latch conservative machine-wide fault in model; retain occupancy | Tested during execution and admission |
| Power overrun | Reserve concurrent maximum, not mean heater duty; queue or use reviewed hard power allocation | Tested at and above budget; no real power control |
| Starvation of a pair/J by recurring singles | Age queued requests; reserve an eventual empty interval by withholding new conflicting starts after a declared drain point | Policy only, not implemented; occupied prints cannot be preemptively moved |
| Head-of-line blocking | Permit bounded bypass for disjoint jobs; log wait reason and age; avoid endless bypass of large groups | Queue policy only, not implemented |
| Barrier waits for failed stream | Abort barrier/inhibit influence domain with bounded response | Protocol requirement only, not implemented |

The kernel deliberately does not include a production queue dispatcher. Callers submit
candidate batches; admission failure is an explicit reason suitable for queueing.
No starvation-freedom, distributed deadlock-freedom, throughput or real-time guarantee is
claimed. Atomic allocation eliminates hold-and-wait **inside this single-threaded model**;
it does not solve an executor that holds an unreported resource or ambiguous commit.

## Reproduction and input contract

From repository root, Python 3.9+ with standard library only:

```sh
python3 -B docs/research/d6_model.py > /tmp/tesseract-d6-results.json
cmp docs/research/d6-results.json /tmp/tesseract-d6-results.json
python3 -B -m unittest discover -s docs/research -p 'test_d6_model.py' -v
```

No network, serial, GPIO, motion or heater commands exist in the model. Units: geometry
and progress mm, time seconds, load W, temperature °C. `speed` is hypothetical progress
rate, **not** nozzle feedrate or a thermal printing prediction. Different layer heights
and temperatures are metadata; heater PID, material compatibility and thermal evolution
are not simulated. Synthetic strips in the tests intentionally decouple logic from
unresolved machine geometry; passing eight-mode admission does not repair D2.

`Job.objects` and `Job.sweeps` are conservative entire-job volumes. `reach` is an assumed
allowed complete-assembly envelope, not bed size. `resources` must include every coupled
axis/support; the kernel automatically adds bed/head claims. `watts` includes the job's
worst concurrent allocation; the caller must subtract fixed machine load from total
capacity before setting `Model.budget`. The power arithmetic is a separate model.

`Evidence` is a single aggregate injected observation with a maximum age, not a sensor
subsystem. Its `guard_permitted` assertion concerns assessed protective access conditions,
not environmental-panel presence; an absent environmental panel alone does not invalidate
evidence. The [state contract](d6-states.md) separates environmental status, protective
access and maintenance isolation without selecting a guard, sensor or interlock. Every
advance rechecks it before progressing; a failed check latches fault and retains reservations. Time is discrete; this is not a continuous fault-latency
simulation. Parks must already be established; a late new job's supplied sweep must
include its departure and final parking route. The caller must establish real end-state
poses before removal/reassignment. Removal/access booleans are synthetic assertions,
not an access procedure or protection.

`transition` requires all old/new changed groups in its affected set and explicit
support/datum/route evidence. Additional affected beds from shared structures must be
supplied by the caller. It records one atomic symbolic change, not intermediate motion.
`reset` conservatively requires all modeled jobs cleared and fresh evidence plus human
acknowledgement. Retaining a print through recovery is an unresolved future extension;
there is no automatic resume path after a fault.
