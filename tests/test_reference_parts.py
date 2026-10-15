"""Negative tests protect provenance and the public/local asset boundary."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('reference_parts', ROOT/'scripts/check_reference_parts.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(check.CATALOG.read_text())
        self.schema = json.loads(check.SCHEMA.read_text())
        self.sample = next(p for p in self.data['parts'] if p['local_asset'])

    def errors(self):
        return check.validate(self.data, self.schema)

    def test_catalog_and_generated_index(self):
        self.assertEqual([], self.errors())
        self.assertEqual(check.render_index(self.data), (check.CATALOG.parent/'INDEX.md').read_text())

    def test_missing_required_field(self):
        del self.data['parts'][0]['revision']
        self.assertTrue(self.errors())

    def test_duplicate_normalized_identity(self):
        part = copy.deepcopy(self.data['parts'][0])
        part['id'] = 'different-id'
        part['manufacturer'] = '  ' + part['manufacturer'].upper() + '  '
        self.data['parts'].append(part)
        self.assertTrue(any('duplicate' in e for e in self.errors()))

    def test_bad_links(self):
        for url in ['http://example.com/a', 'https://', 'https://user:password@example.com',
                    'https://example.com/a b', 'https://example.com/%zz', 'https://example.com:abc']:
            with self.subTest(url=url):
                self.assertFalse(check.https_url(url))
        self.assertTrue(check.https_url('https://example.com/a%20b?q=1#cad'))

    def test_empty_unknown_and_invalid_dates_rejected(self):
        for field,value in [('revision',' '), ('access_date','2026-02-30'), ('status','validated')]:
            with self.subTest(field=field):
                data=copy.deepcopy(self.data)
                data['parts'][0][field]=value
                self.assertTrue(check.validate(data,self.schema))

    def test_local_asset_requires_both_permissions_and_authorization(self):
        for key in ['download','local_ai_processing']:
            original=self.sample['permissions'][key]['status']
            self.sample['permissions'][key]['status']='unknown'
            self.assertTrue(self.errors())
            self.sample['permissions'][key]['status']=original
        self.sample['authorization']['status']='pending'
        self.assertTrue(self.errors())

    def test_grant_requires_basis(self):
        self.sample['permissions']['public_redistribution']['basis_url']=None
        self.assertTrue(self.errors())

    def test_unknown_fields_and_schema_keywords_fail_closed(self):
        self.sample['magic_approval']=True
        self.assertTrue(self.errors())
        self.assertTrue(check.schema_errors({}, {'oneOf':[]}))

    def test_path_traversal_rejected(self):
        for path in ['../outside.step','/tmp/model.step','mcus/../../outside.step','C:\\model.step']:
            with self.subTest(path=path):
                self.sample['local_asset']['path']=path
                self.assertTrue(self.errors())

    def test_binary_and_disguised_models_rejected(self):
        for name,content in [('x.step',b'ISO-10303-21;'),('x.json',b'\x00abc'),
                             ('x.md',b'\xff'),('x.md',b'ISO-10303-21;'),
                             ('x.json',b'version https://git-lfs.github.com/spec/v1')]:
            with self.subTest(name=name,content=content):
                self.assertTrue(check.public_file_errors(Path(name),content))

    def test_staged_binary_cannot_hide_behind_clean_working_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            subprocess.run(['git','init','-q'],cwd=root,check=True)
            p=root/'cad/reference-parts/hidden.json'
            p.parent.mkdir(parents=True)
            p.write_bytes(b'\x00binary')
            subprocess.run(['git','add','cad/reference-parts/hidden.json'],cwd=root,check=True)
            p.write_text('{}')
            self.assertTrue(any('binary' in e for e in check.publication_errors(root)))

    def test_forced_cache_tracking_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            subprocess.run(['git','init','-q'],cwd=root,check=True)
            p=root/'local-cad-references/a.step'; p.parent.mkdir(); p.write_text('test')
            subprocess.run(['git','add','.'],cwd=root,check=True)
            self.assertTrue(any('cache tracked' in e for e in check.publication_errors(root)))

    def test_hash_mismatch_and_symlink_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            a=self.sample['local_asset']
            for key in ['path','license_path']:
                p=root/a[key]; p.parent.mkdir(parents=True,exist_ok=True); p.write_text('changed')
            errors,_=check.check_local(self.data,root)
            self.assertTrue(any('SHA-256 mismatch' in e for e in errors))
            (root/a['path']).unlink()
            (root/a['path']).symlink_to(check.CATALOG)
            errors,_=check.check_local(self.data,root)
            self.assertTrue(any('escapes' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
