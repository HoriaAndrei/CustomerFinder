from .data_type import DataType

class RawDataType(DataType):

    @staticmethod
    def create(raw_data: dict):
        if type(raw_data) == dict:
            return raw_data
        return None
