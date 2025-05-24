def fibonacci_iter(n):
    if n <= 1:
        return n
    sub_fibonacci_iter_2159(n)


def sub_fibonacci_iter_2159(n):
    fib = [0, 1]
    sub_fibonacci_iter_1658(n)


def sub_fibonacci_iter_1658(n):
    i = 2
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    sub_sub_fibonacci_iter_1658_2562(n)


def sub_sub_fibonacci_iter_1658_2562(n):
    return fib[n]


print(fibonacci_iter(10))

import math
import sys