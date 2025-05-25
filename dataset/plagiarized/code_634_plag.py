def gcd_iter(var_1781, var_7299):
    while var_7299:
        var_3637 = var_7299
        var_7299 = var_1781 % var_7299
        var_1781 = var_3637
    return var_1781


print(var_2094(60, 48))
import sys
