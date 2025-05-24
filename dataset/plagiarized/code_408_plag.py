def gcd4(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd54(60, 48))
# Comment 61