# Работа с файлами

'''
handler = open('text.txt', 'w')
handler.write('Hello Sergey! How are you?')
handler.close()

handler = open('text.txt', 'r')
print(handler.read(14))
print(handler.read())
handler.seek(0)
print(handler.read())
handler.close()
'''

file = "text.txt"

while True:
    print("1 - Записать в фаил; 2 - Прочитать файл; 0 - Выход")
    imp = input("Введите команду: ")
    if imp == "0":
        exit(0)
    elif imp == "1":
        text = input("Введите строку: ")
        handler = open(file, 'a')
        handler.write(text + '\n')
        handler.close()
    elif imp == "2":
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла ещё не существует!")
    else:
        print("Неизвестная команда")

