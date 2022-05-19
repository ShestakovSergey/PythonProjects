pi = 3.141592


def squarecircle(rf):
    return pi * rf * rf


radius = float(input("Введите радиус окружности: "))

print("Площадь окружности с радиусом", radius, "равна: ", squarecircle(radius))
