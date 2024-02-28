"""Utility used to transform coordinate"""
#  The MIT License (MIT)
#  
#  Copyright (c) 2014 Federal Office of Topography swisstopo, Wabern, CH and Aaron Schmocker 
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
# 

# WGS84 <-> LV03 converter based on the scripts of swisstopo written for python2.7
# Aaron Schmocker [aaron@duckpond.ch]
# vim: tabstop=4 shiftwidth=4 softtabstop=4 expandtab

# Source: https://www.swisstopo.admin.ch/en/transformation-calculation-services (see PDFs under "Documentation")

import math

class Topo(object):
    '''
    Topo class which is able to perform convertions between the 
    LV95 and WGS84 system.
    '''
    # Convert LV95(E,N,h) to WGS84
    def LV95toWGS84(self, easting=None, northing=None, altitude=None):
        # Convert thr projection coordinates easting and northing in LV95
        # into the civilian system (Bern = 0 / 0) and express in the unit [1000 km]
        easting_p = (easting - 2600000) / 1000000
        northing_p = (northing - 1200000) / 1000000

        # calculate longitude lambda_wgs and latitude phi_wgs in the unit [10000"]
        lambda_wgs_p = 2.6779094 + 4.728982 * easting_p \
                     + 0.791484 * easting_p * northing_p \
                     + 0.1306 * easting_p * pow(northing_p, 2) \
                     - 0.0436 * pow(easting_p, 3)
        phi_wgs_p = 16.9023892 + 3.238272 * northing_p \
                  - 0.270978 * pow(easting_p, 2) \
                  - 0.002528 * pow(northing_p, 2) \
                  - 0.0447 * pow(easting_p, 2) * northing_p \
                  - 0.0140 * pow(northing_p, 3)
        # calculate altitude
        altitude_wgs = altitude + 49.55 \
                     - 12.60 * easting_p \
                     - 22.64 * northing_p
        # convert longitude and latitude to the unit [°]
        lambda_wgs = lambda_wgs_p * 100 / 36
        phi_wgs = phi_wgs_p * 100 / 36
        return [lambda_wgs, phi_wgs, altitude_wgs]


    # Convert decimal angle (° dec) to sexagesimal angle (dd.mmss,ss)
    def DecToSexAngle(self, dec):
        degree = int(math.floor(dec))
        minute = int(math.floor((dec - degree) * 60))
        second = (((dec - degree) * 60) - minute) * 60
        return degree + (float(minute) / 100) + (second / 10000)
		
    # Convert sexagesimal angle (dd.mmss,ss) to seconds
    def SexAngleToSeconds(self, dms):
        degree = 0 
        minute = 0 
        second = 0
        degree = math.floor(dms)
        minute = math.floor((dms - degree) * 100)
        second = (((dms - degree) * 100) - minute) * 100
        return second + (minute * 60) + (degree * 3600)

    # Convert sexagesimal angle (dd.mmss) to decimal angle (degrees)
    def SexToDecAngle(self, dms):
        degree = 0
        minute = 0
        second = 0
        degree = math.floor(dms)
        minute = math.floor((dms - degree) * 100)
        second = (((dms - degree) * 100) - minute) * 100
        return degree + (minute / 60) + (second / 3600)
    

        
if __name__ == "__main__":
    ''' Example usage for the Topo class.'''
    pass    



