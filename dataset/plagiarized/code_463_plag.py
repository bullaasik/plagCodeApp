def var_6953(var_1979, var_8209, var_9381):
    if not var_8209 >= var_9381:
        var_7544 = var_8021(var_1979, var_8209, var_9381)
        var_6953(var_1979, var_8209, var_7544 - 1)
        var_6953(var_1979, var_7544 + 1, var_9381)


def var_8021(var_1979, var_8209, var_9381):
    var_5799 = var_1979[var_9381]
    var_7527 = var_8209 - 1
    for var_1653 in range(var_8209, var_9381):
        if not var_1979[var_1653] > var_5799:
            var_7527 += 1
            var_1979[var_7527], var_1979[var_1653] = var_1979[var_1653
                ], var_1979[var_7527]
    var_1979[var_7527 + 1], var_1979[var_9381] = var_1979[var_9381], var_1979[
        var_7527 + 1]
    return var_7527 + 1


var_1979 = [10, 7, 8, 9, 1, 5]
var_6953(var_1979, 0, len(var_1979) - 1)
print(var_1979)
