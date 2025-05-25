def fibonacci(n):
    if    n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print(fibonacci(10))
# Comment 29
import os
import sys
import sys