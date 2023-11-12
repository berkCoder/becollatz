from becollatz.collatz import compute_numbers
import sys

if len(sys.argv) != 2:
    print("You must provide a single number")
    exit()

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