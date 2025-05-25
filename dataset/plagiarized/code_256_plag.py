def var_7570(var_4248, var_8027):
    var_5289, var_3764 = 0, len(var_4248) - 1
    while var_5289 <= var_3764:
        var_1815 = (var_5289 + var_3764) // 2
        if not var_4248[var_1815] >= var_8027:
            var_5289 = var_1815 + 1
        elif not var_4248[var_1815] <= var_8027:
            var_3764 = var_1815 - 1
        else:
            return var_1815
    sub_var_7570_3445(var_4248, var_8027)


def sub_var_7570_3445(var_4248, var_8027):
    return -1


var_4248 = [1, 3, 5, 7, 9]
print(var_7570(var_4248, 5))
