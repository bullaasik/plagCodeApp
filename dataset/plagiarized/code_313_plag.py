def gcd2(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_3590(a, b)


def sub_gcd_3590(a, b):
    return a


print(gcd4(60, 48))
