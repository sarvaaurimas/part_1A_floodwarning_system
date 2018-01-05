# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:46:47 2017

@author: samue
"""

from floodsystem.stationdata import build_station_list ,update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """ Requirement for Task 1C"""
    stations = build_station_list()
    update_water_levels(stations)
    dangerous_stations =stations_highest_rel_level(stations, 10)
    
    for i in dangerous_stations:
        print(i.name, " :", i.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
