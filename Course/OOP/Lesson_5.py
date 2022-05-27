class Arearectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h

    def __str__(self):
        return "Rectangle x=" + str(self.__x) + " y=" + str(self.__y) + " w=" + str(self.__w) + " h=" + str(self.__h)

    def get_x(self):
        self.__printlog('Property requested x')
        return self.__x

    def get_y(self):
        self.__printlog('Property requested y')
        return self.__y

    def get_w(self):
        self.__printlog('Property requested w')
        return self.__w

    def get_h(self):
        self.__printlog('Property requested h')
        return self.__h

    def set_x(self, x):
        self.__x = x
        self.__printlog('Property changed x')

    def set_y(self, y):
        self.__y = y
        self.__printlog('Property changed y')

    def set_w(self, w):
        self.__w = w
        self.__printlog('Property changed w')

    def set_h(self, h):
        self.__h = h
        self.__printlog('Property changed h')

    def __printlog(self, z):
        print(z)

    def square(self):
        return self.__w * self.__h

    def perimeter(self):
        return 2 * (self.__w + self.__h)


rds = Arearectangle()

rds.set_x(6)
rds.set_y(9)
rds.set_h(100)
rds.set_w(20)
print(rds.get_x(), ':', rds.get_y(), ':', rds.get_w(), ':', rds.get_h())
print("Square of the rectangle", rds.square())
print("rectangle perimeter", rds.perimeter())
