def factorial(n):
    if n == 0:
        return 1
    sub_factorial_9039(n)


def sub_factorial_9039(n):
    return n * factorial(n - 1)


print(factorial52(5))
