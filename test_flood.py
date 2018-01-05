# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:03:26 2017

@author: samue
"""

from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    Aurimas = MonitoringStation(1234, 1234, "Aurimas", (1234,1234), (0.5,1), "Sarva", "Vilnius", 1997-11-12, 1234)
    Aurimas.latest_level = 1
    stations.append(Aurimas)
    x= stations_level_over_threshold(stations,0.9)
    
    assert (Aurimas, 1) in x

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    Aurimas = MonitoringStation(1234, 1234, "Aurimas", (1234,1234), (0.5,1), "Sarva", "Vilnius", 1997-11-12, 1234)
    Aurimas.latest_level = 3
    stations.append(Aurimas)
    x= stations_highest_rel_level(stations,10)
    
    assert Aurimas in x
                                 

