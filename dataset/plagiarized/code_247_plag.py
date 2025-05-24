def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd15(60, 48))
import os
import sys
