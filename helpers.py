from math import sin, cos, sqrt, atan2, radians

class Helpers:
    @staticmethod
    def distance(lat1, lon1, lat2, lon2):
        '''
            returns the distance between the two points
        '''
        # approximate radius of earth in km
        R = 6373.0
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
            raise ValueError('stations array must contain at least 2 stations')
        distance = 0
        o_station = stations[0]
        for s in stations[1:]:
            distance += Helpers.distance(o_station[0], o_station[1], s[0], s[1])
            o_station = s
        return distance

# here we test the distance functions
if __name__ == "__main__":
    lat1 = radians(52.2296756)
    lon1 = radians(21.0122287)
    lat2 = radians(52.406374)
    lon2 = radians(16.9251681)
    print(Helpers.distance(lat1, lon1, lat2, lon2))
    print(Helpers.distanceTrip([(lat1, lon1), (lat2, lon2)]))
    print(Helpers.distanceTrip([(lat1, lon1), (lat2, lon2), (lat1, lon1)]))
    print(Helpers.distanceTrip([(lat1, lon1), (lat2, lon2), (lat2, lon2)]))