# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:57:30 2017

@author: Aurimas
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def polyfit(dates, levels, p):
    """Function computes a least-squares fit of polynomial of degree p to water level data.
    Returns a tuple of the polynomial object and a tuple of any shift in the time(date) axis. """
    
    if len(dates) == 0 or len(levels) == 0:
        pass
    else:
        dates_calc = matplotlib.dates.date2num(dates)
    # Using shifted date values, find coefficient of best-fit polynomial f(date) of degree 4
        p_coeff = np.polyfit(dates_calc - dates_calc[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated e.g. poly(0.3)
        poly = np.poly1d(p_coeff)
        return poly, dates_calc[0]

def danger_assigning(station, prediction):
    """Function assigns keywords to the stations that represents the risk of a flood using the predicted and normal water
    level values"""
    
    if prediction == None or station.typical_range == None:
        pass
    elif (prediction - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0]) > 2:
        return (station.town , "severe")
        
    elif 1.2<(prediction - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])<2:
        return (station.town , "high")
        
    elif 1<(prediction - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])<1.2:
        return (station.town ,"moderate")
    
    else:
        return (station.town ,"low")

def predicted_value(dates, levels):
    """The function calculates the expected water level value by extrapolating a polyfit function from recent real-time data"""
    if len(dates) == 0 or len(levels) == 0:
     pass
    else:
        polynomial, shift = polyfit(dates, levels, 12)
        derivative = np.polyder(polynomial)
        prediction = polynomial(matplotlib.dates.date2num(dates[0]) - shift) + derivative(matplotlib.dates.date2num(dates[0]) - shift -1/(24*8))*1/24
        return prediction
    
    
    
    
