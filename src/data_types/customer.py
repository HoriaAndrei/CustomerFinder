from ..location import Location
from ..data_source import DataType

class Customer(DataType):
    """
    Customer data type.

    Attributes:
        user_id (int)
        name (str)
        location (Location)
    """
    def __init__(self, user_id: int, name: str, lat: str, long: str):
        self.user_id = user_id
        self.name = name
        self.location = Location(lat, long)

    @staticmethod
    def create(raw_data: dict):
        if type(raw_data) == dict and \
                "name" in raw_data and \
                "user_id" in raw_data and \
                "latitude" in raw_data and \
                "longitude" in raw_data:
            try:
                return Customer(
                    raw_data["user_id"],
                    raw_data["name"],
                    raw_data["latitude"],
                    raw_data["longitude"]
                )
            except ValueError:
                print("Invalid customer data provided.")
        return None
