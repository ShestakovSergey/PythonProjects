from datetime import *
from time import *

print(date.today())
print(datetime.today())

d = date(2025, 7, 15)
print(d)

dt = datetime.today()
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print("--------------------------------------------")

print(dt.strftime("%Y/%m/%d %H:%M:%S"))

print("-----------------------------------------")

print(time())
dt1 = datetime.fromtimestamp(1650624330.0)
print(dt1.strftime("%Y/%m/%d %H:%M:%S"))

print(dt.timestamp())

start = time()
i = 0
while i < 10000000:
    i += 1
print(time() - start)

