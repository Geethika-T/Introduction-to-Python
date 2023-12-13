thislist = ["apple", "mango", "orange"]
print(thislist)
thislist = ["apple", "mango", "orange", "apple", "cherry"]
print(thislist)
thislist = ["apple", "mango", "orange"]
print(len(thislist))
list1 = ["apple", "mango", "orange"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
print(list1)
print(list2)
print(list3)
list4 = ["Geethi", 20, 56.5, True]
print(list4)
list1 = ["apple", "mango", "orange"]
print(type(list1))
thislist = list(("apple", "mango", "orange"))
print(thislist)
thislist = ["apple", "mango", "orange"]
print(thislist[1])
thislist = ["apple", "mango", "orange"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:6])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-6:-1])
thislist = ["apple", "banana", "cherry"]
if "orange" in thislist:
    print("Yes, 'orange' is in the fruits list")
else:
    print("No ,'orange' is not in the fruits list")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
thislist = ["apple", "mango", "orange"]
thislist[1] = "banana"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon", "guava"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist1 = ["mango", "pineapple", "papaya"]
thislist.extend(thislist1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x, end=" ")
    print()
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1
thislist = ["apple", "banana", "cherry"]
[print(x)for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = [x.lower() for x in fruits]
print(newlist)
newlist = ['hello' for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return abs(n-50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)







