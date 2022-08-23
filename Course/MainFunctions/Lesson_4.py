from random import *

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
