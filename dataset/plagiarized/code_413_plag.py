def fibonacci1(n):
    if   n <= 1:
        return n
    a, b = 0, 1
    _ = 2
    while _ < n + 1:
        a, b = b, a + b
        _ += 1
    return b


print(fibonacci4(10))
