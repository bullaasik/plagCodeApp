def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_6739(a, b)


def sub_gcd_6739(a, b):
    return a


print(gcd(60, 48))

import os
import math
# Comment 67