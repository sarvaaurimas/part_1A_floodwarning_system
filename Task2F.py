# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:04:31 2017

@author: Aurimas
"""

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_polyfit
from floodsystem.flood import stations_highest_rel_level

def run():
    
    """Requirement for task 2F"""
    
    #build a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk = stations_highest_rel_level(stations, 5)
    
    # Fetch data over past 2 days
    dt = 2
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_polyfit(station, dates, levels)
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    
    run()    
    
    