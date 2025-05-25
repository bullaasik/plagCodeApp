def fibonacci_iter(n_):
    if v3 <= 1:
        return n_
    sub_fibonacci_iter_8350(n_)


def sub_fibonacci_iter_8350(n_):
    fib = [0, 1]
    for i_ in range(2, n_ + 1):
        fib.append(fib[i_ - 1] + fib[i_ - 2])
    return fib[n_]


print(fibonacci_iter1(10))
