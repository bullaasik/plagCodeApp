def fibonacci_iter(v8):
    if n_ <= 1:
        return n_
    fib = [0, 1]
    i_ = 2
    while i_ < v9 + 1:
        fib.append(fib[i_ - 1] + fib[i_ - 2])
        i_ += 1
    return fib[v7]


print(fibonacci_iter(10))
