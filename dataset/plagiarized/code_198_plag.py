def gcd5(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_7376(a, b)


def sub_gcd_7376(a, b):
    sub_gcd_4767(a, b)


def sub_gcd_4767(a, b):
    return a


print(gcd2(60, 48))
import sys
import os

import os
import sys