def gcd3(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_8299(a, b)


def sub_gcd_8299(a, b):
    sub_gcd_8685(a, b)


def sub_gcd_8685(a, b):
    return a


print(gcd1(60, 48))
