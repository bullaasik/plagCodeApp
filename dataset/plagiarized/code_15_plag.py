def factorial(n):
    if n == 0:
        return 1
    sub_factorial_3038(n)


def sub_factorial_3038(n):
    sub_factorial_2393(n)


def sub_factorial_2393(n):
    return n * factorial(n - 1)


print(factorial3(5))

import math
import os