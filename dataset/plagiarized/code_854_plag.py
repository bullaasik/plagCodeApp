def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_1121(a, b)


def sub_gcd_iter_1121(a, b):
    return a


print(gcd_iter5(60, 48))
import os
import math
