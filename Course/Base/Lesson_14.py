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
