def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd3(60, 48))
