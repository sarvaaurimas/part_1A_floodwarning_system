# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:11:32 2017

@author: Aurimas
"""

import gmplot
from floodsystem.stationdata import build_station_list

gmap = gmplot.GoogleMapPlotter(52.215386, 0.105000, 7)
stations = build_station_list()
latitudes = []
longitudes = []
for station in stations:
    latitudes.append(station.coord[0])
    longitudes.append(station.coord[1])
gmap.scatter(latitudes, longitudes, 'r', size=200, marker=False)

gmap.draw("mymap.html")