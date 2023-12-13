#single inheritance
class Parent:
    def f1(self):
        print("hello parent")
class Child(Parent):
    def f2(self):
        print("hello child")
x = Child()
x.f1()
# multilevel inheritance
class Grandparent:
    def f1(self):
        print("Hello grandparent")
class Parent(Grandparent):
    def f2(self):
        print("Hello parent")
class Child(Parent):
    def f3(self):
        print("Hello child")
x = Child()
x.f1()
x.f2()
# multiple inheritance
class Parent1:
    def f1(self):
        print("Hello Parent1")
class Parent2:
    def f2(self):
        print("Hello Parent2")
class Child(Parent1,Parent2):
    def f3(self):
        print("Hello Child")
x = Child()
x.f1()
x.f2()
x.f3()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def f1(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
     Person.__init__(self, fname, lname)
x = Student("Geethika", "T")
x.f1()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
     super().__init__(fname, lname)
x = Student("Geethika", "T")
x.printname()
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
     super().__init__(fname, lname)
     self.graduationyear = 2023
x = Student("Geethika", "T")
x.printname()
print(x.graduationyear)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the graduation ceremony of ",self.graduationyear)
x = Student("Geethika","T",2023)
x.welcome()



