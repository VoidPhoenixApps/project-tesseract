"""Phase 1B analytical screening. Python standard library; no hardware access.

Run from any directory. --write regenerates results.md beside this file.
Models ideal uniform expansion, linear contact constraints and rectangular sweeps.
These are neither engineering acceptance tests nor an assembled collision model.
"""

import argparse
from itertools import combinations, product
from math import hypot
from pathlib import Path

ALPHA = 23.6e-6
B = 180.0
SIGNS = {"A": (-1, 1), "B": (1, 1), "C": (-1, -1), "D": (1, -1)}
TEMPS = (20, 40, 60, 80, 100)


def anchor(signs, strategy, inset=10.0):
    sx, sy = signs
    if strategy == "center":
        return 0.0, 0.0
    if strategy == "x-edge":
        return -sx * B / 2, 0.0
    if strategy == "y-edge":
        return 0.0, -sy * B / 2
    if strategy in ("corner", "inset"):
        h = 0.0 if strategy == "corner" else inset
        if not 0 <= h <= B / 2:
            raise ValueError("inset must lie between edge and center")
        return -sx * (B / 2 - h), -sy * (B / 2 - h)
    raise ValueError("unknown anchor strategy")


def point(center, local, anch, temp, alpha=ALPHA, frame_shift=(0.0, 0.0)):
    return tuple(c + u + f + alpha * (temp - 20) * (u - a)
                 for c, u, a, f in zip(center, local, anch, frame_shift))


def gap(t1, t2, strategy="center", axis=0, cold=0.2, inset=10.0):
    """t1 = negative-axis plate, t2 = positive-axis plate; fixed cold frame."""
    if axis not in (0, 1):
        raise ValueError("axis must be X=0 or Y=1")
    q = (B + cold) / 2
    signs1, signs2 = ((-1, 1), (1, 1)) if axis == 0 else ((-1, -1), (-1, 1))
    c1, c2 = [0.0, 0.0], [0.0, 0.0]
    u1, u2 = [0.0, 0.0], [0.0, 0.0]
    c1[axis], c2[axis] = -q, q
    u1[axis], u2[axis] = B / 2, -B / 2
    p1 = point(c1, u1, anchor(signs1, strategy, inset), t1)
    p2 = point(c2, u2, anchor(signs2, strategy, inset), t2)
    return p2[axis] - p1[axis]


def cold_interval(strategy, temperatures=TEMPS, error=0.0, inset=10.0):
    if error < 0:
        raise ValueError("error bound must be nonnegative")
    closures = [-gap(t1, t2, strategy, cold=0, inset=inset)
                for t1, t2 in product(temperatures, repeat=2)]
    return 0.1 + max(closures) + error, 0.3 + min(closures) - error


def rank(rows, tol=1e-10):
    a = [list(map(float, row)) for row in rows]
    r = 0
    for col in range(len(a[0])):
        pivot = max(range(r, len(a)), key=lambda i: abs(a[i][col]), default=None)
        if pivot is None or abs(a[pivot][col]) <= tol:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][col]
        a[r] = [v / scale for v in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


VERTICAL = [[0, 0, 1, -60, 60, 0], [0, 0, 1, -60, -60, 0],
            [0, 0, 1, 60, 0, 0]]
PLANAR = [[1, 0, 0, 0, 0, -60], [1, 0, 0, 0, 0, 60], [0, 1, 0, 0, 0, 0]]
YAW = [0, 0, 0, 0, 0, 1]


def modes(cold=0.2, separated=130.0):
    q = (B + cold) / 2
    if cold < 0 or separated < q:
        raise ValueError("cold geometry requires nonnegative gap and outward parking")
    # Joined X rows and joined Y columns; all mirrored mixed modes explicit.
    selections = {"I": ((), ()), "H": ((1, -1), ()), "V": ((), (-1, 1)),
                  "MH-top": ((1,), ()), "MH-bottom": ((-1,), ()),
                  "MV-left": ((), (-1,)), "MV-right": ((), (1,)),
                  "J": ((1, -1), (-1, 1))}
    return {name: {bed: (sx * (q if sy in rows else separated),
                         sy * (q if sx in cols else separated))
                   for bed, (sx, sy) in SIGNS.items()}
            for name, (rows, cols) in selections.items()}


def box(center, width):
    return (center[0] - width / 2, center[0] + width / 2,
            center[1] - width / 2, center[1] + width / 2)


def sweep(start, end, width):
    if start[0] != end[0] and start[1] != end[1]:
        raise ValueError("only single-axis segments are certified")
    a, b = box(start, width), box(end, width)
    return min(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), max(a[3], b[3])


def separate(a, b, clearance=0.0):
    # Boundary contact at specified clearance is allowed by this box model.
    return (a[1] + clearance <= b[0] + 1e-9 or b[1] + clearance <= a[0] + 1e-9
            or a[3] + clearance <= b[2] + 1e-9 or b[3] + clearance <= a[2] + 1e-9)


def transition(start, target, width=160.0, clearance=10.0, occupied=()):
    if any(start[b] != target[b] for b in occupied):
        return False
    current = dict(start)
    if any(not separate(box(current[a], width), box(current[b], width), clearance)
           for a, b in combinations(current, 2)):
        return False
    for bed in current:
        for axis in (0, 1):
            end = list(current[bed])
            end[axis] = target[bed][axis]
            swept = sweep(current[bed], end, width)
            if any(not separate(swept, box(pos, width), clearance)
                   for other, pos in current.items() if other != bed):
                return False
            current[bed] = tuple(end)
    return True


def central_corners(temperatures, strategy="inset", cold=0.2, inset=10.0):
    q = (B + cold) / 2
    return {bed: point((sx * q, sy * q), (-sx * 90, -sy * 90),
                        anchor((sx, sy), strategy, inset), temperatures[bed])
            for bed, (sx, sy) in SIGNS.items()}


def report():
    lines = ["# Generated Phase 1B screening results", "",
             "Generated by `python docs/phase1b/analysis.py --write`. Units: mm, N, K, MPa as labeled.",
             "Analytical assumptions only; no physical validation. See [thermal](thermal.md) and [packaging](packaging.md).", "",
             "## Gap at g0=0.20; stationary frame", "",
             "| T1/T2 °C | Center X/Y | X-edge X | X-edge Y | Corner X/Y | Inset 10 X/Y |",
             "| --- | --- | --- | --- | --- | --- |"]
    for t1, t2 in product(TEMPS, repeat=2):
        values = [gap(t1, t2), gap(t1, t2, "x-edge"), gap(t1, t2, "x-edge", axis=1),
                  gap(t1, t2, "corner"), gap(t1, t2, "inset")]
        lines.append(f"| {t1}/{t2} | " + " | ".join(f"{v:.5f}" for v in values) + " |")
    lines += ["", "## Cold-gap intersection for proposed 0.10–0.30 window", "",
              "| Anchor / range | e | Lower | Upper | Intersection exists? |", "| --- | --- | --- | --- | --- |"]
    for strategy, temps, e in [("center", TEMPS, 0), ("center", (60, 80), 0),
                                ("inset", TEMPS, 0), ("inset", TEMPS, 0.03)]:
        lo, hi = cold_interval(strategy, temps, e)
        lines.append(f"| {strategy} / {min(temps)}–{max(temps)} °C | {e:.2f} | {lo:.5f} | {hi:.5f} | {lo <= hi} |")
    lines += ["", "## Inset and height sensitivity", "", "| Inset h | Closure at 100/100 °C |", "| --- | --- |"]
    for h in (0, 5, 10, 20, 90):
        lines.append(f"| {h} | {-gap(100, 100, 'inset', cold=0, inset=h):.5f} |")
    lines += ["", "| Thickness | Strip bow at 1 K | Strip bow at 5 K |", "| --- | --- | --- |"]
    for t in (3, 4, 6):
        w = ALPHA / t * B * B / 8
        lines.append(f"| {t} | {w:.6f} | {5*w:.6f} |")
    lines += ["", f"Radial travel, anchor (80,-80) to (-60,-60), +80 K: {ALPHA*hypot(140,20)*80:.6f} mm.",
              f"Fully restrained uniaxial stress +80 K: {68300*ALPHA*80:.5f} MPa; 180×4 section force {68300*ALPHA*80*720:.2f} N.",
              f"Steel-frame pitch example +20 K: {12e-6*180.2*20:.6f} mm; Al/steel sheet free mismatch +80 K: {(ALPHA-12e-6)*180*80:.5f} mm.",
              "", "## Four-bed corner geometry", "", "A/B/C/D temperatures = 100/80/40/20 °C; inset 10 mm.",
              "", "| Bed | Inner corner X | Inner corner Y |", "| --- | --- | --- |"]
    corners = central_corners(dict(zip(SIGNS, (100, 80, 40, 20))))
    for bed, (x, y) in corners.items():
        lines.append(f"| {bed} | {x:.5f} | {y:.5f} |")
    for label, first, second, axis in (("AB", "A", "B", 0), ("CD", "C", "D", 0),
                                        ("AC", "C", "A", 1), ("BD", "D", "B", 1)):
        lines.append(f"\n{label} normal gap: {corners[second][axis]-corners[first][axis]:.5f} mm.")
    states = modes()
    lines += ["", "## Constraint and box model", "",
              f"B floating rank: {rank(VERTICAL + PLANAR)} of 6 DOFs; plus guide yaw: {len(VERTICAL+PLANAR+[YAW])} equations, rank {rank(VERTICAL+PLANAR+[YAW])}.", "",
              "| Directed mode pairs (including no-op) | Clear | Total |", "| --- | --- | --- |"]
    for width, clear in ((180, 0), (160, 10), (190, 0)):
        results = [transition(a, b, width, clear) for a, b in product(states.values(), repeat=2)]
        lines.append(f"| width {width}, clearance {clear} | {sum(results)} | {len(results)} |")
    lines += ["", "190 mm carriers are a negative control, not a proposed fit.", "",
              "| Mode | A | B | C | D |", "| --- | --- | --- | --- | --- |"]
    for name, state in states.items():
        lines.append(f"| {name} | " + " | ".join(str(state[b]) for b in SIGNS) + " |")
    lines += ["", "| Block center separation | Minimum rail length |", "| --- | --- |"]
    for span in (50, 60, 70):
        lines.append(f"| {span} | {span+44.5+39.9+20:.1f} |")
    lines += ["", "Reservations exclude real stop fingers, motors, cable solids, float deformation, toolheads and objects.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = report()
    if args.write:
        Path(__file__).with_name("results.md").write_text(result, encoding="utf-8")
    else:
        print(result, end="")
