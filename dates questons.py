#current date and time
import datetime
x = datetime.datetime.now()
print(x)
#current year
import datetime
x = datetime.datetime.now()
print(x.year)
#current month
import datetime
x = datetime.datetime.now()
print(x.strftime("%B"))
#day of month
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))
#day of week
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))
c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
