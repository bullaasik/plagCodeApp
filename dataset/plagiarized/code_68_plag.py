def factorial(n):
    if n == 0:
        return 1
    sub_factorial_8170(n)


def sub_factorial_8170(n):
    sub_factorial_7172(n)


def sub_factorial_7172(n):
    return n * factorial(n - 1)


print(factorial(5))
