# Assignment 4: Iterating Over Dictionaries
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.

squares = {x: x**2 for x in range(1, 11)}
for key, value in squares.items():
    print(key, value)
