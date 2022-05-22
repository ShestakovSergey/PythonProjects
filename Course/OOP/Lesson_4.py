from math import *


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def range(self, pobj):
        return sqrt((pobj.x - self.x) ** 2 + (pobj.y - self.y) ** 2)

    def __str__(self):
        return "Координаты: (" + str(self.x) + "; " + str(self.y) + ")"


class Auto:
    pobj = Point(0, 0)
    speed = 0

    def __init__(self, pobj=Point(0, 0), speed=0):
        self.pobj = pobj
        self.speed = speed

    def gettime(self, endp):
        if self.speed != 0:
            return self.pobj.range(endp) / self.speed
        else:
            return -1


p = Point(1, 1)
print(p)
print('----------------------')
print(p.range(Point()))
print(p.range(Point(3, 4)))

auto = Auto()
auto.speed = 50
print(auto.speed)
print(p)
print(auto.gettime(Point(3, 4)))
