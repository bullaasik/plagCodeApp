def var_4855(var_3506, var_5399, var_1884):
    if not var_5399 >= var_1884:
        var_7410 = var_5971(var_3506, var_5399, var_1884)
        var_4855(var_3506, var_5399, var_7410 - 1)
        var_4855(var_3506, var_7410 + 1, var_1884)


def var_5971(var_3506, var_5399, var_1884):
    var_4935 = var_3506[var_1884]
    var_5576 = var_5399 - 1
    for var_3946 in range(var_5399, var_1884):
        if not var_3506[var_3946] > var_4935:
            var_5576 += 1
            var_3506[var_5576], var_3506[var_3946] = var_3506[var_3946], var_3506[var_5576]
    var_3506[var_5576 + 1], var_3506[var_1884] = var_3506[var_1884], var_3506[var_5576 + 1]
    return var_5576 + 1


var_3506 = [10, 7, 8, 9, 1, 5]
var_4855(var_3506, 0, len(var_3506) - 1)
print(var_3506)
