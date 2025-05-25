def var_3339(var_1866, var_8009):
    var_7660, var_9977 = 0, len(var_1866) - 1
    sub_var_3339_5004(var_1866, var_8009)


def sub_var_3339_5004(var_1866, var_8009):
    while var_7660 <= var_9977:
        var_1037 = (var_7660 + var_9977) // 2
        if  var_1866[var_1037] == var_8009:
            return var_1037
        elif  not var_1866[var_1037] >= var_8009:
            var_7660 = var_1037 + 1
        else:
            var_9977 = var_1037 - 1
    return -1


var_1866 = [1, 3, 5, 7, 9]
print(var_33393(var_1866, 5))

import os
# Comment 5