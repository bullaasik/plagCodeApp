def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_5546(a, b)


def sub_gcd_5546(a, b):
    return a


print(gcd3(60, 48))
