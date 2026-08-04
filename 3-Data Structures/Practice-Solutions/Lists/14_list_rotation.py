# Assignment 14: List Rotation
# Write a function that rotates a list by n positions. Print the original and rotated lists.

numbers = [1,2,3,4,5]
rotated = numbers[1:] + numbers[:1]
print(rotated)
