def fibonacci_iter(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    sub_fibonacci_iter_9631(n)


def sub_fibonacci_iter_9631(n):
    return fib[n]


print(fibonacci_iter2(10))
