"""Independent equilibrium/scaling and negative controls for D4's limited models."""
import json
import math
from pathlib import Path
import subprocess
import sys
import unittest
import d4_analysis as d


class D4Tests(unittest.TestCase):
    def test_circle_known(self):
        a, i = d.circular(2)
        self.assertAlmostEqual(a, math.pi)
        self.assertAlmostEqual(i, math.pi/4)
        a2, i2 = d.circular(2, .5)
        self.assertAlmostEqual(a2, 3*math.pi/4)
        self.assertAlmostEqual(i2, 15*math.pi/64)

    def test_beam_boundary_conditions_and_scaling(self):
        base = d.beam(30, 2, 200, 3)
        self.assertAlmostEqual(base, 2/15)
        self.assertAlmostEqual(base, 16*d.beam(30, 2, 200, 3, 'simple_center'))
        self.assertAlmostEqual(d.beam(60, 4, 400, 3), 8*base)
        self.assertEqual(d.beam(0, 2, 200, 3), 0)

    def test_root_compliance(self):
        x = d.arm(20, .3, 210e9, 1e-8, 10000)
        self.assertAlmostEqual(x['moment_nm'], 6)
        self.assertAlmostEqual(x['root_mm'], .18)
        self.assertAlmostEqual(x['total_mm'], x['member_mm']+x['root_mm'])

    def test_buckling_end_and_length(self):
        p = d.buckling(200, 3, 2)
        self.assertAlmostEqual(d.buckling(200, 3, 4), p/4)
        self.assertAlmostEqual(d.buckling(200, 3, 2, 2), p/4)

    def test_truss_equilibrium_and_energy(self):
        x = d.v_truss(100, .3, .15, 2e9, .0004, .02**4/12, 1e6)
        n, length = x['compression_n'], x['length_m']
        self.assertAlmostEqual(2*n*.15/length, 100)
        # Two bar strains plus FOUR end-joint spring energies.
        energy = n*n*length/(2e9*.0004)+2*n*n/1e6
        self.assertAlmostEqual(energy, .5*100*x['deflection_mm']/1000)
        shallow = d.v_truss(100, .3, .015, 2e9, .0004, .02**4/12, 1e6)
        self.assertGreater(shallow['compression_n'], n)
        self.assertGreater(shallow['deflection_mm'], x['deflection_mm'])

    def test_linear_truss_large_motion_and_buckling_warnings(self):
        x = d.v_truss(100, .3, .05, 2e9, .0004, .02**4/12, 1e5)
        self.assertTrue(x['large_displacement_warning'])
        self.assertGreater(x['linear_deflection_over_rise'], .75)
        self.assertFalse(x['K2_euler_demand_exceeded'])  # geometry fails first
        soft = d.v_truss(100, .3, .05, .5e9, .0004, .02**4/12, 1e5)
        self.assertTrue(soft['K2_euler_demand_exceeded'])
        zero = d.v_truss(0, .3, .05, 2e9, .0004, .02**4/12, 1e5)
        self.assertEqual(zero['linear_deflection_over_rise'], 0)
        self.assertFalse(zero['large_displacement_warning'])

    def test_torsion_couple_and_energy(self):
        x = d.bay_torsion(10, .6, 1e5)
        edge = x['edge_motion_mm']/1000
        self.assertAlmostEqual(1e5*edge*.6, 10)
        self.assertAlmostEqual(1e5*edge**2, .5*10*x['angle_rad'])

    def test_pair_force_balance_and_constitutive(self):
        for k2 in (0, 2e5, 1e6):
            for offset in (-.0002, 0, .0002):
                x = d.pair_support(20, 40, 1e6, k2, 1e6, offset)
                self.assertAlmostEqual(x['support1_n']+x['support2_n'], 60)
                self.assertAlmostEqual(x['support1_n']-x['tie_on_1_down_n'], 20)
                self.assertAlmostEqual(x['support2_n']+x['tie_on_1_down_n'], 40)
                self.assertAlmostEqual(x['u1_mm']*1000, x['support1_n'])

    def test_support_loss_is_not_independence(self):
        with self.assertRaises(ValueError):
            d.pair_support(20, 40, 1e6, 0, 0)
        x = d.pair_support(20, 40, 1e6, 0, 1e6)
        self.assertAlmostEqual(x['support1_n'], 60)
        self.assertAlmostEqual(x['tie_on_1_down_n'], 40)
        self.assertAlmostEqual(x['relative_mm'], .04)

    def test_mismatch_can_reverse_reaction(self):
        x = d.pair_support(20, 40, 1e6, 1e6, 1e6, .0002)
        self.assertLess(x['support2_n'], 0)  # gravity-only support loses contact
        self.assertGreater(x['support1_n'], 60)

    def test_independent_and_rigid_tie_limits(self):
        x = d.pair_support(20, 40, 1e6, 1e6, 0)
        self.assertAlmostEqual(x['u1_mm'], .02)
        self.assertAlmostEqual(x['u2_mm'], .04)
        x = d.pair_support(20, 40, 1e6, 1e6, 1e12)
        self.assertLess(abs(x['relative_mm']), 1e-7)

    def test_modes_and_no_cross_group_edges(self):
        expected = {'S': 4, 'R': 2, 'C': 2, 'M12': 3, 'M34': 3, 'M13': 3, 'M24': 3, 'J': 1}
        self.assertEqual(set(d.MODES), set(expected))
        for mode, count in expected.items():
            x = d.mode_graph(mode)
            self.assertEqual(x['progress_coordinates'], count)
            self.assertEqual(sorted(i for g in x['groups'] for i in g), [1, 2, 3, 4])
            self.assertEqual(len(x['L_independent']), 4)
            self.assertEqual(len(x['L_optional_hybrid_ties']), 4-count)
            for a, b in x['L_optional_hybrid_ties']:
                self.assertTrue(any(a in g and b in g for g in x['groups']))
            self.assertEqual(x['unified_platform_attached_compatible'], mode == 'J')

    def test_invalid_inputs(self):
        calls = [lambda: d.circular(0), lambda: d.circular(.025, .013),
                 lambda: d.circular(.025, 0), lambda: d.beam(1, 1, 1, 1, 'fixed'),
                 lambda: d.beam(-1, 1, 1, 1), lambda: d.arm(1, 1, 1, 1, 0),
                 lambda: d.v_truss(1, 1, 0, 1, 1, 1, 1),
                 lambda: d.pair_support(1, 1, 0, 0, 1), lambda: d.mode_graph('X')]
        for value in (float('nan'), float('inf'), -1):
            calls.extend([lambda v=value: d.buckling(v, 1, 1),
                          lambda v=value: d.bay_torsion(1, v, 1),
                          lambda v=value: d.pair_support(1, 1, v, 1, 1)])
        for call in calls:
            with self.assertRaises(ValueError):
                call()

    def test_stock_is_not_rounded_equivalence(self):
        s = d.results()['sections']
        self.assertGreater(s['inch_shaft_half_nominal']['I_mm4'], s['metric_shaft_12']['I_mm4'])
        self.assertNotEqual(s['inch_tube_1x065']['area_mm2'], s['metric_tube_25x1p5']['area_mm2'])

    def test_reproduction_from_other_directory(self):
        here = Path(__file__).resolve().parent
        output = subprocess.check_output([sys.executable, '-B', str(here/'d4_analysis.py')], cwd='/tmp')
        self.assertEqual(output, (here/'d4-results.json').read_bytes())
        self.assertEqual(json.loads(output), d.results())


if __name__ == '__main__':
    unittest.main()
