# D4 — editable conceptual structural diagrams

Original Markdown/text source, **not to scale, CAD, fabrication geometry or proven
clearance**. P=position, L=load support, T=torque. X east, Y north, Z up. View-dependent
arrows are labeled; a drawn line is not an adopted component.

## Top view: structural perimeter and moving regions

```text
                         Y north
                            ↑
       permanent rear triangulated return bay (candidate)
       o================================================o
       |  park/root envelope       park/root envelope   |
       |       [ B1 / H1 ]   :   [ B2 / H2 ]             |
       |            :      P cross?     :               |
       |       [ B3 / H3 ]   :   [ B4 / H4 ]             |
       |   independent XY transport / docking sweeps    |
       o================================================o → X east
         front service corridor + hand panel removal

 : = conceptual seam/datum adjacency, NOT a structural tie
 o = frame node, NOT a chosen support/foot count
 Outer dimensions, bed separation, braces and parks unresolved.
 Rear/side/base returns must carry torsion with front panel absent.
```

## Side view: three alternative structural load paths

```text
A. printed space frame        B. reinforced deep truss     C/E. tube + brace
      load ↓                         load ↓                    load ↓
        o                              o                         o--- root
       /|\                        =====|===== metal chord       /|  ↘ head
      o-o-o                       /\/\/|/\/\ printed web      / |   ↓F
     /|/|/|                      ======|===== metal chord     o--o
    o-o-o-o                        supports ↓              base return
 axial members/nodes             separation h                 diagonal
 Out-of-plane ties needed        end-anchor slip unknown      compression or
 in ALL drawings.                no perfect bond assumed      paired tension
```

## Head root moment and segmentation

```text
 Z ↑          reach L (hypothetical calculation 300 mm)
   |    root o----------------------------------head
   |       ↶ M=F L                               ↓ F
   |      [node] ↶ θroot
   |        ||
   |   permanent braced tower → base → foundation
   +----------------------------------------------→ horizontal

 Tip motion = member bending + L θroot + other omitted compliance.
 Printed-web segments: [cell]--[cell]--[cell]--[cell]
 Continuous chord:     ===========================
 The sketch does not establish Ender fit or chord anchorage.
```

## Independent and optional hybrid support graphs

```text
L: H1 → B1 → U1 → F → foundation       H2 → B2 → U2 → F → foundation
       thermal-relieved mounts              thermal-relieved mounts

Optional hybrid L edge:             B1 ← specified force/moment tie → B2
Alternative P edge:                B1 ← released-follower locator → B2
Optional T edge:           actuator1 → selected transmission → lift2 input

These are THREE different interfaces. No edge deletes independent restraint.
Full eight-mode edge lists and generated records are in d4-load-paths.md.
```

## Pair spring model and thermal incompatibility

```text
 Down positive; fixed frame reference 0
       | k1                    | k2, rest offset e
       v                       v
       o u1 ------- kc ------- o u2
       ↓ F1                    ↓ F2

 kc reduces differential sag but transmits mismatch forces.
 k2=0 is support-path loss. kc=0 as well leaves u2 unsupported.
 No roll/pitch/lateral stability is represented by this scalar sketch.
```

## Enclosure interface separation

```text
 permanent structural node === permanent brace === structural node
              |
       accessory boss → floating panel support + hand retainer → panel
              |
       fixed electrical protection and cable strain relief remain

 Panel removed: all primary braces, rails, supports and restraints remain.
 Hand/panel sweep and safe service access are additional reserved volumes.
```

See [eight-mode constraints](d4-load-paths.md), [enclosure assessment](d4-enclosure.md)
and [calculations](d4-calculations.md). These editable schematics deliberately avoid
inventing purchased-part dimensions or a full-machine envelope.
