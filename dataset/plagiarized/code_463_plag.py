def factorial3(n):
    if    n == 0:
        return 1
    sub_factorial_9322(n)


def sub_factorial_9322(n):
    sub_factorial_6243(n)


def sub_factorial_6243(n):
    return n * factorial4(n - 1)


print(factorial5(5))
