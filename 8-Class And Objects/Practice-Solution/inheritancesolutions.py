class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

# Test
# dog = Dog('Buddy', 'Canine', 'Golden Retriever')
# print(dog.name, dog.species, dog.breed)

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"

# Test
# dog = Dog('Buddy', 'Canine', 'Golden Retriever')
# print(dog)

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

# Test
# dog = Dog('Buddy', 'Canine', 'Golden Retriever')
# dog.bark()

class Walker:
    def walk(self):
        print("Walking...")

class Runner:
    def run(self):
        print("Running...")

class Athlete(Walker, Runner):
    pass

# Test
# athlete = Athlete()
# athlete.walk()
# athlete.run()

class Athlete(Walker, Runner):
    def walk(self):
        print("Athlete walking...")
        super().walk()

# Test
# athlete = Athlete()
# athlete.walk()

class Athlete(Walker, Runner):
    def __init__(self, training_hours):
        self.training_hours = training_hours

    def train(self):
        print(f"Training for {self.training_hours} hours.")

# Test
# athlete = Athlete(5)
# athlete.train()

class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

# Test
# d = D()
# d.show()  # B's show method

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

# Test
# circle = Circle('Red', 5)
# print(circle.color, circle.radius)

class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person, Employee):
    def __init__(self, name, employee_id):
        super().__init__(name)
        Employee.__init__(self, employee_id)

# Test
# manager = Manager('John', 'M123')
# print(manager.name, manager.employee_id)

class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car starting...")
        super().start()

# Test
# car = Car()
# car.start()

class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    pass

# Test
# superhero = Superhero()
# superhero.fly()
# superhero.swim()

class Base1:
    def __init__(self, a):
        self.a = a

class Base2:
    def __init__(self, b):
        self.b = b

class Derived(Base1, Base2):
    def __init__(self, a, b, c):
        super().__init__(a)
        Base2.__init__(self, b)
        self.c = c

# Test
# derived = Derived(1, 2, 3)
# print(derived.a, derived.b, derived.c)

class Animal:
    pass

class Cat(Animal):
    pass

# Test
# animal = Animal()
# cat = Cat()
# print(isinstance(animal, Animal))  # True
# print(isinstance(cat, Animal))  # True
# print(isinstance(cat, Cat))  # True
# print(isinstance(animal, Cat))  # False

class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        print("Parrot says: Squawk!")

class Penguin(Bird):
    def speak(self):
        print("Penguin says: Honk!")

# Test
# birds = [Parrot(), Penguin()]
# for bird in birds:
#     bird.speak()

class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, resolution)

# Test
# smartphone = Smartphone('Apple', 'iPhone 12', '12 MP')
# print(smartphone.brand, smartphone.model, smartphone.resolution)