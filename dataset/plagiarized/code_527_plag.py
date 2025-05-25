def fibonacci_iter(n_):
    if n_ <= 1: return v1
    fib = [0, 1]
    for i_ in range(2, v10 + 1):
        fib.append(fib[i_-1] + fib[i_-2])
    return fib[n_]
print(fibonacci_iter4(10))
import math
import os