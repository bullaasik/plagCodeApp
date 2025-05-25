def var_2983(var_4288, var_3507, var_9516):
    if  not var_3507 >= var_9516:
        var_2587 = var_5050(var_4288, var_3507, var_9516)
        var_2983(var_4288, var_3507, var_2587 - 1)
        var_2983(var_4288, var_2587 + 1, var_9516)


def var_5050(var_4288, var_3507, var_9516):
    var_2879 = var_4288[var_9516]
    var_2100 = var_3507 - 1
    var_1000 = var_3507
    while var_1000 < var_9516:
        if  not var_4288[var_1000] > var_2879:
            var_2100 += 1
            var_4288[var_2100], var_4288[var_1000] = var_4288[var_1000], var_4288[var_2100]
        var_1000 += 1
    var_4288[var_2100 + 1], var_4288[var_9516] = var_4288[var_9516], var_4288[var_2100 + 1]
    return var_2100 + 1


var_4288 = [10, 7, 8, 9, 1, 5]
var_2983(var_4288, 0, len(var_4288) - 1)
print(var_4288)
import os
import math
