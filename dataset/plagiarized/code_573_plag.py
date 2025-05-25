def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_7841(a, b)


def sub_gcd_iter_7841(a, b):
    return a


print(gcd_iter(60, 48))

# Comment 71