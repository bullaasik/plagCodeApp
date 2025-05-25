def var_2799(var_7300, var_5385):
    var_4586, var_9350 = 0, len(var_7300) - 1
    while var_4586 <= var_9350:
        var_3370 = (var_4586 + var_9350) // 2
        if var_7300[var_3370] == var_5385:
            return var_3370
        elif not var_7300[var_3370] >= var_5385:
            var_4586 = var_3370 + 1
        else:
            var_9350 = var_3370 - 1
    return -1


var_7300 = [1, 3, 5, 7, 9]
print(var_2799(var_7300, 5))

import sys