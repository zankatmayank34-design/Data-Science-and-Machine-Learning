# Assignment 2: Accessing Tuple Elements
# Print the first, middle, and last elements of the tuple created in Assignment 1.

numbers = tuple(range(1, 11))
print("First:", numbers[0])
print("Middle:", numbers[len(numbers)//2])
print("Last:", numbers[-1])
