from .json_parser import JsonParser
from .defs import DataFormat

class ParserFactory:
    _parser_map = {
        DataFormat.json: JsonParser
    }

    @classmethod
    def get_parser(cls, data_type: str):
        return cls._parser_map.get(data_type)
