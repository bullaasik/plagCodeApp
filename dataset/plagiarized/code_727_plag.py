def fibonacci_iter(v7):
    if n_ <= 1:
        return v1
    fib = [0, 1]
    v5 = 2
    while v5 < n_ + 1:
        fib.append(fib[i_ - 1] + fib[v9 - 2])
        v5 += 1
    return fib[n_]


print(fibonacci_iter(10))
