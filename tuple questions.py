thistuple = ("red", "yellow", "orange")
x = list(thistuple)
print(x)
thistuple = ("red", "yellow", "orange")
x = list(thistuple)
x.append("blue")
thistuple = tuple(x)
print(thistuple)
thistuple = ("red", "yellow", "orange")
x = list(thistuple)
x.remove("red")
thistuple =  tuple(x)
print(thistuple)