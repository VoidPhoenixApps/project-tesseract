#!/usr/bin/env python3
"""Offline metadata triage; no downloads, CAD execution or permission changes."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

from check_reference_parts import CATALOG, SCHEMA, check_local, validate

REPORT = CATALOG.parent / 'READINESS.md'
PERMISSIONS = ('download', 'local_ai_processing', 'derivative_use',
               'public_redistribution', 'commercial_reuse')


def classify(part, library=None):
    permissions = {k: part['permissions'][k]['status'] for k in PERMISSIONS}
    local = part['local_asset']
    authorization = part['authorization']['status']
    rights_gaps = [k for k in PERMISSIONS if permissions[k] != 'allowed']
    if local:
        group = 'authorized-local-record'
    elif any(permissions[k] != 'allowed' for k in PERMISSIONS[:2]):
        group = 'resolve-inspection-rights'
    else:
        group = 'prepare-authorization-request'
    local_status = 'not-cataloged'
    errors = []
    if local:
        local_status = 'not-checked'
        if library is not None:
            try:
                errors, _ = check_local({'parts': [part]}, library)
                local_status = 'check-failed' if errors else 'hash-checked'
            except (OSError, ValueError) as exc:
                local_status = 'missing-or-unreadable'
                errors = [f'{type(exc).__name__}: {exc}']
    source = part['model_source_status']
    actions = []
    if source != 'listed':
        actions.append('Locate exact CAD' if source == 'not-located' else 'Resolve exact portal configuration')
    if rights_gaps:
        actions.append('Resolve rights by intended action: ' + ', '.join(rights_gaps))
    if authorization != 'approved':
        actions.append('Obtain explicit bounded maintainer authorization')
    if not local:
        actions.append('No cataloged local model; retain link-only until authorized')
    elif local_status != 'hash-checked':
        actions.append('Check approved local bytes/hash before reuse')
    actions.append('Review source/physical revision correspondence and geometry evidence before dependent CAD')
    return {
        'id': part['id'], 'manufacturer': part['manufacturer'],
        'part_number': part['part_number'], 'variant': part['variant'],
        'formats': part['formats'], 'availability': part['availability'],
        'provenance': part['provenance'], 'access_date': part['access_date'],
        'physical_revision': part['revision'], 'category': part['category'],
        'group': group, 'source_status': source, 'model_url': part['model_url'],
        'source_revision': part['source_revision'],
        'source_pin': 'commit-pinned' if re.fullmatch(r'[0-9a-f]{40}', part['source_revision']) else 'review-source-version',
        'permissions': permissions, 'permission_evidence': part['permissions'],
        'authorization': part['authorization'],
        'local_path': local['path'] if local else None,
        'local_status': local_status, 'local_errors': errors,
        'geometry_confidence': part['geometry']['confidence'],
        'geometry_evidence': part['geometry'], 'notes': part['notes'],
        'next_actions': actions,
    }


def select_parts(parts, ids=(), query=None):
    by_id = {p['id']: p for p in parts}
    missing = sorted(set(ids) - by_id.keys())
    selected = [p for p in parts if not ids or p['id'] in ids]
    if query:
        words = query.casefold().split()
        selected = [p for p in selected if all(w in ' '.join(str(p[k]) for k in
                    ('id', 'manufacturer', 'part_number', 'variant', 'revision')).casefold() for w in words)]
    return sorted(selected, key=lambda p: p['id']), missing


def report_data(parts, library=None):
    rows = [classify(p, library) for p in sorted(parts, key=lambda p: p['id'])]
    summary = {key: dict(sorted(Counter(r[key] for r in rows).items())) for key in
               ('group', 'source_status', 'source_pin', 'physical_revision', 'geometry_confidence', 'local_status')}
    summary['authorization'] = dict(sorted(Counter(r['authorization']['status'] for r in rows).items()))
    summary['permissions'] = {k: dict(sorted(Counter(r['permissions'][k] for r in rows).items())) for k in PERMISSIONS}
    return {'count': len(rows), 'summary': summary, 'records': rows}


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def render_report(data):
    lines = ['# CAD library readiness', '',
             'Generated offline from [catalog.json](catalog.json) by `python3 scripts/reference_parts_triage.py --write-report`.', '',
             'Metadata audit, not source availability polling or permission to act. Counts overlap across axes. '
             'A URL may be a landing page or unconfigured portal. Commit pins identify source bytes, not physical revisions. '
             'Named physical revisions also need correspondence review. No record establishes physical fit. '
             'Cloud upload and model training are outside the five permission fields and remain unauthorized.', '',
             '## Counts', '']
    for key, counts in data['summary'].items():
        lines.append(f'- {key}: `{json.dumps(counts, sort_keys=True)}`')
    lines += ['', '## Per-record gates', '',
              'D/A/U/P/C = download / local AI processing / derivative use / public redistribution / commercial reuse. '
              'A=allowed, C=conditional, U=unknown, P=prohibited. These are documented readings with evidence in the catalog. '
              'All nonlocal records remain link-only. Local `not-checked` means this generated report does not inspect the filesystem.', '',
              '| Catalog ID | Source | D/A/U/P/C | Authorization | Local | Physical revision | Geometry | Next group |',
              '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in data['records']:
        perms = '/'.join(r['permissions'][k][0].upper() for k in PERMISSIONS)
        lines.append('| ' + ' | '.join(map(cell, [r['id'], r['source_status'], perms,
                     r['authorization']['status'], r['local_status'], r['physical_revision'],
                     r['geometry_confidence'], r['group']])) + ' |')
    lines += ['', '## Source revision register', '',
              'Read exact notes and geometry checks with `--id CATALOG_ID --json`. '
              'The script does not infer a valid physical revision from a source commit or parse free text into engineering approval.', '',
              '| Catalog ID | Pin classification | Recorded source revision |', '| --- | --- | --- |']
    for r in data['records']:
        lines.append('| ' + ' | '.join(map(cell, [r['id'], r['source_pin'], r['source_revision']])) + ' |')
    return '\n'.join(lines) + '\n'


def render_requests(parts, missing, purpose, blocked):
    lines = ['# Consolidated model request — not authorization', '',
             'Review exact identity, rights evidence and intended scope before approval. '
             'Do not substitute or download automatically. Local assets may need only missing evidence, not another download.', '',
             '| Exact identity / revision | Format / source | Rights and authorization | Geometry purpose | Missing evidence / blocked work |',
             '| --- | --- | --- | --- | --- |']
    for p in parts:
        r = classify(p)
        identity = f"{p['manufacturer']} {p['part_number']} / {p['variant']} / physical revision {p['revision']}"
        source = ', '.join(p['formats']) or 'Format not established; request STEP plus matching native source if available'
        source += '; ' + (p['model_url'] or 'No exact model located; documentation: ' + p['documentation_url'])
        source += '; source revision: ' + p['source_revision']
        rights = '; '.join(f"{k}={v['status']} ({v['basis_url'] or 'no grant established'}; {v['note']})" for k,v in p['permissions'].items())
        rights += '; authorization=' + p['authorization']['status'] + '; ' + p['authorization']['scope']
        gaps = '; '.join(r['next_actions']) + '; ' + p['notes'] + '; blocked work: ' + blocked
        lines.append('| ' + ' | '.join(map(cell, [identity, source, rights, purpose, gaps])) + ' |')
    for identity in missing:
        lines.append('| ' + ' | '.join(map(cell, [identity + ' — no catalog match; confirm manufacturer/part/variant/revision',
                     'Request STEP/native source; source unknown', 'Rights and authorization unknown', purpose, blocked])) + ' |')
    return '\n'.join(lines) + '\n'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--id', action='append', default=[], help='Exact catalog ID; repeat for consolidated requests')
    parser.add_argument('--query', help='Case-insensitive identity keyword search; never an exact-part substitution')
    parser.add_argument('--library', type=Path, help='Read/hash cataloged local assets only')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--requests', action='store_true')
    parser.add_argument('--purpose', help='Intended geometry inspection purpose for selected records')
    parser.add_argument('--blocked-work', help='Actual dependent task; no invented design work')
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--write-report', action='store_true')
    modes.add_argument('--check-report', action='store_true')
    args = parser.parse_args(argv)
    if args.requests and (not args.id or not args.purpose or not args.blocked_work):
        parser.error('--requests requires --id, --purpose and --blocked-work')
    if args.requests and (args.json or args.query or args.library):
        parser.error('--requests cannot combine with --json, --query or --library')
    if (args.write_report or args.check_report) and (args.id or args.query or args.library or args.requests or args.json):
        parser.error('generated report uses the whole catalog without local checks or filters')
    try:
        catalog = json.loads(CATALOG.read_text())
        errors = validate(catalog, json.loads(SCHEMA.read_text()))
        if errors:
            raise ValueError('; '.join(errors))
        parts, missing = select_parts(catalog['parts'], args.id, args.query)
        if args.requests:
            print(render_requests(parts, missing, args.purpose, args.blocked_work), end='')
            return 0
        if missing or not parts:
            raise ValueError('No exact match: ' + ', '.join(missing or [args.query or 'empty selection']))
        data = report_data(parts, args.library)
        if args.write_report:
            REPORT.write_text(render_report(data))
        elif args.check_report:
            if REPORT.read_text() != render_report(data):
                raise ValueError('READINESS.md is stale; regenerate with --write-report')
            print('PASS: readiness report matches catalog')
        else:
            print(json.dumps(data, indent=2) if args.json else render_report(data), end='\n' if args.json else '')
        return 1 if any(r['local_errors'] for r in data['records']) else 0
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
