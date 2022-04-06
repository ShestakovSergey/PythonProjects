import random

myset = set()
print(myset)

myset = set("Python")
print(myset)

myset = {'1', 2, 3, 1, '1'}
print(myset)

list = [int(i * random.random() * 10) for i in range(0, 10)]
print(list)
myset = set(list)
print(myset)

print("------------------------------HOMEWORK----------------------------")

print("Введите количество элементов списка:")
n = int(input())

list = [int(i * random.random() * 100) for i in range(0, n)]

j = 0
while j < n:
    print(j + 1, ":", list[j])
    j += 1

myset = set(list)

j = 0
for i in myset:
    print(j + 1, ":", i)
    j += 1
