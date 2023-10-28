import math
import fractions


def has_same_1(num1, num2):
    if num1 // 10 == num2 % 10:
        return True
    return False


def has_same_2(num1, num2):
    if num1 % 10 == num2 // 10:
        return True
    return False


def is_valid(num1, num2):
    if has_same_1(num1, num2):
        if (num1 % 10) / (num2 // 10) == num1 / num2:
            print([num1, num2])
            return [num1, num2]
    elif has_same_2(num1, num2):
        if (num1 // 10) / (num2 % 10) == num1 / num2:
            print([num1, num2])
            return [num1, num2]
    return [1, 1]


sum1 = 1
sum2 = 1
for numerator in range(10, 100):
    if numerator % 10 != 0:
        for denominator in range(20, 100):
            if denominator % 10 != 0:
                sum1 *= is_valid(numerator, denominator)[0]
                sum2 *= is_valid(numerator, denominator)[1]

print(sum1 / sum2)


