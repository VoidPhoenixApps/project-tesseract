"""Analytic/source checks; never imports Fusion or claims kernel/physical evidence."""

import ast
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import Mock
import uuid

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "cad/fusion/TesseractDockingFixture"
spec = importlib.util.spec_from_file_location("phase1c_test_model", FOLDER / "fixture_model.py")
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


class FixtureChecks(unittest.TestCase):
    def test_source_package(self):
        for source in FOLDER.glob("*.py"):
            compile(source.read_text(encoding="utf-8"), str(source), "exec")
        entry = ast.parse((FOLDER / "TesseractDockingFixture.py").read_text(encoding="utf-8"))
        self.assertEqual(sum(isinstance(n, ast.FunctionDef) and n.name == "run" for n in entry.body), 1)
        manifest = json.loads((FOLDER / "TesseractDockingFixture.manifest").read_text())
        self.assertEqual(manifest["type"], "script")
        self.assertEqual(manifest["autodeskProduct"], "Fusion360")
        self.assertFalse(manifest["runOnStartup"])
        self.assertEqual(manifest["supportedOS"], "windows|mac")
        uuid.UUID(manifest["id"])

    def test_visibility_uses_writable_api(self):
        entry = ast.parse((FOLDER / "TesseractDockingFixture.py").read_text())
        writes = [n for n in ast.walk(entry) if isinstance(n, ast.Attribute)
                  and isinstance(n.ctx, ast.Store)]
        self.assertFalse(any(n.attr == "isVisible" for n in writes))
        for name in ("holes", "sketch", "plane"):
            self.assertTrue(any(n.attr == "isLightBulbOn" and isinstance(n.value, ast.Name)
                                and n.value.id == name for n in writes))

    def test_four_nominal_variants_and_release_sweeps(self):
        for cartridge, anchor in itertools.product(("A", "B"), ("center", "inset")):
            with self.subTest(cartridge=cartridge, anchor=anchor):
                parts = m.parts(cartridge, anchor)
                for x, y in ((0, 0), (0, 4), (0, 8), (20, 8), (40, 8)):
                    m.validate_geometry(m.parameters({"travel_x": x, "travel_y": y}), parts)
                self.assertEqual(m.sweep_collisions(cartridge, anchor), [])

    def test_dimensions_datums_and_parameter_dependencies(self):
        p = m.parameters()
        solids = {item.name: item for item in m.parts()}
        a = solids["Fixed_retained_sheet_ENVELOPE"].bounds(p)
        b = solids["Moving_retained_sheet_ENVELOPE"].bounds(p)
        self.assertEqual(tuple(y-x for x, y in zip(*a)), (180, 180, 1))
        self.assertEqual(a[1][2], 0)
        self.assertEqual(b[1][2], 0)
        self.assertAlmostEqual(b[0][0]-a[1][0], 0.5)
        changed = m.parameters({"gap": 1.25, "carrier": 164, "stroke": 50,
                                "release_y": 10, "travel_x": 50, "travel_y": 10})
        moved = solids["Moving_retained_sheet_ENVELOPE"].bounds(changed)
        self.assertEqual(moved[0][0]-b[0][0], 50.75)
        self.assertEqual(moved[0][1]-b[0][1], 10)
        self.assertEqual(moved[1][2], 0)
        self.assertEqual(solids["Fixed_retained_sheet_ENVELOPE"].bounds(changed), a)

    def test_parameter_endpoints(self):
        # One-factor endpoint coverage, not every combination or a tolerance stack.
        for name, (_, low, high, _) in m.PARAMETERS.items():
            if name in ("travel_x", "travel_y", "guard_gap"):
                continue
            for boundary in (low, high):
                values = m.parameters({name: boundary})
                for cartridge in ("A", "B"):
                    with self.subTest(name=name, value=boundary, cartridge=cartridge):
                        m.validate_geometry(values, m.parts(cartridge))
                        self.assertEqual(m.sweep_collisions(cartridge, "inset", {name: boundary}), [])

    def test_invalid_and_nonfinite_inputs(self):
        cases = ({"gap": 0}, {"bed": 190}, {"carrier": -1}, {"stroke": float("nan")},
                 {"release_y": float("inf")}, {"travel_x": 1}, {"travel_y": 9},
                 {"guard_gap": 1, "float_xy": 0.8, "float_yaw_deg": 0.3}, {"unknown": 1})
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                m.parameters(case)
        with self.assertRaises(ValueError):
            m.evaluate("__import__('os')", {})

    def test_numeric_endpoints_and_representative_cm_roundtrips(self):
        for name, (_, low, high, _) in m.PARAMETERS.items():
            for bound in (low, high):
                samples = [bound]
                if name != "float_yaw_deg":
                    samples += [(bound/10)*10, (bound*0.1)*10]
                for sample in samples:
                    with self.subTest(name=name, bound=bound, sample=sample):
                        overrides = {name: sample}
                        if name == "travel_x":
                            overrides.update(stroke=50, travel_y=8)
                        elif name == "travel_y":
                            overrides.update(release_y=10)
                        result = m.parameters(overrides)[name]
                        if low <= sample <= high:
                            self.assertEqual(result, sample)  # no rounding of valid values
                        else:
                            self.assertEqual(result, bound)

    def test_numeric_range_allowance_is_one_outward_step_only(self):
        for name, (_, low, high, _) in m.PARAMETERS.items():
            for bound, direction in ((low, -math.inf), (high, math.inf)):
                adjacent = math.nextafter(float(bound), direction)
                beyond = math.nextafter(adjacent, direction)
                overrides = {name: adjacent}
                if name == "travel_x":
                    overrides.update(stroke=50, travel_y=8)
                elif name == "travel_y":
                    overrides.update(release_y=10)
                with self.subTest(name=name, bound=bound):
                    if bound == 0:
                        with self.assertRaises(ValueError):
                            m.parameters(overrides)
                    else:
                        self.assertEqual(m.parameters(overrides)[name], bound)
                    for invalid in (beyond, bound + (-1e-9 if direction < 0 else 1e-9)):
                        overrides[name] = invalid
                        with self.assertRaisesRegex(ValueError, name):
                            m.parameters(overrides)
            for invalid in (float("nan"), float("inf"), -float("inf"), True, "164"):
                with self.subTest(name=name, invalid=invalid), self.assertRaises(ValueError):
                    m.parameters({name: invalid})

    def test_nearby_valid_values_are_not_rounded(self):
        for name, (_, low, high, _) in m.PARAMETERS.items():
            if low == high:
                continue
            for value in (math.nextafter(float(low), high), math.nextafter(float(high), low)):
                overrides = {name: value}
                if name == "travel_x":
                    overrides.update(stroke=50, travel_y=8)
                elif name == "travel_y":
                    overrides.update(release_y=10)
                with self.subTest(name=name, value=value):
                    self.assertEqual(m.parameters(overrides)[name], value)
        for value in (math.nextafter(156.0, math.inf), 156.000001,
                      163.999999, math.nextafter(164.0, -math.inf)):
            self.assertEqual(m.parameters({"carrier": value})["carrier"], value)
        with self.assertRaisesRegex(ValueError, r"carrier=164\.000001"):
            m.parameters({"carrier": 164.000001})

    def test_converted_carrier_endpoint_geometry_and_sequence_guards(self):
        converted = (164*0.1)*10
        self.assertEqual(converted, math.nextafter(164.0, math.inf))
        values = m.parameters({"carrier": converted})
        self.assertEqual(values["carrier"], 164)
        self.assertEqual(values["cartridge_side"], 176)
        for cartridge, anchor in itertools.product(("A", "B"), ("center", "inset")):
            m.validate_geometry(values, m.parts(cartridge, anchor))
            self.assertEqual(m.sweep_collisions(cartridge, anchor, {"carrier": converted}), [])
        for overrides in ({"travel_x": 1}, {"travel_x": math.nextafter(0.0, math.inf)},
                          {"travel_x": 1, "travel_y": math.nextafter(8.0, 0.0)},
                          {"travel_x": math.nextafter(40.0, math.inf), "travel_y": 8},
                          {"travel_y": math.nextafter(8.0, math.inf)}):
            with self.subTest(overrides=overrides), self.assertRaisesRegex(
                    ValueError, "Release Y fully|Displayed pose exceeds"):
                m.parameters(dict(overrides, carrier=converted))

    def test_constraint_rank_and_negative_controls(self):
        for cartridge in ("A", "B"):
            self.assertEqual(m.rank(m.constraint_rows(cartridge)), 6)
        b = m.constraint_rows("B")
        self.assertEqual(m.rank(b[:3]+b[4:]), 5)  # one X pad missing
        self.assertEqual(m.rank(m.constraint_rows("B", 0)), 5)  # lost yaw lever
        redundant = b+[[0, 0, 0, 0, 0, 1]]
        self.assertEqual(len(redundant), 7)
        self.assertEqual(m.rank(redundant), 6)  # guide yaw fights B dock

    def test_common_cartridge_interface(self):
        a = {p.name: p for p in m.parts("A")}
        b = {p.name: p for p in m.parts("B")}
        for name in ("Common_cartridge_mount_plate", "Moving_cold_carrier", "Y_station_contact"):
            self.assertEqual(a[name], b[name])
        self.assertEqual(len(a["Common_cartridge_mount_plate"].bores), 4)
        self.assertEqual(sum("X_station_contact" in n for n in a), 1)
        self.assertEqual(sum("X_station_contact" in n for n in b), 2)

    def test_bores_follow_plate_center_pitch_and_diameter(self):
        plate = next(p for p in m.parts() if p.bores)
        for overrides in ({}, {"mount_pitch": 90, "mount_bore": 4},
                          {"mount_pitch": 110, "mount_bore": 6, "carrier": 164},
                          {"gap": 2, "travel_y": 8, "travel_x": 40}):
            with self.subTest(overrides=overrides):
                values = m.parameters(overrides)
                lo, hi = plate.bounds(values)
                centers = [(m.evaluate(x, values), m.evaluate(y, values))
                           for x, y, _ in plate.bores]
                center = tuple((a+b)/2 for a, b in zip(lo, hi))
                half_pitch = values["mount_pitch"]/2
                self.assertEqual(set(centers),
                                 {(center[0]+dx, center[1]+dy)
                                  for dx in (-half_pitch, half_pitch)
                                  for dy in (-half_pitch, half_pitch)})
                self.assertEqual([m.evaluate(d, values) for _, _, d in plate.bores],
                                 [values["mount_bore"]]*4)

    def test_collision_detector_negative_control(self):
        p = m.parameters()
        solids = m.parts()
        sheet = next(s for s in solids if s.name == "Moving_retained_sheet_ENVELOPE")
        collision = m.Part("injected_obstacle", sheet.xyz, sheet.size)
        with self.assertRaisesRegex(ValueError, "interference"):
            m.validate_geometry(p, solids+[collision])
        self.assertFalse(m.overlap(((0, 0, 0), (1, 1, 1)), ((1, 0, 0), (2, 1, 1))))

    def test_float_guard_and_seam_risk_are_distinct(self):
        p = m.parameters()
        carrier_sweep = 2*(p["carrier"]/math.sqrt(2))*math.sin(math.radians(p["float_yaw_deg"])/2)
        self.assertGreater(p["guard_gap"], p["float_xy"]+carrier_sweep)
        sheet_sweep = 2*(p["bed"]/math.sqrt(2))*math.sin(math.radians(p["float_yaw_deg"])/2)
        # An arbitrary floated/yawed plate is NOT safe to bring to the nominal seam.
        self.assertGreater(p["float_xy"]+sheet_sweep, p["gap"])


class Collection(list):
    """Only API collection shape, not a Fusion constraint solver."""
    @property
    def count(self):
        return len(self)

    def item(self, index):
        return self[index]


class BoreAPIContractChecks(unittest.TestCase):
    """Exercise calls/expressions and failures, never claim Fusion execution."""
    def setUp(self):
        tree = ast.parse((FOLDER / "TesseractDockingFixture.py").read_text())
        names = {"expression", "dimension", "constraint_state", "locate", "create_mount_bores"}
        functions = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)
                                    and n.name in names], type_ignores=[])
        import re
        self.scope = {"model": m, "PREFIX": "t1c_", "re": re, "extrude": Mock()}
        self.scope["adsk"] = SimpleNamespace(
            core=SimpleNamespace(Point3D=SimpleNamespace(create=lambda x, y, z: (x, y, z))),
            fusion=SimpleNamespace(DimensionOrientations=SimpleNamespace(
                HorizontalDimensionOrientation="X", VerticalDimensionOrientation="Y"),
                FeatureOperations=SimpleNamespace(CutFeatureOperation="cut")))
        exec(compile(functions, "bore_api_contract", "exec"), self.scope)
        self.sketches = []
        self.fail_axis = None
        self.fail_diameter = False
        self.component = SimpleNamespace(sketches=SimpleNamespace(add=self.add_sketch))
        self.plate = next(p for p in m.parts() if p.bores)

    def add_sketch(self, plane):
        sketch = SimpleNamespace(name="", plane=plane, originPoint=object(),
                                 geometricConstraints=Collection(), profiles=Collection([object()]))
        dimensions = Collection()

        def distance(first, second, orientation, position, driving):
            if self.fail_axis == orientation and len(self.sketches) == 2:
                raise RuntimeError("VCS_SKETCH_OVER_CONSTRAINTS")
            dim = SimpleNamespace(parameter=SimpleNamespace(expression=""),
                                  first=first, second=second, axis=orientation, isDriving=driving)
            dimensions.append(dim)
            return dim

        def diameter(circle, position, driving):
            if self.fail_diameter:
                return None
            dim = SimpleNamespace(parameter=SimpleNamespace(expression=""), isDriving=driving)
            dimensions.append(dim)
            return dim

        def circle(center, radius):
            point = SimpleNamespace(geometry=center, isFixed=False, geometricConstraints=Collection())
            sketch.circle = SimpleNamespace(centerSketchPoint=point, radius=radius)
            return sketch.circle

        dimensions.addDistanceDimension = distance
        dimensions.addDiameterDimension = diameter
        sketch.sketchDimensions = dimensions
        sketch.sketchCurves = SimpleNamespace(sketchCircles=SimpleNamespace(addByCenterRadius=circle))
        self.sketches.append(sketch)
        return sketch

    def test_four_isolated_driving_bores_and_through_cuts(self):
        plane = object()
        self.scope["create_mount_bores"](self.component, plane, self.plate, m.parameters())
        self.assertEqual(len(self.sketches), 4)
        self.assertEqual(self.scope["extrude"].call_count, 4)
        for i, (sketch, bore) in enumerate(zip(self.sketches, self.plate.bores), 1):
            self.assertIs(sketch.plane, plane)
            self.assertIn(f"hole_{i}_", sketch.name)
            self.assertFalse(sketch.isLightBulbOn)
            self.assertEqual(len(sketch.sketchDimensions), 3)
            self.assertEqual([d.parameter.expression for d in sketch.sketchDimensions],
                             [self.scope["expression"](e) for e in bore])
            self.assertTrue(all(d.isDriving for d in sketch.sketchDimensions))
            self.assertEqual([d.axis for d in sketch.sketchDimensions[:2]], ["X", "Y"])
            for dim in sketch.sketchDimensions[:2]:
                self.assertIs(dim.first, sketch.originPoint)
                self.assertIs(dim.second, sketch.circle.centerSketchPoint)
            self.assertEqual(sketch.circle.centerSketchPoint.geometry,
                             tuple(m.evaluate(e, m.parameters())/10 for e in bore[:2])+(0,))
            self.assertEqual(sketch.circle.radius, 0.25)  # 5 mm diameter -> cm radius
            self.scope["extrude"].assert_any_call(self.component, sketch.profiles.item(0),
                                                "4 mm", "cut", f"Common_mount_bore_{i}")

    def test_solver_failure_reports_hole_axis_expression_and_cause(self):
        for axis in ("X", "Y"):
            with self.subTest(axis=axis):
                self.sketches.clear()
                self.fail_axis = axis
                with self.assertRaises(RuntimeError) as caught:
                    self.scope["create_mount_bores"](self.component, object(), self.plate, m.parameters())
                self.assertIn("Common_cartridge_mount_plate, hole 2/4", str(caught.exception))
                inner = caught.exception.__cause__
                self.assertIn(f"create driving dimension {axis}=t1c_moving_", str(inner))
                self.assertIn("Before: sketch constraints=[]", str(inner))
                self.assertIn("center fixed=False", str(inner))
                self.assertIn("VCS_SKETCH_OVER_CONSTRAINTS", str(inner.__cause__))
                self.assertEqual(len(self.sketches), 2)  # stop, no fallback/retry

    def test_null_diameter_fails_with_context(self):
        self.fail_diameter = True
        with self.assertRaisesRegex(RuntimeError, "hole 1/4: create driving diameter"):
            self.scope["create_mount_bores"](self.component, object(), self.plate, m.parameters())
        self.scope["extrude"].assert_not_called()

    def test_constraint_diagnostics_include_inferred_relations(self):
        sketch = self.add_sketch(object())
        constraint = SimpleNamespace(objectType="adsk::fusion::HorizontalPointsConstraint")
        sketch.geometricConstraints.append(constraint)
        point = SimpleNamespace(isFixed=False, geometricConstraints=Collection([constraint]))
        state = self.scope["constraint_state"](sketch, point)
        self.assertEqual(state.count(constraint.objectType), 2)
        self.assertIn("inspection unavailable", self.scope["constraint_state"](None, None))


if __name__ == "__main__":
    unittest.main()
