def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd5(60, 48))
# Comment 50
import os
import math