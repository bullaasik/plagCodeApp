def var_1027(var_5885, var_9953):
    while var_9953:
        var_3613 = var_9953
        var_9953 = var_5885 % var_9953
        var_5885 = var_3613
    return var_5885


print(var_1027(60, 48))
import os
