def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_2420(a, b)


def sub_gcd_2420(a, b):
    sub_gcd_1337(a, b)


def sub_gcd_1337(a, b):
    return a


print(gcd(60, 48))
