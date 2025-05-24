def factorial(n):
    if  n == 0:
        return 1
    sub_factorial_5408(n)


def sub_factorial_5408(n):
    return n * factorial(n - 1)


print(factorial(5))
