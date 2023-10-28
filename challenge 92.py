import math


def get_digits(num):
    l = []
    while num != 0:
        l.append(num % 10)
        num //= 10
    return l


def get_num_chain(num):
    new_num = 0
    l = [num]
    while 89 not in l and 1 not in l:
        for digit in get_digits(l[-1]):
            new_num += math.pow(digit, 2)
        l.append(new_num)
        new_num = 0
    return l[-1] == 89


def exe():
    count = 0
    for i in range(1, 10000000):
        if get_num_chain(i):
            count += 1
    return count



