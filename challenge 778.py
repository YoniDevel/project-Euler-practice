import math


def length(num):
    return len(str(num))

def get_number_of_appearances(num, digit):
    counter = 0
    for d in str(num):
        if str(digit) == d:
            counter += 1
    return counter


def is_dominant(num):
    pass
