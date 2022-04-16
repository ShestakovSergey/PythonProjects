#Математические функции

from math import *

print(e)
print(pi)

print("--------------------------")

print(round(sin(radians(30)), 3))
print(round(cos(radians(60)), 3))
print(round(tan(radians(45)), 3))

print(degrees(1))

print("-----------------------")

print(abs(-5))
print(floor(5.9))
print(ceil(5.1))

x = 4
y = 3
print(sqrt(x * x + y * y))

print("-------------------------")

print(round(7 / 9, 3))

print("-----------------HOMEWORK--------------------------")

print(round(113 / 300, 4))

print("------------------------------")

for n in range(0, 181):
    print(n, "=", sin(radians(n)))