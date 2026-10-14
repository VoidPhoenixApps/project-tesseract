"""Preserve selected smoke observations; never run Fusion or alter original reports.

Usage: python3 preserve_smoke_reports.py /tmp OUTPUT_JSON
Fixed report IDs exclude synthetic tests. Private paths/tracebacks are not retained.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re

REPORT_IDS = 'g6m024s6 hs81n16e jkut1vep rdx62f8g fo9cf9la p62klz0r ynmp_nt4 py9umo0p 89146d90'.split()


def extract(directory):
    reports = {}
    for identifier in REPORT_IDS:
        raw = (directory / ('tesseract-phase1c-check-' + identifier + '.txt')).read_bytes()
        text = raw.decode('utf-8')
        lines = text.splitlines()
        provenance = json.loads(next(x[12:] for x in lines if x.startswith('Provenance: ')))
        selected = [x for x in lines if x.startswith(('Checked 59 named', 'Mounting B-Rep measurements:'))]
        # Retain the directly relevant history observations, including actual modified drivers.
        selected += list(dict.fromkeys(x for x in lines if
            x.startswith(('Fixed_cold_carrier_footprint health/',
                          'Fixed_cold_carrier_footprint constraint types=',
                          'Common_mount_hole_1_NOT_fastener_selection dimensions',
                          'Common_mount_bore_1 health/',
                          'Reinforcement_interface_2_NO_STOCK_SELECTED_thickness health/'))))
        report = {'original_sha256': hashlib.sha256(raw).hexdigest(),
                  'original_bytes': len(raw), 'provenance': provenance,
                  'outcome': 'PASS' if '\nCHECK PASSED\n' in text else 'FAIL',
                  'errors': re.findall(r'^(?:ValueError|RuntimeError): .+$', text, re.M),
                  'timeline_marker_count': sorted(set(re.findall(r'^Timeline marker/count=(.*)$', text, re.M))),
                  'parameters': ast.literal_eval(next(x.split(': ', 1)[1] for x in lines
                      if x.startswith('User parameters before CHECK: '))),
                  'selected_observations': selected}
        serialized = json.dumps(report)
        if any(x in serialized for x in ('/Users/', 'C:\\\\Users\\\\', 'Traceback (')):
            raise ValueError('Private information in selected evidence')
        reports[identifier] = report
    return {'schema': 1, 'attribution': 'Maintainer-run Fusion; agent inspected retained reports, no live rerun',
            'limits': 'Selected observations, not full raw reports. Source hashes identify files at CHECK time, not loaded bytecode or original generation. Hashed document IDs do not independently prove sequence continuity.',
            'identifier_discrepancy': 'User supplied rdx62f8q is unavailable; actual rdx62f8g records the matching altered mounting-hole expression rejection.',
            'reports': reports}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.write_text(json.dumps(extract(args.input), indent=2, sort_keys=True) + '\n')
