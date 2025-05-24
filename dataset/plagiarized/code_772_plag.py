def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_3773(a, b)


def sub_gcd_iter_3773(a, b):
    sub_gcd_iter_1331(a, b)


def sub_gcd_iter_1331(a, b):
    return a


print(gcd_iter23(60, 48))
