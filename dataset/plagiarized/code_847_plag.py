def var_7345(var_2645):
    if  not len(var_2645) <= 1:
        var_3814 = len(var_2645) // 2
        var_1392 = var_2645[:var_3814]
        var_1114 = var_2645[var_3814:]
        var_7345(var_1392)
        var_7345(var_1114)
        var_2543 = var_2610 = var_5097 = 0
        while var_2543 < len(var_1392) and var_2610 < len(var_1114):
            if  not var_1392[var_2543] > var_1114[var_2610]:
                var_2645[var_5097] = var_1392[var_2543]
                var_2543 += 1
            else:
                var_2645[var_5097] = var_1114[var_2610]
                var_2610 += 1
            var_5097 += 1
        while var_2543 < len(var_1392):
            var_2645[var_5097] = var_1392[var_2543]
            var_2543 += 1
            var_5097 += 1
        while var_2610 < len(var_1114):
            var_2645[var_5097] = var_1114[var_2610]
            var_2610 += 1
            var_5097 += 1


var_2645 = [10, 7, 8, 9, 1, 5]
var_7345(var_2645)
print(var_2645)

import os