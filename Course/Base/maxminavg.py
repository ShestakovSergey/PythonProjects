def maxnumbr(number):
    maxi = number[0]
    for n in number:
        if n > maxi:
            maxi = n
    return maxi


def minnumbr(number):
    mini = number[0]
    for n in number:
        if n < mini:
            mini = n
    return mini


def average(number):
    s = 0
    for n in number:
        s += n
    return s / len(number)
