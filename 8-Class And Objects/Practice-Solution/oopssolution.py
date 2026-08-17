import math

class Shape:
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
# shapes = [Circle(5), Square(4)]
# for shape in shapes:
#     print(shape.area())

def describe_shape(shape):
    print(f"The area of the shape is: {shape.area()}")

# Test
# circle = Circle(5)
# square = Square(4)
# describe_shape(circle)
# describe_shape(square)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

# Test
# car = Car()
# bike = Bike()
# car.start_engine()
# bike.start_engine()

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        return "Generic Fuel"

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def fuel_type(self):
        return "Petrol"

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def fuel_type(self):
        return "Diesel"

# Test
# car = Car()
# bike = Bike()
# print(car.fuel_type())
# print(bike.fuel_type())

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

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount

# Test
# account = BankAccount('12345678', 1000)
# account.deposit(500)
# account.withdraw(200)
# print(account.balance)  # 1300
# account.balance = -500  # Balance cannot be negative!

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Test
# student = Student('John', 20, 'S123')
# print(student.get_name(), student.get_age(), student.student_id)
# student.set_name('Alice')
# student.set_age(22)
# print(student.get_name(), student.get_age(), student.student_id)

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

# Test
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.speak()

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Test
# full_time = FullTimeEmployee(5000)
# part_time = PartTimeEmployee(20, 80)
# print(full_time.calculate_salary())  # 5000
# print(part_time.calculate_salary())  # 1600

class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = price

# Test
# product = Product('P001', 'Laptop', 1000)
# print(product.get_product_id(), product.get_name(), product.get_price())
# product.set_price(-500)  # Price cannot be negative!
# product.set_price(1500)
# print(product.get_product_id(), product.get_name(), product.get_price())

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

class Appliance(ABC):
    @property
    @abstractmethod
    def power(self):
        pass

class WashingMachine(Appliance):
    @property
    def power(self):
        return "500W"

class Refrigerator(Appliance):
    @property
    def power(self):
        return "300W"

# Test
# wm = WashingMachine()
# fridge = Refrigerator()
# print(wm.power)  # 500W
# print(fridge.power)  # 300W

class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = balance

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

# Test
# savings = SavingsAccount('12345678', 1000, 0.05)
# print(savings.get_account_number(), savings.get_balance(), savings.interest_rate)
# savings.set_balance(1500)
# print(savings.get_account_number(), savings.get_balance(), savings.interest_rate)

class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    def fly(self):
        print("Superhero flying...")

    def swim(self):
        print("Superhero swimming...")

# Test
# superhero = Superhero()
# superhero.fly()
# superhero.swim()

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Engineer(Worker):
    def work(self):
        print("Engineer working...")

class Doctor(Worker):
    def work(self):
        print("Doctor working...")

class Scientist(Engineer, Doctor):
    def work(self):
        Engineer.work(self)
        Doctor.work(self)

# Test
# scientist = Scientist()
# scientist.work()