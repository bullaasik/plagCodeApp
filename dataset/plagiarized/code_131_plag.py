def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_1507(a, b)


def sub_gcd_1507(a, b):
    return a


print(gcd53(60, 48))
