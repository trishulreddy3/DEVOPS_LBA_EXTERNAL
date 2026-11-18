import unittest
import sys
import os

# Ensure local folder is in Python search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from arithmetic import add, subtract, multiply, divide, compute

class TestArithmeticOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-4, 9), 5)
        self.assertEqual(add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        self.assertEqual(subtract(20, 8), 12)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 100), 0)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 2), 4.5)
        self.assertEqual(divide(-12, 3), -4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(15, 0)

    def test_compute_wrapper(self):
        self.assertEqual(compute('add', 4, 6), 10)
        self.assertEqual(compute('sub', 10, 4), 6)
        self.assertEqual(compute('mul', 3, 5), 15)
        self.assertEqual(compute('div', 20, 4), 5)
        with self.assertRaises(ValueError):
            compute('modulus', 10, 2)

if __name__ == '__main__':
    unittest.main()
