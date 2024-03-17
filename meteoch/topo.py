"""Utility used to transform swiss coordinate"""

# Source: https://www.swisstopo.admin.ch/en/transformation-calculation-services (see PDFs under "Documentation")

import math

class Topo(object):
    '''
    Topo class which is able to perform convertions between the 
    LV95 and WGS84 system.
    '''
    # Convert LV95(E,N) to WGS84
    def LV95toWGS84(self, easting=None, northing=None):
        # Convert the projection coordinates easting and northing in LV95
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
        # convert longitude and latitude to the unit [°]
        lambda_wgs = lambda_wgs_p * 100 / 36
        phi_wgs = phi_wgs_p * 100 / 36

        return [lambda_wgs, phi_wgs]

    # Convert WGS84 to LV95 swiss projection coordinates
    def WGS84toLV95(self, lat=None, long=None):
        # Convert the ellipsoidal latitude and longitude into arcsecond ["]
        wgs_phi = lat * 3600
        wgs_lambda = long * 3600

        # Calculate the auxilary values (difference of latitude and longitude relative to Bern in the unit [10000"])
        phi_p = (wgs_phi - 169028.66) / 10000
        lambda_p = (wgs_lambda - 26782.5) / 10000

        # Calculate projection coordinates in LV95 (E, N)
        east = 2600072.37 + 211455.93 * lambda_p \
             - 10938.51 * lambda_p * phi_p \
             - 0.36 * lambda_p * pow(phi_p, 2) \
             - 44.54 * pow(lambda_p, 3)
        
        north = 1200147.07 + 308807.95 * phi_p \
              + 3745.25 * pow(lambda_p, 2) \
              + 76.63 * pow(phi_p, 2) \
              - 194.56 * pow(lambda_p, 2) * phi_p \
              + 119.79 * pow(phi_p, 3)
        
        return [east, north]
              

    # Convert decimal angle (° dec) to sexagesimal angle (dd.mmss,sss)
    def DecToSexAngle(self, dec):
        degrees = math.floor(dec)
        minutes = (dec - degrees) * 60
        whole_minutes = math.floor(minutes)
        seconds = round((minutes - whole_minutes) * 60, 3)
        return degrees + (whole_minutes / 100) + (seconds / 10000)
		
    # Convert sexagesimal angle (dd.mmss,sss) to decimal angle (degrees)
    def SexToDecAngle(self, dms):
        degrees = math.floor(dms)
        minutes = math.floor((dms - degrees) * 100)
        seconds = round(((dms-degrees)  * 10000) - (minutes *100), 3)
        return degrees + (minutes / 60) + (seconds / 3600)
    

        
if __name__ == "__main__":
    ''' Example usage for the Topo class.'''
    pass    



