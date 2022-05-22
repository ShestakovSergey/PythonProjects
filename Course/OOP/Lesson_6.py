class AutoGPS:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_gps(self):
        print("Location: ", self.x, ":", self.y)

    def move_auto(self, location):
        print("Moved car from", self.x, ":", self.y, "to", location.x, ":", location.y)


class Vehicle(AutoGPS):
    def __init__(self, x, y, brand, model, engine):
        AutoGPS.__init__(self, x, y)
        self.m = model
        self.b = brand
        self.e = engine

    def __str__(self):
        return "Brand: " + str(self.b) + "; Model: " + str(self.m) + "; Engine: " + str(self.e)

    def move_auto(self, location):
        print("Moved " + str(self.b) + " " + str(self.m) + " from", self.x, ":", self.y, "to", location.x, ":", location.y)
        self.x = location.x
        self.y = location.y


location = AutoGPS(100, 100)
location.get_gps()
location.move_auto(AutoGPS(400, 400))
car = Vehicle(1, 1, "Tesla", "M1", "Electro")
print(car)
car.move_auto(AutoGPS(100, 200))
car.move_auto(AutoGPS(400, 400))
