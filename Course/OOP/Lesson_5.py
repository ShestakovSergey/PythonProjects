class Point:
    __x = 0
    __y = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __getx(self):
        return self.__x

    def __gety(self):
        return self.__y

    def __setx(self, x):
        self.__x = x

    def __sety(self, y):
        self.__y = y

    @staticmethod
    def __testing():  # private metod
        print("Private metod")

    def runprivate(self):  # public metod
        self.__testing()

    def get_x(self):
        return self.__getx()

    def get_y(self):
        return self.__gety()

    def set_x(self, x):
        self.__setx(x)

    def set_y(self, y):
        self.__sety(y)


p = Point(3, 5)
p.set_x(10)
p.set_y(20)
print(p.get_x())
print(p.get_y())

p.runprivate()
