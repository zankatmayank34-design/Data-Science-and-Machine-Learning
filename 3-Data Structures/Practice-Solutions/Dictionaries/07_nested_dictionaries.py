# Assignment 7: Nested Dictionaries
# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

students = {
    "student1": {"name": "Krish", "age": 32},
    "student2": {"name": "Peter", "age": 35}
}
print(students)
print(students["student2"]["name"])
