# Assignment 6: Merging Dictionaries
# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

dict1 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
dict2 = {6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}
merged = {**dict1, **dict2}
print(merged)
