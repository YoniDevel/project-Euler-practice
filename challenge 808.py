from builtins import int
import math 
from mathUtils import is_prime, is_palindrom, reverse_num, is_int


def exe() -> int:
    count: int = 0;
    sum: int = 0;
    number: int = 13;
    while(count < 50):
        a: float = math.sqrt(reverse_num(number ** 2));
        if (is_prime(number) 
        and not 
        is_palindrom(number ** 2)
        and 
        is_int(a)
        and
        is_prime(int(a))
        ):
            print(number, count);
            sum += number ** 2;
            print(sum);
            count += 1;
        number += 1;
    return sum;

print(exe());