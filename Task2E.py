# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:21:37 2017

@author: samue
"""
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk = stations_highest_rel_level(stations, 5)
    print(stations_at_risk)

    # Fetch data over past 10 days
    dt = 10
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    
    run()    
    