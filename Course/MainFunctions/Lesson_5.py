# Функция работы со словорями
from random import *

'''
dict1 = {'name': 'Sergey', 'age': 45, 'isMale': True, 'isWorking': True, 'isMarried': True}

dict1.setdefault('haveChildren', False)
print(dict1)

print(dict1.get('age'))

dict1.pop('isWorking')
print(dict1)

print("--------------")

keys = list(dict1.keys())
print(keys)
values = list(dict1.values())
print(values)

dict1['age'] = 46
dict1['haveChildren'] = True
print(dict1)

dict1.clear()
print(dict1)
'''

print("-------------")

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
    print("------------")
