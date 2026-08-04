# Assignment 7: Subsets and Supersets
# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.

set1 = {1,2,3}
set2 = {1,2,3,4,5}
print("Subset:", set1.issubset(set2))
print("Superset:", set2.issuperset(set1))
