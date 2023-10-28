import math


def is_pandigital(num_list):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if sorted(num_list) == l:
        return True
    return False


def split_num(num, l):
    for s in str(num):
        l.append(int(s))


def join_list(l):
    s = ""
    for i in l:
        s += str(i)
    return int(s)


def concatenating_product(num):
    l = []
    mul = 1
    while True:
        split_num(mul * num, l)
        mul += 1
        if is_pandigital(l) or len(l) > 9:
            break
    if is_pandigital(l):
        return l
    else:
        return [0]


def exe():
    max = 927318546
    num = 9274
    while max == 927318546:
        if join_list(concatenating_product(num)) > max:
            max = join_list(concatenating_product(num))
        num += 1
    print("{}\n{}".format(max, num))


exe()




