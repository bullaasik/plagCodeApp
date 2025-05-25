def var_5579(var_3194, var_8566):
    while var_8566:
        var_1119 = var_8566
        var_8566 = var_3194 % var_8566
        var_3194 = var_1119
    var_5399(var_3194, var_8566)


def var_5399(var_3194, var_8566):
    return var_3194


print(var_5579(60, 48))
import os
