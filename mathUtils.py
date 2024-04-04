from builtins import int
import math

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.sqrt(n));
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def is_palindrom(n: int) -> bool:
    return str(n) == str(n)[::-1];

def reverse_num(n: int) -> int:
    return int(str(n)[::-1]);

def is_int(n: float) -> bool:
    return str(n)[str(n).index('.')::] == '.0';

print(is_palindrom(10201));