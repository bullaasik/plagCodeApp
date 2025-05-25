def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd2(60, 48))
import os
import math
# Comment 56