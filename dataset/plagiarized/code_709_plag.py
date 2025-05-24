def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a


print(gcd_iter24(60, 48))

import sys
import os