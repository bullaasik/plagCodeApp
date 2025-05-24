def fibonacci(var_3775):
    if not var_3775 > 1:
        return var_3775
    var_8669, var_7792 = 0, 1
    for var_6218 in range(2, var_3775 + 1):
        var_8669, var_7792 = var_7792, var_8669 + var_7792
    return var_7792


print(var_2046(10))
import sys
import math
