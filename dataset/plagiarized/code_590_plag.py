def var_4909(var_3075, var_4578):
    while var_4578:
        var_3774 = var_4578
        var_4578 = var_3075 % var_4578
        var_3075 = var_3774
    var_9350(var_3075, var_4578)


def var_9350(var_3075, var_4578):
    return var_3075


print(var_4909(60, 48))

import sys