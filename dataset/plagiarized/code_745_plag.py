def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_1254(a, b)


def sub_gcd_iter_1254(a, b):
    sub_gcd_iter_8251(a, b)


def sub_gcd_iter_8251(a, b):
    sub_gcd_iter_1071(a, b)


def sub_gcd_iter_1071(a, b):
    return a


print(gcd_iter224(60, 48))
import os
import math
