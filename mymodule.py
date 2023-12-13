def greeting(name):
    print("hello " + name)
person1 = {
  "name": "Geethika",
  "age": 22,
  "country": "India"
}
import platform
x = platform.system()
print(x)
import platform
x = dir(platform)
print(x)
import datetime
x = datetime.datetime.now()
print(x)
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
import datetime
x = datetime.datetime(2001, 8, 5)
print(x)
import datetime
x = datetime.datetime(2001, 8, 5)
print(x.strftime("%B"))
import datetime
x = datetime.datetime.now()
print(x.strftime("%a"))
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))
import datetime
x = datetime.datetime.now()
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%C"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%%"))
print(x.strftime("%G"))
print(x.strftime("%u"))
print(x.strftime("%V"))
x = min(5, 56, 8)
y = max(34, 8, 5)
print(x)
print(y)
x = abs(-5.67)
print(x)
x = pow(3,4)
print(x)
import math
x = math.sqrt(64)
print(x)
import math
x = math.ceil(2.5)
y = math.floor(3.5)
print(x)
print(y)
import math
x = math.pi
print(x)
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
import re
txt = "The rain in Spain"
x = re.split("\s", txt,1)
print(x)
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt,2)
print(x)
import re
txt = "The rain in Spain"
x = re.findall("[a-h]",txt)
print(x)
import re
txt = "That will be a 60 Dollars"
x = re.findall("\d",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("He..o", txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("^Hello",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("planet$",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("^Hello",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("He.*o",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("He.+o",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("He.?o",txt)
print(x)
import re
txt = "Hello planet"
x = re.findall("He.{2}o",txt)
print(x)
import re
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "8 times before 11:45 AM"
x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
