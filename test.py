#!/usr/bin/python
import re
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

print(haversine(77.5946, 12.9716, 76.6394, 12.2958))
strs = "how much for the maple syrup? $20.99? That's ricidulous!!!"
print(strs)
nstr = re.sub(r'[?|$|.|!]',r'',strs)
print(nstr)
nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',nstr)
print(nestr)
