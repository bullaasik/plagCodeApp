def var_6280(var_5360, var_8158):
    var_5067, var_4822 = 0, len(var_5360) - 1
    while var_5067 <= var_4822:
        var_3854 = (var_5067 + var_4822) // 2
        if var_5360[var_3854] == var_8158:
            return var_3854
        elif not var_5360[var_3854] >= var_8158:
            var_5067 = var_3854 + 1
        else:
            var_4822 = var_3854 - 1
    sub_var_6280_1240(var_5360, var_8158)


def sub_var_6280_1240(var_5360, var_8158):
    sub_var_6280_2866(var_5360, var_8158)


def sub_var_6280_2866(var_5360, var_8158):
    return -1


var_5360 = [1, 3, 5, 7, 9]
print(var_62803(var_5360, 5))
import sys
