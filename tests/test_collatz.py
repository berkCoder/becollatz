import unittest
from becollatz.collatz import *

class TestCollatz(unittest.TestCase):
    # testing the case for 1
    def test_1(self):
        self.assertEqual(compute_numbers(1), [1])
    # testing the case for 3
    def test_3(self):
        self.assertEqual(compute_numbers(3), [3, 10, 5, 16, 8, 4, 2, 1])








