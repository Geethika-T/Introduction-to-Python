thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
set1 = {"abc", 34, True, 40, "male"}
print(set1)
myset = {"apple", "banana", "cherry"}
print(type(myset))
thisset = set(("apple", "banana", "cherry"))
print(thisset)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)