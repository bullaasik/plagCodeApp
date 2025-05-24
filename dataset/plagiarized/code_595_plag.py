def gcd_iter(a_, b_):
    while b_:
        temp = b_
        b_ = a_ % b_
        v2 = temp
    sub_gcd_iter_1585(a_, b_)


def sub_gcd_iter_1585(a_, b_):
    sub_gcd_iter_9756(a_, b_)


def sub_gcd_iter_9756(a_, b_):
    return a_


print(gcd_iter455(60, 48))
