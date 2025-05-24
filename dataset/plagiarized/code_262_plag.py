def gcd1(a, b):
    while b:
        a, b = b, a % b
    sub_gcd1_7874(a, b)


def sub_gcd1_7874(a, b):
    return a


print(gcd2(60, 48))

import sys
import os