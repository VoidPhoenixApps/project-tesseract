"""Traceability checks, not physical tests or independent mechanism verification."""
from pathlib import Path
import unittest
import d7_matrix as d7
from d2_geometry import MODES as D2_MODES


class D7Tests(unittest.TestCase):
    def test_exact_partitions_and_independent_owners(self):
        expected = {'S': 4, 'R': 2, 'C': 2, 'M12': 3, 'M34': 3,
                    'M13': 3, 'M24': 3, 'J': 1}
        self.assertEqual({m: len(g) for m, g in d7.MODES.items()}, expected)
        for mode, groups in d7.MODES.items():
            self.assertEqual(sorted(b for g in groups for b in g), [1, 2, 3, 4])
            self.assertEqual({frozenset(g) for g in groups},
                             {frozenset(g) for g in D2_MODES[mode]})

    def test_full_cross_product_has_no_pass_status(self):
        cells = [d7.verdict(x, z, m) for x in d7.XY for z in d7.Z for m in d7.MODES]
        self.assertEqual(len(cells), 1536)
        self.assertEqual(set(cells), {'X', 'U', 'D', 'K'})
        for profiles in (d7.XY, d7.Z):
            for _, codes in profiles.values():
                self.assertEqual(len(codes), 8)
                self.assertLessEqual(set(codes), {'X', 'U', 'D', 'K'})

    def test_negative_ownership_counterexamples_survive_every_z(self):
        for z in d7.Z:
            for mode in ('R', 'C', 'M12', 'M34', 'M13', 'M24', 'J'):
                self.assertEqual(d7.verdict('A0', z, mode), 'X')
            for mode in ('R', 'C'):
                self.assertEqual(d7.verdict('C0', z, mode), 'X')
            for mode in ('S', 'R', 'C', 'M12', 'M34', 'M13', 'M24'):
                self.assertEqual(d7.verdict('D0', z, mode), 'X')
            for mode in ('S', 'C', 'M12', 'M34', 'M13', 'M24'):
                self.assertEqual(d7.verdict('B1', z, mode), 'X')

    def test_single_job_does_not_inherit_nonpassing_concurrency_exclusion(self):
        self.assertEqual(d7.verdict('B1', 'A', 'J'), 'U')
        self.assertEqual(d7.verdict('B1', 'E-sync', 'J'), 'U')

    def test_grouped_c_f_repair_is_not_feasibility(self):
        for mode in ('R', 'C', 'M12', 'M34', 'M13', 'M24'):
            for restricted in ('C0', 'F0-reroute', 'F0-clutch', 'F-attached', 'D-trim'):
                self.assertEqual(d7.verdict('A+cant', restricted, mode), 'X')
            for grouped in ('C-group', 'F-group-clutch', 'F-group-reroute'):
                self.assertEqual(d7.verdict('A+cant', grouped, mode), 'D')
        self.assertEqual(d7.verdict('A+cant', 'F-group-reroute', 'J'), 'U')

    def test_mirroring_never_supplies_motion(self):
        for z in d7.Z:
            for m in d7.MODES:
                self.assertIn(d7.verdict('E-only', z, m), ('X', 'U'))
        self.assertIn('topological classification is identical', d7.render())

    def test_generated_matrix_current(self):
        self.assertEqual(Path(__file__).with_name('d7-matrix.md').read_text(), d7.render())


if __name__ == '__main__':
    unittest.main()
