def fibonacci_iter(v4):
    if   n_ <= 1:
        return v4
    sub_fibonacci_iter_3843(v4)


def sub_fibonacci_iter_3843(v4):
    fib = [0, 1]
    for v7 in range(2, v9 + 1):
        fib.append(fib[v3 - 1] + fib[i_ - 2])
    return fib[v8]


print(fibonacci_iter2(10))
