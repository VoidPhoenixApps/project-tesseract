"""Independent equilibrium, boundary and negative controls for D3 analytical models."""
import json
from math import pi
from pathlib import Path
import unittest

import d3_analysis as d


class D3Tests(unittest.TestCase):
    def test_all_mode_partitions_and_mass_conservation(self):
        counts = {'S': 4, 'R': 2, 'C': 2, 'M12': 3, 'M34': 3, 'M13': 3, 'M24': 3, 'J': 1}
        for mode, count in counts.items():
            rows = d.group_loads(mode, {1: 1, 2: 2, 3: 3, 4: 4}, 2)
            self.assertEqual(len(rows), count)
            self.assertEqual(sorted(i for r in rows for i in r['beds']), [1, 2, 3, 4])
            self.assertEqual(sum(r['mass_kg'] for r in rows), 10+2*count)
            self.assertAlmostEqual(sum(r['force_n'] for r in rows), (10+2*count)*d.G)

    def test_two_line_equilibrium_and_uplift(self):
        for e in (-150, -60, 0, 60, 150):
            left, right = d.reactions(100, 240, e)
            self.assertAlmostEqual(left+right, 100)
            self.assertAlmostEqual((right-left)*120, 100*e)
        self.assertLess(d.reactions(100, 240, 150)[0], 0)
        self.assertEqual(d.reactions(100, 240, 120)[0], 0)

    def test_tripod_force_moment_and_outside_polygon(self):
        points = ((-120, -120), (120, -120), (0, 120))
        for com in ((0, 0), (90, 90), (-120, -120)):
            r = d.tripod(100, points, com)
            self.assertAlmostEqual(sum(r), 100)
            for axis in (0, 1):
                self.assertAlmostEqual(sum(f*p[axis] for f, p in zip(r, points)), 100*com[axis])
        self.assertTrue(any(r < 0 for r in d.tripod(100, points, (90, 90))))
        with self.assertRaises(ValueError):
            d.tripod(100, ((0, 0), (1, 0), (2, 0)), (0, 0))

    def test_frame_increment_and_work_balance(self):
        a, b = d.lift(10), d.lift(12)
        self.assertAlmostEqual(b['force_n']-a['force_n'], 2*d.G)
        # One motor revolution at R=3 moves a direct belt load by 40/3 mm.
        r = d.lift(12, reduction=3, efficiency=1)
        self.assertAlmostEqual(r['belt_motor_nm']*2*pi, 12*d.G*.04/3)

    def test_cantilever_scaling(self):
        a, b = d.cantilever(20, 90, 1e7), d.cantilever(20, 180, 1e7)
        self.assertAlmostEqual(b['tip_deflection_mm']/a['tip_deflection_mm'], 8)
        self.assertAlmostEqual(a['root_moment_nm'], 1.8)

    def test_guide_clearance_and_reversed_angle(self):
        self.assertEqual(d.guide_loop(200, 0, .02, .05, 1000)['elastic_force_n'], 0)
        a = d.guide_loop(200, .05, 0, 0, 1000)
        b = d.guide_loop(200, -.05, 0, 0, 1000)
        self.assertAlmostEqual(a['elastic_force_n'], b['elastic_force_n'])
        self.assertAlmostEqual(a['mismatch_mm'], -b['mismatch_mm'])

    def test_equal_endpoint_belt_path_is_not_constant(self):
        a, mid, b = [d.selector_span(100, q, 50) for q in (-20, 0, 20)]
        self.assertEqual(a['length_mm'], b['length_mm'])
        self.assertGreater(a['length_mm']-mid['length_mm'], 3.9)
        self.assertEqual(mid['selector_force_n'], 0)
        h = 1e-4
        slope = (d.selector_span(100, 20+h, 50)['length_mm']-
                 d.selector_span(100, 20-h, 50)['length_mm'])/(2*h)
        self.assertAlmostEqual(b['selector_force_n'], 50*slope, places=6)

    def test_downstream_backlash_not_reduced(self):
        self.assertAlmostEqual(d.backlash_mm(0, 1, 40, 3), 40/360)
        self.assertAlmostEqual(d.backlash_mm(1, 0, 40, 3), 40/1080)

    def test_pitch_roll_and_endpoint_error(self):
        budget = d.seam_budget(.02, (.0001, .0001), (.0001, .0001), (90, 90), (-90, 90), {})
        self.assertAlmostEqual(budget['total_mm'], .056)
        center = d.seam_budget(0, (.0001, 0), (.0001, 0), (90, 0), (-90, 0), {})
        self.assertEqual(center['total_mm'], 0)
        # Center-only sensing can miss an opposite-roll seam endpoint error.
        self.assertGreater(budget['tilt_mm'], center['tilt_mm'])

    def test_arrest_energy_not_static_load(self):
        r = d.arrest(12, .01, .02, 1)
        initial_ke = .5*12*.01**2
        gravity_work = 12*d.G*r['total_drop_mm']/1000
        self.assertAlmostEqual(r['absorbed_energy_j'], initial_ke+gravity_work)
        self.assertGreater(r['average_catch_force_n'], 12*d.G)
        self.assertGreater(d.arrest(12, .01, .05, 1)['average_catch_force_n'], r['average_catch_force_n'])

    def test_unified_frame_cannot_supply_two_independent_pairs(self):
        rows = d.graph_groups(((1, 2), (3, 4)))
        columns = d.graph_groups(((1, 3), (2, 4)))
        unified = d.graph_groups(((1, 2), (1, 3), (2, 4), (3, 4)))
        self.assertEqual(rows, [(1, 2), (3, 4)])
        self.assertEqual(columns, [(1, 3), (2, 4)])
        self.assertEqual(unified, [(1, 2, 3, 4)])
        self.assertNotEqual(rows, unified)
        self.assertEqual(d.graph_groups(((1, 2), (1, 3), (3, 4))), unified)

    def test_thermal_historical_negative_preserved(self):
        lo, hi = d.thermal.cold_interval('center')
        self.assertGreater(lo, hi)
        self.assertAlmostEqual(lo-hi, .13984)
        self.assertAlmostEqual(d.thermal.gap(100, 100, 'inset'), .16224)

    def test_invalid_inputs_rejected(self):
        calls = [lambda: d.group_loads('J', {1: 1}), lambda: d.selector_span(0, 0, 1),
                 lambda: d.reactions(1, 0, 0), lambda: d.guide_loop(1, 90, 0, 0, 1),
                 lambda: d.arrest(1, 0, -.1, 1), lambda: d.arrest(1, 0, .1, 0),
                 lambda: d.cantilever(1, 1, float('nan')), lambda: d.graph_groups(((1, 5),)),
                 lambda: d.backlash_mm(1, 1, 40, 0),
                 lambda: d.seam_budget(0, (0, 0), (0, 0), (0, 0), (0, 0), {'x': -1})]
        for call in calls:
            with self.assertRaises(ValueError):
                call()

    def test_committed_results_reproduce(self):
        result = json.dumps(d.results(), indent=2, sort_keys=True)+'\n'
        self.assertEqual(result, Path(__file__).with_name('d3-results.json').read_text())


if __name__ == '__main__':
    unittest.main()
