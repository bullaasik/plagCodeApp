def var_7589(var_7772, var_5446):
    var_6528, var_3107 = 0, len(var_7772) - 1
    while var_6528 <= var_3107:
        var_1999 = (var_6528 + var_3107) // 2
        if  not var_7772[var_1999] >= var_5446:
            var_6528 = var_1999 + 1
        elif  not var_7772[var_1999] <= var_5446:
            var_3107 = var_1999 - 1
        else:
            return var_1999
    return -1


var_7772 = [1, 3, 5, 7, 9]
print(var_75891(var_7772, 5))
import sys
