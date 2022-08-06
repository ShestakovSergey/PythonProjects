str1 = input("Введите произвольную строку: ")

for w in str1:
    print(ord(w))


def check_str(x):
    try:
        int(x)
        print("Спасибо!")
    except ValueError:
        print("Некорректный ввод")


str2 = input("Введите цифры: ")
check_str(str2)
