def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd24(60, 48))
# Comment 26
# Comment 29