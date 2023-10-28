import itertools
import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

