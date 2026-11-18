import unittest
import sys
import os

# Ensure local folder is in Python search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prime import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_negative_and_zero(self):
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_composite_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(49))

    def test_large_prime(self):
        self.assertTrue(is_prime(104729))  # 10,000th prime

if __name__ == "__main__":
    unittest.main()
