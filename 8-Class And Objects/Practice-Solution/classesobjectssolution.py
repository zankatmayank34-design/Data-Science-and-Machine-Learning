class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Test
# car = Car('Toyota', 'Camry', 2020)
# print(car.make, car.model, car.year)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine has started.")

# Test
# car = Car('Toyota', 'Camry', 2020)
# car.start_engine()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Test
# student = Student('John', 20)
# print(student.name, student.age)

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

# Test
# account = BankAccount('12345678', 1000)
# account.deposit(500)
# account.withdraw(200)
# print(account.check_balance())  # 1300
# account.withdraw(2000)  # Insufficient balance!

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

# Test
# employee = Employee('Alice', 30, 'E123')
# print(employee.name, employee.age, employee.employee_id)

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id})"

# Test
# employee = Employee('Alice', 30, 'E123')
# print(employee)

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Test
# address = Address('123 Main St', 'New York', '10001')
# person = Person('John', 25, address)
# print(person.address.street, person.address.city, person.address.zipcode)

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Test
# c1 = Counter()
# c2 = Counter()
# c3 = Counter()
# print(Counter.get_count())  # 3

import math

class MathOperations:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

# Test
# print(MathOperations.sqrt(16))  # 4.0

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

# Test
# rect = Rectangle(10, 5)
# print(rect.length, rect.width)  # 10 5
# rect.length = 15
# rect.width = 7
# print(rect.length, rect.width)  # 15 7

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Test
# circle = Circle(5)
# square = Square(4)
# print(circle.area())  # 78.53981633974483
# print(square.area())  # 16

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
# print(v3)  # Vector(6, 8)

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance!")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

# Test
# account = BankAccount('12345678', 1000)
# account.deposit(500)
# try:
#     account.withdraw(2000)
# except InsufficientBalanceError as e:
#     print(f"Error: {e}")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Test
# with FileManager('sample.txt', 'r') as file:
#     content = file.read()
#     print(content)

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self

    def subtract(self, amount):
        self.value -= amount
        return self

    def multiply(self, amount):
        self.value *= amount
        return self

    def divide(self, amount):
        if amount != 0:
            self.value /= amount
        else:
            print("Cannot divide by zero!")
        return self

# Test
# calc = Calculator()
# calc.add(10).subtract(3).multiply(2).divide(2)
# print(calc.value)  # 7.0