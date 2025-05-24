def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_2788(a, b)


def sub_gcd_2788(a, b):
    sub_gcd_8391(a, b)


def sub_gcd_8391(a, b):
    return a


print(gcd(60, 48))
import os
import sys
