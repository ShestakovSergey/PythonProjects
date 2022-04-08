#Цикл for и генератор списков

str = "Python"
print(str[0])
for s in str:
    print(s)

for s in str:
    if s == 'R':
        break
    print(s)
else:
    print("Символа R в стороке", str, "нет")

array = list(range(2, 15))
print(array)
for n in array:
    print(n)

print("----------------")

array = [i for i in range(1, 200) if (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5) and (i % 7 != 0 or i == 7) and (i % 11 != 0 or i == 11)]
print(array)

print("------------------HOMEWORK----------------------")

array = [1, 5, 0, -1.5, 2.5, 3, -5, 7, -4]
summ = 0
average = 0
for n in array:
    summ += n
average = summ / len(array)
print(array)
print("The sum of the numbers is ", summ)
print("The arithmetic mean of the numbers is", average)