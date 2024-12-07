import unittest
from transformer import transform


class TestTransformer(unittest.TestCase):

    def test_transform_basic(self):
        data = {"name": 123, "age": 45}
        result = transform(data)
        expected = "name -> 123\nage -> 45"
        self.assertEqual(result, expected)

    def test_transform_expression_addition(self):
        data = {"result": [1, '+', 2]}
        result = transform(data)
        expected = "result -> 1 + 2"
        self.assertEqual(result, expected)

    def test_transform_expression_max(self):
        data = {"max_value": ["max", 10, 20, 30]}
        result = transform(data)
        expected = "max_value -> max(10, 20, 30)"
        self.assertEqual(result, expected)

    def test_transform_expression_sqrt(self):
        data = {"sqrt_value": ["sqrt", 16]}
        result = transform(data)
        expected = "sqrt_value -> sqrt(16)"
        self.assertEqual(result, expected)
