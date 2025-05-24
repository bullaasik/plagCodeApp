def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd(60, 48))

# Comment 9
import sys
import os