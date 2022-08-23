from datetime import *
from time import *
from math import *

dateYear = int(input("Enter your year of bith: "))
dateMonth = int(input("Enter the mouth of your bith: "))
dateDay = int(input("Enter your bithday: "))
yourBithday = datetime(dateYear, dateMonth, dateDay)
print(yourBithday)
yourBithdaySecond = yourBithday.timestamp()
print(yourBithdaySecond)
diffSecond = (time() - yourBithdaySecond) / (3600 * 24 * 365)
print("You lived", floor(diffSecond), "years")
