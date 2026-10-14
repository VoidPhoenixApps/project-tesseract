"""Checker diagnostics with API-shaped doubles; no Fusion kernel simulation."""

from datetime import datetime, timezone
import hashlib
import json
import platform
import uuid
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
                          Path=Path, datetime=datetime, timezone=timezone, hashlib=hashlib, json=json, platform=platform, uuid=uuid, __file__=str(FOLDER / "TesseractDockingFixture.py"), PREFIX="t1c_", GROUP="TesseractPhase1C")
        self.scope["adsk"] = NS(core=NS(Matrix3D=NS(
            create=lambda: NS(asArray=lambda: list(self.identity)))))
        cast = lambda kind: NS(cast=lambda obj: obj if getattr(obj, "kind", None) == kind else None)
        self.scope["adsk"].core.Cylinder = cast("cylinder")
        self.scope["adsk"].core.Circle3D = cast("circle")
        self.scope["adsk"].fusion = NS(
            FeatureHealthStates=NS(HealthyFeatureHealthState=0),
            HorizontalConstraint=NS(classType=lambda: "adsk::fusion::HorizontalConstraint"),
            VerticalConstraint=NS(classType=lambda: "adsk::fusion::VerticalConstraint"),
            FeatureOperations=NS(NewBodyFeatureOperation="new", CutFeatureOperation="cut"),
            DistanceExtentDefinition=cast("distance"), Profile=cast("profile"),
            ConstructionPlaneOffsetDefinition=cast("offset"), ProfilePlaneStartDefinition=cast("start"))
        functions = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef)],
                               type_ignores=[])
        exec(compile(functions, "diagnostic_contract", "exec"), self.scope)

    def design(self, carrier=164, overrides=None, cartridge="B", anchor="inset"):
        values = model.parameters(dict({"carrier": carrier}, **(overrides or {})))
        parameters = {"t1c_"+name: NS(expression=(model.DERIVED.get(name) or str(v)+" mm"),
                                    value=v if name == "float_yaw_deg" else v/10)
                      for name, v in values.items()}
        occurrences = Collection()
        for part in model.parts(cartridge, anchor):
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
            expr = self.scope["expression"]
            formulas = (() if lo[0] == 0 and lo[1] == 0 else part.xyz[:2])+part.size[:2]
            dims = Collection([NS(objectType="SketchLinearDimension", isDriving=True,
                                  parameter=NS(expression=expr(raw), value=model.evaluate(raw, values)/10))
                               for raw in formulas])
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
            footprint = NS(name=part.name+"_footprint", healthState=0, isValid=True,
                errorOrWarningMessage="", isFullyConstrained=True, sketchDimensions=dims,
                profiles=Collection([NS()]),
                geometricConstraints=Collection([NS(objectType="adsk::fusion::"+axis+"Constraint")
                                                 for axis in ("Horizontal", "Vertical")*2]),
                sketchCurves=NS(sketchLines=lines, sketchCircles=Collection()),
                sketchToModelSpace=lambda p, z=lo[2]/10: NS(x=p.x, y=p.y, z=p.z+z))
            component.sketches.append(footprint)
            component.constructionPlanes = Collection([NS(name=part.name+"_Z_datum", healthState=0, isValid=True)])
            component.xYConstructionPlane = NS(name="XY")
            component.constructionPlanes[0].definition = NS(kind="offset", planarEntity=component.xYConstructionPlane,
                offset=NS(expression=expr(part.xyz[2]), value=lo[2]/10))
            footprint.referencePlane = component.constructionPlanes[0]
            component.modelParameters.append(NS(name="height", expression=expr(part.size[2]),
                                                value=(hi[2]-lo[2])/10, unit="mm"))
            def feature(name, sketch, operation):
                return NS(name=name, healthState=0, isValid=True, isParametric=True, isSolid=True,
                          errorOrWarningMessage="", isSuppressed=False, operation=operation,
                          hasTwoExtents=False, isThinExtrude=False, taperAngleOne=NS(value=0),
                          profile=NS(kind="profile", parentSketch=sketch), startExtent=NS(kind="start"),
                          extentOne=NS(kind="distance", distance=NS(expression=expr(part.size[2]),
                                                                   value=(hi[2]-lo[2])/10)))
            component.features.extrudeFeatures.append(feature(part.name+"_thickness", footprint, "new"))
            body.faces = Collection()
            for index, (bx, by, bd) in enumerate(part.bores, 1):
                x, y, diameter = (model.evaluate(e, values)/10 for e in (bx, by, bd))
                circle = NS(centerSketchPoint=NS(geometry=NS(x=x, y=y, z=0)), radius=diameter/2)
                sketch = NS(name=f"Common_mount_hole_{index}_NOT_fastener_selection", healthState=0,
                            isValid=True, isFullyConstrained=True, profiles=Collection([NS()]),
                            errorOrWarningMessage="", geometricConstraints=Collection(),
                            sketchCurves=NS(sketchCircles=Collection([circle]), sketchLines=Collection()),
                            sketchToModelSpace=footprint.sketchToModelSpace,
                            sketchDimensions=Collection([NS(isDriving=True, objectType="dimension",
                                parameter=NS(expression=expr(raw), value=model.evaluate(raw, values)/10))
                                for raw in (bx, by, bd)]))
                sketch.referencePlane = component.constructionPlanes[0]
                component.sketches.append(sketch)
                cut = feature(f"Common_mount_bore_{index}", sketch, "cut")
                component.features.extrudeFeatures.append(cut)
                face = NS(isValid=True, body=body, tempId=index,
                          geometry=NS(kind="cylinder", origin=NS(x=x, y=y, z=lo[2]/10),
                                      radius=diameter/2, axis=NS(x=0, y=0, z=1)),
                          area=math.pi*diameter*(hi[2]-lo[2])/10,
                          edges=Collection([NS(geometry=NS(kind="circle", center=NS(x=x, y=y, z=z/10),
                                                           radius=diameter/2)) for z in (lo[2], hi[2])]))
                body.faces.append(face)
                cut.sideFaces = Collection([face])
                self.mount = component
                self.mount_part = part
            component.features.count = component.features.extrudeFeatures.count
        root = NS(occurrences=occurrences, bRepBodies=Collection(),
                  attributes=NS(itemByName=lambda group, key: NS(value=cartridge if key == "cartridge" else anchor)))
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

    def test_correct_bores_follow_parameters_in_all_variants(self):
        for cartridge in ("A", "B"):
            for anchor in ("center", "inset"):
                for values in ({"mount_pitch": 90, "mount_bore": 4, "travel_x": 40, "travel_y": 8},
                               {"mount_pitch": 110, "mount_bore": 6}):
                    with self.subTest(cartridge=cartridge, anchor=anchor, values=values):
                        design = self.design(160, values, cartridge, anchor)
                        self.assertIn("bore cuts agree", self.scope["check_design"](design))

    def test_unhealthy_history_rejected_even_with_matching_geometry(self):
        for kind in ("sketch", "feature", "datum"):
            for state in (1, 2, 3, 4, 5):
                with self.subTest(kind=kind, state=state):
                    design = self.design()
                    c = self.carrier.component
                    item = {"sketch": c.sketches[0], "feature": c.features.extrudeFeatures[0],
                            "datum": c.constructionPlanes[0]}[kind]
                    item.healthState = state
                    with self.assertRaisesRegex(ValueError, "history unhealthy"):
                        self.scope["check_design"](design)

    def test_required_history_missing_invalid_suppressed_or_added(self):
        for change in ("missing sketch", "invalid sketch", "missing cut", "suppressed cut",
                       "invalid cut", "renamed cut", "extra feature", "missing datum"):
            with self.subTest(change=change):
                design = self.design()
                c = self.mount
                if change == "missing sketch": c.sketches.pop()
                if change == "invalid sketch": c.sketches[1].isValid = False
                if change == "missing cut": c.features.extrudeFeatures.pop()
                if change == "suppressed cut": c.features.extrudeFeatures[1].isSuppressed = True
                if change == "invalid cut": c.features.extrudeFeatures[1].isValid = False
                if change == "renamed cut": c.features.extrudeFeatures[1].name = "changed"
                if change == "extra feature": c.features.count += 1
                if change == "missing datum": c.constructionPlanes.clear()
                with self.assertRaises(ValueError): self.scope["check_design"](design)

    def test_constraint_and_driver_edits_rejected_without_geometry_change(self):
        for change in ("footprint", "hole", "driven", "frozen expression", "orientation"):
            with self.subTest(change=change):
                design = self.design()
                if change == "footprint": self.carrier.component.sketches[0].isFullyConstrained = False
                if change == "hole": self.mount.sketches[1].isFullyConstrained = False
                if change == "driven": self.mount.sketches[1].sketchDimensions[0].isDriving = False
                if change == "frozen expression": self.mount.sketches[1].sketchDimensions[0].parameter.expression = "230.5 mm"
                if change == "orientation": self.carrier.component.sketches[0].geometricConstraints.pop()
                with self.assertRaises(ValueError): self.scope["check_design"](design)

    def test_extrusion_changes_rejected(self):
        for change in ("operation", "depth", "profile", "taper", "nonparametric", "extent", "thin", "two sides", "start", "datum", "sketch plane"):
            with self.subTest(change=change):
                design = self.design()
                cut = self.mount.features.extrudeFeatures[1]
                if change == "operation": cut.operation = "join"
                if change == "depth": cut.extentOne.distance.value /= 2
                if change == "profile": cut.profile = None
                if change == "taper": cut.taperAngleOne.value = 0.01
                if change == "nonparametric": cut.isParametric = False
                if change == "extent": cut.extentOne.kind = "through all"
                if change == "thin": cut.isThinExtrude = True
                if change == "two sides": cut.hasTwoExtents = True
                if change == "start": cut.startExtent.kind = "offset start"
                if change == "datum": self.mount.constructionPlanes[0].definition.offset.expression = "-31 mm"
                if change == "sketch plane": self.mount.sketches[1].referencePlane = NS(name="other")
                with self.assertRaises(ValueError): self.scope["check_design"](design)

    def test_brep_holes_checked_independently_of_volume_bounds_and_sketches(self):
        for change in ("x", "y", "diameter", "blind", "axis", "area", "missing rim", "missing face", "duplicate", "wrong body"):
            with self.subTest(change=change):
                design = self.design()
                body = self.mount.bRepBodies[0]
                before = (body.volume, body.boundingBox)
                face = body.faces[0]
                if change == "x": face.geometry.origin.x += 0.1
                if change == "y": face.geometry.origin.y += 0.1
                if change == "diameter": face.geometry.radius += 0.05
                if change == "blind": face.edges[1].geometry.center.z -= 0.1
                if change == "axis": face.geometry.axis.x = 0.01
                if change == "area": face.area /= 2
                if change == "missing rim": face.edges.pop()
                if change == "missing face": body.faces.pop()
                if change == "duplicate": self.mount.features.extrudeFeatures[2].sideFaces = Collection([face])
                if change == "wrong body": face.body = NS()
                with self.assertRaises(ValueError): self.scope["check_design"](design)
                self.assertEqual((body.volume, body.boundingBox), before)

    def test_bore_sketch_location_and_diameter_checked(self):
        for change in ("location", "diameter", "circle"):
            with self.subTest(change=change):
                design = self.design()
                circles = self.mount.sketches[1].sketchCurves.sketchCircles
                if change == "location": circles[0].centerSketchPoint.geometry.x += 0.1
                if change == "diameter": circles[0].radius += 0.05
                if change == "circle": circles.clear()
                with self.assertRaises(ValueError): self.scope["check_design"](design)

    def test_nonfinite_inspection_and_unavailable_required_api_fail_closed(self):
        design = self.design()
        self.mount.bRepBodies[0].faces[0].geometry.radius = math.nan
        with self.assertRaisesRegex(ValueError, "cut diameter"):
            self.scope["check_design"](design)
        design = self.design()
        del self.mount.sketches[1].isFullyConstrained
        with self.assertRaises(AttributeError): self.scope["check_design"](design)

    def test_bore_measurements_and_provenance(self):
        design = self.design(160)
        result = self.scope["check_design"](design)
        data = json.loads(result.split("Mounting B-Rep measurements: ")[1].splitlines()[0])
        self.assertEqual([d["center_xy_mm"] for d in data],
                         [[230.5, 70.0], [230.5, 170.0], [330.5, 70.0], [330.5, 170.0]])
        for d in data:
            self.assertEqual(d["diameter_mm"], 5)
            self.assertEqual(d["rim_z_mm"], [-32, -28])
        design.parentDocument = NS(creationId="synthetic-private-document-id")
        self.scope["adsk"].core.Application = NS(get=lambda: NS(version="test-version"))
        first = self.scope["report_provenance"](design)
        second = self.scope["report_provenance"](design)
        self.assertNotEqual(first["run_id"], second["run_id"])
        self.assertEqual(first["document_creation_id_sha256"], second["document_creation_id_sha256"])
        self.assertEqual(first["fusion_version"], "test-version")
        self.assertNotIn("synthetic-private-document-id", json.dumps(first))
        self.assertNotIn(str(FOLDER), json.dumps(first))
        for name, digest in first["source_sha256"].items():
            self.assertEqual(digest, hashlib.sha256((FOLDER/name).read_bytes()).hexdigest())
        self.assertEqual(self.scope["report_provenance"](None)["document_creation_id_sha256"], "unknown")


if __name__ == "__main__":
    unittest.main()
