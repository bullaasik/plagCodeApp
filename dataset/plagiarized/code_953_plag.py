def fibonacci_iter(n):
    if n <= 1:
        return n
    sub_fibonacci_iter_5037(n)


def sub_fibonacci_iter_5037(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


print(fibonacci_iter5(10))
import math
