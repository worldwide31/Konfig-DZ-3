import unittest
from parser import parse_json

class TestParser(unittest.TestCase):

    def test_valid_input(self):
        data = {"name": 123, "age": 45}
        result = parse_json(data)
        self.assertEqual(result, data)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            parse_json({"1name": 123})

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            parse_json({"name": "invalid"})
