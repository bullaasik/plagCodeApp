def gcd2(a, b):
    while b:
        a, b = b, a % b
    sub_gcd2_4400(a, b)


def sub_gcd2_4400(a, b):
    return a


print(gcd3(60, 48))

# Comment 15
import os