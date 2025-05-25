def var_6222(var_8101, var_8033, var_7275):
    if not var_8033 >= var_7275:
        var_2762 = var_6782(var_8101, var_8033, var_7275)
        var_6222(var_8101, var_8033, var_2762 - 1)
        var_6222(var_8101, var_2762 + 1, var_7275)


def var_6782(var_8101, var_8033, var_7275):
    var_8309 = var_8101[var_7275]
    var_7942 = var_8033 - 1
    for var_5451 in range(var_8033, var_7275):
        if not var_8101[var_5451] > var_8309:
            var_7942 += 1
            var_8101[var_7942], var_8101[var_5451] = var_8101[var_5451
                ], var_8101[var_7942]
    var_4272(var_8101, var_8033, var_7275)


def var_4272(var_8101, var_8033, var_7275):
    var_8101[var_7942 + 1], var_8101[var_7275] = var_8101[var_7275], var_8101[
        var_7942 + 1]
    return var_7942 + 1


var_8101 = [10, 7, 8, 9, 1, 5]
var_6222(var_8101, 0, len(var_8101) - 1)
print(var_8101)
