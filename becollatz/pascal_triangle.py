from typing import List
import math


def triangle_gen(levels: int) -> List[List[int]]:
    assert levels >= 0, "Levels shouldnt be negative"
    triangle = []
    levels = list(range(0, levels + 1))
    for n in levels:
        layer = []
        for k in range(n+1):
            term = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
            layer.append(term)
            # print(f"{n}/{k} ", end="")
        triangle.append(layer)
    return triangle








