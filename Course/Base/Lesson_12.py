#Кортежи

mytuple = tuple()
print(mytuple)

#Создание кортежа из одного элемента
mytuple = (1,)
print(mytuple)

mytuple = (1, '3', '5')
print(mytuple)
print(mytuple[1])

mytuple = tuple('Python')
print(mytuple)

print("-------------------HOMEWORK----------------------")

print("Введите произвольную строку:")
wordtuple = tuple(input())
for i in wordtuple:
    print(i)
