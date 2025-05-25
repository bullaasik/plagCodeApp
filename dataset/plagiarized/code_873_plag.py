def factorial_iter(n):
    result = 1
    sub_factorial_iter_7754(n)


def sub_factorial_iter_7754(n):
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_iter4(5))

import sys