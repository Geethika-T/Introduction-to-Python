mytuple = ("apple", "banana", "orange")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)
mystr = "banana"
for x in mystr:
    print(x)
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
class Mynumbers():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = Mynumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang") # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")   # Create a Plane class
for x in (car1, boat1, plane1):
  x.move()
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
def myfunction():
    x =200
    print(x)
myfunction()
def myfunction():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunction()
x = 400
def myfunc():
  print(x)
myfunc()
print(x)
x = 600
def myfunc():
  x = 500
  print(x)
myfunc()
print(x)
import mymodule
mymodule.greeting("Geethi")
import mymodule
a = mymodule.person1["age"]
print(a)
import mymodule as mx
a = mx.person1["name"]
print(a)
from mymodule import person1
print(person1["country"])

