def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a


print(gcd_iter(60, 48))
import os
import math
