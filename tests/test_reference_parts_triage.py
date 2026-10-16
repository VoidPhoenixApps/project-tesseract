"""Triage must never turn rights, a URL or a pin into retrieval/fit approval."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import reference_parts_triage as triage


class TriageTests(unittest.TestCase):
    def setUp(self):
        self.parts = json.loads(triage.CATALOG.read_text())['parts']
        self.pulley = copy.deepcopy(next(p for p in self.parts if p['part_number'] == '1253'))
        self.feather = copy.deepcopy(next(p for p in self.parts if p['local_asset']))

    def test_readiness_counts_and_generated_report(self):
        report = triage.report_data(self.parts)
        self.assertEqual(45, report['count'])
        self.assertEqual({'authorized-local-record': 1, 'prepare-authorization-request': 2,
                          'resolve-inspection-rights': 42}, report['summary']['group'])
        self.assertEqual(triage.REPORT.read_text(), triage.render_report(report))
        self.assertEqual(triage.render_report(report), triage.render_report(triage.report_data(list(reversed(self.parts)))))

    def test_license_and_pin_are_not_authorization_or_fit(self):
        row = triage.classify(self.pulley)
        self.assertEqual('not-requested', row['authorization']['status'])
        self.assertEqual('not-cataloged', row['local_status'])
        self.assertEqual('unknown', row['physical_revision'])
        self.assertEqual('documentation-only', row['geometry_confidence'])
        self.assertIn('Obtain explicit bounded maintainer authorization', row['next_actions'])

    def test_each_permission_remains_separate(self):
        for name in triage.PERMISSIONS:
            for status in ('unknown', 'conditional', 'prohibited'):
                with self.subTest(name=name, status=status):
                    part = copy.deepcopy(self.pulley)
                    part['permissions'][name]['status'] = status
                    row = triage.classify(part)
                    self.assertEqual(status, row['permissions'][name])
                    self.assertTrue(any(name in action for action in row['next_actions']))
                    if name in triage.PERMISSIONS[:2]:
                        self.assertEqual('resolve-inspection-rights', row['group'])

    def test_url_does_not_resolve_configuration(self):
        part = next(p for p in self.parts if p['model_source_status'] == 'portal-unconfigured')
        self.assertIn('Resolve exact portal configuration', triage.classify(part)['next_actions'])

    def test_local_missing_corrupt_and_unchecked_are_distinct(self):
        self.assertEqual('not-checked', triage.classify(self.feather)['local_status'])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual('missing-or-unreadable', triage.classify(self.feather, root)['local_status'])
            for name in ('path', 'license_path'):
                path = root / self.feather['local_asset'][name]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('wrong bytes')
            self.assertEqual('check-failed', triage.classify(self.feather, root)['local_status'])

    def test_identity_search_and_unknown_ids_do_not_substitute(self):
        rows, missing = triage.select_parts(self.parts, ['adafruit-1253'])
        self.assertEqual([], rows)
        self.assertEqual(['adafruit-1253'], missing)
        rows, _ = triage.select_parts(self.parts, query='ADAFRUIT 1253')
        self.assertEqual([self.pulley['id']], [r['id'] for r in rows])
        request = triage.render_requests(rows, missing, 'bore comparison', 'sample inspection')
        self.assertIn('no catalog match', request)
        self.assertIn('physical revision unknown', request)
        for permission in triage.PERMISSIONS:
            self.assertIn(permission + '=', request)
        self.assertIn('sample inspection', request)

    def test_cli_fails_for_missing_identity_and_incomplete_request(self):
        script = str(ROOT / 'scripts/reference_parts_triage.py')
        for args in (['--id', 'not-a-real-part'], ['--requests', '--id', self.pulley['id']],
                     ['--check-report', '--query', 'pico']):
            result = subprocess.run([sys.executable, script] + args, capture_output=True, text=True)
            self.assertNotEqual(0, result.returncode)

    def test_markdown_escapes_input(self):
        request = triage.render_requests([], ['unknown|part'], 'hole\nspacing', 'fixture|mount')
        self.assertIn('unknown\\|part', request)
        self.assertIn('hole spacing', request)


if __name__ == '__main__':
    unittest.main()
