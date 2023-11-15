from typing import List
import math


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

