#!/usr/bin/env python3
"""Offline catalog/schema, publication guard and opt-in local sample checks.

No downloads, CAD execution or cloud uploads. Only --write-index writes a file.
Python standard library.
"""
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'cad/reference-parts/catalog.json'
SCHEMA = ROOT / 'cad/reference-parts/catalog.schema.json'
CATEGORIES = {'sbcs', 'mcus', 'controller-boards', 'motors',
              'linear-rails-carriages', 'bearings', 'structural-components',
              'belts-pulleys', 'extruders-hotends', 'sensors', 'fans',
              'electrical-hardware', 'fasteners'}


def https_url(value):
    try:
        u = urlsplit(value)
        return (u.scheme == 'https' and bool(u.hostname) and '.' in u.hostname
                and not u.username and not u.password
                and not re.search(r'\s|[<>\\]', value)
                and not re.search(r'%(?![0-9A-Fa-f]{2})', value)
                and u.port in (None, 443))
    except ValueError:
        return False


def schema_errors(value, schema, path='$'):
    """Evaluate exactly the JSON Schema keywords used by catalog.schema.json.

    Fail closed on unsupported keywords so schema evolution cannot bypass checks.
    This is not a general-purpose JSON Schema implementation.
    """
    supported = {'$schema', 'title', 'description', 'type', 'required',
                 'additionalProperties', 'properties', 'items', 'minItems',
                 'minLength', 'minimum', 'pattern', 'enum', 'const', 'format'}
    unknown = set(schema) - supported
    if unknown:
        return [f'{path}: unsupported schema keywords {sorted(unknown)}']
    errors = []
    if 'const' in schema and value != schema['const']:
        errors.append(f'{path}: wrong constant')
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{path}: invalid enum value')
    types = schema.get('type', [])
    types = [types] if isinstance(types, str) else types
    matches = {'null': value is None, 'string': isinstance(value, str),
               'object': isinstance(value, dict), 'array': isinstance(value, list),
               'integer': type(value) is int}
    if types and not any(matches.get(t, False) for t in types):
        return errors + [f'{path}: expected {types}']
    if value is None:
        return errors
    if isinstance(value, dict):
        for key in schema.get('required', []):
            if key not in value:
                errors.append(f'{path}.{key}: missing field')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            for key in value.keys() - props.keys():
                errors.append(f'{path}.{key}: unexpected field')
        for key in value.keys() & props.keys():
            errors.extend(schema_errors(value[key], props[key], f'{path}.{key}'))
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errors.append(f'{path}: too few entries')
        for i, item in enumerate(value):
            errors.extend(schema_errors(item, schema.get('items', {}), f'{path}[{i}]'))
    if isinstance(value, str):
        if len(value.strip()) < schema.get('minLength', 0):
            errors.append(f'{path}: empty string')
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            errors.append(f'{path}: malformed value')
        fmt = schema.get('format')
        if fmt == 'https-url' and not https_url(value):
            errors.append(f'{path}: malformed HTTPS source link')
        if fmt == 'date':
            try:
                if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
                    raise ValueError()
                date.fromisoformat(value)
            except ValueError:
                errors.append(f'{path}: invalid ISO date')
        if fmt and fmt not in {'https-url', 'date'}:
            errors.append(f'{path}: unsupported format')
    if type(value) is int and value < schema.get('minimum', value):
        errors.append(f'{path}: below minimum')
    return errors


def safe_relative(value):
    p = PurePosixPath(value)
    return (not p.is_absolute() and '..' not in p.parts and bool(p.parts)
            and '\\' not in value and ':' not in value)


def validate(data, schema):
    errors = schema_errors(data, schema)
    if errors:
        return errors
    if set(data['categories']) != CATEGORIES or len(data['categories']) != len(CATEGORIES):
        errors.append('categories: expected exactly the 13 supported categories')
    ids, identities, assets = set(), set(), set()
    for p in data['parts']:
        label = p['id']
        identity = tuple(' '.join(p[k].casefold().split()) for k in
                         ('manufacturer', 'part_number', 'variant', 'revision'))
        if label in ids or identity in identities:
            errors.append(f'{label}: duplicate part identity or id')
        ids.add(label)
        identities.add(identity)
        if p['category'] not in CATEGORIES:
            errors.append(f'{label}: unknown category')
        if (p['model_url'] is None) != (p['model_source_status'] == 'not-located'):
            errors.append(f'{label}: model source status and URL disagree')
        for name, perm in p['permissions'].items():
            if perm['status'] != 'unknown' and not perm['basis_url']:
                errors.append(f'{label}: {name} needs a rights source')
        auth = p['authorization']
        if auth['status'] == 'approved' and not auth['evidence']:
            errors.append(f'{label}: approval needs evidence')
        asset = p['local_asset']
        if asset:
            if auth['status'] != 'approved':
                errors.append(f'{label}: local asset lacks explicit authorization')
            for name in ('download', 'local_ai_processing'):
                if p['permissions'][name]['status'] != 'allowed':
                    errors.append(f'{label}: local asset lacks resolved {name} grant')
            for key in ('path', 'license_path'):
                if not safe_relative(asset[key]):
                    errors.append(f'{label}: unsafe local {key}')
                if not asset[key].startswith(p['category'] + '/'):
                    errors.append(f'{label}: local path outside category')
            if asset['path'] in assets:
                errors.append(f'{label}: duplicate local asset path')
            assets.add(asset['path'])
            if not p['model_url'] or p['geometry']['confidence'] == 'documentation-only':
                errors.append(f'{label}: asset provenance/check status incomplete')
        elif p['geometry']['confidence'] != 'documentation-only':
            errors.append(f'{label}: geometry claim without local evidence')
    return errors


def public_file_errors(path, content):
    """Public reference library is metadata only, including text-encoded STEP."""
    errors = []
    if path.suffix.lower() not in {'.json', '.md', '.py'}:
        errors.append(f'{path}: unapproved public reference file type')
    try:
        text = content.decode('utf-8')
        if any(ord(c) < 32 and c not in '\n\r\t' for c in text):
            errors.append(f'{path}: binary/control content')
        if 'ISO-10303-21;' in text[:256] or text.startswith('version https://git-lfs.github.com/spec/'):
            errors.append(f'{path}: CAD model or LFS pointer in metadata library')
    except UnicodeDecodeError:
        errors.append(f'{path}: binary content in metadata library')
    return errors


def publication_errors(root=ROOT):
    errors = []
    # Include the index as well as working files: a clean working copy must not
    # hide a staged binary, and force-adding a gitignored cache must fail.
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).split(b'\0')
    for raw in filter(None, paths):
        rel = raw.decode('utf-8')
        if rel.startswith('local-cad-references/'):
            errors.append(f'{rel}: local cache tracked in Git')
        if rel.startswith('cad/reference-parts/'):
            staged = subprocess.check_output(['git', 'show', ':' + rel], cwd=root)
            errors.extend(public_file_errors(Path(rel), staged))
    for path in (root / 'cad/reference-parts').rglob('*'):
        if '__pycache__' in path.parts:
            continue
        if path.is_symlink():
            errors.append(f'{path}: symlinks forbidden in public library')
        elif path.is_file():
            errors.extend(public_file_errors(path, path.read_bytes()))
    return errors


def check_local(data, library):
    errors, reports = [], []
    library = library.resolve(strict=True)
    for p in data['parts']:
        a = p['local_asset']
        if not a:
            continue
        for name, hashkey in [('path', 'sha256'), ('license_path', 'license_sha256')]:
            f = (library / a[name]).resolve(strict=True)
            if library not in f.parents:
                errors.append(f'{p["id"]}: resolved path escapes library')
                continue
            b = f.read_bytes()
            if hashlib.sha256(b).hexdigest() != a[hashkey]:
                errors.append(f'{p["id"]}: {name} SHA-256 mismatch')
            if name != 'path':
                continue
            if len(b) != a['bytes']:
                errors.append(f'{p["id"]}: size mismatch')
            blob = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
            if blob != a['git_blob_sha1']:
                errors.append(f'{p["id"]}: Git blob identity mismatch')
            text = b.decode('ascii')
            if not (text.lstrip().startswith('ISO-10303-21;') and
                    text.rstrip().endswith('END-ISO-10303-21;') and
                    'HEADER;' in text and 'DATA;' in text and text.count('ENDSEC;') == 2):
                errors.append(f'{p["id"]}: STEP exchange structure markers missing')
            reports.append({'id':p['id'], 'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest(),
                            'millimetre_unit_declarations':len(re.findall(r'SI_UNIT\(\.MILLI\.,\.METRE\.\)', text)),
                            'entity_definitions':len(re.findall(r'^#\d+\s*=', text, re.M)),
                            'limit':'Structural text checks only; no solid, dimension or physical validation'})
    return errors, reports


def render_index(data):
    lines = ['# Candidate parts index', '', 'Generated from [catalog.json](catalog.json) by `python3 scripts/check_reference_parts.py --write-index`.', '',
             'Candidates only; no purchasing or printer architecture selection. Unknown revisions and permissions block dependent CAD. See [workflow and limitations](README.md).', '']
    for category in data['categories']:
        rows = [p for p in data['parts'] if p['category'] == category]
        lines += ['## ' + category, '', f'{len(rows)} records.', '', '| Manufacturer / part | Variant / revision | Model source | Local asset |', '| --- | --- | --- | --- |']
        for p in rows:
            label = p['manufacturer'] + ' ' + p['part_number']
            model = '['+p['model_source_status']+']('+p['model_url']+')' if p['model_url'] else 'Not located'
            lines.append(f'| [{label}]({p["documentation_url"]}) | {p["variant"]} / {p["revision"]} | {model} | '+('File checked; import pending' if p['local_asset'] else 'None')+' |')
        lines += ['']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library', type=Path, help='Explicit local library root; read/hash only')
    parser.add_argument('--write-index', action='store_true')
    args = parser.parse_args()
    try:
        data, schema = json.loads(CATALOG.read_text()), json.loads(SCHEMA.read_text())
        errors = validate(data, schema)
        if not errors:
            index = render_index(data)
            if args.write_index:
                (CATALOG.parent / 'INDEX.md').write_text(index)
            elif (CATALOG.parent / 'INDEX.md').read_text() != index:
                errors.append('INDEX.md is stale; regenerate with --write-index')
            errors.extend(publication_errors())
            if args.library:
                more, reports = check_local(data, args.library)
                errors.extend(more)
                print(json.dumps(reports, indent=2))
        for error in errors:
            print('ERROR:', error)
        if errors:
            return 1
        print(f'PASS: {len(data["parts"])} candidates; {sum(bool(p["local_asset"]) for p in data["parts"])} cataloged local assets')
        print(json.dumps(dict(Counter(p['category'] for p in data['parts'])), sort_keys=True))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'ERROR: {type(exc).__name__}: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
