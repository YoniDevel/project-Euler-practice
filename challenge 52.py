from itertools import permutations


def strip_num(num):
    l = []
    while num != 0:
        l.append(num % 10)
        num //= 10
    return sorted(l)


def is_permuted(og_num, num):
    if strip_num(og_num) == strip_num(num):
        return True
    return False


def is_valid(num):
    if is_permuted(num, num * 2) and is_permuted(num, num * 3) and is_permuted(num, num * 4) and is_permuted(num, num * 5) and is_permuted(num, num * 6):
        return True
    return False


def exe():
    for i in range(11, 1000000):
        if is_valid(i):
            return i


print(exe())
