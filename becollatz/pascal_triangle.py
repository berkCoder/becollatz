from typing import List
import math

# Pascals Triangle can be used to find the binomial coefficients of (a + b)^n
# n choose k = n!/(n-k)! * k! n choose k is written as (n k)
# n choose k represents the amount of ways you can choose a k size subset from n size set
# The sum of all the numbers in nth(starting from 0) row is 2^n


# This function generates pascals triangle up to a certain number of levels.
def triangle_gen(levels: int) -> List[List[int]]:
    assert levels >= 0, "Levels shouldnt be negative"
    triangle = []
    levels = list(range(0, levels + 1))
    for n in levels:
        layer = []
        for k in range(n+1):
            # n choose k = n! / ((n-k)! k!), we use // for integer division
            term = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
            layer.append(term)
        triangle.append(layer)
    return triangle


def row_sum(row: int) -> int:
    return 2 ** row




