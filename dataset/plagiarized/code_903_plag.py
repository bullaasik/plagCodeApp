def var_2780(var_4659):
    for var_3865 in range(1, len(var_4659)):
        var_2222 = var_4659[var_3865]
        var_2865 = var_3865 - 1
        while var_2865 >= 0 and var_4659[var_2865] > var_2222:
            var_4659[var_2865 + 1] = var_4659[var_2865]
            var_2865 -= 1
        var_4659[var_2865 + 1] = var_2222


var_4659 = [64, 34, 25, 12, 22, 11, 90]
var_2780(var_4659)
print(var_4659)
import os
import sys

# Comment 75