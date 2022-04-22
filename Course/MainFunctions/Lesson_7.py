# Функции работы с датой и временем

from datetime import *
from time import *
'''
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
while i < 100000000:
    i += 1
print(time() - start)
'''

# Homework

dateYear = int(input("Enter your year of bith: "))
dateMonth = int(input("Enter the mouth of your bith: "))
dateDay = int(input("Enter your bithday: "))
yourBithday = datetime(dateYear, dateMonth, dateDay)
print(yourBithday)
yourBithdaySecond = yourBithday.timestamp()
print(yourBithdaySecond)
diffSecond = (time() - yourBithdaySecond) / (3600 * 24 * 365)
print("You lived", round(diffSecond), "years")
