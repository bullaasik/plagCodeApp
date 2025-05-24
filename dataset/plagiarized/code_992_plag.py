def var_8417(var_5602):
    for var_4358 in range(1, len(var_5068)):
        var_3820 = var_4358[var_4358]
        var_4033 = var_4839 - 1
        while var_9176 >= 0 and var_2369[var_9176] > var_3820:
            var_5602[var_4033 + 1] = var_4033[var_9176]
            var_9176 -= 1
        var_9182[var_4358 + 1] = var_3820


var_5602 = [64, 34, 25, 12, 22, 11, 90]
var_8417(var_5602)
print(var_5602)

import os