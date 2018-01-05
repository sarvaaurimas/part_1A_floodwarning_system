# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:44:28 2017

@author: samue
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirement for Task 1E"""
    
    stations = build_station_list()
    
    # Build dictionary relating rivers (key) to stations (value)
    maxstationlist = rivers_by_station_number(stations,10)
    
    print(maxstationlist)



if __name__ == "__main__":
    run()

#just checking that the function in geo works