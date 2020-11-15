from unittest import TestCase

from src.filter import CustomerDistanceFromOfficeFilter
from src.data_types.customer import Customer

class TestCustomerFilter(TestCase):
    def setUp(self):
        self.customer_filter = CustomerDistanceFromOfficeFilter(100)

    def test_filter_one_customer(self):
        customers = [Customer(1, "Test", "53", "-6")]
        out_customers = self.customer_filter.filter_data(customers)
        self.assertEqual(1, len(out_customers))

    def test_filter_invalid_data(self):
        data = [1, 2, 3]
        out = self.customer_filter.filter_data(data)
        self.assertEqual(0, len(out))
