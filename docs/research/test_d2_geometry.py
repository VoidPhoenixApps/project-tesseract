import unittest
from dataclasses import replace
from d2_geometry import (Box, Parameters, MODES, ASSIGNMENTS, orient, oriented,
    sweep, ccd, path_hits, beds, regions, nozzle_reach, required_carriage,
    components, mode_screen, eligibility, classification, results)


class GeometryTests(unittest.TestCase):
    def setUp(self):
        self.p=Parameters()

    def test_exact_ABBA_transforms(self):
        p=(-30,20,5)
        self.assertEqual([orient(p,h) for h in range(1,5)],
                         [(-30,20,5),(30,20,5),(-30,-20,5),(30,-20,5)])
        for h in range(1,5):
            self.assertEqual(orient(orient(p,h),h),p)
            self.assertEqual(orient(p,h,False),p)
        self.assertEqual(oriented(Box((-50,-8,10),(8,50,70)),4),Box((-8,-50,10),(50,8,70)))

    def test_carriage_nozzle_offset_and_containment(self):
        for h in range(1,5):
            r=Box((-175,-175,0),(175,175,200))
            carriage=required_carriage(r,h,self.p)
            self.assertEqual(nozzle_reach(carriage,h,self.p),r)
            self.assertFalse(nozzle_reach(carriage,h,self.p).contains(r.inflate(.01)))

    def test_midpath_collision_not_at_endpoints(self):
        a=Box((-1,-1,-1),(1,1,1)); b=Box((4,-1,-1),(6,1,1))
        self.assertFalse(a.overlaps(b)); self.assertFalse(a.move((10,0,0)).overlaps(b))
        self.assertEqual(ccd(a,(0,0,0),(10,0,0),b),(.3,.7))
        self.assertEqual(path_hits(a,[(0,0,0),(10,0,0)],b),[0])

    def test_moving_versus_moving_and_parked(self):
        a=Box((0,0,0),(2,2,2))
        self.assertIsNotNone(ccd(a,(0,0,0),(10,0,0),a,(10,0,0),(0,0,0)))
        self.assertIsNone(ccd(a,(0,0,0),(10,0,0),a,(3,0,0),(13,0,0)))
        self.assertIsNotNone(ccd(a,(0,0,0),(10,0,0),a,(5,0,0),(5,0,0)))

    def test_three_dimensions_and_tall_completed_object(self):
        body=Box((-5,-5,10),(5,5,70)); path=[(-30,0,10),(30,0,10)]
        for height,expected in ((5,False),(200,True)):
            obj=Box((-10,-10,0),(10,10,height))
            self.assertEqual(bool(path_hits(body,path,obj)),expected)
        # Downward bed Z translates the object; it does not erase its height.
        obj=Box((-10,-10,0),(10,10,200)).move((0,0,-195))
        self.assertFalse(path_hits(body,path,obj))

    def test_sweep_is_conservative_not_exact_diagonal_contact(self):
        a=Box((0,0,0),(1,1,1)); b=Box((0,9,0),(1,10,1))
        path=[(0,0,0),(10,10,0)]
        self.assertTrue(sweep(a,path).overlaps(b))
        self.assertIsNone(ccd(a,*path,b))

    def test_touching_and_zero_relative_velocity(self):
        b=Box((0,0,0),(1,1,1))
        self.assertIsNotNone(ccd(b,(0,0,0),(0,0,0),b,(1,0,0),(1,0,0)))
        self.assertIsNone(ccd(b,(0,0,0),(0,0,0),b,(1.01,0,0),(1.01,0,0)))

    def test_all_eight_bed_layouts(self):
        for mode in MODES:
            bs=beds(mode,self.p)
            self.assertEqual(len(bs),4)
            for b in bs.values():
                self.assertEqual((b.hi[0]-b.lo[0],b.hi[1]-b.lo[1]),(180,180))
                self.assertEqual(b.lo[2],0)
        self.assertEqual(beds('R',self.p)[1].hi[0],beds('R',self.p)[2].lo[0])
        self.assertEqual(beds('C',self.p)[3].hi[1],beds('C',self.p)[1].lo[1])

    def test_both_pair_directions_single_head_reach(self):
        for mode,size in (('R',(350,170)),('C',(170,350))):
            for r in regions(mode,self.p):
                self.assertEqual((r.hi[0]-r.lo[0],r.hi[1]-r.lo[1]),size)
            self.assertEqual(eligibility(mode,'local',self.p),'FUNCTION_REJECTED')
            self.assertEqual(eligibility(mode,'local+fifth',self.p),'FUNCTION_REJECTED')
            self.assertEqual(eligibility(mode,'extended',self.p),'REACH_ONLY')

    def test_four_mixed_assignments_and_fifth(self):
        expected={'M12':((1,2),(1,3,4)),'M34':((3,4),(3,1,2)),
                  'M13':((1,3),(1,2,4)),'M24':((2,4),(2,1,3))}
        for mode,(pair,heads) in expected.items():
            self.assertEqual(MODES[mode][0],pair)
            self.assertEqual(ASSIGNMENTS[mode],heads)
            self.assertEqual(eligibility(mode,'local+fifth',self.p),'REACH_ONLY')
            screen=mode_screen(mode,self.p)
            self.assertTrue(all(screen['nominal_nozzle_reach']))
            self.assertEqual(screen['classification'],'REACH_REJECTED')

    def test_joined_full_region_and_parked_machines(self):
        r=regions('J',self.p)[0]
        self.assertEqual(r,Box((-175,-175,0),(175,175,0)))
        s=mode_screen('J',self.p)
        self.assertEqual(s['heads'],(1,))
        self.assertTrue(s['enclosure_outside'])  # parking is not free space
        self.assertEqual(s['classification'],'REACH_REJECTED')
        self.assertEqual(eligibility('J','single-toolchanger',self.p),'REACH_ONLY')
        self.assertEqual(eligibility('S','single-toolchanger',self.p),'FUNCTION_REJECTED')

    def test_stacked_beams_do_not_clear_columns(self):
        s=mode_screen('C',self.p,'stacked-bridge')
        self.assertTrue(any('Z-column' in x and 'beam' in x for x in s['machine_overlap_candidates']))
        self.assertEqual(s['classification'],'REACH_REJECTED')

    def test_mirror_savings_and_outer_penalty(self):
        a=components(1,self.p)['body']; b=components(2,self.p)['body']
        # Same-height near-seam noses 20 mm apart: mirror clear, common collides.
        self.assertFalse(a.move((-10,0,0)).overlaps(b.move((10,0,0))))
        self.assertTrue(a.move((-10,0,0)).overlaps(a.move((10,0,0))))
        self.assertEqual(b.hi[0]-a.hi[0],42)
        self.assertGreater(components(2,self.p)['cable'].hi[0],b.hi[0])

    def test_reconfiguration_midpath_against_occupied_neighbor(self):
        carrier=Box((-10,-10,-20),(10,10,0))
        # Overhanging object/cable reaches below nominal sheet plane.
        occupied=Box((40,-5,-5),(60,5,150))
        self.assertEqual(path_hits(carrier,[(0,0,0),(100,0,0)],occupied),[0])
        self.assertFalse(path_hits(carrier,[(0,-30,0),(100,-30,0)],occupied))

    def test_whole_beam_path_past_tall_neighbor(self):
        beam=Box((-290,-15,90),(290,15,120))
        tall=Box((100,-10,0),(160,10,200))
        path=[(0,-60,0),(0,60,0)]
        self.assertFalse(beam.move(path[0]).overlaps(tall))
        self.assertFalse(beam.move(path[1]).overlaps(tall))
        self.assertEqual(path_hits(beam,path,tall),[0])

    def test_head_path_past_parked_gantry(self):
        head=components(1,self.p)
        parked=Box((-290,245,90),(290,275,120))
        path=[(0,150,60),(0,330,60)]
        hits={name:path_hits(b,path,parked) for name,b in head.items()}
        self.assertTrue(hits['body'])
        self.assertFalse(head['body'].move(path[0]).overlaps(parked))
        self.assertFalse(head['body'].move(path[1]).overlaps(parked))

    def test_unknown_or_invalid_cannot_pass(self):
        for complete,known in ((False,True),(True,False),(False,False)):
            self.assertEqual(classification(complete,known,False),'UNRESOLVED')
        self.assertEqual(eligibility('S','unspecified-rails',self.p),'UNRESOLVED')
        for invalid in ({'gap':-1},{'margin':91},{'clearance':float('nan')}):
            with self.assertRaises(ValueError): Parameters(**invalid)
        with self.assertRaises(ValueError): Box((0,0,0),(-1,1,1))
        with self.assertRaises(ValueError): sweep(Box((0,0,0),(1,1,1)),[])
        with self.assertRaises(ValueError): mode_screen('S',self.p,'rotating-unknown')

    def test_sensitivity_changes_reach_or_enclosure(self):
        self.assertFalse(all(mode_screen('S',replace(self.p,gap=200))['nominal_nozzle_reach']))
        small=mode_screen('J',self.p)['enclosure_outside']
        large=mode_screen('J',replace(self.p,frame_inner=450))['enclosure_outside']
        self.assertTrue(small); self.assertFalse(large)

    def test_park_reach_default_and_boundary(self):
        for topo in ('moving-bridge','stacked-bridge'):
            default=mode_screen('J',self.p,topo)
            self.assertEqual(default['park_nozzle_reach'],{2:False,3:False,4:False})
            self.assertEqual(default['park_required_carriage_mm'][2]['lo'][:2],(280,280))
            boundary=mode_screen('J',replace(self.p,park=220),topo)
            self.assertTrue(all(boundary['park_nozzle_reach'].values()))
            self.assertEqual(boundary['classification'],'UNRESOLVED')
            outside=mode_screen('J',replace(self.p,park=220.01),topo)
            self.assertFalse(any(outside['park_nozzle_reach'].values()))

    def test_results_deterministic_and_no_feasibility_pass(self):
        a=results(); self.assertEqual(a,results())
        self.assertEqual(len(a['screens']['moving-bridge']),8)
        for screens in a['screens'].values():
            for s in screens:
                self.assertEqual(s['classification'],'UNRESOLVED' if s['mode']=='S' else 'REACH_REJECTED')


if __name__=='__main__': unittest.main()
