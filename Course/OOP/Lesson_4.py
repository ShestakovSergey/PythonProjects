#

from math import *

class Point:
    x = 0
    y = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def __str__(self):
        return  "Координаты: (" + str(self.x) + "; " + str(self.y) + ")"

class Auto:
    p = Point(0, 0)
    speed = 0
    def __init__(self, p = Point(0, 0), speed = 0):
        self.p = p
        self.speed = speed
    def gettime(self, endp):
        if self.speed != 0:
            return  self.p.range(endp) / self.speed
        else:
            return  -1

p = Point(1, 1)
print(p)
print(p.range(Point()))
print(p.range(Point(3, 4)))

auto = Auto()
auto.speed = 50
print(auto.speed)
print(p)
print(auto.gettime(Point(3, 4)))