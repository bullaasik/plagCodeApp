def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd3(60, 48))
import sys
import math

import os
import math