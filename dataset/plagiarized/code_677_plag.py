def factorial_iter(n):
    result = 1
    sub_factorial_iter_7485(n)


def sub_factorial_iter_7485(n):
    sub_factorial_iter_7463(n)


def sub_factorial_iter_7463(n):
    for i in range(1, n + 1):
        result *= i
    sub_sub_factorial_iter_7463_6105(n)


def sub_sub_factorial_iter_7463_6105(n):
    return result


print(factorial_iter(5))
import os
import math
