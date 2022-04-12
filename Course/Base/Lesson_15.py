#Глобальные и локальные переменные

isprint = False

def sum(x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s

def sub(x, y):
    global result
    result = float(x) - float(y)

result = 0

x = input("Введите первое число: ")
y = input("Введите второе число: ")
print("Сумма чисел равна: ", sum(x, y))
sub(x, y)
print("Разность равна: ", result)

print("--------------------------HOMEWORK------------------------------")

pi = 3.141592

def squarecircle(r):
    s = 0
    s = pi * r * r
    return s

r = float(input("Введите радиус окружности: "))

print("Площадь окружности с радиусом", r, "равна: ", squarecircle(r))
>>>>>>> origin
