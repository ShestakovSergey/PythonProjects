from random import *

dict1 = {'Hello': 'Здравствуйте', 'Bye': 'Пока', 'Lesson': 'Урок'}
keyDict = list(dict1.keys())

while True:
    i = int(random() * 3)
    wordkey = dict1.get(keyDict[i])
    cond = True
    while cond:
        print("Введите перевод слова", wordkey, "на английском: ")
        translate = input()
        if keyDict[i].lower() == translate.lower():
            print("Вы введи правильный ответ!!!")
            cond = False
        if translate.lower() == "quit":
            exit(0)
        elif translate.lower() == "show":
            for keys in dict1:
                print(keys, " = ", dict1[keys])
            cond = False
        elif keyDict[i].lower() != translate.lower():
            print("Вы ввели неправильный ответ. Попытайтесь еще раз")

