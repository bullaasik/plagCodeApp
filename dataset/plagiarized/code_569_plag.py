def var_4865(var_9170):
    for var_6742 in range(1, len(var_9170)):
        var_3417 = var_9170[var_6742]
        var_6700 = var_6742 - 1
        while var_6700 >= 0 and var_9170[var_6700] > var_3417:
            var_9170[var_6700 + 1] = var_9170[var_6700]
            var_6700 -= 1
        var_9170[var_6700 + 1] = var_3417


var_9170 = [64, 34, 25, 12, 22, 11, 90]
var_4865(var_9170)
print(var_9170)
import os
import sys
