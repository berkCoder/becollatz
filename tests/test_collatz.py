import unittest
from becollatz.collatz import *


class TestCollatz(unittest.TestCase):
    # testing the case for 1
    def test_1(self):
        self.assertEqual(compute_numbers(1), [1])

    # testing the case for 3
    def test_3(self):
        self.assertEqual(compute_numbers(3), [3, 10, 5, 16, 8, 4, 2, 1])


class TestSeries(unittest.TestCase):
    def test_basics(self):
        s = Series(3)
        self.assertEqual(len(s), 8)
        self.assertEqual(s[0], 3)
        self.assertEqual(s[-1], 1)
        self.assertEqual(s.odd_count, 3)
        self.assertEqual(s.even_count, 5)







