def factorial3(n):
    if n == 0:
        return 1
    sub_factorial_1442(n)


def sub_factorial_1442(n):
    return n * factorial5(n - 1)


print(factorial3(5))
