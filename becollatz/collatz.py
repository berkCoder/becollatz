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








