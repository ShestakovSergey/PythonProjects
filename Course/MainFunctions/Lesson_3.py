lenList = int(input("Введите количество объектов в списке: "))
mylist = []
i = 0
while i < lenList:
    print("Введите число с порядковым номером", i, ":")
    numb = int(input())
    mylist.append(numb)
    i += 1
print(mylist)
