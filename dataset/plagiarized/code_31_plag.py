def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_7498(a, b)


def sub_gcd_7498(a, b):
    sub_gcd_6111(a, b)


def sub_gcd_6111(a, b):
    return a


print(gcd(60, 48))
