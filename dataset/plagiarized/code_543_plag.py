def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_2084(a, b)


def sub_gcd_iter_2084(a, b):
    sub_gcd_iter_4744(a, b)


def sub_gcd_iter_4744(a, b):
    sub_gcd_iter_6064(a, b)


def sub_gcd_iter_6064(a, b):
    return a


print(gcd_iter3(60, 48))

import math