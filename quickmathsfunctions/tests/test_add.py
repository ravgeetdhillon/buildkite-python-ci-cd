import unittest
from quickmathsfunctions.src.quickmathsfunctions import add


class TestAdd(unittest.TestCase):
    def test_positive_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_negative_add(self):
        result = add(10, -5)
        self.assertEqual(result, 5)

    def test_addition_with_zero(self):
        result = add(10, 0)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
