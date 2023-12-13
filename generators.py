# generators
def function_name():
    yield 1
    yield 2
    yield 3
x = function_name()
print(next(x))
print(next(x))
print(next(x))
print()


generator_exp = (i * 5 for i in range(5) if i % 2 == 0)
for i in generator_exp:
    print(i)
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
