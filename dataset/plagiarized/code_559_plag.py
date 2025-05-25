def fibonacci_iter(n):
    if  n <= 1:
        return n
    sub_fibonacci_iter_5656(n)


def sub_fibonacci_iter_5656(n):
    sub_fibonacci_iter_1161(n)


def sub_fibonacci_iter_1161(n):
    fib = [0, 1]
    i = 2
    sub_sub_fibonacci_iter_1161_4943(n)


def sub_sub_fibonacci_iter_1161_4943(n):
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n]


print(fibonacci_iter43(10))
