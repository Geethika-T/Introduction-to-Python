x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
x = 1  # int
y = 2.5  # float
z = 3+5j  # complex
# convert int to float
a = float(x)
# convert float to complex
b = complex(y)
# convert complex to int
c = int(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
import random

print(random.randrange(1, 10))

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
print("Hello")
print('Hello')
a = "Hello"
print(a)
a = """Python is a programming language.
It was created by Guido Van Rossom.
It was released in the year 1991."""
print(a)
a = '''Python is a programming language.
It was created by Guido Van Rossom.
It was released in the year 1991.'''
print(a)
a = "Hi, folks!"
print(a[5])
for x in "banana":
  print(x)
for x in "banana":
  print(x, end="")
print()
a = "Hi ,folks"
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("of" in txt)
b = "Hello, World "
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("e", "a"))
print(b.split(","))
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
item_no = 555
price = 50
MyOrder = "I want {} pieces of item {} for {} rupees. "
print(MyOrder.format(quantity, item_no, price))
quantity = 3
item_no = 555
price = 50
MyOrder = "I want to pay {2} rupees for {0} pieces of item {1}. "
print(MyOrder.format(quantity, item_no, price))
txt = "We are so called \"Vikings\" from the north"
print(txt)
txt = "It\'s alright"
print(txt)
txt = "This will insert one \\ (backslash)"
print(txt)
txt = "Hello\n World"
print(txt)
txt = "Hello\rWorld!"
print(txt)
txt = "Hello\tWorld"
print(txt)
txt = "Hello \bWorld"
print(txt)
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
txt = "banana"
x = txt.center(20)
print(x)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
txt = "My name is Ståle"
x = txt.encode()
print(x)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
txt = "Company12"
x = txt.isalnum()
print(x)
txt = "CompanyX"
x = txt.isalpha()
print(x)
txt = "Company123"
x = txt.isascii()
print(x)
txt = "1234"
x = txt.isdecimal()
print(x)
txt = "50800"
x = txt.isdigit()
print(x)
txt = "Demo"
x = txt.isidentifier()
print(x)
txt = "hello world!"
x = txt.islower()
print(x)
txt = "565543"
x = txt.isnumeric()
print(x)
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
txt = "   "
x = txt.isspace()
print(x)
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
txt = "banana"
x = txt.ljust(5)
print(x, "is my favorite fruit.")
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)