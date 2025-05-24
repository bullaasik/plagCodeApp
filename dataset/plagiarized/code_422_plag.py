def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_6231(a, b)


def sub_gcd_6231(a, b):
    return a


print(gcd13(60, 48))
