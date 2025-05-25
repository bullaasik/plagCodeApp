def factorial3(n):
    if n == 0:
        return 1
    sub_factorial_1748(n)


def sub_factorial_1748(n):
    return n * factorial1(n - 1)


print(factorial3(5))
