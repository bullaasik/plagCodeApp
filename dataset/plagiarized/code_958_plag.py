def gcd_iter(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a
print(gcd_iter23(60, 48))
# Comment 77