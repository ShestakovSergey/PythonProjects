class Circle:
    def __init__(self, x=0, y=0, rd=0):
        self.x = x
        self.y = y
        self.rd = rd
        if rd == 0:
            print("Radius equal zero")


c = Circle(5, 7, 10)
print(c.x, ':', c.y, ':', c.rd)

c.x = 25
print(c.x, ':', c.y, ':', c.rd)

c = Circle(5, 7)
print(c.x, ':', c.y, ':', c.rd)


class Arearectangle:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


rds = Arearectangle(2, 3, 15, 10)

print(rds.x, ':', rds.y, ':', rds.w, ':', rds.h)
