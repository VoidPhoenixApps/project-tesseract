import unittest
import json
from pathlib import Path
from dataclasses import replace
from d2_geometry import Box, ccd, MODES, ASSIGNMENTS, Parameters, regions
from d8_geometry import (Envelope, assembly, affine_contact, functional_parts,
                         park, reach, route, scene, witnesses)


class D8Tests(unittest.TestCase):
    def test_affine_growing_box_contact(self):
        # Right face grows 1 -> 5; obstacle begins at 3: first touch t=1/2.
        a=Box((0,0,0),(1,1,1)); end=Box((0,0,0),(5,1,1))
        b=Box((3,0,0),(4,1,1))
        self.assertEqual(affine_contact(a,end,b,b),(.5,1))
        self.assertEqual(affine_contact(end,a,b,b),(0,.5))
        self.assertIsNone(affine_contact(a,end,b.move((0,3,0)),b.move((0,3,0))))

    def test_rigid_reuses_D2_and_touching(self):
        a=Box((0,0,0),(1,1,1)); b=Box((4,0,0),(5,1,1))
        self.assertEqual(affine_contact(a,a.move((10,0,0)),b,b),ccd(a,(0,0,0),(10,0,0),b))
        self.assertIsNotNone(affine_contact(a,a,a.move((1,0,0)),a.move((1,0,0))))

    def test_equal_XY_structure_H_B(self):
        for h in range(1,5):
            hparts=assembly(h,(10,20,150),'H',Envelope())
            bparts=assembly(h,(10,20,0),'B',Envelope())
            for n in ('moving-radial-rail','root-carriage-motor','fixed-tangential-guide','root-cable-reservation'):
                self.assertEqual(hparts[n],bparts[n])
            self.assertEqual(hparts['Z-column'].hi[2]-bparts['Z-column'].hi[2],150)

    def test_radial_rail_tail_does_not_disappear_at_park(self):
        p=Envelope(); b=assembly(1,park(1,0,p),'H',p)['moving-radial-rail']
        self.assertEqual(b.lo[0],-860)
        self.assertEqual(b.hi[0]-b.lo[0],600)
        self.assertTrue(reach(1,[(-175,0,0),(175,0,0)],'H',p))
        self.assertFalse(reach(1,[(175,0,0)],'H',replace(p,rail=450)))
        self.assertFalse(reach(1,[park(1,0,replace(p,park=300))],'H',replace(p,park=300)))

    def test_mirror_functional_parts_but_not_structure(self):
        p=Envelope()
        common=assembly(2,(0,0,0),'H',p,False); mirrored=assembly(2,(0,0,0),'H',p,True)
        self.assertEqual(common['moving-radial-rail'],mirrored['moving-radial-rail'])
        self.assertEqual(mirrored['fan-duct'].hi[0]-common['fan-duct'].hi[0],42)
        self.assertEqual(set(functional_parts(2,p,True)),set(functional_parts(2,p,False)))

    def test_all_modes_parks_return_and_height_ownership(self):
        for m in MODES:
            rs=regions(m,Parameters())
            self.assertEqual(len(rs),len(ASSIGNMENTS[m]))
            for h,r in zip(ASSIGNMENTS[m],rs):
                dep=route(r,h,10,Envelope(),'departure')
                self.assertEqual(route(r,h,10,Envelope(),'approach'),list(reversed(dep)))
                self.assertEqual(dep[-1],park(h,10,Envelope()))
            for a in ('H','B'):
                result=scene(m,a,True,Envelope(),True,finished=ASSIGNMENTS[m][0])
                self.assertEqual(result['status'],'UNRESOLVED_REAL_MACHINE')
                self.assertEqual(result['finished_owner'],ASSIGNMENTS[m][0])

    def test_negative_fixtures_and_height_reversal(self):
        w=witnesses()
        self.assertEqual(w['midpath_tall_object']['endpoint_hits'],[False,False])
        self.assertIsNotNone(w['midpath_tall_object']['interval'])
        self.assertIsNotNone(w['park_blocked_rail']['interval'])
        self.assertIsNotNone(w['adjacent_live_jobs']['interval'])
        self.assertEqual(w['head_Z_column_rise']['interval'],(.1,1))
        self.assertIsNotNone(w['bed_lowering_understructure']['interval'])
        self.assertIsNone(w['bed_down_200_vs_stationary']['B_interval'])
        self.assertIsNotNone(w['bed_down_200_vs_stationary']['H_interval'])

    def test_panels_and_stroke_are_separate_failures(self):
        p=Envelope(rail=450)
        small=scene('J','H',True,p,True)
        large=scene('J','H',True,replace(p,halfwidth=1100,roof=1000),True)
        self.assertTrue(small['failed_head_strokes'])
        self.assertEqual(small['failed_head_strokes'],large['failed_head_strokes'])
        self.assertGreater(small['events']['boundary'],large['events']['boundary'])
        self.assertTrue(scene('S','B',False,replace(p,bed_stroke=100),False)['bed_stroke_failed'])

    def test_one_head_departure_preserves_other_live_paths(self):
        # Changing only the departing owner changes collision exposure, while
        # snapshots still retain all foreign workpieces and parked assemblies.
        isolated=scene('M12','H',False,Envelope(),True,'departure',moving_owner=1)
        together=scene('M12','H',False,Envelope(),True,'departure')
        self.assertEqual(isolated['moving_owner'],1)
        self.assertNotEqual(isolated['events'],together['events'])

    def test_generated_coverage_inventory(self):
        data=json.loads(Path(__file__).with_name('d8-results.json').read_text())
        self.assertEqual(len(data['baseline']),696)
        self.assertEqual(sum(s['mode_cases'] for s in data['sensitivity']),1728)
        for mode in MODES:
            for head in ASSIGNMENTS[mode]:
                for kind in ('departure','approach'):
                    cases=[c for c in data['baseline'] if c['mode']==mode
                           and c['moving_owner']==head and c['route']==kind]
                    self.assertEqual(len(cases),8)
                    self.assertEqual({(c['architecture'],c['orientation'],c['panels']) for c in cases},
                                     {(a,e,p) for a in ('H','B') for e in ('E','common') for p in ('open','enclosed')})
        self.assertTrue(all(c['status']=='UNRESOLVED_REAL_MACHINE' for c in data['baseline']))

    def test_unknown_topology_and_invalid_parameters_do_not_pass(self):
        with self.assertRaises(ValueError): assembly(1,(0,0,0),'R',Envelope())
        for options in ({'cable':0},{'rail':float('nan')},{'rail':30}):
            with self.assertRaises(ValueError): Envelope(**options)


if __name__=='__main__': unittest.main()
