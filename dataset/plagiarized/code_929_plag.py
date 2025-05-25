def fibonacci_iter(n):
    if n <= 1:
        return n
    fib = [0, 1]
    sub_fibonacci_iter_4332(n)


def sub_fibonacci_iter_4332(n):
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


print(fibonacci_iter(10))
import math
import os
import sys
