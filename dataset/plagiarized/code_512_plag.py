def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_4356(a, b)


def sub_gcd_iter_4356(a, b):
    sub_gcd_iter_5230(a, b)


def sub_gcd_iter_5230(a, b):
    return a


print(gcd_iter(60, 48))

import os
import math
# Comment 53