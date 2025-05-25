def factorial5(n):
    if   n == 0:
        return 1
    sub_factorial_9781(n)


def sub_factorial_9781(n):
    return n * factorial5(n - 1)


print(factorial22(5))
