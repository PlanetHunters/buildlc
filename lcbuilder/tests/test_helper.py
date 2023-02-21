import unittest

from lcbuilder.helper import LcbuilderHelper

from lcbuilder.HarmonicSelector import HarmonicSelector
from astropy import units as u


class TestsHarmonics(unittest.TestCase):
    def test_convert_from_to(self):
        mass = 1 # solar radius
        mass = LcbuilderHelper.convert_from_to(mass, u.M_sun, u.M_earth)
        self.assertAlmostEqual(332946, mass, 0)

    def test_periods_matching(self):
        assert HarmonicSelector.multiple_of(1, 3)
        assert HarmonicSelector.multiple_of(1, 2)
        assert HarmonicSelector.multiple_of(1, 1)
        assert HarmonicSelector.multiple_of(3, 1)
        assert HarmonicSelector.multiple_of(2, 1)
        assert HarmonicSelector.multiple_of(1, 3.01)
        assert HarmonicSelector.multiple_of(1, 2.01)
        assert HarmonicSelector.multiple_of(1.01, 1)
        assert HarmonicSelector.multiple_of(2.01, 1)
        assert HarmonicSelector.multiple_of(1.01, 1.02)
        assert not HarmonicSelector.multiple_of(3, 2)
        assert not HarmonicSelector.multiple_of(2, 3)
        assert not HarmonicSelector.multiple_of(1.99, 4.06)

    def test_harmonic(self):
        assert HarmonicSelector.is_harmonic(1000.0, 1002.0, 4, 2)
        assert HarmonicSelector.is_harmonic(1000.0, 1004.0, 6, 2)
        assert HarmonicSelector.is_harmonic(1002.0, 1004.0, 2, 4)
        assert HarmonicSelector.is_harmonic(1004.0, 1000.0, 2, 6)
        assert HarmonicSelector.is_harmonic(1000.0, 999.99, 2, 2)
        assert not HarmonicSelector.is_harmonic(1000.0, 996.99, 2, 2)
        assert not HarmonicSelector.is_harmonic(1000.0, 996.99, 2, 4)
        assert HarmonicSelector.is_harmonic(1548.2578492081934, 1548.2588680913175, 7.5, 14.999495533860332)


if __name__ == '__main__':
    unittest.main()
