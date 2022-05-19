from maxminavg import *

r = 0
while True:
    print("1 - Максимум: 2 - Минимум: 3 - Среднее: 0 - Выход")
    code = input("Введите команду: ")
    if code == "0":
        exit(0)
    mylist = list(map(int, input("Введите список целых чисел через пробел: ").split()))
    if code == "1":
        r = maxnumbr(mylist)
    elif code == "2":
        r = minnumbr(mylist)
    elif code == "3":
        r = average(mylist)
    print("Результат:", r)
