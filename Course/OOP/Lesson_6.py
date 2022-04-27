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
