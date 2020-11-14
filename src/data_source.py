from abc import ABC, abstractmethod, abstractstaticmethod

from .factories import ParserFactory
from .file_reader import FileReader
from .data_types.data_type import DataType
from .data_types.raw_data_type import RawDataType
from .defs import DataFormat

class DataSource(ABC):

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

    def process_raw_data(self, raw_data: dict, data_format: DataFormat,
            data_type: DataType) -> DataType:
        """
        Converts raw data into the required data type.
        Returns None if conversion fails.
        """
        parser = ParserFactory.get_parser(data_format)
        out_data = None
        parsed_data = parser.parse(raw_data)
        if parsed_data is not None:
            out_data = data_type.create(parsed_data)
        return out_data


class FileDataSource(DataSource):
    """
    Iterator over lines in input file.
    Converts data into specified data type.

    Parameters:
        source_file_path: path to input file
        data_format: expected format for data
        data_type: type of output data
    """
    def __init__(self, source_file_path: str, data_format: str,
            data_type: DataType=RawDataType):
        self._source_file = source_file_path
        self._data_format = data_format
        self._data_type = data_type
        self._reader = None

    def __iter__(self):
        self._reader = FileReader(self._source_file)
        return self

    def __next__(self):
        if self._reader is not None:
            out_data = None
            # skip over invalid lines in the file
            while out_data is None:
                raw_data = self._reader.read_line()
                if raw_data is not None:
                    out_data = self.process_raw_data(
                        raw_data, self._data_format, self._data_type)
                else:
                    del self._reader
                    self._reader = None
                    raise StopIteration
            return out_data
        return None
