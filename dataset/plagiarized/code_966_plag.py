def fibonacci_iter(n):
    if n <= 1:
        return n
    sub_fibonacci_iter_9061(n)


def sub_fibonacci_iter_9061(n):
    fib = [0, 1]
    sub_fibonacci_iter_7833(n)


def sub_fibonacci_iter_7833(n):
    i = 2
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    sub_sub_fibonacci_iter_7833_9140(n)


def sub_sub_fibonacci_iter_7833_9140(n):
    return fib[n]


print(fibonacci_iter(10))
import math
import os

# Comment 84