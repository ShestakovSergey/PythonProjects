array = [1, 5, 0, -1.5, 2.5, 3, -5, 7, -4]
summ = 0

for n in array:
    summ += n

average = summ / len(array)
print(array)
print("The sum of the numbers is ", summ)
print("The arithmetic mean of the numbers is", average)
