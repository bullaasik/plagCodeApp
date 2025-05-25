def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_4580(a, b)


def sub_gcd_iter_4580(a, b):
    sub_gcd_iter_9200(a, b)


def sub_gcd_iter_9200(a, b):
    return a


print(gcd_iter(60, 48))
import os
