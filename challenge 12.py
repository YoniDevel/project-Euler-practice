import math


def num_divisors(num):
    if num == 1:
        return 1
    count = 0
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            count += 2
    if math.sqrt(num) % 1 == 0:
        count -= 1
    return count


def is_triangle(num):
    temp = 1
    while num > (temp * (temp + 1)) // 2:
        temp += 1
    if (temp * (temp + 1)) // 2 == num:
        return True
    return False


def exe():
    num = 29
    while True:
        if is_triangle(num) and num_divisors(num) == 50:
            break
        num += 1
    print(num)





