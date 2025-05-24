def factorial5(n):
    if n == 0:
        return 1
    sub_factorial_1749(n)


def sub_factorial_1749(n):
    return n * factorial2(n - 1)


print(factorial3(5))
