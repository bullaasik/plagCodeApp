def fibonacci(n):
    if n <= 1:
        return n
    sub_fibonacci_2374(n)


def sub_fibonacci_2374(n):
    a, b = 0, 1
    _ = 2
    while _ < n + 1:
        a, b = b, a + b
        _ += 1
    return b


print(fibonacci(10))

# Comment 79