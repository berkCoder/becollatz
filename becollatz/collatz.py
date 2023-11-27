from typing import List


# computes all numbers in the collatz series for the given number
def compute_numbers(number: int) -> List[int]:
    numbers = [number]
    while number != 1:
        if number % 2 == 1:
            number = 3 * number + 1
        elif number % 2 == 0:
            number = number/2
        numbers.append(int(number))
    return numbers


class Series:
    def __init__(self, number: int):
        self._numbers = compute_numbers(number)
        self._odd_numbers = []
        for item in self._numbers:
            if item % 2 == 1:
                self._odd_numbers.append(item)

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, item):
        return self._numbers[item]

    @property
    def even_count(self):
        return len(self._numbers) - len(self._odd_numbers)

    @property
    def odd_count(self):
        return len(self._odd_numbers)
