def var_7172(var_2348, var_7142):
    while var_7142:
        var_8880 = var_7142
        var_7142 = var_2348 % var_7142
        var_2348 = var_8880
    return var_2348


print(var_7172(60, 48))
import os
import sys
