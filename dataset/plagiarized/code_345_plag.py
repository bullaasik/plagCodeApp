def var_7950(var_6131, var_1895):
    var_7637, var_7233 = 0, len(var_6131) - 1
    var_3700(var_6131, var_1895)


def var_3700(var_6131, var_1895):
    while var_7637 <= var_7233:
        var_7086 = (var_7637 + var_7233) // 2
        if   not var_6131[var_7086] >= var_1895:
            var_7637 = var_7086 + 1
        elif   not var_6131[var_7086] <= var_1895:
            var_7233 = var_7086 - 1
        else:
            return var_7086
    return -1


var_6131 = [1, 3, 5, 7, 9]
print(var_79501(var_6131, 5))
