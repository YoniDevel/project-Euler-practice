from itertools import permutations
import math



def split_digits(num):
    l = []
    while num != 0:
        l.append(num % 10)
        num //= 10
    return l[::-1]


def connect_digits(tup):
    num = 0
    for i in tup:
        num *= 10
        num += i
    return num


def is_cube(num):
    for i in range(1, num // 2):
        if int(math.pow(i, 3)) == num:
            return True
    return False


def exe():
    count = 0
    num = 1000
    while True:
        l = list(permutations(split_digits(int(math.pow(num, 3)))))
        for i in l:
            if is_cube(connect_digits(i)):
                count += 1
        if count == 5:
            break
    return num


print(exe())


