def gcd2(a, b):
    while b:
        a, b = b, a % b
    sub_gcd2_9893(a, b)


def sub_gcd2_9893(a, b):
    return a


print(gcd15(60, 48))
