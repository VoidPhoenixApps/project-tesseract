"""Analytical invariants and negative controls, not physical acceptance tests."""
import importlib.util
from pathlib import Path
import unittest
from d1_analysis import lift, common_z_interval, seam_step, angular_error_mm, sweep_box, overlaps, results


class AnalysisTests(unittest.TestCase):
    def test_energy_balance(self):
        # Ideal 1 kg lifted 8 mm: work must equal motor torque times 2*pi.
        from math import pi
        self.assertAlmostEqual(lift(1, efficiency=1)['screw_motor_nm']*2*pi, 9.80665*.008)
        self.assertAlmostEqual(lift(4)['belt_motor_nm'], 4*lift(1)['belt_motor_nm'])
        self.assertAlmostEqual(lift(1, reduction=3)['belt_motor_nm']*3, lift(1)['belt_motor_nm'])
        self.assertAlmostEqual(lift(1, advantage=2)['belt_tension_difference_n'], 9.80665/2)

    def test_short_stroke_counterexample(self):
        self.assertEqual(common_z_interval((0,20),((-10,10),)*2,(-300,300)), (10,10))
        self.assertIsNone(common_z_interval((0,21),((-10,10),)*2,(-300,300)))
        self.assertIsNone(common_z_interval((100,),((-10,10),),(0,50)))
        # Z-C retained 0..200 mm downward bed travel permits unrelated heights.
        self.assertEqual(common_z_interval((0,100,200),((0,200),)*3,(0,300)), (0,0))

    def test_seam_error_and_phase(self):
        self.assertEqual(seam_step(0,90,0,0,500), 0)
        self.assertAlmostEqual(seam_step(.02,0,0,10,500), .04)
        self.assertAlmostEqual(angular_error_mm(360,8), 8)
        self.assertAlmostEqual(angular_error_mm(-1,40), -1/9)

    def test_swept_midpath_and_height(self):
        body=(-5,5,-5,5,0,10)
        obstacle=(-1,1,-1,1,0,5)
        self.assertFalse(overlaps(sweep_box(body,(-20,0,0),(-20,0,0)), obstacle))
        self.assertFalse(overlaps(sweep_box(body,(20,0,0),(20,0,0)), obstacle))
        self.assertTrue(overlaps(sweep_box(body,(-20,0,0),(20,0,0)), obstacle))
        self.assertFalse(overlaps(sweep_box(body,(-20,0,20),(20,0,20)), obstacle))
        self.assertTrue(overlaps((0,1,0,1,0,1),(1,2,0,1,0,1)))
        self.assertFalse(results()['head_sweep_conflict_low_object'])
        self.assertTrue(results()['head_sweep_conflict_tall_object'])

    def test_phase1b_independent_reconciliation(self):
        p=Path(__file__).resolve().parents[1]/'phase1b'/'analysis.py'
        spec=importlib.util.spec_from_file_location('phase1b_check',p)
        prior=importlib.util.module_from_spec(spec); spec.loader.exec_module(prior)
        self.assertAlmostEqual(prior.gap(100,100), -.13984)
        self.assertAlmostEqual(prior.gap(100,100,'inset',inset=10), .16224)
        self.assertAlmostEqual(-prior.gap(100,100,cold=0), results()['thermal_mm']['al_180_80K'])

    def test_invalid_inputs(self):
        for kwargs in ({'mass_kg':0},{'mass_kg':float('nan')},{'mass_kg':1,'efficiency':1.1},
                       {'mass_kg':1,'reduction':0},{'mass_kg':1,'drag_n':-1}):
            with self.assertRaises(ValueError): lift(**kwargs)
        with self.assertRaises(ValueError): common_z_interval((),(),(0,1))
        with self.assertRaises(ValueError): seam_step(0,1,0,0,0)
        with self.assertRaises(ValueError): overlaps((1,0,0,1,0,1),(0,1,0,1,0,1))
        with self.assertRaises(ValueError): sweep_box((0,1,0,1,0,1),(0,0,float('inf')),(0,0,0))


if __name__ == '__main__':
    unittest.main()
