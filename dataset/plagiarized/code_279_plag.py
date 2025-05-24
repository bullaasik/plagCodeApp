def var_2438(var_8312):
    var_6395 = len(var_8312)
    var_8656 = 0
    while var_8656 < var_6395:
        for var_7961 in range(0, var_6395 - var_8656 - 1):
            if not var_8312[var_7961] <= var_8312[var_7961 + 1]:
                var_8312[var_7961], var_8312[var_7961 + 1] = var_8312[var_7961 + 1], var_8312[var_7961]
        var_8656 += 1


var_8312 = [64, 34, 25, 12, 22, 11, 90]
var_2438(var_8312)
print(var_8312)
import os
import sys
