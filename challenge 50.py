import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def get_primes_below_num(num):
    l = []
    for i in range(2, num):
        if is_prime(i):
            l.append(i)
    return l


def get_streak(num):
    l = get_primes_below_num(num)
    print(l)
    sum = 0
    temp = 0
    streak = 0
    for i in range(0, len(l) - 2):
        for j in l[i::]:
            sum += j
            temp += 1
            if sum == num:
                streak = temp
                return streak
            elif sum > num:
                sum = 0
                temp = 0
                break
        sum = 0
        temp = 0
    return streak


def exe():
    l = get_primes_below_num(1000000)
    d = {}
    max = 0
    for i in range(2, 1000000):
        if is_prime(i) and get_streak(i) > max:
            d[i] = get_streak(i)
    for i in d:
        if d[i] == max:
            return i


print(exe())







