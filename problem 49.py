import math
from itertools import permutations as perm


def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primesList():
    l = []
    for i in range(1001, 10000, 2):
        if isPrime(i):
            l.append(i)
    return l


