# Assignment 3: Set Operations
# Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.

set1 = set(range(1, 6))
set2 = {2,4,6,8,10}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric difference:", set1.symmetric_difference(set2))
