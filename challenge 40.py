import math


def strip_num(num, l):
    for i in str(num):
        l.append(int(i))


def digit_list():
    l = []
    num = 1
    for i in range(1, 1000000):
        strip_num(num, l)
        num += 1
    print(l[0] * l[9] * l[99] * l[999] * l[9999] * l[99999] * l[999999])


digit_list()



