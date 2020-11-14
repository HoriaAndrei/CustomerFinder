from abc import ABC, abstractstaticmethod

class DataType(ABC):
    @abstractstaticmethod
    def create(raw_data):
        pass
