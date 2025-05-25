def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_6405(a, b)


def sub_gcd_iter_6405(a, b):
    return a


print(gcd_iter34(60, 48))
import math
