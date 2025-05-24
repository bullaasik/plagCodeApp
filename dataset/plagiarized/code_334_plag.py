def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd2(60, 48))

import sys
import math