def var_9422(var_6740, var_3864):
    var_3765, var_7037 = 0, len(var_6740) - 1
    while var_3765 <= var_7037:
        var_5337 = (var_3765 + var_7037) // 2
        if var_6740[var_5337] == var_3864:
            return var_5337
        elif not var_6740[var_5337] >= var_3864:
            var_3765 = var_5337 + 1
        else:
            var_7037 = var_5337 - 1
    return -1


var_6740 = [1, 3, 5, 7, 9]
print(var_9422(var_6740, 5))
import os
