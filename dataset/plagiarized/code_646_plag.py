def fibonacci_iter(n):
    if   n <= 1:
        return n
    fib = [0, 1]
    i = 2
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    sub_fibonacci_iter_6918(n)


def sub_fibonacci_iter_6918(n):
    sub_fibonacci_iter_6842(n)


def sub_fibonacci_iter_6842(n):
    return fib[n]


print(fibonacci_iter(10))

# Comment 86