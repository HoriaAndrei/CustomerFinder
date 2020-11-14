import os

from unittest import TestCase

from src.data_source import FileDataSource
from src.data_types.customer import Customer
from src.defs import DataFormat

class TestDataSource(TestCase):
    def setUp(self):
        source_file = os.path.dirname(__file__) + "/data/json_1line.txt"
        self.ds = FileDataSource(source_file, DataFormat.json)

    def test_get_one_line(self):
        line = None
        for l in self.ds:
            line = l

        self.assertIsInstance(line, dict)
        self.assertIn("key1", line)
        self.assertIn("key2", line)

    def test_iterate_twice(self):
        for l1 in list(self.ds):
            for l2 in list(self.ds):
                self.assertEqual(l1, l2)

class TestCustomerDataSource(TestCase):
    def setUp(self):
        source_file = os.path.dirname(__file__) + "/data/test_customers.txt"
        self.ds = FileDataSource(source_file, DataFormat.json, Customer)

    def test_get_customers(self):
        cust = None
        for l in self.ds:
            cust = l
        
        self.assertIsInstance(cust, Customer)
        self.assertEqual("Test Customer", cust.name)



