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

result = compute_numbers(number)
for n in result:
    print(n)




