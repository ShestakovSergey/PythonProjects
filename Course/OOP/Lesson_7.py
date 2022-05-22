from abc import ABC, abstractmethod


class AutoGPS(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_gps(self):
        print("Location: ", self.x, ":", self.y)

    @abstractmethod
    def move_auto(self):
        pass


class Vehicle(AutoGPS):
    def __init__(self, x, y, brand, model, engine):
        AutoGPS.__init__(self, x, y)
        self.m = model
        self.b = brand
        self.e = engine

    def __str__(self):
        return "Brand: " + str(self.b) + "; Model: " + str(self.m) + "; Engine: " + str(self.e)

    def move_auto(self):
        print("Moved " + str(self.b) + " " + str(self.m) + " from", self.x, ":", self.y, "to", ":")


car = Vehicle(1, 1, "Tesla", "M1", "Electro")
print(car)
car.move_auto()
