# Assignment 10: Flattening a Nested List
# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.

nested = [[1,2],[3,4],[5,6]]
flat = [item for sublist in nested for item in sublist]
print(flat)
