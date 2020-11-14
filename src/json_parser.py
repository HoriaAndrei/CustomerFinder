import json

class JsonParser:
    @staticmethod
    def parse(json_str: str) -> dict:
        out = None
        try:
            out = dict(json.loads(json_str))
        except json.decoder.JSONDecodeError:
            print("Invalid JSON string: " + json_str)
        except TypeError:
            print("Input must be a string")
        return out
