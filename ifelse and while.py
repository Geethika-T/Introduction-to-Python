a = 20
b = 40
if a < b:
    print("a less than b")
a = 36
b = 36
if a > b:
    print('A greater than B')
elif a == b:
    print("A is equal to B")
a = 200
b = 50
if b > a:
    print("B greater than A")
elif a == b:
    print("A equal to B")
else:
    print("A greater than B")
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
if a > b: print("a greater thn b")
a = 2
b = 100
print("GREATER") if a > b else print("LESS THAN")
a = 330
b = 330
print("GREATER") if a > b else print("NOT GREATER") if a == b else print("EQUAL")
print("EQUAL") if a == b else print("NOT EQUAL") if a > b else print("GREATER")
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
x = 51
if x > 10:
    print("greater than ten")
if x < 50:
    print("less than fifty")
else:
    print("less than 10")
a = 33
b = 200
if b > a:
    pass
i = 1
while i < 6:
    print(i)
    i += 1
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)
    fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
for x in range(6):
    print(x)
for x in range(2, 6):
    print(x)
for x in range(2, 30, 3):
    print(x)
for x in range(6):
    print(x)
else:
    print("Finally finished!")
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
for x in [0, 1, 2]:
    pass


