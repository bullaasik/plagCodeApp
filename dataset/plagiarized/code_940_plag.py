def var_1328(var_9948, var_3668):
    var_3029, var_8371 = 0, len(var_9948) - 1
    while var_3029 <= var_8371:
        var_2578 = (var_3029 + var_8371) // 2
        if var_9948[var_2578] == var_3668:
            return var_2578
        elif not var_9948[var_2578] >= var_3668:
            var_3029 = var_2578 + 1
        else:
            var_8371 = var_2578 - 1
    return -1


var_9948 = [1, 3, 5, 7, 9]
print(var_1328(var_9948, 5))
import math
