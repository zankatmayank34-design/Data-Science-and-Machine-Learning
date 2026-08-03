# Assignment 12: Factorial Calculation
number = int(input("Enter a number: "))
factorial = 1
count = 1

while count <= number:
    factorial *= count
    count += 1

print("Factorial:", factorial)
