import math


def get_digit_sum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


def is_valid(num):
    sum_digits = get_digit_sum(num)
    sum = 0
    index = 1
    while True:
        sum = math.pow(sum_digits, index)
        if sum > num:
            return False
        elif sum == num:
            return True
        index += 1


def exe():
    l = []
    num = 10
    while len(l) < 30:
        if is_valid(num):
            l.append(num)
        num += 1
    return l[-1]





