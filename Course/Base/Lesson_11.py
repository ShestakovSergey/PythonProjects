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

