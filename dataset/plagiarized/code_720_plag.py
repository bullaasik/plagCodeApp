def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_1101(a, b)


def sub_gcd_iter_1101(a, b):
    sub_gcd_iter_7081(a, b)


def sub_gcd_iter_7081(a, b):
    return a


print(gcd_iter33(60, 48))
import sys

# Comment 85
# Comment 78