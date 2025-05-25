def var_1709(var_8896):
    for var_6491 in range(1, len(var_8896)):
        var_2090 = var_8896[var_6491]
        var_6410 = var_6491 - 1
        while var_6410 >= 0 and var_8896[var_6410] > var_2090:
            var_8896[var_6410 + 1] = var_8896[var_6410]
            var_6410 -= 1
        var_8896[var_6410 + 1] = var_2090


var_8896 = [64, 34, 25, 12, 22, 11, 90]
var_1709(var_8896)
print(var_8896)
import sys
import os
