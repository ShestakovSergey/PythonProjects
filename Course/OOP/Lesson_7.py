from abc import ABC, abstractmethod
'''
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(' + str(self.x) + ': ' + str(self.y) + ')')

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print('Draw circle (', self.x, ':', self.y, ':', self.r, ')')

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print('Draw rectangle (', self.x, ':', self.y, ':', self.w, ':', self.h, ')')

c = Circle(10, 20, 5)
c.draw()

r = Rectangle(0, 0, 30, 50)
r.draw()
r.h = 100
r.draw()

c.printXY()
r.printXY()
'''
print("----HOMEWORK------")

class autoGPS(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getGPS(self):
        print("Location: ", self.x, ":", self.y)

    @abstractmethod
    def moveAuto(self):
        pass

class vehicle(autoGPS):
    def __init__(self, x, y, brand, model, engine):
        autoGPS.__init__(self, x, y)
        self.m = model
        self.b = brand
        self.e = engine
    def __str__(self):
        return "Brand: " + str(self.b) + "; Model: " + str(self.m) + "; Engine: " + str(self.e)
    def moveAuto(self):
        print("Moved " + str(self.b) + " " + str(self.m) + " from", self.x, ":", self.y, "to", ":")

#location = autoGPS(1, 1)
#location.moveAuto(autoGPS(100, 200))
#location.moveAuto(autoGPS(400, 400))
car = vehicle(1, 1, "Tesla", "M1", "Electro")
print(car)
car.moveAuto()