# Assignment 9: Matrix Transposition
# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
