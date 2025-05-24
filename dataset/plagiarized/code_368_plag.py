def gcd5(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd3(60, 48))

# Comment 22