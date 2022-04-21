#Модули

from maxminavg import *

'''
#import math
#import random
from random import *
from math import sin, cos, pi
import math, cmath as cm
import calc


#print(random.randint(0, 10))
#print(math.sin(1))
print(randint(0, 100))
print(pi)
print(round(sin(pi / 2)))
print(round(cos(pi / 2)))
print(cm.log10(1000))

while True:
    print("1 - Сложение: 2 - Вычитание: 3 - Умножение: 4 - Деление: 0 - Выход")
    code = input("Введите команду: ")
    if code == "0":
        exit(0)
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if code == "1":
        r = calc.add(a, b)
    elif code == "2":
        r = calc.sub(a, b)
    elif code == "3":
        r = calc.mult(a, b)
    elif code == "4":
        r = calc.dev(a, b)
    print("Результат:", r)
'''

while True:
    print("1 - Максимум: 2 - Минимум: 3 - Среднее: 0 - Выход")
    code = input("Введите команду: ")
    if code == "0":
        exit(0)
    mylist = list(map(int, input("Введите список целых чисел через пробел: ").split()))
    if code == "1":
        r = maxnumbr(mylist)
    elif code == "2":
        r = minnumbr(mylist)
    elif code == "3":
        r = average(mylist)
    print("Результат:", r)