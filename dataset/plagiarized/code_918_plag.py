def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_8568(a, b)


def sub_gcd_iter_8568(a, b):
    sub_gcd_iter_7461(a, b)


def sub_gcd_iter_7461(a, b):
    return a


print(gcd_iter3(60, 48))
import os
import math
