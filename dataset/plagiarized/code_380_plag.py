def var_3795(var_4383):
    if not var_4383 > 1:
        return var_4383
    var_3724, var_7947 = 0, 1
    for var_4736 in range(2, var_4383 + 1):
        var_3724, var_7947 = var_7947, var_3724 + var_7947
    return var_7947


print(var_3795(10))
import os
import math

# Comment 86