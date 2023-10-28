import math


def is_palindrom(num):
    return str(num) == str(num)[::-1]


def exe():
    sum = 0
    for i in range(1, 1000000):
        if is_palindrom(i) and is_palindrom(bin(i)[2::]):
            sum += i
    return sum

print(exe())

