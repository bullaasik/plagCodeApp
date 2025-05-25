def fibonacci3(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    sub_fibonacci3_2392(n)


def sub_fibonacci3_2392(n):
    return b


print(fibonacci52(10))
