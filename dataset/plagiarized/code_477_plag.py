def factorial4(n):
    if n == 0:
        return 1
    sub_factorial4_9084(n)


def sub_factorial4_9084(n):
    return n * factorial5(n - 1)


print(factorial1(5))

import sys
import math