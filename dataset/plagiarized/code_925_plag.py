def fibonacci_iter(n_):
    if     n_ <= 1: return n_
    fib = [0, 1]
    for v9 in range(2, n_ + 1):
        fib.append(fib[i_-1] + fib[i_-2])
    return fib[v8]
print(fibonacci_iter2(10))