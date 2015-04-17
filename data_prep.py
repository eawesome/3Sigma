import pandas as pd
import numpy as np
import geopy
from geopy.geocoders import Nominatim
import geocoder

geolocator = Nominatim()


def transform_gps2zip(lat_string, log_string):
    location = geolocator.reverse(log_string+','+lat_string)
    #g = geocoder.google([lat_string, log_string], method='reverse')
    address = location.address
    try:
        #address = g.json['neighborhood']
        zip_code = str([s.strip() for s in address.split(',') if s.strip().isdigit() and len(s.strip()) == 5][0])
        return zip_code
        #return address

    except:
        return 0



