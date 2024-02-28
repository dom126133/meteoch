import unittest
from meteoch import topo

class Topo_testcase(unittest.TestCase):

    def test_LV95toWGS84(self):
        # Convert CH y/x/h to WGS height
        # use http://geodesy.geo.admin.ch/reframe/lv95towgs84?easting=2600000&northing=1200000&altitude=550.0&format=json
        result = topo.Topo.LV95toWGS84(self,easting=2600000,northing=1200000,altitude=550.0)
        self.assertAlmostEqual(result[0], 7.438632502714563, delta=3.33e-5)
        self.assertAlmostEqual(result[1], 46.95108288705888, delta=2.23e-5)
        self.assertAlmostEqual(result[2], 599.6221912624314, delta=0.5)
        # use http://geodesy.geo.admin.ch/reframe/lv95towgs84?easting=2498943.440&northing=1122661.169&altitude=%20421.465&format=json
        result = topo.Topo.LV95toWGS84(self,easting=2498943.440,northing=1122661.169,altitude=421.465)
        self.assertAlmostEqual(result[0], 6.128256946962308, delta=3.33e-5)
        self.assertAlmostEqual(result[1], 46.24777326180602, delta=2.23e-5)
        self.assertAlmostEqual(result[2], 473.8583213845268, delta=0.5)
        # use value from example
        result = topo.Topo.LV95toWGS84(self,easting=2700000,northing=1100000,altitude=600)
        print(result)
        #self.assertAlmostEqual(result[0], 6.128256946962308, delta=3.33e-5)
        #self.assertAlmostEqual(result[1], 46.24777326180602, delta=2.23e-5)
        self.assertAlmostEqual(result[2], 650.6, delta=0.5)
        print(self.dms2deg(3))
 
    #def test_CHtoWGSlat(self):
    #    # Convert CH y/x to WGS lat
    #    result = topo.Topo.CHtoWGSlat(y,x) # y,x
    #    self.assertAlmostEqual(result, 1, places=1)

    #def test_CHtoWGSlng(self):
    #    # Convert CH y/x to WGS long
    #    result = topo.Topo.CHtoWGSlng(y,x) # y,x
    #    self.assertAlmostEqual(result, 1, places=1)

    #def test_DecToSexAngle(self):
    #    # Convert decimal angle (° dec) to sexagesimal angle (dd.mmss,ss)
    #    result = topo.Topo.DecToSexAngle(dec) # dec
    #    self.assertAlmostEqual(result, 1, places=1)

    #def test_SexAngleToSeconds(self):
    #    # Convert sexagesimal angle (dd.mmss,ss) to seconds
    #    result = topo.Topo.SexAngleToSeconds(dms) # dms
    #    self.assertAlmostEqual(result, 1, places=1)

    def test_SexToDecAngle(self):
        # Convert sexagesimal angle (dd.mmss) to decimal angle (degrees)
        result = topo.Topo.SexToDecAngle(self, 3.2345) # dd.mmss
        self.assertAlmostEqual(result, 3.3958, places=4)

    #def test_WGStoCHh(self):
    #    # Convert WGS lat/long (° dec) and height to CH h
    #    result = topo.Topo.WGStoCHh(self, lat, lng, h) # lat, lng, h
    #    self.assertAlmostEqual(result, 3.3958, places=4)

    #def test_WGStoCHn(self):
    #    # Convert WGS lat/long (° dec) to CH n
    #    result = topo.Topo.WGStoCHn(self, lat, lng) # lat, lng
    #    self.assertAlmostEqual(result, 3.3958, places=4)

    #def test_WGStoCHe(self):
    #    # Convert WGS lat/long (° dec) to CH e
    #    result = topo.Topo.WGStoCHe(self, 46.20222, 6.14569) # lat, lng
    #    self.assertAlmostEqual(result, 3.3958, places=4)

    #def test_LV95toWGS84(self):
    #    # Convert LV95 to WGS84
    #    result = topo.Topo.LV95toWGS84(self, east, north, height) # east, north, height
    #    self.assertAlmostEqual(result, 3.3958, places=4)

    #def test_WGS84toLV95(self):
    #    # Convert WGS84 to LV95
    #    # geodesy.geo.admin.ch/reframe/wgs84tolv95?easting=6.14569&northing=46.20222&altitude=420
    #    # 2500204.1762987897, 1117575.5781232517, 367.5086178779602
    #    result = topo.Topo.WGS84toLV95(self, 46.20222, 6.14569, 420) # latitude, longitude, ellHeight
    #    self.assertEquals(result, [2500204.1762987897, 1117575.5781232517, 367.5086178779602])

if __name__ == '__main__':
    unittest.main()
