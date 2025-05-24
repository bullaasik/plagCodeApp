def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_1064(a, b)


def sub_gcd_1064(a, b):
    sub_gcd_1352(a, b)


def sub_gcd_1352(a, b):
    return a


print(gcd(60, 48))
