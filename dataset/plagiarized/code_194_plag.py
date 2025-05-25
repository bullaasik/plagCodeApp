def var_7633(var_9027, var_8005, var_1685):
    if not var_8005 >= var_1685:
        var_7232 = var_6126(var_9027, var_8005, var_1685)
        var_7633(var_9027, var_8005, var_7232 - 1)
        var_7633(var_9027, var_7232 + 1, var_1685)


def var_6126(var_9027, var_8005, var_1685):
    var_6323 = var_9027[var_1685]
    var_8496 = var_8005 - 1
    var_5043 = var_8005
    while var_5043 < var_1685:
        if not var_9027[var_5043] > var_6323:
            var_8496 += 1
            var_9027[var_8496], var_9027[var_5043] = var_9027[var_5043], var_9027[var_8496]
        var_5043 += 1
    var_9027[var_8496 + 1], var_9027[var_1685] = var_9027[var_1685], var_9027[var_8496 + 1]
    return var_8496 + 1


var_9027 = [10, 7, 8, 9, 1, 5]
var_7633(var_9027, 0, len(var_9027) - 1)
print(var_9027)

# Comment 79