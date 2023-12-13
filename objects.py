class Myclass:
    x = 5
print(Myclass)
class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Geethi", 22)
print(p1.name)
print(p1.age)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
p1 = Person("Geethi",22)
print(p1)
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunction(self):
        print("Hello my name is " + self.name)
p1 = Person("Geethi", 22)
p1.myfunction()
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
print(p1.age)
class Person :
    pass
# questions
class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
