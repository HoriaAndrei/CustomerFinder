from math import radians

class Location:
    def __init__(self, lat: str, long: str):
        self.lat = float(lat)
        self.long = float(long)
        if self.lat < -90.0 or self.lat > 90.0 or \
                self.long < -180.0 or self.long > 180.0:
            raise ValueError(
        "Invalid coordonates: %s %s" % (self.lat, self.long))
        self.lat_rad = radians(self.lat)
        self.long_rad = radians(self.long)
