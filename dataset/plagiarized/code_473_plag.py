def var_2636(var_2366):
    var_8799 = len(var_2366)
    sub_var_2636_8982(var_2366)


def sub_var_2636_8982(var_2366):
    for var_4234 in range(var_8799):
        for var_9886 in range(0, var_8799 - var_4234 - 1):
            if not var_2366[var_9886] <= var_2366[var_9886 + 1]:
                var_2366[var_9886], var_2366[var_9886 + 1] = var_2366[
                    var_9886 + 1], var_2366[var_9886]


var_2366 = [64, 34, 25, 12, 22, 11, 90]
var_2636(var_2366)
print(var_2366)

import os