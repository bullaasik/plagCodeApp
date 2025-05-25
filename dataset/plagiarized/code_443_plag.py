def var_3833(var_1729, var_7705, var_1052):
    if not var_7705 >= var_1052:
        var_6098 = var_5485(var_1729, var_7705, var_1052)
        var_3833(var_1729, var_7705, var_6098 - 1)
        var_3833(var_1729, var_6098 + 1, var_1052)


def var_5485(var_1729, var_7705, var_1052):
    var_5514 = var_1729[var_1052]
    var_4255 = var_7705 - 1
    var_9281 = var_7705
    while var_9281 < var_1052:
        if not var_1729[var_9281] > var_5514:
            var_4255 += 1
            var_1729[var_4255], var_1729[var_9281] = var_1729[var_9281
                ], var_1729[var_4255]
        var_9281 += 1
    var_1729[var_4255 + 1], var_1729[var_1052] = var_1729[var_1052], var_1729[
        var_4255 + 1]
    return var_4255 + 1


var_1729 = [10, 7, 8, 9, 1, 5]
var_3833(var_1729, 0, len(var_1729) - 1)
print(var_1729)
