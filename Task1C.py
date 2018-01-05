# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:07:59 2017

@author: Aurimas
"""

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run(): 
    """Requirement for Task 1C"""
    stations = build_station_list()
    stations_in_distance = stations_within_radius(stations, (52.2053, 0.1218), 10)
    print(sorted(stations_in_distance))
    
if __name__ == "__main__":
    run()