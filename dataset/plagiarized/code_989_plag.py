def var_7055(var_3456):
    var_9936 = 1
    while var_9936 < len(var_3456):
        var_5045 = var_3456[var_9936]
        var_6975 = var_9936 - 1
        while var_6975 >= 0 and var_3456[var_6975] > var_5045:
            var_3456[var_6975 + 1] = var_3456[var_6975]
            var_6975 -= 1
        var_3456[var_6975 + 1] = var_5045
        var_9936 += 1


var_3456 = [64, 34, 25, 12, 22, 11, 90]
var_7055(var_3456)
print(var_3456)

import sys