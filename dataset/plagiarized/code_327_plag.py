def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    sub_fibonacci_2218(n)


def sub_fibonacci_2218(n):
    sub_fibonacci_5544(n)


def sub_fibonacci_5544(n):
    _ = 2
    while _ < n + 1:
        a, b = b, a + b
        _ += 1
    sub_sub_fibonacci_5544_5270(n)


def sub_sub_fibonacci_5544_5270(n):
    return b


print(fibonacci(10))

# Comment 84