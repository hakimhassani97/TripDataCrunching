from math import sin, cos, sqrt, atan2, radians
import pandas as pd

class Geo:
    '''
        A class to simplify Geo calculations on our dataset
    '''
    @staticmethod
    def distance(lat1, lon1, lat2, lon2):
        '''
            returns the distance between the two points
        '''
        # approximate radius of earth in km
        R = 6373.0
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    @staticmethod
    def distanceTrip(stations):
        '''
            returns the distance of the whole trip\n
            params :\n
                stations : list of the (lat, long) of all the stations in the trip
        '''
        if len(stations)<2:
            # raise ValueError('stations array must contain at least 2 stations')
            print('Warning : stations array must contain at least 2 stations')
            return 0.
        distance = 0
        o_station = stations[0]
        for s in stations[1:]:
            distance += Geo.distance(o_station[0], o_station[1], s[0], s[1])
            o_station = s
        return distance

    @staticmethod
    def getLatLongStation(stationId, stations):
        '''
            returns the Latitude and Longitude of the station
        '''
        lat, lon = 0, 0
        station = stations[stations['id']==stationId]
        if len(station)>0:
            station = station.iloc[0]
            lat = station['latitude'] if not pd.isna(station['latitude']) else ''
            lon = station['longitude'] if not pd.isna(station['longitude']) else ''
        return (lat,lon)
    
    @staticmethod
    def distanceOfTicket(ticketId, tickets, stations):
        '''
            returns the distance of the trip with ticketId
        '''
        stationIds = []
        middleStations = []
        ticket = tickets[tickets['id']==ticketId]
        if len(ticket)>0:
            ticket = ticket.iloc[0]
            if not pd.isna(ticket['o_station']):
                stationIds.append(ticket['o_station'])
            if not pd.isna(ticket['middle_stations']):
                middleStations = ticket['middle_stations'].replace('{', '').replace('}', '').split(',')
                stationIds.extend(middleStations)
            if not pd.isna(ticket['d_station']):
                stationIds.append(ticket['d_station'])
        stationIds = [int(s) for s in stationIds]
        stationsLatLong = [Geo.getLatLongStation(stationdId, stations) for stationdId in stationIds]
        stationsLatLong = pd.unique(stationsLatLong)
        distance = Geo.distanceTrip(stationsLatLong)
        return distance

# here we test the distance functions
if __name__ == "__main__":
    lat1 = radians(52.2296756)
    lon1 = radians(21.0122287)
    lat2 = radians(52.406374)
    lon2 = radians(16.9251681)
    print(Geo.distance(lat1, lon1, lat2, lon2))
    print(Geo.distanceTrip([(lat1, lon1), (lat2, lon2)]))
    print(Geo.distanceTrip([(lat1, lon1), (lat2, lon2), (lat1, lon1)]))
    print(Geo.distanceTrip([(lat1, lon1), (lat2, lon2), (lat2, lon2)]))
