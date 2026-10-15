"""Read-only inspection of the authorized Feather STEP, run inside Fusion's Py console.

Open the pinned local STEP in a NEW unsaved document first. This script does not
import, save, export, transform or modify CAD. It prints numerical observations;
see cad/reference-parts/stage-b-verification.md for the invocation and limits.
"""
import json


def inspect():
    import adsk.core
    import adsk.fusion

    app = adsk.core.Application.get()
    doc = app.activeDocument
    if not doc or doc.isSaved or not doc.name.startswith('4884-feather-rp2040'):
        raise RuntimeError('Open only the authorized Feather STEP as a new unsaved document first.')
    design = adsk.fusion.Design.cast(app.activeProduct)
    if design is None:
        raise RuntimeError('Active product is not a Fusion design.')
    root = design.rootComponent

    def xyz(point):
        return [point.x * 10, point.y * 10, point.z * 10]

    def bounds(body):
        box = body.preciseBoundingBox
        lo, hi = xyz(box.minPoint), xyz(box.maxPoint)
        return {'min_mm': lo, 'max_mm': hi,
                'size_mm': [b - a for a, b in zip(lo, hi)]}

    bodies = [(root.name, b) for b in root.bRepBodies]
    occurrences = []
    for occurrence in root.allOccurrences:
        occurrences.append({'path': occurrence.fullPathName,
                            'transform_cm': occurrence.transform2.asArray(),
                            'body_count': occurrence.bRepBodies.count})
        bodies.extend((occurrence.fullPathName, b) for b in occurrence.bRepBodies)
    records = []
    for path, body in bodies:
        record = {'occurrence': path, 'body': body.name, 'is_solid': body.isSolid,
                  'face_count': body.faces.count, 'bounds': bounds(body)}
        # Capture cylindrical interfaces only for board-sized bodies. This is
        # a candidate filter, not an automatic identification of mounting holes.
        if max(record['bounds']['size_mm']) > 40:
            record['cylinders'] = []
            for face in body.faces:
                cylinder = adsk.core.Cylinder.cast(face.geometry)
                if cylinder:
                    record['cylinders'].append({
                        'diameter_mm': cylinder.radius * 20,
                        'origin_mm': xyz(cylinder.origin),
                        'axis': list(cylinder.axis.asArray())})
        records.append(record)
    if not records:
        raise RuntimeError('No BRep bodies found.')
    lo = [min(r['bounds']['min_mm'][i] for r in records) for i in range(3)]
    hi = [max(r['bounds']['max_mm'][i] for r in records) for i in range(3)]
    return {'app_version': app.version, 'document_name': doc.name,
            'document_is_saved': doc.isSaved,
            'display_length_units': design.unitsManager.defaultLengthUnits,
            'reported_length_units': 'mm', 'api_to_mm_factor': 10,
            'coordinate_frame': 'root assembly context; no transform applied by script',
            'body_count': len(records), 'solid_count': sum(r['is_solid'] for r in records),
            'assembly_bounds': {'min_mm': lo, 'max_mm': hi,
                                'size_mm': [b-a for a,b in zip(lo,hi)]},
            'occurrences': occurrences, 'bodies': records}


if __name__ == '__main__':
    print(json.dumps(inspect(), indent=2))
