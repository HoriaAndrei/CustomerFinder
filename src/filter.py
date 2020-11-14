from abc import ABC, abstractmethod

from .location import Location
from .distance_calculator import calculate_distance
from .data_types.data_type import DataType
from .data_types.customer import Customer

class Filter(ABC):

    @abstractmethod
    def filter_function(self, data: DataType):
        return data

    def filter_data(self, data):
        output_data = []
        for item in data:
            if self.filter_function(item):
                output_data.append(item)
        return output_data

class CustomerDistanceFromOfficeFilter(Filter):
    _office_location = Location("53.339428", "-6.257664")

    def __init__(self, max_distance):
        self._max_distance = max_distance

    def filter_function(self, customer: Customer):
        return calculate_distance(
            self._office_location, customer.location) <= self._max_distance
        