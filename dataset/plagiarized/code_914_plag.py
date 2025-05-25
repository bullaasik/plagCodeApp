def var_1325(var_8415):
    if not var_8415 > 1:
        return var_8415
    var_1686 = [0, 1]
    for var_2040 in range(2, var_8415 + 1):
        var_1686.append(var_1686[var_2040 - 1] + var_1686[var_2040 - 2])
    return var_1686[var_8415]


print(var_1325(10))
import math
