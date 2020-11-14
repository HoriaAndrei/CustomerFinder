import os

from src.data_source import FileDataSource
from src.data_types.customer import Customer
from src.filter import CustomerDistanceFromOfficeFilter
from src.defs import DataFormat

MAX_DISTANCE_KM = 100

if __name__ == "__main__":
    data_source = FileDataSource(
        os.path.join(os.path.dirname(__file__), "data", "customers.txt"),
        DataFormat.json,
        Customer
    )
    customer_filter = CustomerDistanceFromOfficeFilter(MAX_DISTANCE_KM)
    matching_customers = customer_filter.filter_data(data_source)

    matching_customers_sorted = sorted(matching_customers, key=lambda c: c.user_id)

    for customer in matching_customers_sorted:
        print("%s,%s" % (customer.name, customer.user_id))
