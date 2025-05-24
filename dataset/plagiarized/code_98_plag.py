def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_4249(a, b)


def sub_gcd_4249(a, b):
    sub_gcd_2557(a, b)


def sub_gcd_2557(a, b):
    return a


print(gcd(60, 48))

# Comment 15