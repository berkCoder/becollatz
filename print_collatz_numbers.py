from becollatz.collatz import compute_numbers
import sys
import matplotlib.pyplot as plt

# if len(sys.argv) != 2:
#     print("You must provide a single number")
#     exit()

def convert_to_integer(str_value: str) -> int:
     try:
         if str_value.startswith("0b"):
            return int(str_value, 2)
         return int(str_value)
     except ValueError as e:
        print(f"The str doesn't contain all integers, it contains {str_value}")
        # raise e
        exit(1)


def print_collatz_numbers(number: int):
    print(f"You provided {number} as input")
    result = compute_numbers(number)
    print("HGere")
    index = 0
    for n in result:
        print(f"Step {index:4} {n:10}")
        index += 1
    print(f"Total number of steps till we reached 1: {len(result) - 1} steps")
    return len(result)



def get_arguments():
    arguments = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if "-" in arg:
            first, second = arg.split("-")
            first = convert_to_integer(first)
            second = convert_to_integer(second)
            if first > second:
                print(f"{first} is greater than {second} in {arg}")
                exit()
            arguments.append((first, second))
        else:
            arguments.append(convert_to_integer(arg))
        i += 1
    return arguments


args = get_arguments()
arguments = []
for arg in args:
    if type(arg) == tuple:  # if isinstance(arg, tuple):
        arg1, arg2 = arg
        print(arg1, arg2)
        for i in range(arg1, arg2 + 1):
            print_collatz_numbers(i)
            arguments.append(print_collatz_numbers(i))
    else:
        print_collatz_numbers(arg)
        arguments.append(print_collatz_numbers(arg))

sys.exit(1)



