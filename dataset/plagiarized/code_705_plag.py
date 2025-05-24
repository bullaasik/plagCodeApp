def fibonacci_iter(var_8410):
    if not var_8410 > 1:
        return var_8410
    var_5808 = [0, 1]
    for var_7310 in range(2, var_8410 + 1):
        var_5808.append(var_5808[var_7310 - 1] + var_5808[var_7310 - 2])
    return var_5808[var_8410]


print(var_8663(10))
import math
import sys
