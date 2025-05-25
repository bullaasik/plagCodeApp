def gcd3(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd455(60, 48))

import sys