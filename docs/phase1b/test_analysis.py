"""Check physical invariants and counterexamples, not hardware acceptance."""

import unittest
from itertools import product
from pathlib import Path

import analysis as a


class ThermalChecks(unittest.TestCase):
    def test_ambient_and_temperature_exchange(self):
        for strategy in ("center", "x-edge", "y-edge", "corner", "inset"):
            for axis in (0, 1):
                self.assertAlmostEqual(a.gap(20, 20, strategy, axis), 0.2)
                self.assertAlmostEqual(a.gap(100, 40, strategy, axis), a.gap(40, 100, strategy, axis))

    def test_known_interference_and_no_fixed_gap(self):
        self.assertAlmostEqual(a.gap(80, 80), -0.05488)
        low, high = a.cold_interval("center")
        self.assertGreater(low, high)
        low, high = a.cold_interval("inset", error=0.03)
        self.assertLess(low, 0.2)
        self.assertGreater(high, 0.2)

    def test_rotation_and_inset_limits(self):
        for t1, t2 in product(a.TEMPS, repeat=2):
            self.assertAlmostEqual(a.gap(t1, t2, "x-edge", 0), a.gap(t1, t2, "y-edge", 1))
            self.assertAlmostEqual(a.gap(t1, t2, "x-edge", 1), a.gap(t1, t2, "center", 0))
            self.assertAlmostEqual(a.gap(t1, t2, "inset", inset=90), a.gap(t1, t2))
            self.assertAlmostEqual(a.gap(t1, t2, "inset", inset=0), 0.2)

    def test_rigid_translation_does_not_change_relative_edge(self):
        p = a.point((0, 0), (90, 90), (80, 80), 100)
        shifted = a.point((0, 0), (90, 90), (80, 80), 100, frame_shift=(7, -3))
        self.assertAlmostEqual(shifted[0] - p[0], 7)
        self.assertAlmostEqual(shifted[1] - p[1], -3)

    def test_four_corners_equal_heat_symmetry(self):
        c = a.central_corners(dict.fromkeys(a.SIGNS, 100))
        self.assertAlmostEqual(c["A"][0], -c["B"][0])
        self.assertAlmostEqual(c["A"][1], -c["C"][1])
        self.assertAlmostEqual(c["B"][0] - c["A"][0], 0.16224)


class MechanicalChecks(unittest.TestCase):
    def test_rank_and_lost_yaw(self):
        self.assertEqual(a.rank(a.VERTICAL + a.PLANAR), 6)
        self.assertEqual(a.rank(a.VERTICAL + a.PLANAR[1:]), 5)
        self.assertEqual(a.rank(a.VERTICAL + [a.PLANAR[0], a.PLANAR[0], a.PLANAR[2]]), 5)
        guide = a.VERTICAL + [[1, 0, 0, 0, 0, 0], a.PLANAR[2], a.YAW]
        self.assertEqual(a.rank(guide), 6)
        self.assertEqual(a.rank(a.VERTICAL + a.PLANAR + [a.YAW]), 6)

    def test_every_directed_mode_transition(self):
        for start, end in product(a.modes().values(), repeat=2):
            self.assertTrue(a.transition(start, end))
            self.assertTrue(a.transition(start, end, 180, 0))

    def test_collision_and_midpath_counterexample(self):
        modes = a.modes()
        self.assertFalse(a.transition(modes["I"], modes["J"], 190, 0))
        # Endpoints clear, but the continuous segment crosses a stationary box.
        self.assertFalse(a.transition({"A": (-10, 0), "B": (0, 0)},
                                      {"A": (10, 0), "B": (0, 0)}, 2, 0))

    def test_occupied_regions(self):
        modes = a.modes()
        self.assertTrue(a.transition(modes["I"], modes["MH-top"], occupied=("C", "D")))
        self.assertFalse(a.transition(modes["I"], modes["MV-left"], occupied=("A",)))
        self.assertFalse(a.transition(modes["J"], modes["I"], occupied=tuple(a.SIGNS)))

    def test_input_boundaries(self):
        with self.assertRaises(ValueError):
            a.sweep((0, 0), (1, 1), 10)
        with self.assertRaises(ValueError):
            a.modes(cold=-0.1)
        with self.assertRaises(ValueError):
            a.anchor((1, 1), "inset", -1)

    def test_generated_report_current(self):
        self.assertEqual(Path(__file__).with_name("results.md").read_text(encoding="utf-8"), a.report())


if __name__ == "__main__":
    unittest.main()
