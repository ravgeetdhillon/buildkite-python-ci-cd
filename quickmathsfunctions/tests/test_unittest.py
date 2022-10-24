import unittest
from quickmathsfunctions.src.quickmathsfunctions import add, divide, multiply, subtract


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        result = multiply(10, 5)
        self.assertEqual(result, 50)

class TestDivide(unittest.TestCase):
    def test_dividet(self):
        result = divide(10, 5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
