def gcd(a, b):
    while b:
        a, b = b, a % b
    sub_gcd_9076(a, b)


def sub_gcd_9076(a, b):
    return a


print(gcd1(60, 48))

# Comment 15