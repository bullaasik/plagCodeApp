def fibonacci3(n):
    if n <= 1:
        return n
    sub_fibonacci3_9033(n)


def sub_fibonacci3_9033(n):
    sub_fibonacci3_8713(n)


def sub_fibonacci3_8713(n):
    a, b = 0, 1
    sub_sub_fibonacci3_8713_8756(n)


def sub_sub_fibonacci3_8713_8756(n):
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci4(10))
import os
import math
