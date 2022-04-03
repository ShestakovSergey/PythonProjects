list = []
print(list)

list = ['h', 'e', 'l', 'l', 'o']
print(list[1])
print(list[0])
print("Последний элемент массива:", list[-1])
print("Последний элемент массива:", list[len(list) - 1])

print("-------------------------------------")

list = ['a', 3, 5, True, 3.5, '7.1']
i = 0
while i < len(list):
    print(list[i])
    i += 1

print(list)
list[1] = 'b'
list[len(list) - 1] = False
print(list)

list = [['a', 'b', 'c'], [1, 2, 3]]
print(list)

print("----------------------------------------------------")

i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1

print("----------------------------------------------------")

prices = [20, 30, 15, 37, 48, 17]
i = 0
minimum = prices[0]
maximum = prices[0]
while i < len(prices):
    if prices[i] < minimum:
        minimum = prices[i]
    if prices[i] > maximum:
        maximum = prices[i]
    i += 1
print("MIN value of prices:", minimum)
print("MAX value of prices:", maximum)

print("------------------HOMEWORK------------------------")

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
