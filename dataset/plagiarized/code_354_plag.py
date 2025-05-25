def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd23(60, 48))
# Comment 11
import sys
import math