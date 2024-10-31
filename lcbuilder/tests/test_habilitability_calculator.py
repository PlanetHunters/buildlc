import unittest

from lcbuilder.star.HabitabilityCalculator import HabitabilityCalculator

from lcbuilder.HarmonicSelector import HarmonicSelector
from lcbuilder.tests.test_lcbuilder_abstract import TestsLcBuilderAbstract


class TestsHarmonics(TestsLcBuilderAbstract):
    habitability_calculator: HabitabilityCalculator = HabitabilityCalculator()

    def test_au_to_period(self):
        self.assertAlmostEqual(self.habitability_calculator.au_to_period(1, 0.1), 11.51742564487683, 3)

    def test_calculate_semi_major_axis(self):
        au = 0.100
        self.assertAlmostEqual(
            self.habitability_calculator.calculate_semi_major_axis(
                self.habitability_calculator.au_to_period(1, au),
                0, 0, 1, 0, 0
            )[0],
            au,
            3
        )

    def test_calculate_teq(self):
        teq_default_albedo = (
            self.habitability_calculator.calculate_teq(1, 0.1, 0.1, 1,
                                                       0.1, 0.1,20, 0.1,
                                                       0.1, 6000, 100, 100,
                                                       albedo=0.3)
        )
        teq_albedo_0 = (
            self.habitability_calculator.calculate_teq(1, 0.1, 0.1, 1,
                                                       0.1, 0.1,20, 0.1,
                                                       0.1, 6000, 100, 100,
                                                       albedo=0)
        )
        self.assertAlmostEqual(teq_default_albedo[0], 696.2537, 3)
        self.assertAlmostEqual(teq_default_albedo[1], 38.5044, 3)
        self.assertAlmostEqual(teq_albedo_0[0], 761.1899, 3)
        self.assertAlmostEqual(teq_albedo_0[1], 42.0955, 3)


if __name__ == '__main__':
    unittest.main()
