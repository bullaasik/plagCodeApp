def gcd3(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_4651(a, b)


def sub_gcd_4651(a, b):
    return a


print(gcd4(60, 48))
