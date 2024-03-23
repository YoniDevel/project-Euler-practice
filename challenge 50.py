import math;
import mathUtils;

def get_primes_below_limit(limit: int) -> list[int]:
    l: list[int] = [];
    for i in range(2, limit):
        if mathUtils.is_prime(i):
            l.append(i);
    return l;

def get_consecutive_primes_sum(startNumber: int, limit: int): 
    primesList: list[int] = get_primes_below_limit(1000000);
    sum: int = 0;
    startIndex: int = primesList.index(startNumber);
    index: int = startIndex;
    while (sum < limit):
        sum += primesList[index];
        index += 1;
        if (sum == limit):
            return [True, index - startIndex];
        elif (sum > limit):
            return [False, index - startIndex];
def get_prime_which_is_longest_consecutive_primes_sum():
    maxLength: int = 0;
    maximizingPrime: int = 0;
    primesList: list[int] = get_primes_below_limit(1000000);
    for prime1 in primesList:
        print(prime1);
        for prime2 in primesList:
            result: list[int, bool] = get_consecutive_primes_sum(prime2, prime1);
            if result[0] and result[1] > maxLength:
                maxLength = result[1];
                maximizingPrime = prime1;
            if prime2 > prime1:
                break;
    return maximizingPrime;

def get_longest_consecutive_sum_bellow_limit(primeStart: int, primeLimit: int, primesList: list[int]) -> list[int]:
    sum: int = primeStart;
    index: int = primesList.index(primeStart);
    while (sum + primesList[index] < primeLimit):
        index += 1;
        sum += primesList[index];
    return [sum, index + 1];

def get_sum_of_list_between_indexes(list: list[int], startIndex: int, endIndex: int):
    return sum(list[startIndex: endIndex + 1]);

def get_longest_prime_sum_of_primes_bellow_limit(startPrime: int, limit: int):
    primesList: list[int] = get_primes_below_limit(100000);
    startIndex: int = primesList.index(startPrime);
    setback: int = 0;
    initials = get_longest_consecutive_sum_bellow_limit(startPrime, limit, primesList);
    sum: int = initials[0];
    while (not mathUtils.is_prime(sum)):
        setback += 1;
        sum = get_sum_of_list_between_indexes(primesList, startIndex, initials[1] - setback);
    return [sum, initials[1] - setback - startIndex];

def get_longest_consecutive_prime_sum_of_primes_bellow_limit(limit: int):
    primesList: list[int] = get_primes_below_limit(100000);
    print(primesList);
    maxLength: int = 0;
    maxPrime: int = 2;
    result: list[int] = [];
    for prime in primesList:
        print(prime, maxPrime, maxLength);
        result = get_longest_prime_sum_of_primes_bellow_limit(prime, limit);
        if (result[1] > maxLength):
            maxLength = result[1];
            maxPrime = result[0];
    return maxPrime;

print(get_longest_consecutive_prime_sum_of_primes_bellow_limit(1000000));
        
        



        
