# Assignment 3: Tuple Slicing
# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.

numbers = tuple(range(1, 11))
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Index 2 to 5:", numbers[2:6])
