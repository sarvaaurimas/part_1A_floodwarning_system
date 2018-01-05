# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:02:13 2017

@author: Aurimas
"""

from floodsystem.analysis import predicted_value, danger_assigning
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key


def run():
    
    """Requirement for task 2G"""
    
    #build a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk = stations_highest_rel_level(stations, 10)
    
    # Fetch data over past 2 days
    dt = 0.5
    danger_stations = []
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        try:
            prediction = predicted_value(dates, levels)
            danger_level = danger_assigning(station, prediction)
            if danger_level is not None:
                if danger_level[1] == "severe" or danger_level[1] == "high":
                    danger_stations.append(danger_level)
                    
        except:
            pass
    sorted_stations = sorted_by_key(danger_stations, 1, reverse = True)
    for i in sorted_stations:
        print(i[0] + ":" + i[1])                


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
    
