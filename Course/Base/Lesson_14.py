#Функции

def printpython():
    print("Python")

printpython()

def sum(x, y):
    return x + y

s = sum(5, 7)
print(s)

def sub(x, y):
    return x - y

print(sub(10, 15))

def summaprint(x, y, r=False):
    s = x + y
    if r:
        return s
    else:
        print(s)
summaprint(8, 6)
print(6 + summaprint(8, 6, True))

def bigsumm(*numbers):
    s = 0
    print(numbers)
    for n in numbers:
        s += n
    return s

print(bigsumm(1, 3, 8, 2, 6, 10, 5))

def printdict(**dict):
    for key in dict:
        print(key, "=", dict[key])


printdict(name="Alex", age=15)

print("Анонимные функции")

lambdafunc = lambda  x, y: print(x + y)
print(lambdafunc(13, 17))

result = (lambda x, y: x + y)(1, 3)
print(result)

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

print(getmax([1, 3, 8, 2, 6, 10, 5]))

print("---------------HOMEWORK------------------------")

def evennumber(n):
    if (n % 2) == 0:
        return True
    else:
        return False

print("Enter number:")
numb = int(input())
print(evennumber(numb))

def average(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s / len(numbers)

print(average(1, 3, 7, 5, 35))
