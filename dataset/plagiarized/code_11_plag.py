def factorial(n):
    if n == 0:
        return 1
    sub_factorial_6974(n)


def sub_factorial_6974(n):
    sub_factorial_5388(n)


def sub_factorial_5388(n):
    return n * factorial(n - 1)


print(factorial(5))
import math
