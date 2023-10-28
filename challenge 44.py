import math
from itertools import permutations


def remove_repeats(l):
    new_l = []
    for i in l:
        if i not in new_l:
            new_l.append(i)
    return new_l


l = list(permutations([0, 0, 1, 1]))
print(remove_repeats(l))
print(len(remove_repeats(l)))
