from  itertools import permutations


perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def join_tup(tup):
    s = ""
    for i in tup:
        s += str(i)
    if s[0] == "0":
        return int(s[1::])
    else:
        return int(s)


def is_valid(tup):
    if join_tup(tup[1:4]) % 2 == 0 and join_tup(tup[2:5]) % 3 == 0 and join_tup(tup[3:6]) % 5 == 0 and join_tup(tup[4:7]) % 7 == 0 and join_tup(tup[5:8]) % 11 == 0 and join_tup(tup[6:9]) % 13 == 0 and join_tup(tup[7:10]) % 17 == 0:
        return True
    return False


def exe(l):
    sum = 0
    for i in l:
        if is_valid(i):
            sum += join_tup(i)
    print(sum)


exe(list(perm))





