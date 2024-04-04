from builtins import int
import math


def digitSum(num):
    sum = 0
    for digit in str(num):
        sum += int(digit);
    return sum


def s(num):
    if num < 10:
        return num
    else:
        candidate_number = 10
        while True:
            if digitSum(candidate_number) == num:
                return candidate_number
            candidate_number += 1


def S(num):
    sum = 0
    for i in range(1, num + 1):
        sum += s(i)
    return sum


def fibonacciSequence(index: int) -> list[int]:
    l = []
    l.append(0)
    l.append(1)

    for i in range(2, index + 1):
        l.append(l[i-2] + l[i - 1])
    return l

def exe():
    sum: int = 0;
    fibo: list[int] = fibonacciSequence(90);
    for num in fibo:
        print(num);
        sum += S(num);
    return sum % 1000000007;

exe()


