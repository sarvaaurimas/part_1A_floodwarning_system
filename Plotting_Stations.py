# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:03:39 2017

@author: samue
"""
import gmplot
from floodsystem.stationdata import build_station_list

gmap = gmplot.GoogleMapPlotter(51.5074, 0.1278, 16)

stations = build_station_list()

latitudes = []
longitudes = []

for station in stations:
    latitudes.append(station.coord[0])
    longitudes.append(station.coord[1])



gmap.scatter(latitudes, longitudes, '#3B0B39', size=50, marker=True, color = "#CD5c5c")

gmap.draw("mymap.html")