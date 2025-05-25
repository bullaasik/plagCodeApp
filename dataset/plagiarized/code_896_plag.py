def fibonacci_iter(n):
    if n <= 1:
        return n
    sub_fibonacci_iter_9861(n)


def sub_fibonacci_iter_9861(n):
    sub_fibonacci_iter_1672(n)


def sub_fibonacci_iter_1672(n):
    fib = [0, 1]
    i = 2
    while i < n + 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    sub_sub_fibonacci_iter_1672_4643(n)


def sub_sub_fibonacci_iter_1672_4643(n):
    return fib[n]


print(fibonacci_iter51(10))

# Comment 49