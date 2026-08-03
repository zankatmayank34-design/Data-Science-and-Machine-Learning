# Assignment 8: break Statement
total = 0

while True:
    number = float(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Sum:", total)
