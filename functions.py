def my_function():
    print("hello from my function")
my_function()
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
def my_function(fname,lname):
    print(fname+" "+lname)
my_function("Emil", "Refsnes")
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
def my_function(country = "India"):
    print("I am from "+ country)
my_function()
my_function("Sweden")
my_function("Nepal")
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "orange","mango"]
my_function(fruits)
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print()


# example of recursion
def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(6))

# function questions
def myfunction(x,y):
    sum = x + y
    return sum
x = 5
y = 4
print(myfunction(x,y))
def area(r):
    area = 3.14 * r * r
    return area
r = 2
print(area(r))
# lambda
x = lambda a: a + 10
print(x(2))
x = lambda a, b: a * b
print(x(2,3))
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))
def my_function(n):
    return lambda a : a * n
mydoubler = my_function(2)
print(mydoubler(11))
def my_function(n):
    return lambda a : a * n
mytripler = my_function(3)
print(mytripler(11))
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
#arrays
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
cars[0] = "toyota"
print(cars[0])
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
for x in cars:
  print(x)
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

