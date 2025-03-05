#1 Завдання
for numbers in range(1, 11):
    print(numbers)

print("\n")

for numbers in range(2, 21, 2):
    print(numbers)

print("\n")

for numbers in range(10, 0, -1):
    print(numbers)

print("\n")

#2 Завдання
for numbers in range(1, 11):
    for numbers2 in range(1, 11):
        print(f"{numbers} * {numbers2} = {numbers * numbers2}")

#3 Завдання
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, мене звуть {self.name}"

class Student(Person):
    def is_student(self):
        return True

student = Student("Юра")

print(student.greet())
print(student.is_student())

#4 Завдання
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Площа кола:", circle.area())
print("Площа прямокутника:", rectangle.area())