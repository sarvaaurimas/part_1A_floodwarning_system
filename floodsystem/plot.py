# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:15:07 2017

@author: samue
"""

import matplotlib
import matplotlib.pyplot as plt
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    
    """Plots dates vs levels for a specific station together 
    with the values for its typical high and typical low water depth"""
    
    matplotlib.pyplot.plot_date(dates, levels, label = "Real Data") #Similar to the plot() command, except the dates or levels (or both) data is considered to be dates, and the axis is labeled accordingly.
    plt.plot(dates, [station.typical_range[0]]*len(dates), label= "Typical Low") #plotting the dates vs. typical low (since this is a horizontal straight line, I created a list the same length as dates with only typical low as elements)
    plt.plot(dates, [station.typical_range[1]]*len(dates), label = "Typical High") #plotting the dates vs. typical high (for the same reason as above I multiply a singleton by the number elements in dates)
    plt.ylabel('Water Level (m)') #labelling the axes
    plt.title(station.name) #giving the plot a title
    plt.xlabel('Date')
    plt.grid(True) #i want a grid
    plt.legend(loc = 'best')#i want a legend
    plt.tight_layout() #making sure that the labels fit in the axes (otherwise it looks very messy)
    plt.show() #showing the plot
   
def plot_water_level_with_polyfit(station, dates, levels):
    """Plots water level using real time data and polyfit"""
    if len(dates) == 0 or len(levels) == 0:
     print("not enough data available for {}".format(station.name))
    else:
        polynomial, shift = polyfit(dates, levels, 12)
        x = np.linspace(matplotlib.dates.date2num(dates[-1]), matplotlib.dates.date2num(dates[0]), 200)
     #creates an array of 30 points between starting and end date
        plt.plot(x, polynomial(x - shift), label = "polyfit") 
        plot_water_levels(station, dates, levels)
    