def gcd_iter(a_, b_):
    while b_:
        temp = v1
        b_ = a_ % v1
        a_ = temp
    return a_


print(gcd_iter1(60, 48))
