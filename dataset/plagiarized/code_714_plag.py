def var_2273(var_7062, var_5191):
    var_6795, var_9530 = 0, len(var_7062) - 1
    while var_6795 <= var_9530:
        var_4056 = (var_6795 + var_9530) // 2
        if var_7062[var_4056] == var_5191:
            return var_4056
        elif not var_7062[var_4056] >= var_5191:
            var_6795 = var_4056 + 1
        else:
            var_9530 = var_4056 - 1
    return -1


var_7062 = [1, 3, 5, 7, 9]
print(var_2273(var_7062, 5))
import sys
