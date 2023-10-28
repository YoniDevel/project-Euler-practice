import math


def is_abundant(num):
    sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += i
            if num // i != i:
                sum += num // i
    if sum > num:
        return True
    return False


def abundant_list():
    l = []
    for num in range(12, 28112):
        if is_abundant(num):
            l.append(num)
    return l


def is_a_sum_of_two(l, num):
    p1 = 0
    p2 = len(l) - 1
    while True:
        if p2 < p1:
            return False
        elif l[p1] + l[p2] == num:
            return True
        elif l[p1] + l[p2] > num:
            p2 -= 1
        elif l[p1] + l[p2] < num:
            p1 += 1


def target_sum():
    sum = 0
    abundant_numbers_list = abundant_list()
    for num in range(1, 28124):
        if not is_a_sum_of_two(abundant_numbers_list, num):
            sum += num
    return sum


print(target_sum())
