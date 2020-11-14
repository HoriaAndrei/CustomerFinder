from unittest import TestCase

from math import pi

from src.location import Location

class TestLocation(TestCase):
    def test_location_create_ok(self):
        l = Location("90", "180")
        self.assertEqual(90.0, l.lat)
        self.assertEqual(180.0, l.long)
        self.assertEqual(pi/2, l.lat_rad)
        self.assertEqual(pi, l.long_rad)

    def test_location_create_ko(self):
        self.assertRaises(ValueError, Location, "x", "y")
        self.assertRaises(ValueError, Location, "1800", "0")
        self.assertRaises(ValueError, Location, "1", "")