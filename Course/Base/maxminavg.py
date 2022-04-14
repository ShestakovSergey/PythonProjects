def maxnumbr(number):
    max = number[0]
    for n in number:
        if n > max:
            max = n
    return max

def minnumbr(number):
    min = number[0]
    for n in number:
        if n < min:
            min = n
    return min

def average(number):
    s = 0
    for n in number:
        s += n
    return s / len(number)