import math


def is_triangle(num):
    count = 1
    while True:
        if count * (count + 1) // 2 == num:
            return True
        elif count * (count + 1) // 2 > num:
            return False
        count += 1


def is_pentagonal(num):
    count = 1
    while True:
        if (3 * count ** 2 - count) // 2 == num:
            return True
        elif (3 * count ** 2 - count) // 2 > num:
            return False
        count += 1


def is_hexagonal(num):
    count = 1
    while True:
        if count * (2 * count - 1) == num:
            return True
        elif count * (2 * count - 1) > num:
            return False
        count += 1


def exe():
    num = 40756
    while True:
        if is_triangle(num) and is_pentagonal(num) and is_hexagonal(num):
            break
        num += 1
    return num


print(exe())