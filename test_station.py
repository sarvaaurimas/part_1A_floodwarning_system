"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    dateopened="Some Date"
    stationreference = "Some reference"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, dateopened, stationreference)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.dateopened == dateopened
    assert s.stationreference == stationreference 
    

def test_inconsistent_typical_range_stations():
    """Checks for inconsistencies in the reported typical ranges of the monitoring stations"""
    
    stations = build_station_list()
    x = inconsistent_typical_range_stations(stations)
    y = sorted(x)
    assert 'Addlestone' in y