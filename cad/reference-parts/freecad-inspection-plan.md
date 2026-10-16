# Proposed independent Feather inspection — FreeCAD / OCCT

**Stage D, 2026-10-15. Not executed; no independent geometry verification claimed.** This refines [Stage C](stage-c-verification.md#freeopen-reproduction-path). It is a proposed measurement experiment, not a selected production CAD toolchain.

## Available environment and authority

Read-only discovery found Fusion in `~/Applications`; no FreeCAD app in `/Applications` or `~/Applications`, no `FreeCAD`, `FreeCADCmd`, `freecad` or `freecadcmd` on PATH, and no `FreeCAD`, `Part`, `OCP` or `OCC` importable by the active Python 3.9 environment. This is a bounded search, not proof none exists anywhere. Existing Python can reproduce approved asset hashes and STEP structural checks; it cannot replace a solid kernel. Nothing was installed or launched for a new import.

The [official FreeCAD Part import reference](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_Import.md) describes GUI import; its repository is now archived. For the proposed Python path, current [Part module API](https://github.com/FreeCAD/FreeCAD/blob/4a1904f8db57d4a31e44cdb1dd984d4c98447c10/src/Mod/Part/App/Part.module.pyi), [TopoShape API](https://github.com/FreeCAD/FreeCAD/blob/4a1904f8db57d4a31e44cdb1dd984d4c98447c10/src/Mod/Part/App/TopoShape.pyi) and [STEP import implementation](https://github.com/FreeCAD/FreeCAD/blob/4a1904f8db57d4a31e44cdb1dd984d4c98447c10/src/Mod/Part/App/TopoShape.cpp) were consulted through Context7. `Part.read` returns one shape; its STEP reader transfers roots then obtains `OneShape()`. The [OCCT STEP guide](https://occt3d.com/dev/doc/overview/html/occt_user_guides__step.html) distinguishes basic geometry/assembly transfer from XDE metadata, units and healing settings. These references do not establish behavior for a future installed binary.

## Procedure to execute after engine approval

1. Obtain explicit approval for an exact FreeCAD release/build and installation on the intended machine, or identify an already installed authorized binary. Record OS/architecture, executable path, FreeCAD build/commit, OCCT and Python versions from Help → About/build information. Keep macOS and Windows runs separate. Do not assume the latest source pin equals the installed release.
2. Use only the existing approved Feather file. Run the library validator below first; stop on missing bytes, hash mismatch or authorization/rights mismatch. Record the STEP header/schema, units and the native-frame evidence from [Stage B](stage-b-verification.md). Do not retrieve a replacement automatically.
3. Start a fresh FreeCAD process with no existing designs open. Record importer unit policy, precision/tolerance and shape-healing defaults from that build. The low-level `Part.read` path below is the baseline; GUI assembly/XDE import is a separate experiment because settings/object trees differ. Do not promise zero internal importer healing: log defaults/diagnostics and distinguish them from deliberate repair. Do not refine, fuse, scale, heal or export to force agreement.
4. Run the following proposed bootstrap in the FreeCAD Python console after setting the two local paths. It reads the approved STEP and prints numeric metadata only. It is not a full inspection macro and has **not been runtime tested here**. Use the applicable local paths on each OS; no network is involved.

```sh
python3 scripts/check_reference_parts.py --library '/Users/todd/Development Projects/tesseract-cad-library'
```

```python
from pathlib import Path
import hashlib
import json
import FreeCAD as App
import Part

repo = Path('/Users/todd/Development Projects/project-tesseract')
library = Path('/Users/todd/Development Projects/tesseract-cad-library')
catalog = json.loads((repo / 'cad/reference-parts/catalog.json').read_text())
part = next(p for p in catalog['parts'] if p['id'] == 'adafruit-4884-feather-rp2040')
if part['authorization']['status'] != 'approved' or any(
        part['permissions'][k]['status'] != 'allowed'
        for k in ('download', 'local_ai_processing')):
    raise RuntimeError('Inspection authorization/rights missing')
asset = part['local_asset']
source = (library / asset['path']).resolve(strict=True)
if library.resolve() not in source.parents:
    raise RuntimeError('Source escapes approved library')
before = hashlib.sha256(source.read_bytes()).hexdigest()
if before != asset['sha256']:
    raise RuntimeError('Source hash mismatch')
shape = Part.read(str(source))
if shape.isNull() or not shape.isValid():
    raise RuntimeError('Null/invalid import: preserve diagnostics, stop')

def bounds(s):
    b = s.BoundBox
    return [b.XMin, b.YMin, b.ZMin, b.XMax, b.YMax, b.ZMax]

print('FreeCAD', App.Version())
print('source_sha256', before, 'bounds_mm', bounds(shape))
print('solids', len(shape.Solids))
for index, solid in enumerate(shape.Solids, 1):
    print(index, solid.isValid(), bounds(solid), 'volume_mm3', solid.Volume)
if hashlib.sha256(source.read_bytes()).hexdigest() != before:
    raise RuntimeError('Source changed during inspection')
```

5. Enumerate **only the imported root's solids once**. Do not sum every document object's solids (parents can contain children). Repeated located occurrences are real occurrences: do not deduplicate merely by equal shape/volume. Record solid index, validity, bounds, volume and placement in the result. Do not reapply an occurrence transform to a shape already placed by the reader. Any difference from Fusion's 58 bodies needs an occurrence/topology explanation; 58 is a comparison target, not permission to discard extra geometry.
6. Identify the PCB from its thin rectangular geometry and hole pattern, then visually confirm it in a temporary document. Do not select by expected dimensions alone and silently ignore other candidates. Stop on ambiguous identity. Preserve the native root frame: PCB bottom Z=0; lower-left X=Y=0; +Z toward components; USB toward −X. Record any measured transform; do not rotate to conceal a mismatch. Only axis-aligned bounds in this confirmed frame establish the intended outline dimensions.
7. Inspect the PCB's four through mounting holes using analytical cylindrical faces/circular edges in the installed build's supported measurement tools. Record stable evidence for that run: solid/face/edge indices, surface type, axis direction, radius, center at the PCB plane and face extent. Split cylindrical faces sharing an axis/radius are one hole; connector holes/pads and PCB outline arcs are not mounting holes. Measure center-to-center X/Y differences, not edge gaps. If the importer converts surfaces to splines or geometry is ambiguous, mark that measurement unresolved rather than fit a cylinder without a separately reviewed method.
8. Compare raw numbers with the Stage B observations below and the pinned PCB source facts. Proposed numerical comparison threshold: **absolute difference ≤0.001 mm** per dimension/center coordinate, recorded to at least 0.000001 mm without rounding before comparison. This is an investigation threshold, **not manufacturing tolerance or physical measurement uncertainty**; it is intentionally much smaller than the 0.04 mm hole-pair difference. Review this threshold against importer tolerances before calling a comparison consistent; report deltas and settings even when within threshold. Invalid solids, unit ambiguity, import errors or unexplained transforms/count differences prevent an overall comparison conclusion.
9. Close without saving, terminate the process, repeat from an independent fresh import and rehash the original. Compare both OCCT runs and Fusion evidence. Two reads of one imported object do not establish repeat-import behavior. Retain numerical observations, warnings and failed measurements; no third-party geometry is exported or committed. Require review of the result before upgrading catalog confidence.

| Quantity | Stage B reference, mm unless count | Required distinction |
| --- | --- | --- |
| Solid count | 58 | Fusion occurrences/body grouping may differ; no forced count match |
| PCB X/Y/Z spans | 50.8 / 22.86 / 1.57 | Not the assembly envelope |
| Mount centers | X=2.54,48.26; Y=2.54,20.32 | Center rectangle 45.72 × 17.78; coordinates at board plane |
| Mount diameters | X=2.54 pair: 2.50; X=48.26 pair: 2.54 | Drill-source agreement does not establish finished hole sizes |
| Assembly X/Y/Z spans | 51.946 / 22.86 / 6.37 | Preserve minima/maxima too; USB projection matters |

## Evidence needed before a result can be claimed

Save only an original numerical report: source hash, engine/build/OCCT version, importer route/options, unit interpretation, diagnostics, per-solid/face measurements, datum mapping, expected/observed/delta table, comparison threshold, two-run comparison and unresolved items. Validate the report against the actual imported model and source drawing. A unit-display preference is not proof of STEP units: compare source declarations with import scale. Bounding-box algorithm tolerances can affect extrema, so investigate rather than relabel them physical deviations.

FreeCAD/OCCT comparison would be independent of Fusion's numerical import, not independent manufactured-part validation. It does not establish current-board correspondence, connector mating clearance, safe machine function or physical fit. A future native OCCT harness is optional; building/installing one is not authorized in Stage D.
