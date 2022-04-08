#Строковые операции

mystr1 = "abc"
mystr2 = "xyz"

print("Конкатенация строк mystr1 and mystr2 =", mystr1 + mystr2)


mystr1 = '''Данная строка 
на несколько 
строк'''

print(mystr1)

#print("Введите первое число: ")
#number1 = int(input())
#print("Вы ввели", number1)

#print("Введите второе число: ")
#number2 = int(input())
#print("Вы ввели", number2)

#print("Сумма чисел", number1 + number2)

print("Введите первое число: ")
number1 = int(input())
print("Вы ввели", number1)

print("Введите второе число: ")
number2 = int(input())
print("Вы ввели", number2)

print("Введите первое число: ")
number3 = int(input())
print("Вы ввели", number3)

print("--------------------------------------------------")

print("Среднее арифметическое", number1, ",", number2, ",", number3, "=", ((number1 + number2 + number3) / 3))
