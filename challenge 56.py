

def get_sum_digit(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


def exe():
    max = 0
    for i in range(1, 100):
        for j in range(1, 100):
            if get_sum_digit(i ** j) > max:
                max = get_sum_digit(i ** j)
    return max


print(exe())