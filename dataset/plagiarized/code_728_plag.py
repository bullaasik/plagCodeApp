def var_7970(var_4192):
    var_2964 = 1
    while var_2964 < len(var_4192):
        var_1433 = var_4192[var_2964]
        var_5933 = var_2964 - 1
        while var_5933 >= 0 and var_4192[var_5933] > var_1433:
            var_4192[var_5933 + 1] = var_4192[var_5933]
            var_5933 -= 1
        var_4192[var_5933 + 1] = var_1433
        var_2964 += 1


var_4192 = [64, 34, 25, 12, 22, 11, 90]
var_7970(var_4192)
print(var_4192)
import sys
