def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_8823(a, b)


def sub_gcd_8823(a, b):
    sub_gcd_4248(a, b)


def sub_gcd_4248(a, b):
    return a


print(gcd(60, 48))
