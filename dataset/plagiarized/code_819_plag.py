def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_4590(a, b)


def sub_gcd_iter_4590(a, b):
    return a


print(gcd_iter11(60, 48))
