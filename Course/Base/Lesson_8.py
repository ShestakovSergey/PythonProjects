s = 0
while True:
    print("Введите число или sum, чтобы узнать сумму введеных чисел или exit, чтобы завершить процесс: ")
    j = input()
    if j == "sum":
        print("Сумма ваших чисел равна", s)
        s = 0
        j = 0
    elif j == "exit":
        exit(0)
    cont = int(j)
    s += cont