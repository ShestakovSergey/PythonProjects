#Функции работы со списками и кортежами
'''
mylist = list(i for i in range(1, 11))
print(mylist)
print(len(mylist))
mylist.append(11)
mylist.extend([12, 13])
print(mylist)
mylist.insert(0, -1)
print(mylist)

print("-------------------------")

def nmbrIndex(str_nmb):
    arr = list(map(int, str_nmb.split()))
    try:
        return arr.index(5)
    except ValueError:
        print("Такого числа нет в списке!")

print(nmbrIndex(input("Введите числа через пробел: ")))

print([3, 6, 1, -1, 25, 8, 1, 7, 28].index(1))
print([3, 6, 1, -1, 25, 8, 1, 7, 28].index(1, 4))
print([3, 6, 1, -1, 25, 8, 1, 7, 28, 85, 1].count(1))

print("-----------------------")

list = [3, 6, 1, -1, 25, 8, 1, 7, 28]
list.reverse()
print(list)

list.remove(1)
print(list)

list.pop(4)
print(list)

list.sort()
print(list)
list.sort(reverse=True)
print(list)

# Все операци со списками так же работают и с кортежами, кроме тех, которые меняют значения

t = tuple("Hello")
print(t.index("e"))
print(t.count("l"))
'''

print("--------HOMEWORK---------")

lenList = int(input("Введите количество объектов в списке: "))
mylist = []
i = 0
while i < lenList:
    print("Введите число с порядковы номером", i, ":")
    numb = int(input())
    mylist.append(numb)
    i += 1
print(mylist)