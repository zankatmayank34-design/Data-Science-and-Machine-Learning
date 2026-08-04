# Assignment 6: List Methods
# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.

numbers = [5, 2, 8, 2, 1, 5, 9, 3]
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
unique_numbers = list(set(numbers))
print("Without duplicates:", unique_numbers)
