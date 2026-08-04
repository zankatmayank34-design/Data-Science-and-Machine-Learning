# Assignment 5: Dictionary Comprehensions
# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.

cubes = {x: x**3 for x in range(1, 11)}
print(cubes)
