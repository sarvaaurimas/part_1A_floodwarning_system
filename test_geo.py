# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:28:43 2017

@author: samue
"""

import pytest
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number, stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list



def test_rivers_with_station():
    stations = build_station_list()
    x= rivers_with_station(stations)
    sorted_stations = sorted(x)
    
    assert 'Adur' in sorted_stations
 
def test_stations_by_river():
    stations = build_station_list()
    x= stations_by_river(stations)
    y = sorted(x['River Aire'])
     
    assert  'Airmyn' in y

def test_stations_by_distance():
    stations = build_station_list()
    x = stations_by_distance(stations, (52.2053, 0.1218))
    
    assert ('Cambridge Jesus Lock', 'Cambridge', 0.8402364331431944) in x
        
    # for i,p in zip(x[:10],l):
    #    if abs(i[2]-p[2]) > 0.0000001:
     #       raise ValueError('The lists of tuples with distances from an origin differ significantly')
      #  else:
       #     pass

def test_stations_within_radius():
    stations = build_station_list()
    x = stations_within_radius(stations,(52.2053, 0.1218), 10)
 
    assert 'Cambridge Baits Bite' in x
    
    
def test_rivers_by_station_number():
    stations = build_station_list()
    x = rivers_by_station_number(stations, 10)
    assert ('Thames', 55) in x



    
    
    
    