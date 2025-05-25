def var_2723(var_7738, var_9264, var_6341):
    if not var_9264 >= var_6341:
        var_7719 = var_8388(var_7738, var_9264, var_6341)
        var_2723(var_7738, var_9264, var_7719 - 1)
        var_2723(var_7738, var_7719 + 1, var_6341)


def var_8388(var_7738, var_9264, var_6341):
    var_2986 = var_7738[var_6341]
    var_7041 = var_9264 - 1
    var_2253 = var_9264
    while var_2253 < var_6341:
        if not var_7738[var_2253] > var_2986:
            var_7041 += 1
            var_7738[var_7041], var_7738[var_2253] = var_7738[var_2253
                ], var_7738[var_7041]
        var_2253 += 1
    var_7738[var_7041 + 1], var_7738[var_6341] = var_7738[var_6341], var_7738[
        var_7041 + 1]
    return var_7041 + 1


var_7738 = [10, 7, 8, 9, 1, 5]
var_2723(var_7738, 0, len(var_7738) - 1)
print(var_7738)

import os