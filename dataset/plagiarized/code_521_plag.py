def fibonacci_iter(n_):
    if n_ <= 1:
        return n_
    fib = [0, 1]
    sub_fibonacci_iter_5033(n_)


def sub_fibonacci_iter_5033(n_):
    for v7 in range(2, n_ + 1):
        fib.append(fib[v9 - 1] + fib[i_ - 2])
    return fib[n_]


print(fibonacci_iter(10))
