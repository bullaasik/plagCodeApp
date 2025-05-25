def fibonacci_iter(var_8682):
    if not var_8682 > 1:
        return var_8682
    var_6615 = [0, 1]
    for var_7096 in range(2, var_8682 + 1):
        var_6615.append(var_6615[var_7096 - 1] + var_6615[var_7096 - 2])
    sub_fibonacci_iter_9977(var_8682)


def sub_fibonacci_iter_9977(var_8682):
    return var_6615[var_8682]


print(var_5228(10))
import math
import os
