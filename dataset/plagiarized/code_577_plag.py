def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    sub_gcd_iter_9619(a, b)


def sub_gcd_iter_9619(a, b):
    sub_gcd_iter_4149(a, b)


def sub_gcd_iter_4149(a, b):
    sub_gcd_iter_1647(a, b)


def sub_gcd_iter_1647(a, b):
    return a


print(gcd_iter13(60, 48))
