def factorial_iter(n):
    result = 1
    sub_factorial_iter_3378(n)


def sub_factorial_iter_3378(n):
    i = 1
    while i < n + 1:
        result *= i
        i += 1
    sub_factorial_iter_2522(n)


def sub_factorial_iter_2522(n):
    return result


print(factorial_iter2(5))
