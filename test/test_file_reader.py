import os

from unittest import TestCase
from src.file_reader import FileReader

class TestFileReader(TestCase):
    def test_file_does_not_exist(self):
        self.assertRaises(FileNotFoundError, FileReader, "fake_file.txt")

    def test_read_three_lines(self):
        reader = FileReader(os.path.dirname(__file__) + "/data/file_3lines.txt")
        self.assertEqual("abc", reader.read_line())
        self.assertEqual("def", reader.read_line())
        self.assertEqual("123", reader.read_line())
        self.assertIsNone(reader.read_line())
