def factorial(n_):
    if n_ == 0:
        return 1
    sub_factorial_6021(n_)


def sub_factorial_6021(n_):
    return n_ * factorial(n_ - 1)


print(factorial(5))
