thisset ={"apple", "mango", "orange"}
print(thisset)
thisset ={"apple", "mango", "orange"}
thisset.add("banana")
print(thisset)
thisset ={"apple", "mango", "orange"}
thisset.remove("orange")
print(thisset)
thisset ={"apple", "mango", "orange"}
thisset.discard("apple")
print(thisset)
thisset ={"apple", "mango", "orange"}
if "apple" in thisset:
    thisset.remove("apple")
    print(thisset)
else:
    print("apple is not in the list")
thisset ={"apple", "mango", "orange"}
if "banana" in thisset:
    thisset.remove("banana")
    print(thisset)
else:
    print("banana is not in the list")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
