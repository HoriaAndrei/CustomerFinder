from unittest import TestCase

from src.data_types.customer import Customer
from src.location import Location

class TestCustomer(TestCase):

    def test_customer_attributes(self):
        cust = Customer(1, "Test Customer", "45", "45")
        self.assertIsInstance(cust.user_id, int)
        self.assertIsInstance(cust.name, str)
        self.assertIsInstance(cust.location, Location)

    def test_customer_create(self):
        c = Customer.create({"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"})
        self.assertEqual(12, c.user_id)
        self.assertEqual("Christina McArdle", c.name)
        self.assertIsInstance(c.location, Location)

    def test_customer_create_none(self):
        cust = Customer.create(100)
        self.assertIsNone(cust)