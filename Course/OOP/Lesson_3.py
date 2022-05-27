class Arearectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


rds = Arearectangle(2, 3, 15, 10)

print(rds.x, ':', rds.y, ':', rds.w, ':', rds.h)
