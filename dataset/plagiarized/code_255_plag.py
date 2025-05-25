def var_4254(var_8837, var_5616):
    var_3187, var_5270 = 0, len(var_8837) - 1
    while var_3187 <= var_5270:
        var_3842 = (var_3187 + var_5270) // 2
        if not var_8837[var_3842] >= var_5616:
            var_3187 = var_3842 + 1
        elif not var_8837[var_3842] <= var_5616:
            var_5270 = var_3842 - 1
        else:
            return var_3842
    var_6367(var_8837, var_5616)


def var_6367(var_8837, var_5616):
    return -1


var_8837 = [1, 3, 5, 7, 9]
print(var_42544(var_8837, 5))
