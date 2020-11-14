from unittest import TestCase

from src.filter import CustomerDistanceFromOfficeFilter
from src.data_types.customer import Customer

class TestCustomerFilter(TestCase):

    def test_filter_one_customer(self):
        customers = [Customer(1, "Test", "53", "-6")]
        customer_filter = CustomerDistanceFromOfficeFilter(100)
        out_customers = customer_filter.filter_data(customers)
        self.assertEqual(1, len(out_customers))
