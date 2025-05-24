def factorial_iter(n):
    result = 1
    sub_factorial_iter_7457(n)


def sub_factorial_iter_7457(n):
    i = 1
    while i < n + 1:
        result *= i
        i += 1
    return result


print(factorial_iter5(5))
import os
