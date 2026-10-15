"""Synthetic counterexamples and invariants only; no firmware/hardware tests."""
from dataclasses import replace
import json
from pathlib import Path
import unittest
from d6_model import Box, Evidence, Job, Model, MODES, demo, power


def fixture(mode='S', budget=2000):
    parks = {h: (Box((h * 30, -100, 0), (h * 30 + 10, -90, 10)), True)
             for h in range(1, 5)}
    return Model(mode=mode, budget=budget, ttl=100, parks=parks)


def jobs(mode='S'):
    # Artificial mutually disjoint strips, NOT Tesseract bed geometry or D2 repair.
    return [Job('j%d' % i, group, i,
                (Box((i * 100, 0, 0), (i * 100 + 10, 10, 20)),),
                (Box((i * 100 - 5, -5, -5), (i * 100 + 15, 15, 30)),),
                Box((-1000, -1000, -1000), (1000, 1000, 1000)),
                frozenset('z:%d' % b for b in group),
                200, i, 20 * i, 50 + 5 * i, 190 + 10 * i, .1 * i)
            for i, group in enumerate(MODES[mode], 1)]


class SchedulingTests(unittest.TestCase):
    def test_all_eight_modes_and_group_ownership(self):
        self.assertEqual(len(MODES), 8)
        for mode, groups in MODES.items():
            with self.subTest(mode=mode):
                m = fixture(mode)
                self.assertTrue(m.admit(jobs(mode))[0])
                self.assertEqual({r.job.beds for r in m.runs.values()}, set(groups))
                m.advance(2)
                self.assertEqual([r.progress for r in m.runs.values()],
                                 [2 * i for i in range(1, len(groups) + 1)])

    def test_four_unrelated_progress_temperatures_and_layers(self):
        m = fixture()
        self.assertTrue(m.admit(jobs())[0])
        m.advance(3)
        self.assertEqual([r.progress for r in m.runs.values()], [3, 6, 9, 12])
        self.assertEqual(len({r.job.layer_mm for r in m.runs.values()}), 4)
        self.assertEqual(len({r.job.nozzle_c for r in m.runs.values()}), 4)
        self.assertEqual(len({r.job.bed_c for r in m.runs.values()}), 4)

    def test_pause_cancel_one_leave_others_running(self):
        m = fixture()
        m.admit(jobs())
        self.assertTrue(m.pause('j1'))
        self.assertTrue(m.cancel('j2'))
        m.advance(1)
        self.assertEqual([r.progress for r in m.runs.values()], [0, 0, 3, 4])
        self.assertTrue(m.resume('j1'))
        self.assertFalse(m.resume('j2'))
        self.assertFalse(m.clear('j2'))
        self.assertIn('j2', m.runs)

    def test_different_completion_times_and_new_job(self):
        m = fixture()
        js = jobs()
        js[0] = replace(js[0], height=1)
        m.admit(js)
        m.advance(1)
        self.assertEqual(m.runs['j1'].state, 'FINISHED_OCCUPIED')
        replacement = replace(js[0], name='new')
        self.assertFalse(m.admit([replacement])[0])
        self.assertTrue(m.clear('j1', removal_confirmed=True, cool=True, isolated_access=True))
        self.assertTrue(m.admit([replacement])[0])
        self.assertEqual(m.runs['j4'].state, 'RUNNING')

    def test_partial_arrival_without_stopping_other_job(self):
        m = fixture()
        js = jobs()
        self.assertTrue(m.admit(js[:1])[0])
        m.advance(1)
        self.assertTrue(m.admit(js[1:])[0])
        m.advance(1)
        self.assertEqual(m.runs['j1'].progress, 2)
        self.assertEqual(m.runs['j2'].progress, 2)

    def test_occupied_and_cancelled_transition_rejected(self):
        for cancel in (False, True):
            m = fixture()
            m.admit(jobs())
            if cancel:
                m.cancel('j1')
            ok, reason = m.transition('M12', (1, 2),
                                     (Box((-20, 0, 0), (-10, 10, 10)),), support_proven=True)
            self.assertFalse(ok)
            self.assertEqual(reason, 'occupied affected bed')
            self.assertEqual(m.mode, 'S')

    def test_empty_group_and_ungroup_unaffected_job(self):
        m = fixture()
        m.admit([jobs()[3]])
        route = (Box((-20, 0, 0), (-10, 10, 10)),)
        for target in ('M12', 'S'):
            self.assertTrue(m.transition(target, (1, 2), route, support_proven=True)[0])
        self.assertEqual(m.runs['j4'].state, 'RUNNING')

    def test_transition_evidence_and_affected_domain(self):
        for case in ('domain', 'support', 'datum', 'route'):
            m = fixture()
            m.evidence.at_datum = case != 'datum'
            route = () if case == 'route' else (Box((-20, 0, 0), (-10, 10, 10)),)
            self.assertFalse(m.transition('J', (1,) if case == 'domain' else (1, 2, 3, 4),
                                          route, support_proven=case != 'support')[0])

    def test_transition_route_hits_unaffected_object(self):
        m = fixture()
        j = jobs()[3]
        m.admit([j])
        self.assertEqual(m.transition('M12', (1, 2), j.objects, support_proven=True)[1],
                         'transition collision')

    def test_joined_full_region_head_exclusive(self):
        m = fixture('J')
        j = jobs('J')[0]
        self.assertTrue(m.admit([j])[0])
        self.assertFalse(m.admit([replace(j, name='second', head=2)])[0])
        self.assertFalse(fixture('J').admit([jobs()[0]])[0])

    def test_unknown_unreachable_and_occupied_parks(self):
        for variant in ('unknown', 'unreachable', 'occupied'):
            m = fixture('J')
            if variant == 'unknown':
                del m.parks[2]
            elif variant == 'unreachable':
                m.parks[2] = (m.parks[2][0], False)
            else:
                m.parks[2] = (jobs('J')[0].objects[0], True)
            self.assertFalse(m.admit(jobs('J'))[0])

    def test_park_park_and_park_obstacle_conflicts(self):
        m = fixture('J')
        m.parks[3] = m.parks[2]
        self.assertFalse(m.admit(jobs('J'))[0])
        m = fixture('J')
        m.obstacles = (m.parks[2][0],)
        self.assertFalse(m.admit(jobs('J'))[0])

    def test_transition_rejects_invalid_park_set(self):
        route = (Box((-20, 0, 0), (-10, 10, 10)),)
        for case in ('park', 'obstacle', 'retained-job'):
            m = fixture()
            if case == 'park':
                m.parks[2] = m.parks[1]
            elif case == 'obstacle':
                m.obstacles = (m.parks[2][0],)
            else:
                m.admit([jobs()[3]])
                m.parks[2] = (jobs()[3].objects[0], True)
            history = list(m.history)
            state = {n: (r.job, r.state, r.progress) for n, r in m.runs.items()}
            self.assertEqual(m.transition('M12', (1, 2), route, support_proven=True)[1],
                             'occupied transition park')
            self.assertEqual(m.mode, 'S')
            self.assertEqual(m.history, history)
            self.assertEqual({n: (r.job, r.state, r.progress) for n, r in m.runs.items()}, state)

    def test_coupled_z_and_shared_axis_constraints(self):
        for shared in ('z:unified-frame', 'xy:shared-beam'):
            m = fixture()
            js = [replace(j, resources=j.resources | {shared}) for j in jobs()]
            self.assertEqual(m.admit(js)[1], 'resource conflict')
            self.assertFalse(m.runs)

    def test_resource_deadlock_prevention_atomic_no_hold_and_wait(self):
        m = fixture()
        a, b = jobs()[:2]
        a = replace(a, resources=frozenset(('lift-A', 'lift-B')))
        b = replace(b, resources=frozenset(('lift-B', 'lift-A')))
        self.assertFalse(m.admit([a, b])[0])
        self.assertFalse(m.runs)
        self.assertTrue(m.admit([b])[0])
        self.assertFalse(m.admit([a])[0])
        self.assertEqual(set(m.runs), {'j2'})

    def test_geometry_not_bed_rectangle(self):
        m = fixture()
        a, b = jobs()[:2]
        # Different beds but an overhang intrudes into the other job's sweep.
        b = replace(b, objects=(Box((110, 0, 0), (205, 10, 20)),))
        self.assertEqual(m.admit([a, b])[1], 'job geometry conflict')
        a = replace(a, reach=Box((0, 0, 0), (5, 5, 5)))
        self.assertEqual(fixture().admit([a])[1], 'unreachable geometry')

    def test_same_xy_disjoint_z_and_touching_boundary(self):
        a = Box((0, 0, 0), (10, 10, 10))
        self.assertFalse(a.intersects(Box((0, 0, 11), (10, 10, 20))))
        self.assertTrue(a.intersects(Box((0, 0, 10), (10, 10, 20))))

    def test_stale_failed_and_missing_evidence_latches(self):
        for attr in ('healthy', 'connected', 'position_known', 'sheets_ready',
                     'locks_confirmed', 'guard_permitted', 'thermal_ready'):
            m = fixture()
            m.admit(jobs())
            setattr(m.evidence, attr, False)
            m.advance(1)
            self.assertEqual(m.state, 'FAULT_LATCHED')
            self.assertTrue(all(r.progress == 0 for r in m.runs.values()))
        m = fixture()
        m.admit(jobs())
        m.advance(101)
        self.assertEqual(m.state, 'FAULT_LATCHED')

    def test_future_timestamp_rejected(self):
        m = fixture()
        m.evidence.stamp = 1
        self.assertFalse(m.admit(jobs())[0])

    def test_disconnect_reconnect_no_auto_restart(self):
        m = fixture()
        m.admit(jobs())
        m.evidence.connected = False
        m.advance(1)
        m.evidence.connected = True
        self.assertFalse(m.resume('j1'))
        self.assertFalse(m.reset(human_ack=True))
        for name in list(m.runs):
            m.clear(name, removal_confirmed=True, cool=True, isolated_access=True)
        self.assertFalse(m.reset())
        self.assertTrue(m.reset(human_ack=True))
        self.assertFalse(m.runs)

    def test_heater_budget_overrun_and_boundary(self):
        self.assertTrue(fixture(budget=800).admit(jobs())[0])
        m = fixture(budget=799.99)
        self.assertEqual(m.admit(jobs())[1], 'power budget')
        self.assertFalse(m.runs)

    def test_invalid_inputs(self):
        for value in (float('nan'), float('inf'), -1):
            with self.assertRaises(ValueError):
                power(bed_w=value)
            with self.assertRaises(ValueError):
                replace(jobs()[0], watts=value)
        with self.assertRaises(ValueError):
            Box((0, 0, 0), (0, 1, 1))
        self.assertFalse(fixture().admit([jobs()[0], jobs()[0]])[0])


class PowerTests(unittest.TestCase):
    def test_peak_typical_and_staged_arithmetic(self):
        p = power()
        self.assertEqual(p['peak_dc_w'], 880)
        self.assertEqual(p['typical_dc_w'], 400)
        self.assertEqual(p['one_bed_start_dc_w'], 646)
        self.assertAlmostEqual(p['peak_dc_a'], 36.6666666667)
        self.assertAlmostEqual(p['peak_ac_real_w'], 977.7777777778)

    def test_voltage_efficiency_and_accessory_sensitivity(self):
        self.assertEqual(power(voltage=48)['peak_dc_a'] * 2, power()['peak_dc_a'])
        self.assertEqual(power(accessory_w=50)['peak_dc_w'], 930)
        for args in ({'voltage': 0}, {'efficiency': 0}, {'bed_duty': 1.01}):
            with self.assertRaises(ValueError):
                power(**args)

    def test_reproducible_json(self):
        saved = Path(__file__).with_name('d6-results.json').read_text()
        self.assertEqual(saved, json.dumps(demo(), indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    unittest.main()
