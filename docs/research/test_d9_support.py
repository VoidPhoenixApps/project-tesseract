"""Negative/boundary tests of a desk model, not physical fault injection."""
from dataclasses import replace
import unittest

from d9_support import (MODES, Observation, affected_beds, handoff, reactions,
                        arrest, cantilever, transfer_errors, uncovered)


class D9Tests(unittest.TestCase):
    def test_exact_eight_partitions(self):
        expected = {'S': [(1,), (2,), (3,), (4,)], 'R': [(1, 2), (3, 4)],
                    'C': [(1, 3), (2, 4)], 'M12': [(1, 2), (3,), (4,)],
                    'M34': [(3, 4), (1,), (2,)], 'M13': [(1, 3), (2,), (4,)],
                    'M24': [(2, 4), (1,), (3,)], 'J': [(1, 2, 3, 4)]}
        self.assertEqual({k: sorted(map(tuple, v)) for k, v in MODES.items()},
                         {k: sorted(v) for k, v in expected.items()})

    def test_affected_closure_and_reverse(self):
        for a, b, expected in [('S', 'M12', {1, 2}), ('M12', 'R', {3, 4}),
                                ('R', 'C', {1, 2, 3, 4}), ('M24', 'J', {1, 2, 3, 4}),
                                ('M12', 'M13', {1, 2, 3})]:
            self.assertEqual(affected_beds(a, b), expected)
            self.assertEqual(affected_beds(b, a), expected)
        self.assertEqual(affected_beds('S', 'M12', ((3, 4), (2, 3))), {1, 2, 3, 4})

    def test_all_mode_pairs_partition_coverage(self):
        for a in MODES:
            for b in MODES:
                affected = affected_beds(a, b)
                for group in MODES[a] + MODES[b]:
                    if affected.intersection(group):
                        self.assertTrue(set(group) <= affected)

    def test_idle_inventory_and_upstream_brake(self):
        inventory = ('bed1', 'parked_head', 'unused_platform')
        support = {b: [(b, 'belt', 'frame')] for b in inventory}
        restraint = {b: [(b, 'belt', 'motor_brake', 'frame')] for b in inventory}
        self.assertEqual(uncovered(inventory, support, restraint), {})
        self.assertEqual(set(uncovered(inventory, support, restraint, ('belt',))), set(inventory))
        self.assertEqual(uncovered(inventory, {}, {})['unused_platform'], ['L', 'R'])

    def test_independent_catch_and_common_root(self):
        support = {'head': [('guide', 'root')]}
        restraint = {'head': [('catch', 'root')]}
        self.assertEqual(uncovered(('head',), support, restraint, ('guide',)), {'head': ['L']})
        self.assertEqual(uncovered(('head',), support, restraint, ('root',)), {'head': ['L', 'R']})
        self.assertEqual(uncovered(('head',), {'head': [()]}, {'head': [()]}), {'head': ['L', 'R']})

    def test_stale_future_epoch_upstream_disagreement(self):
        o = Observation(4, 10, True, True)
        self.assertTrue(o.usable(4, 10.1, .2))
        for item, epoch, now, age in [(o, 4, 10.3, .2), (o, 4, 9, .2), (o, 5, 10, .2),
                                      (replace(o, downstream=False), 4, 10, .2),
                                      (replace(o, agrees=False), 4, 10, .2),
                                      (o, 4, float('nan'), .2), (o, 4, 10, -1)]:
            self.assertFalse(item.usable(epoch, now, age))

    def test_supported_handoff_and_missing_overlap(self):
        self.assertEqual(transfer_errors(handoff()), [])
        self.assertTrue(any('release before' in s for s in transfer_errors([handoff()[0], handoff()[-1]])))
        self.assertTrue(transfer_errors([]))

    def test_fault_at_every_handoff_state(self):
        mutations = [dict(old_support=False, new_support=False), dict(restraint=False),
                     dict(compatible=False), dict(observed=False), dict(at_datum=False),
                     dict(selector_full=False, torque_enabled=True)]
        for i in range(4):
            for mutation in mutations:
                states = handoff()
                states[i] = replace(states[i], **mutation)
                with self.subTest(i=i, mutation=mutation):
                    self.assertTrue(transfer_errors(states))

    def test_unaccepted_load_and_finished_occupancy(self):
        states = handoff()
        states[-1] = replace(states[-1], load_accepted=False)
        self.assertTrue(transfer_errors(states))
        self.assertIn('occupied affected bed', transfer_errors(handoff(), {2}, {1, 2}))
        self.assertEqual(transfer_errors(handoff(), {3}, {1, 2}), [])  # only declared isolation

    def test_signed_reaction_equilibrium_and_uplift(self):
        for e in (-150, -120, 0, 120, 150):
            a, b = reactions(100, 240, e)
            self.assertAlmostEqual(a+b, 100)
            self.assertAlmostEqual((b-a)*120, 100*e)
        self.assertEqual(reactions(100, 240, 120), (0, 100))
        self.assertLess(reactions(100, 240, 150)[0], 0)

    def test_arrest_energy_and_scaling(self):
        a, b = arrest(1, .01, .02, 1), arrest(12, .01, .02, 1)
        self.assertEqual(a['precatch_drop_mm'], b['precatch_drop_mm'])
        self.assertAlmostEqual(b['absorbed_energy_j'], 12*a['absorbed_energy_j'])
        self.assertAlmostEqual(b['average_catch_force_n']*.001, b['absorbed_energy_j'])
        self.assertGreater(arrest(12, .01, .05, 1)['average_catch_force_n'], b['average_catch_force_n'])

    def test_cubic_arm_scaling(self):
        a, b = cantilever(20, 90, 1e7), cantilever(20, 180, 1e7)
        self.assertAlmostEqual(b['tip_deflection_mm'], 8*a['tip_deflection_mm'])
        self.assertAlmostEqual(b['root_moment_nm'], 2*a['root_moment_nm'])


if __name__ == '__main__':
    unittest.main()
