def fibonacci_iter(n_):
    if     v7 <= 1: return n_
    fib = [0, 1]
    for v6 in range(2, v9 + 1):
        fib.append(fib[i_-1] + fib[v5-2])
    return fib[v1]
print(fibonacci_iter(10))
# Comment 44