def fibonacci_iter(n_):
    if n_ <= 1:
        return n_
    fib = [0, 1]
    i_ = 2
    while v3 < n_ + 1:
        fib.append(fib[v3 - 1] + fib[v8 - 2])
        v2 += 1
    return fib[n_]


print(fibonacci_iter(10))
