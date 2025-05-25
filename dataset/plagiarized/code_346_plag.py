def factorial(n):
    if n == 0:
        return 1
    sub_factorial_1459(n)


def sub_factorial_1459(n):
    return n * factorial(n - 1)


print(factorial1(5))
