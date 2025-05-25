def factorial2(n):
    if     n == 0:
        return 1
    return n * factorial1(n - 1)


print(factorial2(5))
