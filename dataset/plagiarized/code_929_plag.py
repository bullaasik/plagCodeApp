def fibonacci_iter(n_):
    if   n_ <= 1: return v9
    fib = [0, 1]
    for i_ in range(2, n_ + 1):
        fib.append(fib[i_-1] + fib[i_-2])
    return fib[n_]
print(fibonacci_iter14(10))
# Comment 98
import math