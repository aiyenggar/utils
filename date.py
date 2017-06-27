# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:26:57 2017

@author: aiyenggar
"""
from datetime import datetime
import math

def years(fromdate, todate):
    try:
        dt1=datetime.strptime(todate, '%Y-%m-%d')
        dt2=datetime.strptime(fromdate, '%Y-%m-%d')
    except ValueError:
        return None
    return math.floor(((dt1 - dt2).days)/365.2425)
    
time1="2011-04-21"
time2="2006-04-21"

delta = years(time2, time1)
if  delta == None or delta >= 5:
    print("Out of range")
else:
    print(delta)