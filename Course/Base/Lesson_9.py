fruits = ['apple', 'apricots', 'avocado', 'banano', 'blackberries', 'blackcurrant', 'carambola']
t = 0
while t < len(fruits):
    print(t, "-", fruits[t])
    t += 1
print("Input index of element list fruits:")
y = int(input())
if y < 0 or y >= len(fruits):
    print("Element isn't likewise index")
    exit(0)
print(fruits[y])
