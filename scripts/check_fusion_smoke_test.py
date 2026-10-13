"""Check the Fusion source package without importing or simulating Fusion."""

import ast
import json
from pathlib import Path
import uuid


def main():
    folder = Path(__file__).resolve().parents[1] / "cad/fusion/TesseractSmokeTest"
    name = folder.name
    source_path = folder / (name + ".py")
    source = source_path.read_text(encoding="utf-8")
    compile(source, str(source_path), "exec")  # No execution or bytecode writes.
    tree = ast.parse(source)
    entry_points = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                    and node.name == "run" and len(node.args.args) == 1]
    if len(entry_points) != 1:
        raise ValueError("Expected one Fusion run(context) entry point")
    manifest = json.loads((folder / (name + ".manifest")).read_text(encoding="utf-8"))
    expected = {"autodeskProduct": "Fusion360", "type": "script",
                "supportedOS": "windows", "runOnStartup": False, "editEnabled": True}
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise ValueError("Unexpected manifest value: " + key)
    uuid.UUID(manifest["id"])
    if not manifest.get("description", {}).get("") or not manifest.get("version"):
        raise ValueError("Missing manifest description or version")
    print("PASS: Python compilation, entry point, matching filenames, manifest metadata")
    print("Fusion execution, geometry and parametric editability: NOT VERIFIED")


if __name__ == "__main__":
    main()
