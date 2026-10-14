"""Generate/check a cold Phase 1C concept inside Fusion. No save/export or motion."""

from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import platform
import uuid
import importlib.util
import math
from pathlib import Path
import re
import sys
import tempfile
import traceback

import adsk.core
import adsk.fusion


# Load beside this entry point, independent of Fusion's package name/sys.path.
_path = Path(__file__).with_name("fixture_model.py")
_spec = importlib.util.spec_from_file_location("tesseract_phase1c_model", _path)
model = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = model
_spec.loader.exec_module(model)
PREFIX = "t1c_"
GROUP = "TesseractPhase1C"


def expression(text):
    """Qualify only model symbols; preserve explicit mm and numeric arithmetic."""
    return re.sub(r"\b[A-Za-z_]\w*\b", lambda match: PREFIX+match[0]
                  if match[0] in model.PARAMETERS or match[0] in model.DERIVED
                  else match[0], text)


def value(text):
    return adsk.core.ValueInput.createByString(expression(text))


def dimension(sketch, first, second, horizontal, text, position):
    orientation = (adsk.fusion.DimensionOrientations.HorizontalDimensionOrientation
                   if horizontal else adsk.fusion.DimensionOrientations.VerticalDimensionOrientation)
    before = constraint_state(sketch, second)
    stage = "create driving dimension"
    try:
        dim = sketch.sketchDimensions.addDistanceDimension(first, second, orientation, position, True)
        if not dim:
            raise RuntimeError("API returned no dimension")
        stage = "set driving expression"
        dim.parameter.expression = expression(text)
    except Exception as error:
        axis = "X" if horizontal else "Y"
        raise RuntimeError(
            f"{sketch.name}: {stage} {axis}={expression(text)} failed. "
            f"Before: {before}. After: {constraint_state(sketch, second)}. "
            "Inspect this sketch's constraints; do not fix points or change dimensions to driven."
        ) from error


def constraint_state(sketch, point):
    """Read-only solver evidence; diagnostics must never mask the original error."""
    try:
        def types(collection):
            return [collection.item(i).objectType for i in range(collection.count)]
        return (f"sketch constraints={types(sketch.geometricConstraints)}, "
                f"center constraints={types(point.geometricConstraints)}, "
                f"dimensions={sketch.sketchDimensions.count}, center fixed={point.isFixed}")
    except Exception as error:
        return f"constraint inspection unavailable ({type(error).__name__})"


def locate(sketch, point, x, y, values):
    # Every non-base component lies strictly within +X/+Y, preventing unsigned
    # distance dimensions from flipping quadrant under supported parameter edits.
    px, py = model.evaluate(x, values)/10, model.evaluate(y, values)/10
    dimension(sketch, sketch.originPoint, point, True, x,
              adsk.core.Point3D.create(px/2, py-1, 0))
    dimension(sketch, sketch.originPoint, point, False, y,
              adsk.core.Point3D.create(px-1, py/2, 0))


def extrude(component, profiles, height, operation, name):
    features = component.features.extrudeFeatures
    item = features.createInput(profiles, operation)
    extent = adsk.fusion.DistanceExtentDefinition.create(value(height))
    if not item.setOneSideExtent(extent, adsk.fusion.ExtentDirections.PositiveExtentDirection):
        raise RuntimeError("Cannot set extrusion extent: " + name)
    feature = features.add(item)
    feature.name = name
    return feature


def create_mount_bores(component, plane, part, values):
    # One circle per sketch: no other bore center can acquire a redundant
    # cross-hole alignment relation. Keep the common XY/Z datums and expressions,
    # not frozen coordinates; the plate and bores share moving_x/moving_y.
    for index, (x, y, diameter) in enumerate(part.bores, 1):
        holes = None
        circle = None
        stage = "create sketch"
        try:
            holes = component.sketches.add(plane)
            holes.name = f"Common_mount_hole_{index}_NOT_fastener_selection"
            cx, cy = model.evaluate(x, values)/10, model.evaluate(y, values)/10
            stage = "create circle"
            circle = holes.sketchCurves.sketchCircles.addByCenterRadius(
                adsk.core.Point3D.create(cx, cy, 0), model.evaluate(diameter, values)/20)
            if not circle:
                raise RuntimeError("API returned no circle")
            stage = "locate center"
            locate(holes, circle.centerSketchPoint, x, y, values)
            stage = "create driving diameter"
            dim = holes.sketchDimensions.addDiameterDimension(
                circle, adsk.core.Point3D.create(cx+1, cy+1, 0), True)
            if not dim:
                raise RuntimeError("API returned no diameter dimension")
            stage = "set diameter expression"
            dim.parameter.expression = expression(diameter)
            stage = "check circular profile"
            if holes.profiles.count != 1:
                raise RuntimeError("Expected one circular profile")
            stage = "cut through plate"
            extrude(component, holes.profiles.item(0), part.size[2],
                    adsk.fusion.FeatureOperations.CutFeatureOperation, f"Common_mount_bore_{index}")
            holes.isLightBulbOn = False
        except Exception as error:
            state = constraint_state(holes, circle.centerSketchPoint) if circle else "no circle"
            raise RuntimeError(
                f"{part.name}, hole {index}/{len(part.bores)}: {stage} failed; "
                f"X={expression(x)}, Y={expression(y)}, diameter={expression(diameter)}. {state}"
            ) from error


def constrain_footprint(sketch, part, values):
    lo, hi = part.bounds(values)
    first = (sketch.originPoint if lo[0] == 0 and lo[1] == 0 else
             adsk.core.Point3D.create(lo[0]/10, lo[1]/10, 0))
    lines = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        first, adsk.core.Point3D.create(hi[0]/10, hi[1]/10, 0))
    if not lines or lines.count != 4:
        raise RuntimeError("Rectangle failed: " + part.name)
    # API rectangles need explicit edge orientation constraints (Autodesk's
    # CreateSketchLines sample does the same). Coordinate seeds are not constraints.
    for index, edge in enumerate(lines, 1):
        horizontal = abs(edge.startSketchPoint.geometry.y-edge.endSketchPoint.geometry.y) < 1e-7
        axis = "horizontal" if horizontal else "vertical"
        try:
            constraints = sketch.geometricConstraints
            constraint = (constraints.addHorizontal(edge) if horizontal else
                          constraints.addVertical(edge))
            if not constraint:
                raise RuntimeError("API returned no constraint")
        except Exception as error:
            raise RuntimeError(f"{part.name}: footprint edge {index} {axis} constraint failed") from error
    # Find the lower-left vertex explicitly, independent of returned line order.
    corner = next(point for line in lines for point in (line.startSketchPoint, line.endSketchPoint)
                  if abs(point.geometry.x-lo[0]/10) < 1e-7
                  and abs(point.geometry.y-lo[1]/10) < 1e-7)
    if lo[0] != 0 or lo[1] != 0:
        locate(sketch, corner, part.xyz[0], part.xyz[1], values)
    for horizontal, size in ((True, part.size[0]), (False, part.size[1])):
        edge = next(line for line in lines if
                    (abs(line.startSketchPoint.geometry.y-line.endSketchPoint.geometry.y) < 1e-7)
                    == horizontal)
        dimension(sketch, edge.startSketchPoint, edge.endSketchPoint, horizontal, size,
                  adsk.core.Point3D.create(hi[0]/10+1, hi[1]/10+1, 0))
    if sketch.profiles.count != 1:
        raise RuntimeError("Expected one profile: " + part.name)
    if not sketch.isFullyConstrained:
        raise RuntimeError(f"{part.name}: footprint remains underconstrained after "
                           "edge orientation, lower-corner location and driving sizes")


def create_part(root, part, values):
    occurrence = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    component = occurrence.component
    component.name = part.name
    component.attributes.add(GROUP, "part", part.name)
    plane_input = component.constructionPlanes.createInput()
    if not plane_input.setByOffset(component.xYConstructionPlane, value(part.xyz[2])):
        raise RuntimeError("Cannot set height plane: " + part.name)
    plane = component.constructionPlanes.add(plane_input)
    plane.name = part.name+"_Z_datum"
    sketch = component.sketches.add(plane)
    sketch.name = part.name+"_footprint"
    constrain_footprint(sketch, part, values)
    extrude(component, sketch.profiles.item(0), part.size[2],
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation, part.name+"_thickness")
    if part.bores:
        create_mount_bores(component, plane, part, values)
    if component.bRepBodies.count != 1:
        raise RuntimeError("Expected one body per component: " + part.name)
    component.bRepBodies.item(0).name = part.name
    sketch.isLightBulbOn = False
    plane.isLightBulbOn = False
    occurrence.isLightBulbOn = part.role != "reservation"


def bounds_mm(bounds):
    """Fusion length coordinates are cm; return min/max XYZ in model mm."""
    return tuple(tuple(getattr(point, axis)*10 for axis in "xyz")
                 for point in (bounds.minPoint, bounds.maxPoint))


def diagnostic_read(reader):
    """Optional evidence must not mask a real validation error."""
    try:
        return reader()
    except Exception as error:
        return f"unavailable ({type(error).__name__}: {error})"


def parameter_snapshot(design):
    result = {}
    for name in (*model.PARAMETERS, *model.DERIVED):
        def read():
            parameter = design.userParameters.itemByName(PREFIX+name)
            return (parameter.expression, parameter.value)
        result[name] = diagnostic_read(read)
    return result


def bounds_report(name, actual, wanted):
    delta = tuple(tuple(a-b for a, b in zip(va, vb)) for va, vb in zip(actual, wanted))
    size = tuple(b-a for a, b in zip(*actual))
    center = tuple((a+b)/2 for a, b in zip(*actual))
    return (f"Part: {name}; XYZ in mm; delta = actual - expected\n"
            f"Actual min={actual[0]!r}; max={actual[1]!r}\n"
            f"Expected min={wanted[0]!r}; max={wanted[1]!r}\n"
            f"Delta min XYZ={delta[0]!r}; max XYZ={delta[1]!r}\n"
            f"Actual dimensions XYZ={size!r}; center XYZ={center!r}")


def part_diagnostics(design, occurrence, part, values,
                     before_bounds, before_parameters, recomputed):
    """Read-only evidence; never substitute these measurements for the checker."""
    component = occurrence.component
    body = component.bRepBodies.item(0)
    rows = ["Checked bounds: native component body.boundingBox; tolerance remains 0.001 mm.",
            f"Native bounds before computeAll (mm)={before_bounds!r}",
            f"computeAll returned={recomputed!r}; completion is not proof of feature health."]

    def add(label, reader):
        rows.append(f"{label}={diagnostic_read(reader)!r}")

    add("Timeline marker/count", lambda: (design.timeline.markerPosition, design.timeline.count))
    add("Occurrence transform2 (identity required)", lambda: occurrence.transform2.asArray())
    add("Native precise bounds (mm; diagnostic only)", lambda: bounds_mm(body.preciseBoundingBox))
    add("Assembly proxy bounds (mm; diagnostic only)",
        lambda: bounds_mm(body.createForAssemblyContext(occurrence).boundingBox))
    add("Assembly proxy precise bounds (mm; diagnostic only)",
        lambda: bounds_mm(body.createForAssemblyContext(occurrence).preciseBoundingBox))
    rows.append(f"Source lower XYZ={part.xyz!r}; size XYZ={part.size!r}")

    # Include dependencies recursively plus the settings used in this investigation.
    names = {"carrier", "gap", "travel_x", "travel_y"}
    formulas = list(part.xyz+part.size) + [e for bore in part.bores for e in bore]
    while formulas:
        for name in re.findall(r"\b[A-Za-z_]\w*\b", formulas.pop()):
            if name not in names and (name in model.PARAMETERS or name in model.DERIVED):
                names.add(name)
                if name in model.DERIVED:
                    formulas.append(model.DERIVED[name])
    after_parameters = parameter_snapshot(design)
    rows.append("User parameters: (expression, API internal value in cm; yaw unitless).")
    for name in sorted(names):
        rows.append(f"{PREFIX+name}: before={before_parameters.get(name)!r}; "
                    f"after={after_parameters.get(name)!r}; model mm={values[name]!r}")
    add("Component model parameters (name, expression, internal value, declared unit)",
        lambda: [(p.name, p.expression, p.value, p.unit) for p in component.modelParameters])
    for sketch in component.sketches:
        add(sketch.name+" health/message/fullyConstrained",
            lambda: (sketch.healthState, sketch.errorOrWarningMessage, sketch.isFullyConstrained))
        add(sketch.name+" dimensions (type, expression, internal value, driving)",
            lambda: [(d.objectType, d.parameter.expression, d.parameter.value, d.isDriving)
                     for d in sketch.sketchDimensions])
        add(sketch.name+" linear dimension references (expression, orientation, component XYZ mm)",
            lambda: [(d.parameter.expression, diagnostic_read(lambda: d.orientation),
                      [diagnostic_read(lambda e=e: tuple(
                          getattr(sketch.sketchToModelSpace(getattr(d, e).geometry), axis)*10
                          for axis in "xyz")) for e in ("entityOne", "entityTwo")])
                     for d in sketch.sketchDimensions])
        add(sketch.name+" constraint types",
            lambda: [c.objectType for c in sketch.geometricConstraints])
        add(sketch.name+" line endpoints in component XYZ mm",
            lambda: [tuple(tuple(getattr(sketch.sketchToModelSpace(p.geometry), axis)*10
                                 for axis in "xyz")
                           for p in (line.startSketchPoint, line.endSketchPoint))
                     for line in sketch.sketchCurves.sketchLines])
    for feature in component.features.extrudeFeatures:
        add(feature.name+" health/message/suppressed",
            lambda: (feature.healthState, feature.errorOrWarningMessage, feature.isSuppressed))
    return "\n".join(rows)


def require_close(actual, expected, label, tolerance=0.001):
    if not math.isfinite(actual) or abs(actual-expected) > tolerance:
        raise ValueError(f"{label}: actual={actual!r}, expected={expected!r}")


def require_healthy(item):
    # Healthy is enum value zero: truthiness would invert the acceptance test.
    if not item.isValid or item.healthState != adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:
        raise ValueError(f"Required history unhealthy/invalid: {item.name}")


def named_items(collection, names, label):
    items = {item.name: item for item in collection}
    if collection.count != len(names) or set(items) != set(names):
        raise ValueError("Required history missing, duplicated or altered: " + label)
    for item in items.values():
        require_healthy(item)
    return items


def normalized_expression(text):
    return re.sub(r"\s+", "", text)


def expression_key(text):
    """Keep symbolic drivers strict; compare unit-qualified literals exactly in mm."""
    text = normalized_expression(text)
    literal = re.fullmatch(r"([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)(mm|cm|m|in|ft)", text)
    if literal:
        scales = {"mm": Fraction(1), "cm": Fraction(10), "m": Fraction(1000),
                  "in": Fraction(127, 5), "ft": Fraction(1524, 5)}
        return ("literal_mm", Fraction(literal[1])*scales[literal[2]])
    return ("expression", text)


def same_native_entity(actual, expected):
    """Compare Fusion entities in the same native context, never by name/geometry/token."""
    if actual is None or expected is None or not actual.isValid or not expected.isValid:
        return False
    actual = actual.nativeObject or actual
    expected = expected.nativeObject or expected
    return actual.isValid and expected.isValid and actual == expected


def check_dimensions(sketch, formulas):
    dims = list(sketch.sketchDimensions)
    if (len(dims) != len(formulas) or any(not d.isDriving for d in dims)
            or sorted(expression_key(d.parameter.expression) for d in dims)
            != sorted(expression_key(expression(f)) for f in formulas)):
        raise ValueError("Required driving dimensions altered: " + sketch.name)


def datum_diagnostics(component, datum, part, values):
    """Bounded read-only evidence for the three original Z-datum predicates."""
    offset = adsk.fusion.ConstructionPlaneOffsetDefinition.cast(datum.definition)
    expected = component.xYConstructionPlane
    actual = offset.planarEntity if offset else None
    typed = adsk.fusion.ConstructionPlane.cast(actual) if actual else None
    def describe(entity):
        return {"python_type": type(entity).__name__,
                "object_type": diagnostic_read(lambda: entity.objectType),
                "valid": diagnostic_read(lambda: entity.isValid),
                "name": diagnostic_read(lambda: entity.name),
                "is_deletable": diagnostic_read(lambda: entity.isDeletable),
                "component_id": diagnostic_read(lambda: entity.component.id),
                "assembly_context": diagnostic_read(lambda: entity.assemblyContext.fullPathName if entity.assemblyContext else None),
                "has_native_object": diagnostic_read(lambda: entity.nativeObject is not None),
                "origin_cm": diagnostic_read(lambda: entity.geometry.origin.asArray()),
                "normal": diagnostic_read(lambda: entity.geometry.normal.asArray())}
    return {"definition_type": diagnostic_read(lambda: datum.definition.objectType),
            "offset_cast": bool(offset), "raw_reference": describe(actual),
            "typed_reference": describe(typed), "expected_reference": describe(expected),
            "raw_reference_equal": diagnostic_read(lambda: actual == expected),
            "raw_reference_not_equal": diagnostic_read(lambda: actual != expected),
            "typed_reference_equal": diagnostic_read(lambda: typed == expected),
            "native_reference_equal": diagnostic_read(lambda: (actual.nativeObject or actual) == (expected.nativeObject or expected)),
            "sketch_reference_equal": diagnostic_read(lambda: component.sketches.item(0).referencePlane == datum),
            "native_sketch_reference_equal": diagnostic_read(lambda: (component.sketches.item(0).referencePlane.nativeObject or component.sketches.item(0).referencePlane) == (datum.nativeObject or datum)),
            "actual_expression": diagnostic_read(lambda: offset.offset.expression),
            "expected_expression": expression(part.xyz[2]),
            "raw_expression_equal": diagnostic_read(lambda: normalized_expression(offset.offset.expression)
                                                  == normalized_expression(expression(part.xyz[2]))),
            "equivalent_expression": diagnostic_read(lambda: expression_key(offset.offset.expression) == expression_key(expression(part.xyz[2]))),
            "actual_offset_cm": diagnostic_read(lambda: offset.offset.value),
            "expected_offset_cm": model.evaluate(part.xyz[2], values)/10,
            "datum": describe(datum), "health": diagnostic_read(lambda: datum.healthState),
            "health_message": diagnostic_read(lambda: datum.errorOrWarningMessage)}


def check_history(component, part, values):
    """Fail closed on missing API evidence; never roll back or repair the timeline."""
    footprint_name = part.name+"_footprint"
    hole_names = [f"Common_mount_hole_{i}_NOT_fastener_selection" for i in range(1, len(part.bores)+1)]
    sketches = named_items(component.sketches, [footprint_name]+hole_names, part.name+" sketches")
    planes = named_items(component.constructionPlanes, [part.name+"_Z_datum"], part.name+" datum")
    datum = planes[part.name+"_Z_datum"]
    offset = adsk.fusion.ConstructionPlaneOffsetDefinition.cast(datum.definition)
    if (not offset or not same_native_entity(offset.planarEntity, component.xYConstructionPlane)
            or expression_key(offset.offset.expression) != expression_key(expression(part.xyz[2]))):
        raise ValueError("Required Z datum altered: " + part.name + "\nZ datum diagnostics: "
                         + json.dumps(datum_diagnostics(component, datum, part, values), sort_keys=True))
    try:
        require_close(offset.offset.value*10, model.evaluate(part.xyz[2], values), part.name+" Z datum")
    except ValueError as exc:
        raise ValueError(str(exc)+"\nZ datum diagnostics: "
                         + json.dumps(datum_diagnostics(component, datum, part, values), sort_keys=True)) from exc
    feature_names = [part.name+"_thickness"] + [f"Common_mount_bore_{i}" for i in range(1, len(part.bores)+1)]
    features = named_items(component.features.extrudeFeatures, feature_names, part.name+" extrusions")
    if component.features.count != len(feature_names):
        raise ValueError("Unexpected modeling features: " + part.name)
    for sketch in sketches.values():
        if (not sketch.isFullyConstrained or sketch.profiles.count != 1
                or not same_native_entity(sketch.referencePlane, datum)):
            raise ValueError("Required sketch underconstrained or profile altered: " + sketch.name)
    footprint = sketches[footprint_name]
    lo, _ = part.bounds(values)
    check_dimensions(footprint, (() if lo[0] == 0 and lo[1] == 0 else part.xyz[:2])+part.size[:2])
    orientations = [c.objectType for c in footprint.geometricConstraints]
    if (orientations.count(adsk.fusion.HorizontalConstraint.classType()) != 2
            or orientations.count(adsk.fusion.VerticalConstraint.classType()) != 2
            or footprint.sketchCurves.sketchLines.count != 4):
        raise ValueError("Required rectangle orientations altered: " + footprint_name)
    for hole_name, bore in zip(hole_names, part.bores):
        check_dimensions(sketches[hole_name], bore)
        if sketches[hole_name].sketchCurves.sketchCircles.count != 1:
            raise ValueError("Required bore circle altered: " + hole_name)
    for name, sketch_name in zip(feature_names, [footprint_name]+hole_names):
        feature = features[name]
        operation = (adsk.fusion.FeatureOperations.NewBodyFeatureOperation if name == feature_names[0]
                     else adsk.fusion.FeatureOperations.CutFeatureOperation)
        extent = adsk.fusion.DistanceExtentDefinition.cast(feature.extentOne)
        profile = adsk.fusion.Profile.cast(feature.profile)
        if (not feature.isParametric or feature.isSuppressed or not feature.isSolid
                or feature.operation != operation or feature.hasTwoExtents or feature.isThinExtrude
                or not adsk.fusion.ProfilePlaneStartDefinition.cast(feature.startExtent)
                or not extent or not profile or not same_native_entity(profile.parentSketch, sketches[sketch_name])
                or expression_key(extent.distance.expression) != expression_key(expression(part.size[2]))):
            raise ValueError("Required extrusion altered: " + name)
        require_close(extent.distance.value*10, model.evaluate(part.size[2], values), name+" depth")
        require_close(feature.taperAngleOne.value, 0, name+" taper", 1e-9)
    return sketches, features


def check_bores(component, part, values, sketches, features):
    """Inspect final native B-Rep and each cut, not merely seeded sketch circles."""
    if not part.bores:
        return []
    body = component.bRepBodies.item(0)
    cylinders = {face.tempId: face for face in body.faces if adsk.core.Cylinder.cast(face.geometry)}
    if len(cylinders) != len(part.bores):
        raise ValueError("Mount plate must have exactly four cylindrical bore faces")
    lo, hi = part.bounds(values)
    seen = set()
    measurements = []
    for index, bore in enumerate(part.bores, 1):
        label = f"Common_mount_bore_{index}"
        x, y, diameter = (model.evaluate(e, values) for e in bore)
        radius = diameter/2
        sketch = sketches[f"Common_mount_hole_{index}_NOT_fastener_selection"]
        circle = sketch.sketchCurves.sketchCircles.item(0)
        center = sketch.sketchToModelSpace(circle.centerSketchPoint.geometry)
        for axis, expected in zip("xyz", (x, y, lo[2])):
            require_close(getattr(center, axis)*10, expected, label+" sketch center "+axis)
        require_close(circle.radius*20, diameter, label+" sketch diameter")
        sides = features[label].sideFaces
        if sides.count != 1:
            raise ValueError("Bore cut must have one cylindrical side face: " + label)
        face = sides.item(0)
        if not same_native_entity(face.body, body) or face.tempId not in cylinders or face.tempId in seen or not face.isValid:
            raise ValueError("Bore cut does not identify a distinct final plate face: " + label)
        seen.add(face.tempId)
        cylinder = adsk.core.Cylinder.cast(face.geometry)
        if not cylinder:
            raise ValueError("Bore cut is not cylindrical: " + label)
        for axis, expected in zip("xy", (x, y)):
            require_close(getattr(cylinder.origin, axis)*10, expected, label+" cut center "+axis)
        require_close(cylinder.radius*20, diameter, label+" cut diameter")
        for axis, expected in zip("xyz", (0, 0, 1)):
            require_close(abs(getattr(cylinder.axis, axis)), expected, label+" cut axis "+axis, 1e-9)
        rims = [adsk.core.Circle3D.cast(edge.geometry) for edge in face.edges]
        rims = [rim for rim in rims if rim]
        if len(rims) != 2:
            raise ValueError("Bore cut must have two complete circular rims: " + label)
        rims.sort(key=lambda rim: rim.center.z)
        for rim, z in zip(rims, (lo[2], hi[2])):
            for axis, expected in zip("xyz", (x, y, z)):
                require_close(getattr(rim.center, axis)*10, expected, label+" rim "+axis)
            require_close(rim.radius*20, diameter, label+" rim diameter")
        require_close(face.area*100, 2*math.pi*radius*(hi[2]-lo[2]), label+" cylindrical area",
                      max(0.001, 2*math.pi*radius*(hi[2]-lo[2])*1e-6))
        measurements.append({"feature": label, "center_xy_mm": [cylinder.origin.x*10, cylinder.origin.y*10],
                             "diameter_mm": cylinder.radius*20,
                             "rim_z_mm": [rim.center.z*10 for rim in rims], "area_mm2": face.area*100})
    return measurements


def report_provenance(design):
    """No document titles, account IDs or machine paths in provenance."""
    def optional(reader):
        try:
            return reader()
        except Exception:
            return "unknown"
    def document_id():
        identifier = design.parentDocument.creationId
        return hashlib.sha256(identifier.encode("utf-8")).hexdigest() if identifier else "unknown"
    return {"schema": 1, "run_id": str(uuid.uuid4()), "utc": datetime.now(timezone.utc).isoformat(),
            "fusion_version": optional(lambda: adsk.core.Application.get().version),
            "os": platform.system(), "os_version": platform.mac_ver()[0] or platform.release(),
            "document_creation_id_sha256": optional(document_id),
            "source_sha256": {name: optional(lambda name=name: hashlib.sha256(
                Path(__file__).with_name(name).read_bytes()).hexdigest()) for name in
                ("TesseractDockingFixture.py", "fixture_model.py")}}


def check_design(design, diagnostics=None):
    root = design.rootComponent
    tag = root.attributes.itemByName(GROUP, "cartridge")
    anchor = root.attributes.itemByName(GROUP, "anchor")
    if not tag or not anchor:
        raise ValueError("Active document is not a generated Phase 1C fixture")
    inputs = {}
    for name in model.PARAMETERS:
        parameter = design.userParameters.itemByName(PREFIX+name)
        if not parameter:
            raise ValueError("Missing parameter: " + name)
        inputs[name] = parameter.value if name == "float_yaw_deg" else parameter.value*10
    values = model.parameters(inputs)
    expected = model.parts(tag.value, anchor.value)
    model.validate_geometry(values, expected)
    if model.sweep_collisions(tag.value, anchor.value, inputs):
        raise ValueError("Nominal release sweep intersects modeled solids")
    before_parameters = parameter_snapshot(design)
    before_bounds = {}
    for occurrence in root.occurrences:
        part_tag = occurrence.component.attributes.itemByName(GROUP, "part")
        if part_tag:
            before_bounds[part_tag.value] = diagnostic_read(
                lambda: bounds_mm(occurrence.component.bRepBodies.item(0).boundingBox))
    recomputed = design.computeAll()
    if diagnostics is not None:
        # Snapshot every expected component before the first geometry rejection.
        # These optional reads neither repair geometry nor decide acceptance.
        by_name = {part.name: part for part in expected}
        for occurrence in root.occurrences:
            part_tag = occurrence.component.attributes.itemByName(GROUP, "part")
            if part_tag and part_tag.value in by_name:
                part = by_name[part_tag.value]
                diagnostics.append(diagnostic_read(lambda: bounds_report(
                    part.name, bounds_mm(occurrence.component.bRepBodies.item(0).boundingBox),
                    part.bounds(values))))
                diagnostics.append(diagnostic_read(lambda: part_diagnostics(
                    design, occurrence, part, values, before_bounds.get(part.name),
                    before_parameters, recomputed)))
    if not recomputed:
        raise RuntimeError("Fusion recompute failed")
    found = {}
    for occurrence in root.occurrences:
        part_tag = occurrence.component.attributes.itemByName(GROUP, "part")
        if not part_tag:
            raise ValueError("Untagged component is outside this check's geometry scope")
        if part_tag:
            identity = adsk.core.Matrix3D.create().asArray()
            if any(abs(a-b) > 1e-9 for a, b in zip(occurrence.transform2.asArray(), identity)):
                raise ValueError("Component was moved outside parameter control: " + part_tag.value)
            if part_tag.value in found:
                raise ValueError("Duplicate generated component: " + part_tag.value)
            found[part_tag.value] = occurrence
    if root.bRepBodies.count:
        raise ValueError("Root-level added bodies are outside the generated geometry scope")
    if set(found) != {part.name for part in expected}:
        raise ValueError("Generated component set differs from the source specification")
    carrier_report = ""
    mounting = []
    for part in expected:
        occurrence = found[part.name]
        component = occurrence.component
        if component.occurrences.count:
            raise ValueError("Nested added components are outside the generated geometry scope")
        if component.bRepBodies.count != 1 or not component.bRepBodies.item(0).isSolid:
            raise ValueError("Expected one solid: " + part.name)
        body = component.bRepBodies.item(0)
        actual = bounds_mm(body.boundingBox)
        wanted = part.bounds(values)
        mismatch = any(abs(a-b) > 0.001 for va, vb in zip(actual, wanted) for a, b in zip(va, vb))
        if mismatch or part.name == "Fixed_cold_carrier":
            report = bounds_report(part.name, actual, wanted)+"\n"+diagnostic_read(lambda: part_diagnostics(
                design, occurrence, part, values,
                before_bounds.get(part.name), before_parameters, recomputed))
            if mismatch:
                raise ValueError("Body bounds disagree with parameters: " + part.name+"\n"+report)
            carrier_report = "\n\nFixed-carrier diagnostic (not a separate acceptance):\n"+report
        volume = math.prod(b-a for a, b in zip(*wanted))
        for _, _, diameter in part.bores:
            volume -= math.pi*(model.evaluate(diameter, values)/2)**2*model.evaluate(part.size[2], values)
        if abs(body.volume*1000-volume) > max(0.001, volume*1e-6):
            raise ValueError("Body volume disagrees with primitive/bores: " + part.name)
        sketches, features = check_history(component, part, values)
        mounting.extend(check_bores(component, part, values, sketches, features))
    return (f"Checked {len(expected)} named solids/reservations against parameters.\n"
            "Bounds, volume, required history and bore cuts agree; nominal box release sweep has no penetrations.\n"
            + "Mounting B-Rep measurements: " + json.dumps(mounting, sort_keys=True) + "\n"
            + "Not a contact simulation, full interference certification or physical validation."
            + carrier_report)


def check_report(design):
    """Persist the full CHECK result; return only a short UI summary and path."""
    diagnostics = []
    # macOS/Linux reports go to the requested /tmp, not macOS's per-user temp
    # directory. Preserve Windows support using its native temporary directory.
    directory = None if sys.platform == "win32" else "/tmp"
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", prefix="tesseract-phase1c-check-",
                                     suffix=".txt", dir=directory, delete=False) as report:
        report.write("Project Tesseract Phase 1C CHECK diagnostics\n")
        report.write("Provenance: " + json.dumps(report_provenance(design), sort_keys=True) + "\n")
        report.write("User parameters before CHECK: " +
                     str(diagnostic_read(lambda: parameter_snapshot(design))) + "\n\n")
        try:
            if not design:
                raise ValueError("Activate a generated Fusion design first")
            result = check_design(design, diagnostics)
            summary = "CHECK PASSED: " + result.splitlines()[0]
            report.write("CHECK PASSED\n" + result + "\n")
        except Exception as error:
            summary = "CHECK FAILED: " + str(error).split("\n", 1)[0]
            report.write("CHECK FAILED\n" + traceback.format_exc())
        report.write("\n\nComplete component diagnostics:\n" + "\n\n".join(diagnostics))
        path = report.name
    return summary + "\nDiagnostics: " + path


def run(context):
    ui = None
    document = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        choice, cancelled = ui.inputBox(
            "Enter A,center / A,inset / B,center / B,inset to create a NEW unsaved concept.\n"
            "Enter CHECK to inspect the active generated design after parameter edits.\n"
            "Cold desk concept only; no physical-test approval.", "Tesseract Phase 1C", "B,inset")
        if cancelled:
            return
        if choice.strip().upper() == "CHECK":
            design = adsk.fusion.Design.cast(app.activeProduct)
            try:
                message = check_report(design)
            except OSError as error:
                message = "CHECK diagnostic file could not be written: " + str(error)
            ui.messageBox(message, "Phase 1C CAD check")
            return
        cartridge, anchor = (word.strip() for word in choice.split(","))
        cartridge, anchor = cartridge.upper(), anchor.lower()
        items = model.parts(cartridge, anchor)
        values = model.parameters()
        model.validate_geometry(values, items)
        if model.sweep_collisions(cartridge, anchor):
            raise ValueError("Release envelope failed before document creation")
        document = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        document.name = f"Tesseract Phase1C {cartridge} {anchor} COLD CONCEPT"
        design = adsk.fusion.Design.cast(document.products.itemByProductType("DesignProductType"))
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        for name, (default, low, high, description) in model.PARAMETERS.items():
            units = "" if name == "float_yaw_deg" else "mm"
            design.userParameters.add(PREFIX+name,
                adsk.core.ValueInput.createByString(str(default)+(" mm" if units else "")), units,
                f"{description}; supported range {low}..{high}. Run CHECK after edits.")
        for name, formula in model.DERIVED.items():
            design.userParameters.add(PREFIX+name, value(formula), "mm", "Derived; do not override")
        root = design.rootComponent
        root.attributes.add(GROUP, "cartridge", cartridge)
        root.attributes.add(GROUP, "anchor", anchor)
        for part in items:
            create_part(root, part, values)
        result = check_design(design)
        app.activeViewport.fit()
        ui.messageBox(result+"\nNew design is unsaved. Follow docs/phase1c/verification.md.",
                      "Phase 1C concept generated")
    except Exception:
        message = "Phase 1C generation/check failed:\n"+traceback.format_exc()
        if document:
            message += "\nNew document may be incomplete; inspect then close without saving."
        if ui:
            ui.messageBox(message, "Phase 1C error")
        else:
            raise
