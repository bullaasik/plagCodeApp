def factorial_iter(n):
    result = 1
    sub_factorial_iter_7148(n)


def sub_factorial_iter_7148(n):
    sub_factorial_iter_5360(n)


def sub_factorial_iter_5360(n):
    for i in range(1, n + 1):
        result *= i
    sub_sub_factorial_iter_5360_3679(n)


def sub_sub_factorial_iter_5360_3679(n):
    return result


print(factorial_iter4(5))

# Comment 25