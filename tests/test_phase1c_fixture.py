"""Analytic/source checks; never imports Fusion or claims kernel/physical evidence."""

import ast
import importlib.util
import itertools
import json
import math
from pathlib import Path
import sys
import unittest
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
        uuid.UUID(manifest["id"])

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


if __name__ == "__main__":
    unittest.main()
