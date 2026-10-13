"""Fusion-only parametric geometry smoke test; not a printer component."""

import traceback

import adsk.core
import adsk.fusion


PARAMETERS = (
    ("tesseract_length", "40 mm", "Block length along X"),
    ("tesseract_width", "30 mm", "Block width along Y"),
    ("tesseract_height", "10 mm", "Block height along positive Z"),
)


def run(context):
    """Create a separate unsaved design on every run; preserve open documents."""
    ui = None
    document = None
    try:
        app = adsk.core.Application.get()
        if not app:
            raise RuntimeError("Run this script from inside Autodesk Fusion.")
        ui = app.userInterface
        document = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        document.name = "Tesseract Smoke Test - Unvalidated"
        design = adsk.fusion.Design.cast(
            document.products.itemByProductType("DesignProductType")
        )
        if not design:
            raise RuntimeError("The new document does not contain a Fusion design.")
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType

        for name, expression, description in PARAMETERS:
            parameter = design.userParameters.add(
                name, adsk.core.ValueInput.createByString(expression), "mm", description
            )
            if not parameter:
                raise RuntimeError("Could not create user parameter: " + name)

        occurrence = design.rootComponent.occurrences.addNewComponent(
            adsk.core.Matrix3D.create()
        )
        component = occurrence.component
        component.name = "TesseractSmokeTest_Block"
        sketch = component.sketches.add(component.xYConstructionPlane)
        sketch.name = "TesseractSmokeTest_Footprint"

        # Fusion API coordinates and length parameter values are in centimeters.
        # Explicit mm expressions above avoid dependence on document display units.
        length_cm = design.userParameters.itemByName("tesseract_length").value
        width_cm = design.userParameters.itemByName("tesseract_width").value
        lines = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
            sketch.originPoint, adsk.core.Point3D.create(length_cm, width_cm, 0)
        )
        if not lines or lines.count != 4:
            raise RuntimeError("Could not create the rectangular footprint.")

        # Select edges by geometry rather than relying on API return ordering.
        horizontal = next(
            line for line in lines
            if abs(line.startSketchPoint.geometry.y - line.endSketchPoint.geometry.y)
            < 1e-9
        )
        vertical = next(
            line for line in lines
            if abs(line.startSketchPoint.geometry.x - line.endSketchPoint.geometry.x)
            < 1e-9
        )
        for edge, orientation, label_position, parameter_name in (
            (horizontal, adsk.fusion.DimensionOrientations.HorizontalDimensionOrientation,
             adsk.core.Point3D.create(length_cm / 2, -1, 0), "tesseract_length"),
            (vertical, adsk.fusion.DimensionOrientations.VerticalDimensionOrientation,
             adsk.core.Point3D.create(-1, width_cm / 2, 0), "tesseract_width"),
        ):
            dimension = sketch.sketchDimensions.addDistanceDimension(
                edge.startSketchPoint, edge.endSketchPoint,
                orientation, label_position, True
            )
            if not dimension:
                raise RuntimeError("Could not create driving dimension: " + parameter_name)
            dimension.parameter.expression = parameter_name

        if sketch.profiles.count != 1:
            raise RuntimeError("Expected exactly one closed rectangular profile.")
        extrudes = component.features.extrudeFeatures
        extrusion_input = extrudes.createInput(
            sketch.profiles.item(0), adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )
        extent = adsk.fusion.DistanceExtentDefinition.create(
            adsk.core.ValueInput.createByString("tesseract_height")
        )
        if not extrusion_input.setOneSideExtent(
            extent, adsk.fusion.ExtentDirections.PositiveExtentDirection
        ):
            raise RuntimeError("Could not set the parameter-driven extrusion extent.")
        extrusion = extrudes.add(extrusion_input)
        extrusion.name = "TesseractSmokeTest_Height"
        if extrusion.bodies.count != 1 or not extrusion.bodies.item(0).isSolid:
            raise RuntimeError("Expected exactly one solid body.")
        extrusion.bodies.item(0).name = "TesseractSmokeTest_Solid"
        sketch.isVisible = False
        app.activeViewport.fit()
        ui.messageBox(
            "Created a new unsaved parametric smoke-test design.\n"
            "Target dimensions: 40 x 30 x 10 mm (X x Y x Z).\n"
            "Verify with Inspect > Measure and Modify > Change Parameters.\n"
            "This is not an approved component or validated printer design.",
            "TesseractSmokeTest"
        )
    except Exception:
        detail = traceback.format_exc()
        message = "TesseractSmokeTest failed.\n"
        if document:
            message += (
                "The new unsaved test document may be incomplete. "
                "Inspect it, then close without saving before retrying.\n"
            )
        message += detail
        if ui:
            ui.messageBox(message, "TesseractSmokeTest error")
        else:
            raise
