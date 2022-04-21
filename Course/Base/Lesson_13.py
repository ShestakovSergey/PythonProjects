#Словари
'''
mydict = dict()
print(mydict)

mydict = {'Name': 'Jonn', 'Age': 35}
print(mydict)

mydict = dict(Name='Smit', Age=46, isMale=True)
print(mydict)

print(mydict['Age'])

print("-------------------------------------")

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'isMale')
for key in mytuple:
    print(key, '=', mydict[key])

mydict = {str(i): i * 3 for i in range(1, 10)}
print(mydict)
'''

print("-------------------HOMEWORK----------------------")

mydict = {'name': 'none', 'age': -1}
print(mydict)
yourName = input("Введите ваше имя: ")
yourAge = input("Введите ваш возраст: ")
mydict['name'] = yourName
mydict['age'] = yourAge
print(mydict)

