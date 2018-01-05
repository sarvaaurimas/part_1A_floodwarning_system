"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, dateopened, stationreference):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.dateopened = dateopened
        self.stationreference = stationreference

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   Date Opened: {}\n".format(self.dateopened)
        d += "   Station Reference: {}".format(self.stationreference)
        return d

    def typical_range_consistent(self):
        a = self.typical_range
        
        if a is None:
            return False
            
        elif a[0] > a[1]:
            return False
        
        else:
            return True
            
    def relative_water_level(self):
        if self.latest_level == None or self.typical_range_consistent() == False:
            return None
    
        else:
            a = (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            return a
        
        

def inconsistent_typical_range_stations(stations):
    
    """Returns a list with stations that have inconsistent data from a list with all stations"""
    
    l = []
    for i in stations:
        if i.typical_range_consistent() == False:
            l.append(i.name)
    return l