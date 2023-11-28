import unittest
from becollatz.linear_expression import LinearExpression


class TestLinearExpression(unittest.TestCase):
    def test_basics(self):
        # 2 x + 3
        self.assertEqual(LinearExpression(2, 3).m, 2)
        # 2 x + 3
        self.assertEqual(LinearExpression(2, 3).b, 3)

    def test_string(self):
        self.assertEqual(str(LinearExpression(2, 3)), "2x + 3")
        self.assertEqual(str(LinearExpression(2, 0)), "2x")
        self.assertEqual(str(LinearExpression(1, 3)), "x + 3")
        self.assertEqual(str(LinearExpression(1, 0)), "x")
