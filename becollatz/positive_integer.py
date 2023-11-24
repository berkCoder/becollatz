from __future__ import annotations


class PositiveInteger:
    def __init__(self, number: int):
        assert number > 0, f"{number} is not a positive integer"
        self._number = number

    @property
    def is_odd(self) -> bool:
        # return self._number % 2 == 1
        if self._number % 2 == 1:
            return True
        else:
            return False

    @property
    def is_even(self) -> bool:
        # return not self.is_odd
        if self._number % 2 == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self._number}"

    def next_collatz_number(self) -> int:
        if self.is_odd:
            return self._number * 3 + 1
        return self._number//2


x = PositiveInteger(8)
