def gcd4(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd52(60, 48))

import sys