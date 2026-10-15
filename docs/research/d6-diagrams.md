# D6 — editable conceptual control diagrams

Original Mermaid source, controller-independent, **not wiring, implemented architecture,
physical clearance or a validated protective system**. Arrows are information/authority
relationships, not selected buses. [Study](d6-engineering-study.md).

## A — centralized execution

```mermaid
flowchart TD
  Input[Independent job inputs and geometry] --> Admission[Admission and resource ownership]
  Admission --> Central[Central multi-queue planner - four lifecycles unproven]
  Central --> IO[Local or expansion motion and thermal IO]
  IO --> Plant[Heads - beds - locks - restraints]
  Plant --> Sense[Position - support - thermal observations]
  Sense --> Admission
  Protection[Independent protective functions - design unresolved] --> Energy[Hazardous energy and load retention]
  Plant --> Protection
```

## B and C — distributed execution, different coordination scope

```mermaid
flowchart TD
  Jobs[Jobs and toolpath geometry] --> Supervisor[Supervisor]
  Supervisor --> B[B: fixed region dispatch and status]
  Supervisor --> C[C: configuration epochs and atomic reservations]
  B --> Executors[Independent motion executors 1 through 4]
  C --> Executors
  Executors --> Regions[Owned head and bed resources]
  Regions --> Feedback[Fresh observed state and executed-sequence replies]
  Feedback --> Supervisor
  Group[Connected Z group - one deterministic motion authority required] --> Regions
  Protect[Separate protective-function design] --> Energy[Heat interruption and gravity-safe motion response]
  Regions --> Protect
```

An executor is not necessarily one board. A connected Z group cannot receive unrelated
trajectories from several owners; changing ownership requires empty affected beds,
retained support and a new verified configuration. Neither USB nor CAN implies a safety
bus. Separate processors can still share a failing host, power supply, ground or sensor.

## Proposed grouping sequence and fault latch

```mermaid
stateDiagram-v2
  [*] --> Inhibited
  Inhibited --> Ready: fresh evidence and explicit enable
  Ready --> Reserved: atomic admission
  Reserved --> Printing: executor acknowledgement
  Printing --> Paused: controlled stop within reservation
  Paused --> Printing: recheck and explicit resume
  Printing --> Occupied: completed or cancelled
  Occupied --> Ready: safe removal and readiness evidence
  Ready --> DatumSupported: affected beds empty and route reserved
  DatumSupported --> HorizontalConversion: support and common datum confirmed
  HorizontalConversion --> LockCheck: position reached
  LockCheck --> Ready: observed support and new epoch committed
  Printing --> FaultLatched: unknown state or protective event
  Paused --> FaultLatched: evidence lost
  HorizontalConversion --> FaultLatched: any handoff failure
  LockCheck --> FaultLatched: disagreement
  FaultLatched --> Inhibited: cause corrected and deliberate reset
```

Fault transitions apply to every operational state even where omitted for readability.
No automatic fault-to-print arrow exists. This diagram describes the future contract;
the Python kernel collapses conversion into one abstract atomic transition.

## Independent job ownership and physical coupling

```mermaid
flowchart LR
  J12[Job pair 12] --> H1[One pair-capable head]
  J12 --> Z12[One group-Z trajectory]
  Z12 --> B1[Bed 1 support and restraint]
  Z12 --> B2[Bed 2 support and restraint]
  J3[Independent job 3] --> H3[Head 3]
  J3 --> Z3[Independent Z 3]
  J4[Independent job 4] --> H4[Head 4]
  J4 --> Z4[Independent Z 4]
  Park[Head 2 and entire assembly parked] --> Check[Complete 3D clearance required]
  B1 --> Shared[Shared frame and power still require influence analysis]
  B2 --> Shared
  Z3 --> Shared
  Z4 --> Shared
```

The example is M12 only. Reflecting it does not validate M34/M13/M24 geometry. A common
frame may transmit disturbances even though the resource graph has no shared actuator.
