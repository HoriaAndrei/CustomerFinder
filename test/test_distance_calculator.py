from unittest import TestCase
from math import pi

from src.distance_calculator import calculate_distance, RADIUS
from src.location import Location

class TestCalculateDistance(TestCase):
    def test_calculate_distance(self):
        loc1 = Location("90", "0")
        loc2 = Location("0", "0")
        self.assertEqual(pi * RADIUS / 2, calculate_distance(loc1, loc2))

        loc1 = Location("0", "180")
        loc2 = Location("0", "0")
        self.assertEqual(pi * RADIUS, calculate_distance(loc1, loc2))