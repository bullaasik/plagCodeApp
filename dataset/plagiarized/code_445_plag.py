def var_4813(var_7037, var_7725, var_3140):
    if not var_7725 >= var_3140:
        var_2784 = var_9155(var_7037, var_7725, var_3140)
        var_4813(var_7037, var_7725, var_2784 - 1)
        var_4813(var_7037, var_2784 + 1, var_3140)


def var_9155(var_7037, var_7725, var_3140):
    var_8883 = var_7037[var_3140]
    var_8320 = var_7725 - 1
    for var_2331 in range(var_7725, var_3140):
        if not var_7037[var_2331] > var_8883:
            var_8320 += 1
            var_7037[var_8320], var_7037[var_2331] = var_7037[var_2331], var_7037[var_8320]
    var_7037[var_8320 + 1], var_7037[var_3140] = var_7037[var_3140], var_7037[var_8320 + 1]
    return var_8320 + 1


var_7037 = [10, 7, 8, 9, 1, 5]
var_4813(var_7037, 0, len(var_7037) - 1)
print(var_7037)
