# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:40:22 2017

@author: Aurimas
"""

from floodsystem.analysis import polyfit, predicted_value, danger_assigning
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_polyfit, plot_water_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
def run():
    
    """Requirement for task 2F"""
    
    #build a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations_at_risk = stations_highest_rel_level(stations, 10)
    
    # Fetch data over past x days
    dt = 0.5
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        prediction = predicted_value(dates, levels)
        danger_level = danger_assigning(station, prediction)
        if len(dates) != 0:
            a = matplotlib.dates.date2num(dates[0])+1/48
            prediction_date = matplotlib.dates.num2date(a)
            plt.plot(prediction_date, prediction, "o", label = "Prediction")
            plot_water_level_with_polyfit(station, dates, levels)
        
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()    