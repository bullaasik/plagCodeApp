def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd4(60, 48))
