from math import *


class Test:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ':' + str(self.y)

    def range(self, pdj):
        return sqrt((pdj.x - self.x) ** 2 + (pdj.y - self.y) ** 2)


obj = Test(3, 4)
print(obj.x)
print(obj.y)
print(obj.range(Test()))
