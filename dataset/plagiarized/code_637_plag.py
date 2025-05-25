def fibonacci_iter(n):
    if n <= 1:
        return n
    fib = [0, 1]
    sub_fibonacci_iter_4831(n)


def sub_fibonacci_iter_4831(n):
    i = 2
    sub_fibonacci_iter_9049(n)


def sub_fibonacci_iter_9049(n):
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    sub_sub_fibonacci_iter_9049_4795(n)


def sub_sub_fibonacci_iter_9049_4795(n):
    return fib[n]


print(fibonacci_iter(10))
