from unittest import TestCase

from src.json_parser import JsonParser

class TestJsonParser(TestCase):
    def test_valid_json(self):
        output_dict = JsonParser.parse('{"key1": "val1", "key2": 2}')
        self.assertIsInstance(output_dict, dict)
        self.assertIn("key1", output_dict)
        self.assertIn("key2", output_dict)
        self.assertEqual("val1", output_dict["key1"])
        self.assertEqual(2, output_dict["key2"])

    def test_invalid_json(self):
        output = JsonParser.parse('{"key1": "val1", "key2": 2')
        self.assertIsNone(output)

        output = JsonParser.parse('')
        self.assertIsNone(output)

        output = JsonParser.parse(1)
        self.assertIsNone(output)
