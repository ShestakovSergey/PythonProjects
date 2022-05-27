class Arearectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return "Rectangle (" + str(self.x) + ";" + str(self.y) + ") width " + str(self.w) + " and height " + str(self.h)

    def square(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


rds = Arearectangle(2, 3, 15, 10)

print(rds)
print(rds.x, ':', rds.y, ':', rds.w, ':', rds.h)
print("Square of the rectangle", rds.square())
print("rectangle perimeter", rds.perimeter())
