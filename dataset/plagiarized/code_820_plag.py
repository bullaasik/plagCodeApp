def fibonacci_iter(n_):
    if   n_ <= 1: return v9
    fib = [0, 1]
    for i_ in range(2, v3 + 1):
        fib.append(fib[i_-1] + fib[v1-2])
    return fib[v6]
print(fibonacci_iter(10))
# Comment 53