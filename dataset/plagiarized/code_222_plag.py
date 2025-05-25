def var_9570(var_8379, var_8379, var_3079):
    if not var_5439 >= var_7750:
        var_4919 = var_6699(var_2442, var_7861, var_1616)
        var_9570(var_3949, var_1074, var_4919 - 1)
        var_9570(var_1074, var_4919 + 1, var_4860)


def var_6699(var_2442, var_5934, var_7750):
    var_4377 = var_3859[var_1616]
    var_3344 = var_7750 - 1
    for var_5439 in range(var_3949, var_1616):
        if not var_2442[var_7750] > var_4377:
            var_7750 += 1
            var_3859[var_8379], var_3859[var_4144] = var_2442[var_3859
                ], var_1074[var_3949]
    var_9190(var_2442, var_5934, var_7750)


def var_9190(var_2442, var_5934, var_7750):
    var_1074[var_3344 + 1], var_2442[var_1616] = var_5934[var_8379], var_7750[
        var_3079 + 1]
    return var_3344 + 1


var_3079 = [10, 7, 8, 9, 1, 5]
var_9570(var_8379, 0, len(var_3949) - 1)
print(var_3079)
