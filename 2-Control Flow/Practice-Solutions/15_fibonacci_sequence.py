# Assignment 15: Fibonacci Sequence
n = int(input("Enter the number of Fibonacci terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b
