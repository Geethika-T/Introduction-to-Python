class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunction(self):
        print("Hello my name is " + self.name)
p1 = Person("Geethi", 22)
p1.myfunction()

class Car():
    def __init__(self, colour, model, year):
        self.colour = colour
        self.model = model
        self.year = year
    def myfunction(self):
        print("The colour of the car is " + self.colour)
        print("The model of the car is "+ self.model)
p2 = Car("white", "Honda", 1999)
p2.myfunction()
class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def myfunction(self):
        print("The name of the book is " + self.name)
        print("The author of the book is "+ self.author)
p3 = Book("Harry Potter", "J.K Rowling")
p3.myfunction()
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
p4 = Circle(2)
print(p4.area())

