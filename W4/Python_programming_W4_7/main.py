
print("Program starting.\n")

print("Check multiplicative persistence.")
number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    digits = str(number)
    result = 1

    for digit in digits:
        result *= int(digit)

    print(" * ".join(digits), "=", result)

    number = result
    steps += 1

print("No more steps.\n")

print(f"This program took {steps} step(s)")

print("\nProgram ending.")
