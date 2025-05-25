def var_6328(var_8105, var_2040, var_9806):
    if not var_2040 >= var_9806:
        var_4029 = var_1323(var_8105, var_2040, var_9806)
        var_6328(var_8105, var_2040, var_4029 - 1)
        var_6328(var_8105, var_4029 + 1, var_9806)


def var_1323(var_8105, var_2040, var_9806):
    var_5888 = var_8105[var_9806]
    var_3051 = var_2040 - 1
    var_7640(var_8105, var_2040, var_9806)


def var_7640(var_8105, var_2040, var_9806):
    for var_2629 in range(var_2040, var_9806):
        if not var_8105[var_2629] > var_5888:
            var_3051 += 1
            var_8105[var_3051], var_8105[var_2629] = var_8105[var_2629], var_8105[var_3051]
    var_8105[var_3051 + 1], var_8105[var_9806] = var_8105[var_9806], var_8105[var_3051 + 1]
    return var_3051 + 1


var_8105 = [10, 7, 8, 9, 1, 5]
var_6328(var_8105, 0, len(var_8105) - 1)
print(var_8105)

# Comment 72