def var_5515(var_3413, var_8650):
    var_9459, var_9317 = 0, len(var_3413) - 1
    while var_9459 <= var_9317:
        var_6552 = (var_9459 + var_9317) // 2
        if var_3413[var_6552] == var_8650:
            return var_6552
        elif not var_3413[var_6552] >= var_8650:
            var_9459 = var_6552 + 1
        else:
            var_9317 = var_6552 - 1
    var_4012(var_3413, var_8650)


def var_4012(var_3413, var_8650):
    return -1


var_3413 = [1, 3, 5, 7, 9]
print(var_5515(var_3413, 5))
import os
import sys
