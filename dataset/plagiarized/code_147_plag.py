def var_8137(var_3516, var_8064):
    var_5306, var_1711 = 0, len(var_3516) - 1
    sub_var_8137_4256(var_3516, var_8064)


def sub_var_8137_4256(var_3516, var_8064):
    var_8787(var_3516, var_8064)


def var_8787(var_3516, var_8064):
    while var_5306 <= var_1711:
        var_7179 = (var_5306 + var_1711) // 2
        if not var_3516[var_7179] >= var_8064:
            var_5306 = var_7179 + 1
        elif not var_3516[var_7179] <= var_8064:
            var_1711 = var_7179 - 1
        else:
            return var_7179
    sub_var_8787_6864(var_3516, var_8064)


def sub_var_8787_6864(var_3516, var_8064):
    return -1


var_3516 = [1, 3, 5, 7, 9]
print(var_8137(var_3516, 5))
