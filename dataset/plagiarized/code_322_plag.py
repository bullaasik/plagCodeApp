def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    sub_fibonacci_7953(n)


def sub_fibonacci_7953(n):
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci(10))
