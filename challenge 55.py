import math


def reverse_num(num):
    return int(str(num)[::-1])


def is_lychrel(num):
    count = 1
    sum = 0
    temp = num
    while count < 50:
        sum = temp + reverse_num(temp)
        if str(sum) == str(sum)[::-1]:
            return False
        count += 1
        temp += reverse_num(temp)
    return True


def exe():
    count = 0
    for i in range(1, 10000):
        if is_lychrel(i):
            count += 1
    return count


print(exe())