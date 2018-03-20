#!/usr/bin/python3

geoDict = {'Bangalore, Mysore, 140': 30, 'Bangalore, New York, 12000': 1, 'Bangalore, Chennai, 350': 5, 'Bangalore, Hyderabad, 650': 1}
delkeys = []
for k, v in geoDict.items():
    if (v <= 1):
        delkeys.append(k)
print(geoDict)
print(delkeys)
for key in delkeys:
    del(geoDict[key])
print(geoDict)
