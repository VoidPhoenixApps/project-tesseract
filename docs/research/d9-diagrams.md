# D9 — editable load-path and handoff diagrams

[Contract](d9-contract.md) · [faults](d9-faults.md).
Conceptual Mermaid/text source; no dimensions, component selection or CAD geometry.
Arrows identify functions, not proven contact capacity or physical independence.
X east, Y north, Z up; beds 1 NW, 2 NE, 3 SW, 4 SE.

## H: stationary bed, full-range head Z

```mermaid
flowchart TD
    HEAD[Head plus moving Z column, active or parked] -->|L axial support and guide moments| ARM[XY arm and root]
    ARM -->|L| FRAME[Primary frame and foundation]
    HEAD -->|R bypasses failed transmission| CATCH[Load-side retention and anchor]
    CATCH -->|R load and moment| FRAME
    MOTOR[Head Z motor] -->|T via transmission| HEAD
    HEAD -.->|O actual downstream pose and tilt| OBS[Observation and fault response]
    BED[Hot bed and retained sheet] -->|L through relieved mounts| CARRIER[Cold carrier]
    CARRIER -->|L and R| STATION[Supported horizontal transport and stationary dock]
    STATION --> FRAME
    STATION -.->|P cold datum| CARRIER
    BED -.->|O surface and seam| OBS
```

R is separate from the broken T element, but the drawing does not establish anchor
independence: a shared printed root or foundation fault can defeat both arrows.
Horizontal bed conversion remains at z=0 with continuous transport support. H parks
still carry complete head/column mass, cable force and catching moments.

## B: E-sync and separately optional hybrid / transmission tie

```mermaid
flowchart TD
    B1[Bed 1 sheet and cold carrier] -->|L| U1[Axial support plus guide 1]
    B2[Bed 2 sheet and cold carrier] -->|L| U2[Axial support plus guide 2]
    U1 --> FRAME[Primary frame and foundation]
    U2 --> FRAME
    B1 -->|R| R1[Load-side restraint 1]
    B2 -->|R| R2[Load-side restraint 2]
    R1 --> FRAME
    R2 --> FRAME
    G[One group trajectory, not a physical shaft] -.-> T1[Drive 1]
    G -.-> T2[Drive 2]
    T1 -->|T| U1
    T2 -->|T| U2
    B1 -.->|O pose and seam| O[Downstream observation]
    B2 -.->|O pose and seam| O
    B1 <-.->|Optional L tie only with compatible released freedoms| B2
    T1 <-.->|Optional T-link, no L credit| T2
```

P locates each carrier in its moving assembly, or uses a separately analyzed released
follower datum. The dashed optional edges are alternatives, not simultaneous mandatory
parts of E-sync. Fixed-Z heads still return their weight/moments through drop structures
and arms to the frame. Other beds/heads/platforms are omitted for legibility only;
the inventory in the contract retains them.

## Eight group graphs

Each bracket is an independent height owner, not one physical lift. Every bed has L/R
irrespective of whether it is connected to another bed for P, T or optional L.

```text
S     [1] [2] [3] [4]        R     [1--2] [3--4]
C     [1--3] [2--4]          M12   [1--2] [3] [4]
M34   [3--4] [1] [2]         M13   [1--3] [2] [4]
M24   [2--4] [1] [3]         J     [1--2, 1--3, 3--4]
```

J's displayed spanning tree describes scalar equality or a possible T tree only.
It does not establish a statically determinate six-DOF support structure. H realizes
these job coordinates in head lifts; B realizes them in descending bed groups.

## Optional F-group J support transfer and fault logic

```mermaid
flowchart LR
    A[Old local L and R retained] --> B[Empty affected beds at common datum]
    B --> C[Horizontal P seating and new L capture]
    C --> D[Compatible overlap; receiving load accepted; O fresh]
    D --> E[Release old ownership; receiving L and R retained]
    E --> F[Verify full T and plane before print eligibility]
    C -->|Unknown or partial engagement| HOLD[Retain available supports; inhibit release]
    D -->|Binding, uplift or stale O| HOLD
    E -->|Fault| STOP[Contain gravity and hazardous energy; latch recovery]
    STOP --> REVIEW[Deliberate supported recovery, no automatic restart]
```

Receiving path is bed → platform load locks → platform axial support/guide → frame,
with independent platform R. A platform detached in partial modes remains retained
clear of every bed stroke. C-group instead receives onto stationary J supports and
adds head/gantry Z. Neither arrangement has a designed handoff. An overlap that
requires forced vertical bed motion is a rejection, not a completed transfer.
