"""Generate/check a cold Phase 1C concept inside Fusion. No save/export or motion."""

import importlib.util
import math
from pathlib import Path
import re
import sys
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
    dim = sketch.sketchDimensions.addDistanceDimension(first, second, orientation, position, True)
    if not dim:
        raise RuntimeError("Cannot create driving dimension: " + text)
    dim.parameter.expression = expression(text)


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
    lo, hi = part.bounds(values)
    first = (sketch.originPoint if lo[0] == 0 and lo[1] == 0 else
             adsk.core.Point3D.create(lo[0]/10, lo[1]/10, 0))
    lines = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        first, adsk.core.Point3D.create(hi[0]/10, hi[1]/10, 0))
    if not lines or lines.count != 4:
        raise RuntimeError("Rectangle failed: " + part.name)
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
    extrude(component, sketch.profiles.item(0), part.size[2],
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation, part.name+"_thickness")
    if part.bores:
        holes = component.sketches.add(plane)
        holes.name = "Common_mount_pattern_NOT_fastener_selection"
        for x, y, diameter in part.bores:
            cx, cy = model.evaluate(x, values)/10, model.evaluate(y, values)/10
            circle = holes.sketchCurves.sketchCircles.addByCenterRadius(
                adsk.core.Point3D.create(cx, cy, 0), model.evaluate(diameter, values)/20)
            locate(holes, circle.centerSketchPoint, x, y, values)
            dim = holes.sketchDimensions.addDiameterDimension(
                circle, adsk.core.Point3D.create(cx+1, cy+1, 0), True)
            dim.parameter.expression = expression(diameter)
        profiles = adsk.core.ObjectCollection.create()
        for profile in holes.profiles:
            profiles.add(profile)
        if profiles.count != len(part.bores):
            raise RuntimeError("Mount-hole profiles failed")
        extrude(component, profiles, part.size[2],
                adsk.fusion.FeatureOperations.CutFeatureOperation, "Common_mount_bores")
        holes.isVisible = False
    if component.bRepBodies.count != 1:
        raise RuntimeError("Expected one body per component: " + part.name)
    component.bRepBodies.item(0).name = part.name
    sketch.isVisible = False
    plane.isVisible = False
    occurrence.isLightBulbOn = part.role != "reservation"


def check_design(design):
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
    if not design.computeAll():
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
            found[part_tag.value] = occurrence.component
    if root.bRepBodies.count:
        raise ValueError("Root-level added bodies are outside the generated geometry scope")
    if set(found) != {part.name for part in expected}:
        raise ValueError("Generated component set differs from the source specification")
    for part in expected:
        component = found[part.name]
        if component.occurrences.count:
            raise ValueError("Nested added components are outside the generated geometry scope")
        if component.bRepBodies.count != 1 or not component.bRepBodies.item(0).isSolid:
            raise ValueError("Expected one solid: " + part.name)
        body = component.bRepBodies.item(0)
        bounds = body.boundingBox
        actual = ((bounds.minPoint.x*10, bounds.minPoint.y*10, bounds.minPoint.z*10),
                  (bounds.maxPoint.x*10, bounds.maxPoint.y*10, bounds.maxPoint.z*10))
        wanted = part.bounds(values)
        if any(abs(a-b) > 0.001 for va, vb in zip(actual, wanted) for a, b in zip(va, vb)):
            raise ValueError("Body bounds disagree with parameters: " + part.name)
        volume = math.prod(b-a for a, b in zip(*wanted))
        for _, _, diameter in part.bores:
            volume -= math.pi*(model.evaluate(diameter, values)/2)**2*model.evaluate(part.size[2], values)
        if abs(body.volume*1000-volume) > max(0.001, volume*1e-6):
            raise ValueError("Body volume disagrees with primitive/bores: " + part.name)
    return (f"Checked {len(expected)} named solids/reservations against parameters.\n"
            "Bounds and volume agree; nominal box release sweep has no penetrations.\n"
            "Not a contact simulation, full interference certification or physical validation.")


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
            if not design:
                raise ValueError("Activate a generated Fusion design first")
            ui.messageBox(check_design(design), "Phase 1C CAD check")
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
