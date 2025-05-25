def var_7230(var_3384, var_2022, var_6922):
    if   not var_2022 >= var_6922:
        var_8046 = var_8756(var_3384, var_2022, var_6922)
        var_7230(var_3384, var_2022, var_8046 - 1)
        var_7230(var_3384, var_8046 + 1, var_6922)


def var_8756(var_3384, var_2022, var_6922):
    var_4497 = var_3384[var_6922]
    var_6245 = var_2022 - 1
    for var_1513 in range(var_2022, var_6922):
        if   not var_3384[var_1513] > var_4497:
            var_6245 += 1
            var_3384[var_6245], var_3384[var_1513] = var_3384[var_1513], var_3384[var_6245]
    var_3384[var_6245 + 1], var_3384[var_6922] = var_3384[var_6922], var_3384[var_6245 + 1]
    return var_6245 + 1


var_3384 = [10, 7, 8, 9, 1, 5]
var_7230(var_3384, 0, len(var_3384) - 1)
print(var_3384)
import math
import os

# Comment 35