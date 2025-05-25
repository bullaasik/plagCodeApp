def fibonacci2(n):
    if n <= 1:
        return n
    a, b = 0, 1
    _ = 2
    sub_fibonacci2_8195(n)


def sub_fibonacci2_8195(n):
    while _ < n + 1:
        a, b = b, a + b
        _ += 1
    return b


print(fibonacci3(10))
import math
