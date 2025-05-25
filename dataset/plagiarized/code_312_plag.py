def fibonacci1(n):
    if   n <= 1:
        return n
    sub_fibonacci1_9495(n)


def sub_fibonacci1_9495(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci1(10))
