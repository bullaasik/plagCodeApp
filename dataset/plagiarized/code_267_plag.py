def var_9651(var_5930):
    if   not var_5930 > 1:
        return var_5930
    var_8364, var_9142 = 0, 1
    for var_5533 in range(2, var_5930 + 1):
        var_8364, var_9142 = var_9142, var_8364 + var_9142
    var_3927(var_5930)


def var_3927(var_5930):
    return var_9142


print(var_9651(10))
import sys
