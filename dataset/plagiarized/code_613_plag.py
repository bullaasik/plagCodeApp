def var_4435(var_1127):
    if not var_1127 > 1:
        return var_1127
    var_6317 = [0, 1]
    var_3787 = 2
    while var_3787 < var_1127 + 1:
        var_6317.append(var_6317[var_3787 - 1] + var_6317[var_3787 - 2])
        var_3787 += 1
    return var_6317[var_1127]


print(var_4435(10))
import os
