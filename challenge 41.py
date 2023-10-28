import math


def is_pandigital(num):
    check_l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    digits_l = []
    while num != 0:
        digits_l.append(num % 10)
        num //= 10
    return sorted(digits_l) == check_l[:len(digits_l)]


def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def exe():
    max = 0
    for i in range(12, 7654322):
        if is_prime(i) and is_pandigital(i) and i > max:
            max = i
    return max


print(is_prime(7456321))


