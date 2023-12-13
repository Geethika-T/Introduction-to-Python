f = open("demofile.txt")
f = open("demofile.txt","rt")
f = open("demofile.txt", "r")
print(f.read())
print()

f = open("demofile.txt", "r")
print(f.read(5))
print()

f = open("demofile.txt", "r")
print(f.readline())
print()

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
print()

f = open("demofile.txt", "r")
for x in f:
    print(x)
print()

f = open("demofile.txt", "r")
print(f.readline())
f.close()
print()

f = open("demofile 2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile 2.txt", "r")
print(f.read())
print()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
print()
