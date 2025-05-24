def var_7250(var_8573):
    for var_6745 in range(1, len(var_8573)):
        var_2821 = var_8573[var_6745]
        var_1583 = var_6745 - 1
        while var_1583 >= 0 and var_8573[var_1583] > var_2821:
            var_8573[var_1583 + 1] = var_8573[var_1583]
            var_1583 -= 1
        var_8573[var_1583 + 1] = var_2821


var_8573 = [64, 34, 25, 12, 22, 11, 90]
var_7250(var_8573)
print(var_8573)
import os
import sys

import sys
# Comment 16