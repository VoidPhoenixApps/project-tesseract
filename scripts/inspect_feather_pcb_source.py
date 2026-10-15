#!/usr/bin/env python3
"""Summarize two pinned Feather PCB sources from stdin; no network/file writes.

This extracts source facts, not tolerances, solid geometry or physical evidence.
Only the reviewed source hashes are accepted. Do not feed unapproved CAD assets.
"""
import hashlib
import json
import sys
import xml.etree.ElementTree as ET

SOURCES = {
    'ed5eff88e1ab8f1cc5ae8db1a1188c1932a65c35a5df9f06b8910f73ff65b0d7': 'Original',
    '8ed4623de172bab6f33e27ac1675b28ac32fe68f8a6caf89c444167db343dda2': 'Later',
}


def summarize(data):
    digest = hashlib.sha256(data).hexdigest()
    if digest not in SOURCES:
        raise ValueError('Unreviewed source hash; do not infer revision equivalence')
    board = ET.fromstring(data).find('./drawing/board')
    elements = {e.get('name'): e for e in board.findall('./elements/element')}
    result = {'source': SOURCES[digest], 'sha256': digest, 'units': 'mm',
              'plain_holes': [dict(h.attrib) for h in board.findall('./plain/hole')],
              'mounting_pads': [], 'components': {}}
    for name in ('U$31', 'U$32', 'X1', 'X6', 'CONN1', 'SW1', 'SW2', 'SW3'):
        if name not in elements:
            continue
        e = elements[name]
        package = board.find("./libraries/library[@name='%s']/packages/package[@name='%s']" %
                             (e.get('library'), e.get('package')))
        item = {k: e.get(k) for k in ('name', 'package', 'x', 'y', 'rot')}
        if name in ('U$31', 'U$32'):
            item['pads'] = [dict(p.attrib) for p in package.findall('pad')]
            result['mounting_pads'].append(item)
        else:
            result['components'][name] = item
        if name == 'X6':
            # Compare transformed USB mounting-pad centers; R270 maps (x,y) to (y,-x).
            if e.get('rot') != 'R270':
                raise ValueError('Unexpected USB rotation')
            item['board_pad_centers_mm'] = {
                p.get('name'): [round(float(e.get('x')) + float(p.get('y')), 6),
                                round(float(e.get('y')) - float(p.get('x')), 6)]
                for p in package.findall('pad')}
    return result


if __name__ == '__main__':
    try:
        print(json.dumps(summarize(sys.stdin.buffer.read()), indent=2))
    except (ValueError, ET.ParseError) as exc:
        sys.exit(str(exc))
