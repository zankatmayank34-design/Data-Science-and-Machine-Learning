# Assignment 2: Accessing Dictionary Elements
# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

squares = {x: x**2 for x in range(1, 11)}
print("Value of key 5:", squares[5])
print("Keys:", squares.keys())
