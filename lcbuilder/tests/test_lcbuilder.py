import os
import unittest
from lcbuilder.lcbuilder_class import LcBuilder
from lcbuilder.objectinfo.InputObjectInfo import InputObjectInfo
from lcbuilder.objectinfo.MissionFfiCoordsObjectInfo import MissionFfiCoordsObjectInfo
from lcbuilder.objectinfo.MissionFfiIdObjectInfo import MissionFfiIdObjectInfo
from lcbuilder.objectinfo.MissionInputObjectInfo import MissionInputObjectInfo
from lcbuilder.objectinfo.MissionObjectInfo import MissionObjectInfo


class TestsLcBuilder(unittest.TestCase):
    def test_short_cadence(self):
        lc, lc_data, star_info, transits_min_count, sectors, quarters = \
            LcBuilder().build(MissionObjectInfo("TIC 352315023", 'all'), "./")
        self.assertGreater(len(lc), 0)
        self.__test_tess_star_params(star_info)

    def test_short_cadence_kic(self):
        lc, lc_data, star_info, transits_min_count, sectors, quarters = \
            LcBuilder().build(MissionObjectInfo("KIC 12557548", 'all'), "./")
        self.assertGreater(len(lc), 0)
        self.__test_kepler_star_params(star_info)

    def test_short_cadence_epic(self):
        lc, lc_data, star_info, transits_min_count, sectors, quarters = \
            LcBuilder().build(MissionObjectInfo("EPIC 211945201", 'all'), "./")
        self.assertGreater(len(lc), 0)
        self.__test_k2_star_params(star_info)

    def test_long_cadence(self):
        lc, lc_data, star_info, transits_min_count, sectors, quarters = \
            LcBuilder().build(MissionFfiIdObjectInfo("TIC 352315023", 'all'), "./")
        self.assertGreater(len(lc), 0)
        self.__test_tess_star_params(star_info)

    def test_long_cadence_coords(self):
        lc, lc_data, star_info, transits_min_count, sectors, quarters =\
            LcBuilder().build(MissionFfiCoordsObjectInfo(300.47, -71.96, 'all'), "./")
        self.assertGreater(len(lc), 0)
        self.__test_tess_star_params(star_info)

    def test_input_with_id(self):
        directory = os.path.dirname(__file__) + "/input.csv"
        lc, lc_data, star_info, transits_min_count, sectors, quarters = \
            LcBuilder().build(MissionInputObjectInfo("TIC 352315023", directory), "./")
        self.assertGreater(len(lc), 0)
        self.__test_tess_star_params(star_info)

    def test_input_without_id(self):
        directory = os.path.dirname(__file__) + "/input.csv"
        lc, lc_data, star_info, transits_min_count, sectors, quarters = \
            LcBuilder().build(InputObjectInfo(directory), "./")
        self.assertGreater(len(lc), 0)
        self.assertTrue(star_info.mass_assumed)
        self.assertTrue(star_info.radius_assumed)

    def __test_tess_star_params(self, star_info):
        self.assertAlmostEqual(star_info.mass, 0.47, 1)
        self.assertAlmostEqual(star_info.mass_min, 0.44, 2)
        self.assertAlmostEqual(star_info.mass_max, 0.5, 1)
        self.assertAlmostEqual(star_info.radius, 0.18, 1)
        self.assertAlmostEqual(star_info.radius_min, 0.076, 3)
        self.assertAlmostEqual(star_info.radius_max, 0.284, 3)
        self.assertEqual(star_info.teff, 31000)
        self.assertAlmostEqual(star_info.ra, 300.47, 2)
        self.assertAlmostEqual(star_info.dec, -71.96, 2)

    def __test_kepler_star_params(self, star_info):
        self.assertAlmostEqual(star_info.mass, 0.666, 3)
        self.assertAlmostEqual(star_info.mass_min, 0.611, 3)
        self.assertAlmostEqual(star_info.mass_max, 0.733, 3)
        self.assertAlmostEqual(star_info.radius, 0.66, 2)
        self.assertAlmostEqual(star_info.radius_min, 0.606, 3)
        self.assertAlmostEqual(star_info.radius_max, 0.714, 3)
        self.assertEqual(star_info.teff, 4550)
        self.assertAlmostEqual(star_info.ra, 290.966, 3)
        self.assertAlmostEqual(star_info.dec, 51.50472, 3)

    def __test_k2_star_params(self, star_info):
        self.assertAlmostEqual(star_info.mass, 1.102, 3)
        self.assertAlmostEqual(star_info.mass_min, 0.989, 3)
        self.assertAlmostEqual(star_info.mass_max, 1.215, 3)
        self.assertAlmostEqual(star_info.radius, 1.251, 2)
        self.assertAlmostEqual(star_info.radius_min, 1.012, 3)
        self.assertAlmostEqual(star_info.radius_max, 1.613, 3)
        self.assertEqual(star_info.teff, 6043)
        self.assertAlmostEqual(star_info.ra, 136.573975, 3)
        self.assertAlmostEqual(star_info.dec, 19.402252, 3)




if __name__ == '__main__':
    unittest.main()
