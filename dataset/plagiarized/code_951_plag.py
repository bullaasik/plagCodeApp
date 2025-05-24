def factorial_iter(n):
    result = 1
    sub_factorial_iter_8722(n)


def sub_factorial_iter_8722(n):
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_iter(5))

# Comment 44
# Comment 91