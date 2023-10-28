import math


def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def get_squares():
    l = []
    for i in range(1, 50000000):
        if is_prime(i):
            l.append(math.pow(i, 2))
    return l


def get_cubes():
    l = []
    for i in range(1, 50000000):
        if is_prime(i):
            l.append(math.pow(i, 3))
    return l


def get_fourths():
    l = []
    for i in range(1, 50000000):
        if is_prime(i):
            l.append(math.pow(i, 4))
    return l



