# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 23:18:01 2017

@author: Aurimas
"""


from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list 

def run():
    """ Requirement for Task 1B"""
    
    
    stations = build_station_list()
    stations_distance = stations_by_distance(stations, (52.2053, 0.1218))
    print("10 Closest Entries: ", stations_distance[:10])
    print("\n")
    print("10 Furthest Entries", stations_distance[-10:])

if __name__ == "__main__":
    run()