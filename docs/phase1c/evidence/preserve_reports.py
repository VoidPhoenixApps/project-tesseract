"""Extract retained observations, never regenerate measurements. Standard library only.

Usage: python preserve_reports.py INPUT_DIRECTORY OUTPUT_JSON_GZ
Only archived report IDs are accepted, avoiding accidental inclusion of test doubles.
"""
import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path
import re

REPORT_IDS = """sdagtrxu 5_4b7dhl g01ccjx0 041lzbqg xzxem_9s by48kx2v b_834fp4
c8bl8bzi ktzo4_2p 493onqe6 xs753e5c 4s22_vxj m5w5komd 4lxhb_3v 6suhxuzl krnw8b8w
flqonjex lntp606d rlgahkc_ h1or_1v8 6ms7rolq nu6ojds0 oe73bpp7 ukhsf0as 13jlczwi
8_3_xzwm qb3wy0p3 _nfqa89y 99_zv4yv mmm883gw b8y4p1hz uwuq5tzb _hq6gs8v xhotdiee
3nb7l73f mm0alj_4""".split()


def extract(directory):
    bundle = {"schema": 1, "attribution": "Maintainer-run Fusion observations; agent extraction, not live rerun",
              "source_attribution": "See README.md; source hashes were not embedded in historical reports",
              "fusion_version": "unknown", "os_version": "unknown", "document_ids": "unknown",
              "run_timestamps": "unknown; file modification times are not execution timestamps",
              "reports": {}, "component_observations": {}}
    for report_id in REPORT_IDS:
        path = directory / ("tesseract-phase1c-check-"+report_id+".txt")
        if not path.exists():
            bundle["reports"][report_id] = {"availability": "missing"}
            continue
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        parameters = next(line.split(": ", 1)[1] for line in text.splitlines()
                          if line.startswith("User parameters before CHECK: "))
        report = {"original_sha256": hashlib.sha256(raw).hexdigest(), "original_bytes": len(raw),
                  "outcome": "PASS" if "\nCHECK PASSED\n" in text else "FAIL",
                  "parameters_expression_and_internal_value": ast.literal_eval(parameters),
                  "errors": re.findall(r"^(?:ValueError|RuntimeError): .+$", text, re.M),
                  "components": {}}
        # Whitelist retained fields. No paths, tracebacks, identities or free-form headers.
        sections = text.split("Complete component diagnostics:\n", 1)
        if len(sections) == 2:
            for block in re.split(r"(?=^Part: )", sections[1], flags=re.M):
                if not block.startswith("Part: "):
                    continue
                lines = block.strip().splitlines()
                name = lines[0].split(";", 1)[0][6:]
                observation = [line for line in lines if line.startswith((
                    "Part:", "Actual min=", "Expected min=", "Delta min", "Actual dimensions",
                    "computeAll returned=", "Timeline marker/count=", "Occurrence transform2",
                    "Source lower XYZ=", "Component model parameters")) or any(marker in line for marker in (
                    " health/message/fullyConstrained=", " health/message/suppressed=",
                    " dimensions (type, expression, internal value, driving)=", " constraint types="))]
                # Retain actual vertices and dimension references for the failed trapezoid.
                if report_id == "mm0alj_4":
                    observation += [line for line in lines if "line endpoints in component XYZ mm=" in line
                                    or "linear dimension references" in line]
                if any("/Users/" in line or "C:\\Users\\" in line for line in observation):
                    raise ValueError("Private path in selected evidence")
                digest = hashlib.sha256(json.dumps(observation, ensure_ascii=True).encode()).hexdigest()
                bundle["component_observations"][digest] = observation
                report["components"][name] = digest
        bundle["reports"][report_id] = report
    return bundle


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = (json.dumps(extract(args.input), indent=2, sort_keys=True)+"\n").encode("utf-8")
    args.output.write_bytes(gzip.compress(payload, mtime=0))
