#Строковые функции
'''
def isThisNumb(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

s1 = "ASUSVivoBook"
s2 = "MacBook\nAir"
s3 = r"MacBook\nAir"
s4 = "1387.56"
s5 = "    sdflkj   "

print(len(s1))
print(s1[3])
print(s1[-4])
print(s1[4:])

print(s2)
print(s3)

print(s1 * 2)
print(s1.find("S"))
print(s1.find("S", 2))

print(s1.isalpha())
print(s4.isdigit())
print(isThisNumb(s4))
print(s1.lower())
print(s1.upper())

print("----------------")

print(ord("а"))
for n in range(1072, 1104):
    print(chr(n))

print(s5)
print(s5.strip())

s6 = "Здравствуйте, {name}! Вам {age} лет!"
print(s6.format(name='Сергей', age=45))

s6 = "Здравствуйте, {0[0]}! Вам {0[1]} лет!"
data = ('Максим', 43)
print(s6.format(data))

s7 = "int: {0:d}; bin: {0:b}"
print(s7.format(127))

s8 = "Round: (150/29): {0:.4}"
print(s8.format(150 / 29))
'''

print("-----------HOMEWORK-------------")

str1 = input("Введите произвольную строку: ")

for w in str1:
    print(ord(w))


def checkStr(x):
    try:
        int(x)
        print("Спасибо!")
    except ValueError:
        print("Некорректный ввод")


str2 = input("Введите цифры: ")
checkStr(str2)

