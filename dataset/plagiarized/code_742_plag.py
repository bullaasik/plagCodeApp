def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_4972(a, b)


def sub_gcd_iter_4972(a, b):
    sub_gcd_iter_7480(a, b)


def sub_gcd_iter_7480(a, b):
    return a


print(gcd_iter(60, 48))
import sys
import os
import sys

import os
import sys
import os