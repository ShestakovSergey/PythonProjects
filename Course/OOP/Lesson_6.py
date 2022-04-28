'''
class Shape:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print("(" + self.x + "; " + self.y + ")")
    def draw(self):
        print("Draw figure")

class Circle(Shape):
    def __init__(self, x, y, r = 0):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print("Draw circle (", self.x, ";", self.y, ";", self.r, ")")

class Rectangle(Shape):
    w = 0
    h = 0


    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print("Draw rectangle (", self.x, ";", self.y, ";", self.w, ";", self.h,  ")")

s = Shape(5, 7)
s.draw()

c = Circle(10, 20, 5)
c.draw()

r = Rectangle(5, 15, 30, 40)
r.draw()
'''

print("----HOMEWORK------")

class autoGPS:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getGPS(self):
        print("Location: ", self.x, ":", self.y)
    def moveAuto(self, location):
        print("Moved car from", self.x, ":", self.y, "to", location.x, ":", location.y)

class vehicle(autoGPS):
    brand = "no"
    model = "no"
    capacity = 0
    mileage = 0
    def __init__(self, x, y, brand, model, capacity, mileage):
        autoGPS.__init__(self, x, y)
        self.md = model
        self.b = brand
        self.c = capacity
        self.ml = mileage
    def __str__(self):
        return "Brand: " + str(self.b) + " Model: " + str(self.md)

location = autoGPS(1, 1)
location.moveAuto(autoGPS(100, 200))
car = vehicle(1, 1, "Hyundai", "Solaris", 2, 50)
print(car)

