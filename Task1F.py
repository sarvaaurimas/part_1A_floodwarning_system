# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:24:43 2017

@author: samue
"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    
    """Requirement for Task 1F"""
    
    stations = build_station_list()
    # Build set of rivers
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    sorted_inconsistent_stations = sorted(inconsistent_stations)
    print(sorted_inconsistent_stations)
if __name__ == "__main__":
    run()