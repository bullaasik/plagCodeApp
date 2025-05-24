def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd1(60, 48))
import os
import sys
# Comment 30
import sys
import os