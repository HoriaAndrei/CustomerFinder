from .location import Location

from math import acos, sin, cos

RADIUS = 6371

def calculate_distance(a: Location, b: Location) -> float:
    angle = acos(
        sin(a.lat_rad)*sin(b.lat_rad) + cos(a.lat_rad) * cos(b.lat_rad) * cos(a.long_rad-b.long_rad)
    )
    return RADIUS * angle
