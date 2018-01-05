# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 08:14:08 2017

@author: samue
"""

#demonstration program

from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """1st Requirement for Task 1D"""
    stations = build_station_list()
    # Build set of rivers
    rivers = rivers_with_station(stations)
    sorted_rivers = sorted(rivers)
    print("First 10 rivers in alphabetical order:", sorted_rivers[:10])
    # print
    print("\n")
    print("Number of rivers with at least one station:", len(rivers))
    
if __name__ == "__main__":
    run()
print("\n")

def run2():
    """2nd Requirement for Task 1D"""
    print('\033[1m'+ 'Stations by River')
    print("\n")
    stations = build_station_list()
    rivers = stations_by_river(stations)
    print("River Aire: ", sorted(rivers["River Aire"]))
    print("\n")
    print("River Cam: ", sorted(rivers["River Cam"]))
    print("\n")
    print("Thames: ", sorted(rivers["Thames"]))
if __name__ == "__main__":
    run2()

    