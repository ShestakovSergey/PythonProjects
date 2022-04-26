class Point:
    __x = 0
    __y = 0
    def __init__(self, x, y,):
        self.__x = x
        self.__y = y
    def __getX(self):
        return self.__x
    def __getY(self):
        return self.__y
    def __setX(self, x):
        self.__x = x
    def __setY(self, y):
        self.__y = y
    def __test(self): # private metod
        print("Private metod")
    def runPrivate(self): # public metod
        self.__test()
    def geTx(self):
        return self.__getX()
    def geTy(self):
        return self.__getY()
    def seTx(self, x):
        self.__setX(x)
    def seTy(self, y):
        self.__setY(y)

p = Point(3, 5)
#print(p.__x) mistake
p.seTx(10)
p.seTy(20)
print(p.geTx())
print(p.geTy())

#p.__test()

p.runPrivate()
