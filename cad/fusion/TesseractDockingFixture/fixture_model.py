"""Cold fixture specification in mm. Pure Python; no CAD kernel or hardware claims."""

import ast
from dataclasses import dataclass
import math
import operator


# name: (default, lower, upper, purpose); bounds define this concept's supported domain.
PARAMETERS = {
    "bed": (180, 180, 180, "Nominal retained surface envelope side"),
    "gap": (0.5, 0.2, 2, "Cold illustrative sheet gap, not thermal acceptance"),
    "carrier": (160, 156, 164, "Cold carrier side"),
    "stroke": (40, 20, 50, "Positive X transport release"),
    "release_y": (8, 6, 10, "Positive Y unseat before X release"),
    "travel_x": (0, 0, 50, "Displayed X pose; <= stroke"),
    "travel_y": (0, 0, 10, "Displayed Y pose; <= release_y"),
    "pad_baseline": (120, 100, 130, "B X-contact Y separation"),
    "float_xy": (0.5, 0.2, 0.8, "B required planar translation allowance each way"),
    "float_yaw_deg": (0.2, 0.05, 0.3, "B required yaw allowance, degrees"),
    "guard_gap": (1.5, 1, 2, "B carrier-to-guard gap at neutral"),
    "support_span": (100, 90, 110, "Three support-pad triangle span"),
    "anchor_inset": (16, 14, 20, "Inward-corner thermal reservation inset"),
    "mount_pitch": (100, 90, 110, "Shared four-point cartridge mount pattern"),
    "mount_bore": (5, 4, 6, "Illustrative through bore, no fastener selected"),
    "print_xy": (200, 180, 220, "Conservative candidate print budget, verify printer"),
    "print_z": (180, 100, 250, "Candidate print height budget, verify printer"),
}

# Derived expressions are shared verbatim with Fusion (explicit mm constants).
DERIVED = {
    "fixed_x": "100 mm", "center_y": "120 mm",
    "dock_x": "fixed_x+bed+gap", "moving_x": "dock_x+travel_x",
    "moving_y": "center_y+travel_y",
    "left": "dock_x-carrier/2", "bottom": "center_y-carrier/2",
    "base_length": "dock_x+carrier/2+stroke+30 mm",
    "base_width": "240 mm", "cartridge_side": "carrier+12 mm",
}


def evaluate(expression, values):
    """Restricted arithmetic, never eval arbitrary text. Numbers represent mm here."""
    operations = {ast.Add: operator.add, ast.Sub: operator.sub,
                  ast.Mult: operator.mul, ast.Div: operator.truediv}

    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.Name):
            return values[node.id]
        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](visit(node.left), visit(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -visit(node.operand)
        raise ValueError("Unsupported expression: " + expression)
    return visit(ast.parse(expression.replace(" mm", ""), mode="eval").body)


def parameters(overrides=None):
    values = {key: row[0] for key, row in PARAMETERS.items()}
    for key, value in (overrides or {}).items():
        if key not in PARAMETERS:
            raise ValueError("Unknown input parameter: " + key)
        values[key] = value
    for key, (_, low, high, _) in PARAMETERS.items():
        value = values[key]
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError(f"{key}={value!r} must be finite and within [{low}, {high}]")
        # A cm/mm roundtrip can land one representable float outside a limit:
        # (164 * 0.1) * 10 == 164.00000000000003. Admit only that adjacent
        # representation, then normalize before derived/geometry checks. This
        # is not a dimensional tolerance. Keep zero and all in-range values exact.
        if value < low and low != 0 and value == math.nextafter(float(low), -math.inf):
            values[key] = low
        elif value > high and high != 0 and value == math.nextafter(float(high), math.inf):
            values[key] = high
        elif not low <= value <= high:
            raise ValueError(f"{key}={value!r} must be finite and within [{low}, {high}]")
    if values["travel_x"] > values["stroke"] or values["travel_y"] > values["release_y"]:
        raise ValueError("Displayed pose exceeds the transport range")
    if values["travel_x"] > 0 and values["travel_y"] < values["release_y"]:
        raise ValueError("Release Y fully before moving X; reverse this sequence to dock")
    radius = values["carrier"] / math.sqrt(2)
    yaw_sweep = 2 * radius * math.sin(math.radians(values["float_yaw_deg"]) / 2)
    if values["guard_gap"] <= values["float_xy"] + yaw_sweep:
        raise ValueError("Float guards intrude into translation + yaw capture allowance")
    if values["pad_baseline"] + 12 >= values["carrier"]:
        raise ValueError("X pads must fit on the carrier with edge reserve")
    for key, expression in DERIVED.items():
        values[key] = evaluate(expression, values)
    return values


@dataclass(frozen=True)
class Part:
    name: str
    # Lower corner and positive dimensions; all expressions evaluate to mm.
    xyz: tuple
    size: tuple
    motion: str = "fixed"  # fixed, x (lower stage), xy (upper stage)
    role: str = "solid"  # solid, reservation (hidden, excluded from interference)
    printable: bool = False
    bores: tuple = ()  # (global x expression, global y expression, diameter expression)

    def bounds(self, values):
        lo = tuple(evaluate(e, values) for e in self.xyz)
        size = tuple(evaluate(e, values) for e in self.size)
        return lo, tuple(a + b for a, b in zip(lo, size))


def parts(cartridge="B", anchor="inset"):
    if cartridge not in ("A", "B") or anchor not in ("center", "inset"):
        raise ValueError("Choose cartridge A/B and anchor center/inset")
    result = []

    def box(name, xyz, size, motion="fixed", role="solid", printable=False, bores=()):
        result.append(Part(name, tuple(xyz), tuple(size), motion, role, printable, tuple(bores)))

    box("Laboratory_base_ENVELOPE", ("0 mm", "0 mm", "-68 mm"),
        ("base_length", "base_width", "8 mm"))
    for label, cx, cy, motion in (("Fixed", "fixed_x", "center_y", "fixed"),
                                  ("Moving", "moving_x", "moving_y", "xy")):
        box(label + "_retained_sheet_ENVELOPE", (cx+"-bed/2", cy+"-bed/2", "-1 mm"),
            ("bed", "bed", "1 mm"), motion)
        box(label + "_plate_ENVELOPE", (cx+"-bed/2", cy+"-bed/2", "-4 mm"),
            ("bed", "bed", "3 mm"), motion)
        box(label + "_cold_carrier", (cx+"-carrier/2", cy+"-carrier/2", "-24 mm"),
            ("carrier", "carrier", "6 mm"), motion, printable=True)
        # Noncollinear Z supports are separate from planar plate-anchor reservations.
        for i, (u, v) in enumerate((("-support_span/2", "-support_span/2"),
                                    ("+support_span/2", "-support_span/2"),
                                    ("+0 mm", "+support_span/2"))):
            box(f"{label}_plate_Z_support_{i+1}", (cx+u+"-5 mm", cy+v+"-5 mm", "-18 mm"),
                ("10 mm", "10 mm", "14 mm"), motion, printable=True)
        inward = "+bed/2-anchor_inset" if label == "Fixed" else "-bed/2+anchor_inset"
        ax = cx if anchor == "center" else cx+inward
        ay = cy if anchor == "center" else cy+"-bed/2+anchor_inset"
        box(label+"_"+anchor+"_XY_anchor_RESERVED", (ax+"-5 mm", ay+"-5 mm", "-18 mm"),
            ("10 mm", "10 mm", "14 mm"), motion, "reservation")
        # Radial relief axis is +Y from chosen anchor; no actual slot/fastener claim.
        box(label+"_radial_secondary_RESERVED", (ax+"-5 mm", ay+"+30 mm", "-18 mm"),
            ("10 mm", "20 mm", "14 mm"), motion, "reservation")
        # Exposed below-edge targets separate carrier metrology from sheet metrology.
        for i, u in enumerate(("-50 mm", "+50 mm")):
            box(f"{label}_carrier_probe_target_{i+1}",
                (cx+u+"-4 mm", cy+"+carrier/2", "-24 mm"),
                ("8 mm", "8 mm", "6 mm"), motion, printable=True)

    for i, (u, v) in enumerate(((-50, -50), (50, -50), (0, 50))):
        box(f"Fixed_pedestal_{i+1}", (f"fixed_x+{u-10} mm", f"center_y+{v-10} mm", "-60 mm"),
            ("20 mm", "20 mm", "36 mm"), printable=True)
    # Idealized stacked guide envelopes, not catalog rails/bearings or joints.
    for i, offset in enumerate((-50, 50)):
        box(f"X_rail_{i+1}_ENVELOPE", ("left+20 mm", f"center_y+{offset-6} mm", "-60 mm"),
            ("carrier-40 mm+stroke", "12 mm", "10 mm"))
        for j, u in enumerate((-40, 40)):
            box(f"X_block_{i+1}_{j+1}_ENVELOPE",
                (f"moving_x+{u-10} mm", f"center_y+{offset-6} mm", "-50 mm"),
                ("20 mm", "12 mm", "6 mm"), "x")
    box("X_bridge", ("moving_x-carrier/2", "center_y-carrier/2", "-44 mm"),
        ("carrier", "carrier", "4 mm"), "x", printable=True)
    for i, u in enumerate((-50, 50)):
        box(f"Y_rail_{i+1}_ENVELOPE", (f"moving_x+{u-6} mm", "bottom+20 mm", "-40 mm"),
            ("12 mm", "carrier-40 mm+release_y", "4 mm"), "x")
        for j, v in enumerate((-40, 40)):
            box(f"Y_block_{i+1}_{j+1}_ENVELOPE",
                (f"moving_x+{u-6} mm", f"moving_y+{v-10} mm", "-36 mm"),
                ("12 mm", "20 mm", "4 mm"), "xy")
    bores = tuple(("moving_x"+sx+"mount_pitch/2", "moving_y"+sy+"mount_pitch/2", "mount_bore")
                  for sx in ("-", "+") for sy in ("-", "+"))
    box("Common_cartridge_mount_plate", ("moving_x-cartridge_side/2", "moving_y-cartridge_side/2", "-32 mm"),
        ("cartridge_side", "cartridge_side", "4 mm"), "xy", printable=True, bores=bores)
    # Three bearing shoes below B allow ideal planar slip. A substitutes rigid keys.
    for i, (u, v) in enumerate((("-support_span/2", "-support_span/2"),
                                ("+support_span/2", "-support_span/2"),
                                ("+0 mm", "+support_span/2"))):
        box(f"{cartridge}_"+("rigid_key_" if cartridge == "A" else "sliding_Z_shoe_")+str(i+1),
            ("moving_x"+u+"-8 mm", "moving_y"+v+"-8 mm", "-28 mm"),
            ("16 mm", "16 mm", "4 mm"), "xy", printable=(cartridge == "A"))
    if cartridge == "B":
        for side, x, y, w, d in (
            ("left", "moving_x-carrier/2-guard_gap-3 mm", "moving_y-12 mm", "3 mm", "24 mm"),
            ("right", "moving_x+carrier/2+guard_gap", "moving_y-12 mm", "3 mm", "24 mm"),
            ("front", "moving_x+30 mm", "moving_y-carrier/2-guard_gap-3 mm", "24 mm", "3 mm"),
            ("rear", "moving_x-12 mm", "moving_y+carrier/2+guard_gap", "24 mm", "3 mm")):
            box("B_float_limit_"+side, (x, y, "-28 mm"), (w, d, "10 mm"), "xy", printable=True)
        box("B_weak_centering_and_hold_down_RESERVED", ("moving_x-30 mm", "moving_y-30 mm", "-28 mm"),
            ("60 mm", "60 mm", "10 mm"), "xy", "reservation")

    ys = ("center_y",) if cartridge == "A" else ("center_y-pad_baseline/2", "center_y+pad_baseline/2")
    for i, y in enumerate(ys):
        box(f"{cartridge}_X_stop_tower_{i+1}", ("left-12 mm", y+"-6 mm", "-60 mm"),
            ("4 mm", "12 mm", "38 mm"), printable=True)
        box(f"{cartridge}_X_station_contact_{i+1}", ("left-12 mm", y+"-6 mm", "-22 mm"),
            ("8 mm", "12 mm", "4 mm"))
        box(f"{cartridge}_X_carrier_contact_{i+1}", ("moving_x-carrier/2-4 mm", y+"+travel_y-6 mm", "-22 mm"),
            ("4 mm", "12 mm", "4 mm"), "xy")
    box("Y_stop_tower", ("dock_x-6 mm", "bottom-12 mm", "-60 mm"),
        ("12 mm", "4 mm", "38 mm"), printable=True)
    box("Y_station_contact", ("dock_x-6 mm", "bottom-12 mm", "-22 mm"),
        ("12 mm", "8 mm", "4 mm"))
    box("Y_carrier_contact", ("moving_x-6 mm", "moving_y-carrier/2-4 mm", "-22 mm"),
        ("12 mm", "4 mm", "4 mm"), "xy")
    for label, xyz, size in (
        ("X_preload_minus_X", ("dock_x+carrier/2", "center_y-6 mm", "-22 mm"), ("20 mm", "12 mm", "4 mm")),
        ("Y_preload_minus_Y", ("dock_x-6 mm", "center_y+carrier/2", "-22 mm"), ("12 mm", "20 mm", "4 mm"))):
        box(label+"_RETRACT_BEFORE_RELEASE", xyz, size, role="reservation")
    for i, x in enumerate(("40 mm", "base_length-40 mm")):
        box(f"Reinforcement_interface_{i+1}_NO_STOCK_SELECTED", (x, "10 mm", "-60 mm"),
            ("25 mm", "20 mm", "12 mm"), role="reservation")
    return result


def overlap(a, b, tolerance=1e-8):
    return all(min(a[1][i], b[1][i]) - max(a[0][i], b[0][i]) > tolerance for i in range(3))


def validate_geometry(values, solids):
    names = [p.name for p in solids]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate component names")
    for part in solids:
        lo, hi = part.bounds(values)
        if any(not math.isfinite(v) for v in lo+hi) or any(a >= b for a, b in zip(lo, hi)):
            raise ValueError("Invalid box: " + part.name)
        if lo[0] < 0 or lo[1] < 0:
            raise ValueError("Sketch offsets must stay in the positive XY quadrant")
        if part.printable and (max(hi[0]-lo[0], hi[1]-lo[1]) > values["print_xy"]
                               or hi[2]-lo[2] > values["print_z"]):
            raise ValueError("Part exceeds candidate printable envelope: " + part.name)
        for x, y, diameter in part.bores:
            cx, cy, radius = evaluate(x, values), evaluate(y, values), evaluate(diameter, values)/2
            if not (lo[0] < cx-radius < cx+radius < hi[0] and lo[1] < cy-radius < cy+radius < hi[1]):
                raise ValueError("Bore outside mounting plate")
    actual = [p for p in solids if p.role == "solid"]
    collisions = [(a.name, b.name) for i, a in enumerate(actual) for b in actual[i+1:]
                  if overlap(a.bounds(values), b.bounds(values))]
    if collisions:
        raise ValueError("Positive-volume box interference: " + str(collisions))


def sweep_collisions(cartridge, anchor, overrides=None):
    """Exact union boxes for each constant-or-axis-translating part per path segment.

    Pairwise relative swept AABBs; no rotation, contact friction, hidden reservations,
    cables, fasteners, deformation or stopping distance. Touching faces are allowed.
    """
    defaults = dict(overrides or {}, travel_x=0, travel_y=0)
    v = parameters(defaults)
    poses = [(0, 0), (0, v["release_y"]), (v["stroke"], v["release_y"])]
    solids = [p for p in parts(cartridge, anchor) if p.role == "solid"]
    hits = []
    for start, end in zip(poses, poses[1:]):
        a = parameters(dict(defaults, travel_x=start[0], travel_y=start[1]))
        b = parameters(dict(defaults, travel_x=end[0], travel_y=end[1]))
        for i, first in enumerate(solids):
            f0, f1 = first.bounds(a), first.bounds(b)
            df = tuple(f1[0][k]-f0[0][k] for k in range(3))
            for second in solids[i+1:]:
                s0, s1 = second.bounds(a), second.bounds(b)
                relative = tuple(s1[0][k]-s0[0][k]-df[k] for k in range(3))
                sweep = (tuple(s0[0][k]+min(0, relative[k]) for k in range(3)),
                         tuple(s0[1][k]+max(0, relative[k]) for k in range(3)))
                if overlap(f0, sweep):
                    hits.append((start, end, first.name, second.name))
    return hits


def constraint_rows(cartridge, baseline=120):
    vertical = [[0, 0, 1, -50, 50, 0], [0, 0, 1, -50, -50, 0], [0, 0, 1, 50, 0, 0]]
    planar = ([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
              if cartridge == "A" else
              [[1, 0, 0, 0, 0, -baseline/2], [1, 0, 0, 0, 0, baseline/2], [0, 1, 0, 0, 0, 0]])
    return vertical + planar


def rank(rows):
    matrix = [list(map(float, row)) for row in rows]
    row = 0
    for col in range(6):
        pivot = next((i for i in range(row, len(matrix)) if abs(matrix[i][col]) > 1e-9), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][col]
        matrix[row] = [v/scale for v in matrix[row]]
        for i in range(len(matrix)):
            if i != row:
                factor = matrix[i][col]
                matrix[i] = [a-factor*b for a, b in zip(matrix[i], matrix[row])]
        row += 1
        if row == len(matrix):
            break
    return row
