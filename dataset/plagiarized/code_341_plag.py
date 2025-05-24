def fibonacci5(n):
    if   n <= 1:
        return n
    sub_fibonacci_7442(n)


def sub_fibonacci_7442(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci5(10))
