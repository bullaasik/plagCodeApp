def fibonacci_iter(n):
    if n <= 1:
        return n
    fib = [0, 1]
    sub_fibonacci_iter_3774(n)


def sub_fibonacci_iter_3774(n):
    i = 2
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n]


print(fibonacci_iter3(10))
