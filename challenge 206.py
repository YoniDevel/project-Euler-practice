from builtins import int
import math

digitsList: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

def is_matching_form(num: int):
    return str(num)[0::2] == '1234567890';

def get_unique_number():
    num = 349328506;
    while (not is_matching_form(num ** 2)):
        num += 1;
        print(num, num ** 2);
    return num

print(get_unique_number());