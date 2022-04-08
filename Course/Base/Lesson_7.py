#Условный оператор if

print("Введите 0, 1 или 2:")
a = input()
if a == "0":
	print("Вы ввели ноль")
	print("Вы ввели меньше 10")
elif a == "1":
	print("Вы ввели один")
elif a == "2":
    print("Вы ввели два")
else:
    print("Некорректное число")

cond = a == "0" and (a != "1" or a != "2")

print("Вы ввели ноль") if cond else print("Вы ввели 1 или 2")


print("--------HOMEWORK----------")

print("Введите первое число:")
x = input()

print("Введите второе число отличное от 0:")
y = input()

z = (int(x) / int(y)) if y != "0" else print("Второе число не должно быть равно 0")

print(x, "/", y, "=", z)
