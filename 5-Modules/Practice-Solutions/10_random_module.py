import random

random_numbers = [random.randint(1, 50) for _ in range(5)]
print(random_numbers)

lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)
