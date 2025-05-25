def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_8015(a, b)


def sub_gcd_8015(a, b):
    return a


print(gcd42(60, 48))
