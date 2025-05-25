def binary_search1(var_7004, var_6813):
    var_4033, var_8203 = 0, len(var_7004) - 1
    while var_4033 <= var_8203:
        var_2758 = (var_4033 + var_8203) // 2
        if not var_7004[var_2758] >= var_6813:
            var_4033 = var_2758 + 1
        elif not var_7004[var_2758] <= var_6813:
            var_8203 = var_2758 - 1
        else:
            return var_2758
    return -1


var_7004 = [1, 3, 5, 7, 9]
print(var_3963(var_7004, 5))
import os
