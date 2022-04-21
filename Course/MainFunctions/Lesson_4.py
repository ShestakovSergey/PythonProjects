# Функции для работы с множество
from random import *

'''
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(len(set1))
print(len(set2))

set1.add(10)
print(set1)

set1.discard(10)
print(set1)

print("-------------------")
print(set1 == set2)
print(set1 < set2)
print(set1 > set2)

print("-------------------")
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

print("--------------------")
set1.clear()
set2.clear()
print(set1)
print(set2)
'''

print("----HOMEWORK--------")

set1 = set()
set2 = set()

i = 0
while i < 10:
    set1.add(int(random() * 10))
    set2.add(int(random() * 10))
    i += 1

print(set1)
print(set2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))