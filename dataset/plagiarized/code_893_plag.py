def var_7418(var_9751, var_6270):
    var_9855, var_1203 = 0, len(var_9751) - 1
    while var_9855 <= var_1203:
        var_3483 = (var_9855 + var_1203) // 2
        if var_9751[var_3483] == var_6270:
            return var_3483
        elif not var_9751[var_3483] >= var_6270:
            var_9855 = var_3483 + 1
        else:
            var_1203 = var_3483 - 1
    sub_var_7418_2483(var_9751, var_6270)


def sub_var_7418_2483(var_9751, var_6270):
    return -1


var_9751 = [1, 3, 5, 7, 9]
print(var_7418(var_9751, 5))
import os
