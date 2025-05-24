def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    _ = 2
    while _ < n + 1:
        a, b = b, a + b
        _ += 1
    sub_fibonacci_3900(n)


def sub_fibonacci_3900(n):
    return b


print(fibonacci(10))
