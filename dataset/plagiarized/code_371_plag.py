def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_2399(a, b)


def sub_gcd_2399(a, b):
    return a


print(gcd(60, 48))
