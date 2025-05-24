def gcd4(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_2748(a, b)


def sub_gcd_2748(a, b):
    return a


print(gcd3(60, 48))
