def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_2060(a, b)


def sub_gcd_2060(a, b):
    return a


print(gcd(60, 48))
import math
import os

# Comment 23