from becollatz.collatz import compute_numbers
import sys

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


arguments = []
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if "-" in arg:
        first, second = arg.split("-")
        arguments.append((convert_to_integer(first), convert_to_integer(second)))
    else:
        arguments.append(convert_to_integer(arg))
    i += 1

print(arguments)

sys.exit(1)











try:
    number = int(sys.argv[1])
except:
    print("You did not provide a whole number")
    exit()

print(f"You provided {number} as input")
result = compute_numbers(number)
index = 0
for n in result:
    print(f"Step {index:4} {n:10}")
    index += 1
print(f"Total number of steps till we reached 1: {len(result)-1} steps")