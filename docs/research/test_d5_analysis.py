"""Arithmetic, limiting cases, negative controls; not physical acceptance tests."""
import json
import math
from pathlib import Path
import unittest
import d5_analysis as d
from d2_geometry import Box, path_hits


class D5Tests(unittest.TestCase):
    def test_expansion_and_cooling(self):
        self.assertAlmostEqual(d.growth(.6,65e-6,40),.00156)
        self.assertEqual(d.growth(.6,65e-6,0),0)
        self.assertAlmostEqual(d.growth(.6,65e-6,-40),-.00156)

    def test_panel_mass_units(self):
        self.assertAlmostEqual(d.panel_mass(.6,.6,.004,2500),3.6)
        self.assertAlmostEqual(d.panel_mass(.6,.6,.004,1200),1.728)

    def test_deflection_scaling_and_invalid_linear_example(self):
        a = d.strip_deflection(50,.6,.004,2.3e9)
        b = d.strip_deflection(50,.3,.004,2.3e9)
        self.assertAlmostEqual(a['deflection_mm']/b['deflection_mm'],16)
        self.assertTrue(a['linear_warning'])
        self.assertFalse(b['linear_warning'])
        self.assertEqual(d.strip_deflection(0,.6,.004,2.3e9)['deflection_mm'],0)

    def test_load_equilibrium_and_lost_support(self):
        a=d.retention(3.6,2,30,.03,.5,2)
        b=d.retention(3.6,2,30,.03,.5,1)
        self.assertAlmostEqual(2*a['ideal_per_support_n'],42.516)
        self.assertAlmostEqual(b['ideal_per_support_n'],42.516)
        self.assertAlmostEqual(a['upper_retainer_total_n']+a['lower_normal_reaction_n'],30)
        self.assertAlmostEqual(a['upper_retainer_total_n']*.5,42.516*.03+30*.25)

    def test_heat_resistance_and_ventilation(self):
        # Two equal film resistances plus slab: R=1+1+1=3 m2 K/W.
        g=d.heat_conductance(3,1,1,1,1,0)
        self.assertAlmostEqual(g,1)
        self.assertAlmostEqual(d.heat_conductance(3,1,1,1,1,3600)-g,1206)

    def test_transient_boundaries_and_cooling(self):
        self.assertEqual(d.lumped_rise(300,10,10000,0)['rise_k'],0)
        self.assertAlmostEqual(d.lumped_rise(300,10,10000,1000)['rise_k'],30*(1-math.exp(-1)))
        self.assertAlmostEqual(d.lumped_rise(0,10,10000,1000,30)['rise_k'],30/math.e)
        self.assertAlmostEqual(d.lumped_rise(300,10,10000,1e8)['rise_k'],30)

    def test_two_zone_energy_and_symmetry(self):
        for mix in (0,1,20,1e6):
            a=d.two_zone(80,220,4,4,mix)
            self.assertAlmostEqual(a['loss_w'],300)
        self.assertAlmostEqual(d.two_zone(80,220,4,4,0)['difference_k'],35)
        self.assertEqual(d.two_zone(100,100,4,4,2)['difference_k'],0)
        self.assertLess(d.two_zone(80,220,4,4,1e6)['difference_k'],.001)

    def test_relaxation_can_remove_friction_margin(self):
        self.assertEqual(d.friction_reserve(200,.5,.2,20)['reserve_n'],0)
        self.assertLess(d.friction_reserve(200,.25,.2,20)['reserve_n'],0)
        self.assertEqual(d.friction_reserve(200,0,.2,20)['assumed_friction_n'],0)

    def test_installed_clear_does_not_mean_removable(self):
        r=d.removal_example()
        self.assertFalse(r['installed_overlap'])
        self.assertIn(0,r['lift_then_out_hit_segments'])
        self.assertEqual(r['out_then_lift_hit_segments'],[])
        self.assertEqual(r['reverse_install_hit_segments'],[])

    def test_contact_and_midpath_are_conflicts(self):
        b=Box((0,0,0),(1,1,1)); obstacle=Box((2,0,0),(3,1,1))
        self.assertEqual(path_hits(b,[(0,0,0),(1,0,0)],obstacle),[0])
        self.assertEqual(path_hits(b,[(0,0,0),(5,0,0)],obstacle),[0])

    def test_invalid_inputs(self):
        calls=[lambda:d.growth(0,1,1),lambda:d.growth(1,1,float('nan')),
               lambda:d.panel_mass(1,1,-1,1),lambda:d.strip_deflection(1,1,0,1),
               lambda:d.retention(1,0,1,1,1,0),lambda:d.retention(1,0,1,1,1,1.5),
               lambda:d.heat_conductance(1,1,1,0,1,0),lambda:d.two_zone(1,1,0,1,1),
               lambda:d.lumped_rise(1,0,1,1),lambda:d.friction_reserve(1,1.1,1,1)]
        for call in calls:
            with self.assertRaises(ValueError): call()

    def test_all_modes_no_enclosure_pass(self):
        rows=d.results()['clearance_sensitivity']
        self.assertEqual(len(rows),48)
        self.assertEqual({r['mode'] for r in rows},set(d.MODES))
        for r in rows:
            self.assertIn(r['inherited_status'],('UNRESOLVED','REACH_REJECTED'))
        # Moving a wall cannot fix unreachable parked carriages.
        for r in rows:
            if r['mode']!='S': self.assertEqual(r['inherited_status'],'REACH_REJECTED')

    def test_reproduction(self):
        saved=Path(__file__).with_name('d5-results.json').read_text()
        self.assertEqual(saved,json.dumps(d.results(),indent=2,sort_keys=True,allow_nan=False)+'\n')


if __name__ == '__main__':
    unittest.main()
