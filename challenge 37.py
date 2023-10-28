import math


def is_prime(num):
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def num_cuts(num):
    l = []
    temp = num
    while temp != 0:
        l.append(temp)
        temp //= 10
    count = 1
    while count < len(str(num)):
        l.append(int(str(num)[count::]))
        count += 1
    return l


def is_truncatable(num):
    if num % 2 != 0:
        for i in num_cuts(num):
            if not is_prime(i):
                return False
        return True
    return False


def exe():
    sum = 0
    for i in range(11, 1000000):
        if is_truncatable(i):
            sum += i
    return sum


print(exe())

