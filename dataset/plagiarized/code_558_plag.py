def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_4648(a, b)


def sub_gcd_iter_4648(a, b):
    sub_gcd_iter_5620(a, b)


def sub_gcd_iter_5620(a, b):
    return a


print(gcd_iter(60, 48))
import math
import os
