# Assignment 3: Dictionary Methods
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

squares = {x: x**2 for x in range(1, 11)}
squares[11] = 121
del squares[1]
print(squares)
