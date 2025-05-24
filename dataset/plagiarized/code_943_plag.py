def var_5646(var_6569):
    for var_7241 in range(1, len(var_6569)):
        var_5480 = var_6569[var_7241]
        var_5338 = var_7241 - 1
        while var_5338 >= 0 and var_6569[var_5338] > var_5480:
            var_6569[var_5338 + 1] = var_6569[var_5338]
            var_5338 -= 1
        var_6569[var_5338 + 1] = var_5480


var_6569 = [64, 34, 25, 12, 22, 11, 90]
var_5646(var_6569)
print(var_6569)
import math
