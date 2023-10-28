import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_primes():
    l = []
    for i in range(2, 1000000):
        if is_prime(i):
            l.append(i)
    return l


def exe():
    l = get_primes()
    temp_l = l
    temp = 1
    sum = 0
    max_count = 0
    count = 1
    num = 0
    for i in l[162::]:
        for j in range(0, len(temp_l)):
            sum = temp_l[j]
            while sum < i:
                sum += temp_l[j + temp]
                temp += 1
                count += 1
            if sum == i and count > max_count:
                max_count = count
                num = i
            sum = 0
            temp = 1
            count = 0
    print(num, max_count)


exe()




