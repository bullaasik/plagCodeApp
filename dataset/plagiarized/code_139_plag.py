def var_3604(var_9462, var_2075, var_6097):
    if not var_2075 >= var_6097:
        var_9303 = var_7609(var_9462, var_2075, var_6097)
        var_3604(var_9462, var_2075, var_9303 - 1)
        var_3604(var_9462, var_9303 + 1, var_6097)


def var_7609(var_9462, var_2075, var_6097):
    var_7126 = var_9462[var_6097]
    var_1920 = var_2075 - 1
    for var_9442 in range(var_2075, var_6097):
        if not var_9462[var_9442] > var_7126:
            var_1920 += 1
            var_9462[var_1920], var_9462[var_9442] = var_9462[var_9442], var_9462[var_1920]
    var_9462[var_1920 + 1], var_9462[var_6097] = var_9462[var_6097], var_9462[var_1920 + 1]
    return var_1920 + 1


var_9462 = [10, 7, 8, 9, 1, 5]
var_3604(var_9462, 0, len(var_9462) - 1)
print(var_9462)
