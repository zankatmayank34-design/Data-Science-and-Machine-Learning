# Assignment 13: Nested Tuple Iteration
# Create a nested tuple and iterate over the elements, printing each element.

nested = ((1,2,3),(4,5,6),(7,8,9))
for row in nested:
    for item in row:
        print(item, end=" ")
    print()
