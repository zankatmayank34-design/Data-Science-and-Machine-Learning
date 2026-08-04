# Assignment 11: Dictionary Filtering
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

squares = {x: x**2 for x in range(1, 11)}
even_keys = {k:v for k,v in squares.items() if k % 2 == 0}
print(even_keys)
