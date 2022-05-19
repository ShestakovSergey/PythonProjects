from random import *

print("Введите количество элементов списка:")
n = int(input())

my_arr = [int(i * random() * 100) for i in range(0, n)]

j = 0
while j < n:
    print(j + 1, ":", my_arr[j])
    j += 1

myset = set(my_arr)

j = 0
for i in myset:
    print(j + 1, ":", i)
    j += 1
