# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:32:49 2017

@author: samue
"""
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Input list of stations and a float (tolerance level) and 
    creates a list of tuples containing the stations with a relative
    water level above the tolerance value and their respective relative water levels"""
    l = [] #creating empty list
    for i in stations:
        if i.relative_water_level() == None: #if the water level has not been updated dont do anything
            pass
        elif i.relative_water_level() > tol: #if the relative water level is above the tolerance
            l.append((i,i.relative_water_level())) # append a tuple with the station and its relative water level
    l = sorted_by_key(l, 1, reverse= True) #sort the list by the second element in the tuple
    
    return l
    
            
def stations_highest_rel_level(stations, N):
    """Input list of stations and an integer and returns a list with
    the n stations having the highest relative water level"""
    l = [] #create empty list
    p = stations_level_over_threshold(stations, 0.2) #using the function above i create a list with all the stations with a relative water level aboev that small tolerance
    for i in p:
        l.append(i[0]) #I then append only the station to the list l
    l_cut = l[:N] #i then slice only the first N elements out of the list 
    return l_cut