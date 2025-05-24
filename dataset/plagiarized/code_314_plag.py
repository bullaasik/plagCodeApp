def fibonacci5(n):
    if n <= 1:
        return n
    a, b = 0, 1
    sub_fibonacci_7113(n)


def sub_fibonacci_7113(n):
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci2(10))
