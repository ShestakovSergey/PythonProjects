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
