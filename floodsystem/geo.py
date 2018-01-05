"""
Created on Sat Feb 25 18:39:20 2017

@author: Aurimas
"""


"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from math import *
#function that prints the names of all rivers with stations

def rivers_with_station(stations):
    """ This function creates a list with all the name of the rivers
    that have at least one station"""
    l= [] #create empty list
    for i in stations:
        l.append(i.river) #add the name of the river with a station to list
    return set(l) #convert list into set
    
def stations_by_river(stations):
    """ This function creates a dictionary mapping rivers (keys) to 
    a list with their monitoring stations (values)"""
    dic = {} #empty dic
    for i in stations: #iterate over Monitoring stations (class) in list : stations
        if i.river in dic: #if the river has more than one station 
            dic[i.river].append(i.name) #append it to the end of the list of stations
        else: #if the river has only appeared once in the iteration create a new key
            dic[i.river] = [i.name]
        
    return dic #please show me the dictionary

def rivers_by_station_number(stations, N):
    """ This function returns the N rivers with the largest number
    of stations in decreasing order, in the form of tuples with
    the name of the river first and the number of stations the river has second"""
    stations_dict = stations_by_river(stations) #I will re-use the previous function to get dictionary
    stations_tuplist = []
    for i in stations_dict: #iterate over keys in dictionary
        stations_tuplist.append((i, len(stations_dict[i])))
    stations_tuplist = sorted_by_key(stations_tuplist, 1, reverse = True)
    sorted_list = stations_tuplist [0:N]
    while stations_tuplist[N-1][1] == stations_tuplist[N][1]:
        sorted_list.append(stations_tuplist[N])
        N += 1
    return sorted_list #returning list of tuples sorted by second value in tuple, in descending order
        
def stations_by_distance(stations, p):
    """ This function sorts stations by distance
    from input coordinates."""
    
    list_of_distances = [] #creates an empty list1
    for station in stations: #iterate through all the stations
        diff_long = abs(radians(p[1]-station.coord[1])) #same with longitude
        distance = 6371*acos(sin(radians(station.coord[0]))*sin(radians(p[0]))+cos(radians(station.coord[0]))*cos(radians(p[0]))*cos(diff_long))
        list_of_distances.append((station.name, station.town, distance))# creates a list of stations with their distances from an input point
    return sorted_by_key(list_of_distances, 2)
        
def stations_within_radius(stations, centre, r):
    """ This function builds a list of stations that are within
    required distance of input coordinates """
    
    list_of_stations = [] #create an empty list
    stations_with_distance = stations_by_distance(stations, centre) #use previously developed function to build a list with distances
    for station in stations_with_distance:
        if station[2] <= r:
            list_of_stations.append(station[0])
        else:
            break
    return list_of_stations
        
        
        