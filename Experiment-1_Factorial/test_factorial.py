import unittest
import sys
import os

# Ensure local folder is in Python search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_recursive(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_recursive(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_iterative(6), 720)
        self.assertEqual(factorial_recursive(6), 720)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-5)
        with self.assertRaises(ValueError):
            factorial_recursive(-5)

if __name__ == "__main__":
    unittest.main()
