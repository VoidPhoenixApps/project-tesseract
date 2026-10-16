"""S1 offline acceptance/counterexample tests; no physical feasibility inference."""
from dataclasses import replace
import json
from pathlib import Path
import unittest
from d6_model import Box, MODES
from s1_contract import Coordinator, synthetic_jobs, demo

ROUTE = (Box((-20, 0, 0), (-10, 10, 10)),)


class ContractTests(unittest.TestCase):
    def test_eight_mode_counts_and_independent_metadata(self):
        expected = {'S': 4, 'R': 2, 'C': 2, 'M12': 3, 'M34': 3,
                    'M13': 3, 'M24': 3, 'J': 1}
        self.assertEqual(set(MODES), set(expected))
        for mode, count in expected.items():
            with self.subTest(mode=mode):
                c = Coordinator(mode)
                js = synthetic_jobs(mode)
                self.assertTrue(c.admit([c.stamp(j) for j in js])[0])
                c.model.advance(1)
                self.assertEqual(len(c.model.runs), count)
                self.assertEqual([r.progress for r in c.model.runs.values()],
                                 list(range(1, count + 1)))
                for attr in ('height', 'layer_mm', 'bed_c', 'nozzle_c'):
                    self.assertEqual(len({getattr(j, attr) for j in js}), count)

    def test_late_arrival_pause_cancel_finish_and_retained_occupancy(self):
        c = Coordinator()
        js = synthetic_jobs()
        js[0] = replace(js[0], height=2)
        self.assertTrue(c.admit([c.stamp(js[0])])[0])
        c.model.advance(1)
        self.assertTrue(c.admit([c.stamp(j) for j in js[1:]])[0])
        c.model.advance(.5)
        self.assertEqual([r.progress for r in c.model.runs.values()], [1.5, 1, 1.5, 2])
        self.assertTrue(c.model.pause('j2'))
        self.assertTrue(c.model.cancel('j3'))
        c.model.advance(.5)
        self.assertEqual([r.state for r in c.model.runs.values()],
                         ['FINISHED_OCCUPIED', 'PAUSED', 'CANCELLED_OCCUPIED', 'RUNNING'])
        self.assertEqual(c.model.runs['j4'].progress, 4)
        self.assertFalse(c.admit([c.stamp(replace(js[0], name='replacement'))])[0])
        self.assertFalse(c.model.clear('j3'))
        self.assertEqual(c.transition('M12', (1, 2), ROUTE, support_proven=True)[1],
                         'occupied affected bed')
        self.assertEqual(c.epochs, dict.fromkeys(range(1, 5), 0))
        self.assertTrue(c.model.resume('j2'))
        c.model.advance(1)
        self.assertEqual(c.model.runs['j2'].progress, 3)
        self.assertEqual(c.model.runs['j3'].progress, 1.5)

    def test_epoch_aba_and_unaffected_job_preservation(self):
        c = Coordinator()
        js = synthetic_jobs()
        stale = c.stamp(js[0])
        unaffected = c.stamp(js[3])
        self.assertTrue(c.admit([unaffected])[0])
        for target in ('M12', 'S'):
            self.assertTrue(c.transition(target, (1, 2), ROUTE, support_proven=True)[0])
        self.assertEqual(c.admit([stale])[1], 'stale configuration')
        self.assertEqual(c.epochs, {1: 2, 2: 2, 3: 0, 4: 0})
        c.model.advance(1)
        self.assertEqual(c.model.runs['j4'].progress, 4)
        self.assertTrue(c.admit([c.stamp(js[0])])[0])

    def test_metadata_rejections_are_atomic(self):
        c = Coordinator('R')
        a, b = [c.stamp(j) for j in synthetic_jobs('R')]
        for bad in (replace(b, dialect='unknown'), replace(b, profile=''),
                    replace(b, mesh=''), replace(b, epochs=()),
                    replace(b, bed_targets=((3, 60), (4, 100)))):
            self.assertFalse(c.admit([a, bad])[0])
            self.assertFalse(c.model.runs)
        # Different temperatures between unrelated groups are permitted.
        self.assertTrue(c.admit([a, b])[0])

    def test_shared_axes_heaters_and_group_z_reject_independence(self):
        for resource in ('xy:shared-beam', 'z:joined-lift', 'heater:shared'):
            c = Coordinator()
            js = [replace(j, resources=j.resources | {resource}) for j in synthetic_jobs()]
            self.assertEqual(c.admit([c.stamp(j) for j in js])[1], 'resource conflict')
            self.assertFalse(c.model.runs)

    def test_joined_exclusive_and_park_or_route_collision(self):
        c = Coordinator('J')
        j = synthetic_jobs('J')[0]
        self.assertTrue(c.admit([c.stamp(j)])[0])
        self.assertFalse(c.admit([c.stamp(replace(j, name='other', head=2))])[0])
        c = Coordinator('J')
        c.model.parks[2] = (j.objects[0], True)
        self.assertFalse(c.admit([c.stamp(j)])[0])
        c = Coordinator()
        j = synthetic_jobs()[3]
        self.assertTrue(c.admit([c.stamp(j)])[0])
        self.assertEqual(c.transition('M12', (1, 2), j.objects, support_proven=True)[1],
                         'transition collision')
        self.assertEqual(c.model.mode, 'S')

    def test_fault_and_reconnect_do_not_restore_authority(self):
        c = Coordinator()
        js = synthetic_jobs()
        old = c.stamp(js[0])
        c.admit([c.stamp(j) for j in js])
        c.fault('lost executor or power state unknown')
        c.model.evidence.connected = True
        c.model.advance(1)
        self.assertEqual(len(c.model.runs), 4)
        self.assertTrue(all(r.state == 'FAULTED' and r.progress == 0
                            for r in c.model.runs.values()))
        self.assertFalse(c.reset(human_ack=True))
        self.assertFalse(c.model.resume('j1'))
        self.assertEqual(c.admit([old])[1], 'stale configuration')
        for name in list(c.model.runs):
            self.assertTrue(c.model.clear(name, removal_confirmed=True, cool=True,
                                          isolated_access=True))
        c.model.evidence.stamp = c.model.now
        self.assertTrue(c.reset(human_ack=True))
        self.assertFalse(c.admit([old])[0])
        self.assertTrue(c.admit([c.stamp(js[0])])[0])

    def test_stale_observation_faults_all(self):
        c = Coordinator()
        c.admit([c.stamp(j) for j in synthetic_jobs()])
        old = c.stamp(synthetic_jobs()[0])
        c.model.advance(101)
        self.assertEqual(c.model.state, 'FAULT_LATCHED')
        self.assertTrue(all(r.state == 'FAULTED' for r in c.model.runs.values()))
        for name in list(c.model.runs):
            c.model.clear(name, removal_confirmed=True, cool=True, isolated_access=True)
        c.model.evidence.stamp = c.model.now
        self.assertTrue(c.reset(human_ack=True))
        self.assertEqual(c.admit([old])[1], 'stale configuration')

    def test_saved_trace(self):
        self.assertEqual(Path(__file__).with_name('s1-results.json').read_text(),
                         json.dumps(demo(), indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    unittest.main()
