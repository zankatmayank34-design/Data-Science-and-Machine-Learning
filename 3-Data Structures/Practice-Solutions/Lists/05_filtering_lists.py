# Assignment 5: Filtering Lists
# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.

numbers = list(range(1, 21))
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
