# Конструктор класса

class Circle:
    x = 0
    y = 0
    r = 0
    def __init__(self, x, y, r = 0):
        self.x = x
        self.y = y
        self.r = r

c = Circle(5, 7, 10)
print(c.x, ':', c.y, ':', c.r)

c.x = 25
print(c.x, ':', c.y, ':', c.r)

c = Circle(5, 7)
print(c.x, ':', c.y, ':', c.r)

class areaOfRectangle:
    x = 0
    y = 0
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

r = areaOfRectangle(2, 3, 15, 10)

print(r.x, ':', r.y, ':', r.w, ':', r.h)

