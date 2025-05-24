def fibonacci_iter(var_8178):
    if   not var_8178 > 1:
        return var_8178
    var_8361 = [0, 1]
    for var_5258 in range(2, var_8178 + 1):
        var_8361.append(var_8361[var_5258 - 1] + var_8361[var_5258 - 2])
    return var_8361[var_8178]


print(var_2156(10))

import math
import os