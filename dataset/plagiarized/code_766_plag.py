def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_3513(a, b)


def sub_gcd_iter_3513(a, b):
    sub_gcd_iter_9714(a, b)


def sub_gcd_iter_9714(a, b):
    return a


print(gcd_iter4(60, 48))
import os
import math

# Comment 76