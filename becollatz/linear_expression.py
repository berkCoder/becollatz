from __future__ import annotations


# represents an expression in the form of y = mx + b
class LinearExpression:
    def __init__(self, m: int, b: int):
        self._m = m
        self._b = b

    @property
    def m(self):
        return self._m

    @property
    def b(self):
        return self._b

    def __str__(self):
        if self._m == 1:
            if self._b < 0:
                return f"x - {self._b}"
            elif self._b > 0:
                return f"x + {self._b}"
            else:
                return f"x"
        else:
            if self._b < 0:
                return f"{self._m}x - {self._b}"
            elif self._b > 0:
                return f"{self._m}x + {self._b}"
            else:
                return f"{self._m}x"