def factorial(n):
    if n == 0:
        return 1
    sub_factorial_9944(n)


def sub_factorial_9944(n):
    sub_factorial_7540(n)


def sub_factorial_7540(n):
    sub_factorial_9482(n)


def sub_factorial_9482(n):
    return n * factorial(n - 1)


print(factorial(5))
import os
