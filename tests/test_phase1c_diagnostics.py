"""Checker diagnostics with API-shaped doubles; no Fusion kernel simulation."""

import ast
import importlib.util
import math
from pathlib import Path
import re
import sys
import tempfile
import traceback
from types import SimpleNamespace as NS
import unittest
from unittest.mock import Mock

FOLDER = Path(__file__).resolve().parents[1] / "cad/fusion/TesseractDockingFixture"
spec = importlib.util.spec_from_file_location("diagnostic_test_model", FOLDER / "fixture_model.py")
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)


class Collection(list):
    @property
    def count(self):
        return len(self)

    def item(self, index):
        return self[index]


def box(bounds):
    points = [NS(**dict(zip("xyz", (v/10 for v in point)))) for point in bounds]
    return NS(minPoint=points[0], maxPoint=points[1])


class DiagnosticChecks(unittest.TestCase):
    def setUp(self):
        tree = ast.parse((FOLDER / "TesseractDockingFixture.py").read_text())
        self.identity = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
        self.scope = dict(model=model, math=math, re=re, sys=sys, tempfile=tempfile, traceback=traceback,
                          Path=Path, __file__=str(FOLDER / "TesseractDockingFixture.py"), PREFIX="t1c_", GROUP="TesseractPhase1C")
        self.scope["adsk"] = NS(core=NS(Matrix3D=NS(
            create=lambda: NS(asArray=lambda: list(self.identity)))))
        functions = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)],
                               type_ignores=[])
        exec(compile(functions, "diagnostic_contract", "exec"), self.scope)

    def design(self, carrier=164):
        values = model.parameters({"carrier": carrier})
        parameters = {"t1c_"+name: NS(expression=(model.DERIVED.get(name) or str(v)+" mm"),
                                    value=v if name == "float_yaw_deg" else v/10)
                      for name, v in values.items()}
        occurrences = Collection()
        for part in model.parts():
            lo, hi = part.bounds(values)
            volume = math.prod(b-a for a, b in zip(lo, hi))
            volume -= sum(math.pi*(model.evaluate(d, values)/2)**2 *
                          model.evaluate(part.size[2], values) for _, _, d in part.bores)
            body = NS(boundingBox=box((lo, hi)), preciseBoundingBox=box((lo, hi)),
                      volume=volume/1000, isSolid=True)
            body.createForAssemblyContext = Mock(return_value=NS(
                boundingBox=box((lo, hi)), preciseBoundingBox=box((lo, hi))))
            component = NS(attributes=NS(itemByName=lambda group, key, n=part.name: NS(value=n)),
                           bRepBodies=Collection([body]), occurrences=Collection(),
                           sketches=Collection(), modelParameters=Collection(),
                           features=NS(extrudeFeatures=Collection()))
            occurrence = NS(component=component, transform2=NS(asArray=lambda: list(self.identity)))
            occurrences.append(occurrence)
            if part.name == "Fixed_cold_carrier":
                self.carrier = occurrence
                self.part = part
                dims = Collection([NS(objectType="SketchLinearDimension", isDriving=True,
                                      parameter=NS(expression=e, value=model.evaluate(raw, values)/10))
                                   for e, raw in zip(
                                       ("t1c_fixed_x-t1c_carrier/2", "t1c_center_y-t1c_carrier/2",
                                        "t1c_carrier", "t1c_carrier"),
                                       part.xyz[:2]+part.size[:2])])
                corners = [NS(geometry=NS(x=x/10, y=y/10, z=0)) for x, y in
                           ((lo[0], lo[1]), (hi[0], lo[1]), (hi[0], hi[1]), (lo[0], hi[1]))]
                origin = NS(geometry=NS(x=0, y=0, z=0))
                for dim, first, second, orientation in zip(
                        dims, (origin, origin, corners[0], corners[0]),
                        (corners[0], corners[0], corners[1], corners[3]),
                        ("horizontal", "vertical", "horizontal", "vertical")):
                    dim.entityOne, dim.entityTwo, dim.orientation = first, second, orientation
                lines = Collection([NS(startSketchPoint=corners[i], endSketchPoint=corners[(i+1)%4])
                                    for i in range(4)])
                component.sketches.append(NS(
                    name="Fixed_cold_carrier_footprint", healthState="healthy",
                    errorOrWarningMessage="", isFullyConstrained=True, sketchDimensions=dims,
                    geometricConstraints=Collection([NS(objectType="HorizontalConstraint")]),
                    sketchCurves=NS(sketchLines=lines),
                    sketchToModelSpace=lambda p: NS(x=p.x, y=p.y, z=p.z-2.4)))
                component.modelParameters.append(NS(name="height", expression="6 mm", value=0.6, unit="mm"))
                component.features.extrudeFeatures.append(NS(
                    name="Fixed_cold_carrier_thickness", healthState="healthy",
                    errorOrWarningMessage="", isSuppressed=False))
        root = NS(occurrences=occurrences, bRepBodies=Collection(),
                  attributes=NS(itemByName=lambda group, key: NS(value="B" if key == "cartridge" else "inset")))
        return NS(rootComponent=root, userParameters=NS(itemByName=parameters.get),
                  computeAll=Mock(return_value=True), timeline=NS(markerPosition=100, count=100))

    def test_default_and_boundary_reports_preserve_checker_passes(self):
        for carrier, wanted in ((160, ((20, 40, -24), (180, 200, -18))),
                                (164, ((18, 38, -24), (182, 202, -18)))):
            with self.subTest(carrier=carrier):
                design = self.design(carrier)
                parameter = design.userParameters.itemByName("t1c_carrier")
                before = (parameter.expression, parameter.value)
                result = self.scope["check_design"](design)
                self.assertIn("Checked 59", result)
                self.assertIn(f"Actual dimensions XYZ=({float(carrier)}, {float(carrier)}, 6.0)", result)
                self.assertIn("center XYZ=(100.0, 120.0, -21.0)", result)
                self.assertEqual(self.scope["bounds_mm"](self.carrier.component.bRepBodies[0].boundingBox), wanted)
                self.assertEqual((parameter.expression, parameter.value), before)
                design.computeAll.assert_called_once_with()

    def test_observed_y_shift_fails_and_dimension_references_are_reported(self):
        design = self.design(164)
        self.carrier.component.bRepBodies[0].boundingBox = box(((18, 36, -24), (182, 200, -18)))
        with self.assertRaises(ValueError) as caught:
            self.scope["check_design"](design)
        report = str(caught.exception)
        for expected in ("Delta min XYZ=(0.0, -2.0, 0.0); max XYZ=(0.0, -2.0, 0.0)",
                         "dimensions XYZ=(164.0, 164.0, 6.0)", "center XYZ=(100.0, 118.0, -21.0)",
                         "linear dimension references", "vertical", "(18.0, 38.0, -24.0)"):
            self.assertIn(expected, report)
        # Sketch coordinates here are synthetic, not captured from the failed design.

    def test_complete_reports_are_unique_local_files_with_short_dialogs(self):
        paths = []
        try:
            for failed in (False, True):
                design = self.design(164)
                if failed:
                    self.carrier.component.bRepBodies[0].boundingBox = box(((18, 36, -24), (182, 200, -18)))
                message = self.scope["check_report"](design)
                path = Path(message.split("Diagnostics: ", 1)[1])
                paths.append(path)
                self.assertEqual(path.parent.resolve(),
                                 Path(tempfile.gettempdir() if sys.platform == "win32" else "/tmp").resolve())
                self.assertEqual(len(message.splitlines()), 2)
                self.assertIn("CHECK FAILED" if failed else "CHECK PASSED", message)
                if failed:
                    self.assertIn("Fixed_cold_carrier", message)
                text = path.read_text(encoding="utf-8")
                for part in model.parts():
                    self.assertIn(part.name, text)
                for detail in ("Component model parameters", "linear dimension references",
                               "constraint types", "line endpoints", "health/message/suppressed",
                               "Actual min", "User parameters", "fullyConstrained"):
                    self.assertIn(detail, text)
                self.assertGreater(len(text), len(message)*10)
                design.computeAll.assert_called_once_with()
            self.assertNotEqual(*paths)
        finally:
            for path in paths:
                path.unlink()  # Only temporary files created by this test.

    def test_early_check_failure_is_logged(self):
        message = self.scope["check_report"](None)
        path = Path(message.split("Diagnostics: ", 1)[1])
        try:
            self.assertIn("CHECK FAILED: Activate a generated Fusion design first", message)
            self.assertIn("Traceback", path.read_text())
        finally:
            path.unlink()

    def test_stale_geometry_reports_all_axes_and_feature_evidence(self):
        design = self.design()
        self.carrier.component.bRepBodies[0].boundingBox = box(((20, 40, -24), (180, 200, -18)))
        self.carrier.component.sketches[0].isFullyConstrained = False
        self.carrier.component.sketches[0].sketchDimensions[0].isDriving = False
        feature = self.carrier.component.features.extrudeFeatures[0]
        feature.healthState, feature.errorOrWarningMessage = "warning", "injected warning"
        with self.assertRaises(ValueError) as caught:
            self.scope["check_design"](design)
        text = str(caught.exception)
        for expected in ("Fixed_cold_carrier", "Actual min=(20.0, 40.0, -24.0)",
                         "Expected min=(18.0, 38.0, -24)", "max=(182.0, 202.0, -18)",
                         "Delta min XYZ=(2.0, 2.0, 0.0); max XYZ=(-2.0, -2.0, 0.0)",
                         "dimensions XYZ=(160.0, 160.0, 6.0)", "center XYZ=(100.0, 120.0, -21.0)",
                         "computeAll returned=True", "t1c_carrier", "t1c_fixed_x-t1c_carrier/2",
                         "False", "injected warning", "Assembly proxy bounds", "Native precise bounds"):
            self.assertIn(expected, text)
        self.assertIn("line endpoints in component XYZ mm=[((18.0, 38.0, -24.0)", text)

    def test_precise_or_proxy_bounds_do_not_override_a_genuine_mismatch(self):
        design = self.design()
        self.carrier.component.bRepBodies[0].boundingBox = box(((18.002, 38, -24), (182.002, 202, -18)))
        # Precise and proxy boxes still match the model; original strict gate must fail.
        with self.assertRaisesRegex(ValueError, "Body bounds disagree.*Fixed_cold_carrier"):
            self.scope["check_design"](design)

    def test_optional_diagnostic_failure_keeps_actual_expected_error(self):
        design = self.design()
        body = self.carrier.component.bRepBodies[0]
        body.boundingBox = box(((20, 40, -24), (180, 200, -18)))
        del body.preciseBoundingBox
        body.createForAssemblyContext.side_effect = RuntimeError("proxy unavailable")
        with self.assertRaises(ValueError) as caught:
            self.scope["check_design"](design)
        self.assertIn("Actual min=(20.0, 40.0, -24.0)", str(caught.exception))
        self.assertIn("Expected min=(18.0, 38.0, -24)", str(caught.exception))
        self.assertIn("unavailable (AttributeError", str(caught.exception))
        self.assertIn("proxy unavailable", str(caught.exception))

    def test_pre_and_post_recompute_measurements_are_distinct(self):
        design = self.design()
        body = self.carrier.component.bRepBodies[0]
        correct = body.boundingBox
        body.boundingBox = box(((20, 40, -24), (180, 200, -18)))
        def compute():
            body.boundingBox = correct
            return True
        design.computeAll.side_effect = compute
        result = self.scope["check_design"](design)
        self.assertIn("Native bounds before computeAll (mm)=((20.0, 40.0, -24.0)", result)
        self.assertIn("Actual min=(18.0, 38.0, -24.0)", result)

    def test_recompute_failure_and_moved_occurrence_still_rejected(self):
        design = self.design()
        design.computeAll.return_value = False
        with self.assertRaisesRegex(RuntimeError, "Fusion recompute failed"):
            self.scope["check_design"](design)
        design.computeAll.return_value = True
        translated = list(self.identity)
        translated[3] = 1
        self.carrier.transform2.asArray = lambda: translated
        with self.assertRaisesRegex(ValueError, "Component was moved.*Fixed_cold_carrier"):
            self.scope["check_design"](design)


if __name__ == "__main__":
    unittest.main()
