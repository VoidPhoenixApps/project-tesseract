"""Linear constraint contract tests, not a simulation of Fusion's solver/kernel."""
import ast
import itertools
from pathlib import Path
from types import SimpleNamespace as NS
import unittest

from test_phase1c_diagnostics import Collection, model


class FootprintSketch:
    """Collect the actual generator's API calls as Cartesian linear equations."""
    def __init__(self, values, omit_orientation=False):
        self.values = values
        self.rows = []
        self.originPoint = NS(geometry=NS(x=0, y=0, z=0), index=None)
        self.profiles = Collection([object()])
        self.sketchCurves = NS(sketchLines=NS(addTwoPointRectangle=self.rectangle))
        self.geometricConstraints = NS(
            addHorizontal=lambda edge: self.orient(edge, 1, omit_orientation),
            addVertical=lambda edge: self.orient(edge, 0, omit_orientation))

    def rectangle(self, first, last):
        p = first.geometry if first is self.originPoint else first
        self.points = [NS(geometry=NS(x=x, y=y, z=0), index=i)
                       for i, (x, y) in enumerate(((p.x, p.y), (last.x, p.y),
                                                  (last.x, last.y), (p.x, last.y)))]
        if first is self.originPoint:
            for axis in (0, 1):
                self.equation(self.originPoint, self.points[0], axis, "0 mm")
        # Deliberately differ from Autodesk's returned edge order: corner and
        # orientation selection must not accidentally depend on list indices.
        return Collection(NS(startSketchPoint=self.points[i], endSketchPoint=self.points[(i+1)%4])
                          for i in (2, 3, 0, 1))

    def equation(self, first, second, axis, expression):
        row = [0.0]*8
        for point, sign in ((first, -1), (second, 1)):
            if point.index is not None:
                row[2*point.index+axis] += sign
        # Fusion distance dimensions use unsigned magnitude. Keep the seed's
        # orientation branch; the supported domains never invert these edges.
        delta = getattr(second.geometry, "xy"[axis])-getattr(first.geometry, "xy"[axis])
        self.rows.append((row, expression, -1 if delta < 0 else 1))

    def orient(self, edge, axis, omit):
        if not omit:
            self.equation(edge.startSketchPoint, edge.endSketchPoint, axis, "0 mm")
        return object()

    def solve(self, values):
        rows = [coeffs[:]+[sign*model.evaluate(expr, values)] for coeffs, expr, sign in self.rows]
        pivot = 0
        for col in range(8):
            selected = next((i for i in range(pivot, len(rows)) if abs(rows[i][col]) > 1e-12), None)
            if selected is None:
                continue
            rows[pivot], rows[selected] = rows[selected], rows[pivot]
            divisor = rows[pivot][col]
            rows[pivot] = [v/divisor for v in rows[pivot]]
            for i in range(len(rows)):
                if i != pivot:
                    factor = rows[i][col]
                    rows[i] = [a-factor*b for a, b in zip(rows[i], rows[pivot])]
            pivot += 1
        if pivot != 8:
            raise ValueError(f"rank {pivot}, eight corner coordinates require rank 8")
        return [(rows[2*i][-1], rows[2*i+1][-1]) for i in range(4)]

    @property
    def isFullyConstrained(self):
        try:
            self.solve(self.values)
            return True
        except ValueError:
            return False


class FootprintChecks(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "cad/fusion/TesseractDockingFixture/TesseractDockingFixture.py"
        tree = ast.parse(source.read_text())
        funcs = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)
                                and n.name == "constrain_footprint"], type_ignores=[])
        scope = dict(adsk=NS(core=NS(Point3D=NS(create=lambda x, y, z: NS(x=x, y=y, z=z)))))
        scope["dimension"] = lambda sketch, a, b, horizontal, expr, pos: sketch.equation(a, b, 0 if horizontal else 1, expr)
        def locate(sketch, corner, x, y, values):
            for axis, expr in enumerate((x, y)):
                sketch.equation(sketch.originPoint, corner, axis, expr)
        scope["locate"] = locate
        exec(compile(funcs, str(source), "exec"), scope)
        self.constrain = scope["constrain_footprint"]

    def test_all_variants_resize_both_directions_without_reseeding(self):
        values = model.parameters()
        for variant in itertools.product(("A", "B"), ("center", "inset")):
            for part in model.parts(*variant):
                sketch = FootprintSketch(values)
                self.constrain(sketch, part, values)
                for carrier in (160, 164, 160, 156, 164, 156, 160):
                    changed = model.parameters({"carrier": carrier})
                    points = sketch.solve(changed)
                    lo, hi = part.bounds(changed)
                    expected = ((lo[0], lo[1]), (hi[0], lo[1]), (hi[0], hi[1]), (lo[0], hi[1]))
                    with self.subTest(variant=variant, part=part.name, carrier=carrier):
                        for actual, wanted in zip(points, expected):
                            for a, b in zip(actual, wanted):
                                self.assertAlmostEqual(a, b, places=9)
                # Other coordinate-driving edits use the same graph, no new seeds.
                for overrides in ({"gap": 2}, {"travel_y": 8}, {"travel_y": 8, "travel_x": 40}, {}):
                    changed = model.parameters(overrides)
                    points = sketch.solve(changed)
                    lo, hi = part.bounds(changed)
                    self.assertAlmostEqual(points[0][0], lo[0])
                    self.assertAlmostEqual(points[0][1], lo[1])
                    self.assertAlmostEqual(points[2][0], hi[0])
                    self.assertAlmostEqual(points[2][1], hi[1])

    def test_missing_orientation_reproduces_underconstraint(self):
        part = next(p for p in model.parts() if p.name == "Fixed_cold_carrier")
        sketch = FootprintSketch(model.parameters(), omit_orientation=True)
        with self.assertRaisesRegex(RuntimeError, "Fixed_cold_carrier: footprint remains underconstrained"):
            self.constrain(sketch, part, sketch.values)
        with self.assertRaisesRegex(ValueError, "rank 4"):
            sketch.solve(model.parameters({"carrier": 164}))

    def test_observed_trapezoid_satisfies_old_drivers_but_not_rectangle(self):
        # From Forbidden Fruit's 164 mm CHECK report, rounded here to mm.
        # This reproduces the measured constraint satisfaction, not the solver.
        observed = ((18, 38), (182, 36), (182, 200), (18, 200))
        lower_left, lower_right, upper_right, _ = observed
        self.assertEqual(lower_left, (18, 38))
        self.assertEqual(lower_right[0]-lower_left[0], 164)  # horizontal driver
        self.assertEqual(upper_right[1]-lower_right[1], 164)  # vertical driver
        self.assertEqual(tuple(min(p[i] for p in observed) for i in (0, 1)), (18, 36))
        self.assertEqual(tuple(max(p[i] for p in observed) for i in (0, 1)), (182, 200))
        self.assertNotEqual(lower_left[1], lower_right[1])
        part = next(p for p in model.parts() if p.name == "Fixed_cold_carrier")
        sketch = FootprintSketch(model.parameters())
        self.constrain(sketch, part, sketch.values)
        flat = [v for point in observed for v in point]
        values = model.parameters({"carrier": 164})
        residuals = [sum(a*b for a, b in zip(row, flat))-sign*model.evaluate(expr, values)
                     for row, expr, sign in sketch.rows]
        self.assertTrue(any(abs(v) > 0.001 for v in residuals))
        self.assertEqual(sketch.solve(values), [(18, 38), (182, 38), (182, 202), (18, 202)])

    def test_constraint_rejection_identifies_part_edge_axis(self):
        part = next(p for p in model.parts() if p.name == "Fixed_cold_carrier")
        sketch = FootprintSketch(model.parameters())
        def reject(edge):
            raise RuntimeError("injected solver rejection")
        sketch.geometricConstraints.addHorizontal = reject
        with self.assertRaisesRegex(RuntimeError, "Fixed_cold_carrier: footprint edge 1 horizontal") as caught:
            self.constrain(sketch, part, sketch.values)
        self.assertIn("injected solver rejection", str(caught.exception.__cause__))
