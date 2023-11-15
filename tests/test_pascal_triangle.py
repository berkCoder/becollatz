import unittest
from becollatz.pascal_triangle import *


class TestTriangle(unittest.TestCase):
    def test_up_to_5(self):
        r = triangle_gen(6)
        self.assertEqual(len(r), 7)
        self.assertEqual(r[0], [1])
        self.assertEqual(r[1], [1, 1])
        self.assertEqual(r[2], [1, 2, 1])
        self.assertEqual(r[3], [1, 3, 3, 1])
        self.assertEqual(r[4], [1, 4, 6, 4, 1])
        self.assertEqual(r[5], [1, 5, 10, 10, 5, 1])
        self.assertEqual(r[6], [1, 6, 15, 20, 15, 6, 1])



