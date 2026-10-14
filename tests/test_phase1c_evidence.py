"""Validate the retained archive's integrity and attribution, not Fusion behavior."""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'docs/phase1c/evidence'


class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = gzip.decompress((FOLDER/'runtime-observations.json.gz').read_bytes()).decode()
        cls.bundle = json.loads(cls.text)

    def test_retained_reports_and_original_published_hashes(self):
        reports = self.bundle['reports']
        self.assertEqual(len(reports), 36)
        self.assertEqual(sum(r['outcome'] == 'PASS' for r in reports.values()), 33)
        self.assertEqual(sum(r['outcome'] == 'FAIL' for r in reports.values()), 3)
        source = (ROOT/'docs/phase1c/verification.md').read_text()
        matches = re.findall(r'`(?:tesseract-phase1c-check-)?([\w-]+)(?:\.txt)?` \| `([a-f0-9]{64})`', source)
        self.assertEqual(len(matches), 11)
        for report_id, digest in matches:
            self.assertEqual(reports[report_id]['original_sha256'], digest)
        for report in reports.values():
            for digest in report['components'].values():
                lines = self.bundle['component_observations'][digest]
                self.assertEqual(hashlib.sha256(json.dumps(lines, ensure_ascii=True).encode()).hexdigest(), digest)
        for private in ('/Users/', 'C:\\Users\\', 'Source: ', 'Traceback ('):
            self.assertNotIn(private, self.text)
        for key in ('fusion_version', 'os_version', 'document_ids'):
            self.assertEqual(self.bundle[key], 'unknown')

    def test_original_failure_and_corrected_observations_remain_distinct(self):
        def observation(report_id, name):
            key = self.bundle['reports'][report_id]['components'][name]
            return '\n'.join(self.bundle['component_observations'][key])
        failure = observation('mm0alj_4', 'Fixed_cold_carrier')
        self.assertIn("health/message/fullyConstrained=(0, '', False)", failure)
        self.assertIn('constraint types=[]', failure)
        self.assertIn('35.99999999999998', failure)
        self.assertIn('line endpoints in component XYZ mm=', failure)
        corrected = observation('5_4b7dhl', 'Fixed_cold_carrier')
        self.assertIn("health/message/fullyConstrained=(0, '', True)", corrected)
        self.assertIn('HorizontalConstraint', corrected)
        for report_id in ('uwuq5tzb', 'xhotdiee'):
            self.assertTrue(self.bundle['reports'][report_id]['errors'])
            self.assertEqual(self.bundle['reports'][report_id]['components'], {})
        for report in self.bundle['reports'].values():
            if report['outcome'] == 'PASS':
                self.assertIn(len(report['components']), (51, 59))
                key = report['components']['Common_cartridge_mount_plate']
                data = '\n'.join(self.bundle['component_observations'][key])
                for i in range(1, 5):
                    self.assertIn(f'Common_mount_bore_{i} health/message/suppressed=', data)
                    self.assertIn(f'Common_mount_hole_{i}_NOT_fastener_selection dimensions', data)

    def test_extractor_ignores_unlisted_files_and_marks_missing(self):
        spec = importlib.util.spec_from_file_location('preserve_reports', FOLDER/'preserve_reports.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder/'tesseract-phase1c-check-synthetic.txt').write_text('CHECK PASSED')
            result = module.extract(folder)
        self.assertEqual(set(result['reports']), set(self.bundle['reports']))
        self.assertTrue(all(r == {'availability': 'missing'} for r in result['reports'].values()))
        self.assertFalse(result['component_observations'])


if __name__ == '__main__':
    unittest.main()
