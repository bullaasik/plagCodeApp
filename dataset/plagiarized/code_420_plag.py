def gcd5(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd5(60, 48))
