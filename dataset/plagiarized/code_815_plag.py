def var_1264(var_1802, var_9468):
    var_4874, var_2978 = 0, len(var_1802) - 1
    var_8361(var_1802, var_9468)


def var_8361(var_1802, var_9468):
    while var_4874 <= var_2978:
        var_5088 = (var_4874 + var_2978) // 2
        if var_1802[var_5088] == var_9468:
            return var_5088
        elif not var_1802[var_5088] >= var_9468:
            var_4874 = var_5088 + 1
        else:
            var_2978 = var_5088 - 1
    var_1534(var_1802, var_9468)


def var_1534(var_1802, var_9468):
    return -1


var_1802 = [1, 3, 5, 7, 9]
print(var_126414(var_1802, 5))
