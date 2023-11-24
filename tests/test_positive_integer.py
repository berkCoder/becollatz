import unittest
from becollatz.positive_integer import *

class Test_Positive_Int(unittest.TestCase):
    def test_is_odd(self):
        self.assertFalse(PositiveInteger(4).is_odd)
        self.assertTrue(PositiveInteger(5).is_odd)
        self.assertTrue(PositiveInteger(1).is_odd)
        self.assertFalse(PositiveInteger(12425460).is_odd)
        self.assertTrue(PositiveInteger(12424141).is_odd)
    def test_is_even(self):
        self.assertTrue(PositiveInteger(4).is_even)
        self.assertFalse(PositiveInteger(5).is_even)
        self.assertFalse(PositiveInteger(537573171).is_even)
        self.assertTrue(PositiveInteger(112321310).is_even)
        self.assertTrue(PositiveInteger(6).is_even)
    def test_next_collatz_num(self):
        self.assertTrue(PositiveInteger(4), 2)
        self.assertTrue(PositiveInteger(5), 16)
        self.assertTrue(PositiveInteger(3), 10)
        self.assertTrue(PositiveInteger(1), 1)
        self.assertTrue(PositiveInteger(2), 1)


