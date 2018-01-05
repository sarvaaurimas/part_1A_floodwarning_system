# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:40:44 2017

@author: samue
"""

from floodsystem.stationdata import build_station_list ,update_water_levels
from floodsystem.flood import stations_level_over_threshold 



def run():
    """ Requirement for Task 2B"""
    stations = build_station_list()
    update_water_levels(stations)
    tuplist = stations_level_over_threshold(stations, 0.8)
    
    for i in tuplist:
        print(i[0].name, " :", i[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()
