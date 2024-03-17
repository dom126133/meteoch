import unittest
from meteoch import topo

class Topo_testcase(unittest.TestCase):

    def test_LV95toWGS84(self):
        # use http://geodesy.geo.admin.ch/reframe/lv95towgs84?easting=2600000&northing=1200000&format=json
        result = topo.Topo.LV95toWGS84(self,easting=2600000,northing=1200000)
        self.assertAlmostEqual(result[0], 7.438632495, delta=3.33e-5)
        self.assertAlmostEqual(result[1], 46.951082887, delta=2.23e-5)
        # use http://geodesy.geo.admin.ch/reframe/lv95towgs84?easting=2498943.440&northing=1122661.169&format=json
        result = topo.Topo.LV95toWGS84(self,easting=2498943.440,northing=1122661.169)
        self.assertAlmostEqual(result[0], 6.128256956, delta=3.33e-5)
        self.assertAlmostEqual(result[1], 46.247773277, delta=2.23e-5)
        # use value from example
        result = topo.Topo.LV95toWGS84(self,easting=2700000,northing=1100000)
        self.assertAlmostEqual(result[0], 8.730497076, delta=3.33e-5)
        self.assertAlmostEqual(result[1], 46.044130339, delta=2.23e-5)
        #print(self.dms2deg(3))

    def test_WGS84toLV95(self):
        # use https://www.swisstopo.admin.ch/en/coordinates-conversion-navref
        result = topo.Topo.WGS84toLV95(self, lat=46.951082887, long=7.438632495)
        self.assertAlmostEqual(result[0], 2600000, delta=1)
        self.assertAlmostEqual(result[1], 1200000, delta=1)
        result = topo.Topo.WGS84toLV95(self, lat=46.247773277, long=6.128256956)
        self.assertAlmostEqual(result[0], 2498943.440, delta=1)
        self.assertAlmostEqual(result[1], 1122661.169, delta=1)
        result = topo.Topo.WGS84toLV95(self, lat=46.044130339, long=8.730497076)
        self.assertAlmostEqual(result[0], 2700000, delta=1)
        self.assertAlmostEqual(result[1], 1100000, delta=1)

    def test_DecToSexAngle(self):
        # https://www.inchcalculator.com/convert-degrees-to-degrees-minutes-seconds/
        result = topo.Topo.DecToSexAngle(self, 47.314)
        self.assertAlmostEqual(result, 47.18504, places=7)

    def test_SexToDecAngle(self):
        # https://www.rapidtables.com/convert/number/degrees-minutes-seconds-to-degrees.html
        result = topo.Topo.SexToDecAngle(self, 47.18504) # dd.mmss,sss
        self.assertAlmostEqual(result, 47.314, places=7)

if __name__ == '__main__':
    unittest.main()
