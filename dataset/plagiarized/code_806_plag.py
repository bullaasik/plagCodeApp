def factorial_iter(n):
    result = 1
    i = 1
    sub_factorial_iter_4353(n)


def sub_factorial_iter_4353(n):
    while i < n + 1:
        result *= i
        i += 1
    return result


print(factorial_iter(5))
import math
import sys
