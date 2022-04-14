#Исключения
'''
while True:
    a = input("Введите положительное число: ")
    try:
        a = float(a)
        if a <= 0:
            raise Exception("Число не положительное!")
    except ValueError:
        print("Невозможно привести к числу")
    except Exception as exp:
        print(exp)
    else:
        print("Спасибо за корректный ввод")
    finally:
        print("В любом случае завершаем программу")
        exit(0)

'''
print("----------------HOMEWORK-----------------")

while True:
    a = input("Введите число: ")
    b = input("Введите число отличное от нуля: ")
    try:
        a = float(a)
        b = float(b)
        print(a / b)
    except ValueError:
        print("Невозможно привести к числу")
    except ZeroDivisionError:
        print("При деление на ноль получается бесконечность")
    finally:
        print("Завершение программы")
        exit(0)

