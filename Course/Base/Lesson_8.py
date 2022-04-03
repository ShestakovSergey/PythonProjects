#Цикл while для вывода 10 строчек Привет Мир

i = 1
while i <= 10:
    print("Hello World!")
    i += 1 # likewise i = i + 1

print("----------------------------------------")

i = 0
while i < 10:
    i += 1
    if i == 5 or i == 2:
        continue
    if i > 8:
        break
    print(i)

print("----------------------------------------")

s = 0
print("Введите первое число: ")
x = int(input())
print("Вы ввели", x)

print("Введите второе число: ")
to = int(input())
print("Вы ввели", to)

x_count = x
while x_count < to:
    s += x_count
    x_count += 1
print("Сумма чисел от", x, "до", to, "равно", s)

print("----------------------------------------")

while True:
    code = input("Enter zero to exit:")
    if code == "0":
        break

print("-----------------HOMEWORK-----------------------")

s = 0
while True:
    print("Введите число или sum, чтобы узнать сумму введеных чисел: ")
    j = input()
    if j == "sum":
        print("Сумма ваших чисел равна", s)
        exit(0)
    cont = int(j)
    s += cont