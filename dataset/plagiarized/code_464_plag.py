def var_4420(var_1162):
    if   not var_1162 > 1:
        return var_1162
    var_3410, var_3532 = 0, 1
    var_2148 = 2
    while var_2148 < var_1162 + 1:
        var_3410, var_3532 = var_3532, var_3410 + var_3532
        var_2148 += 1
    return var_3532


print(var_4420(10))
import sys
import math
