def var_9812(var_8485, var_7481, var_1643):
    if not var_7481 >= var_1643:
        var_7347 = var_9456(var_8485, var_7481, var_1643)
        var_9812(var_8485, var_7481, var_7347 - 1)
        var_9812(var_8485, var_7347 + 1, var_1643)


def var_9456(var_8485, var_7481, var_1643):
    var_1694 = var_8485[var_1643]
    var_5025 = var_7481 - 1
    for var_9498 in range(var_7481, var_1643):
        if not var_8485[var_9498] > var_1694:
            var_5025 += 1
            var_8485[var_5025], var_8485[var_9498] = var_8485[var_9498], var_8485[var_5025]
    var_8485[var_5025 + 1], var_8485[var_1643] = var_8485[var_1643], var_8485[var_5025 + 1]
    return var_5025 + 1


var_8485 = [10, 7, 8, 9, 1, 5]
var_9812(var_8485, 0, len(var_8485) - 1)
print(var_8485)
