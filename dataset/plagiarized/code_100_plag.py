def var_1505(var_2354, var_4683, var_2854):
    if not var_9006 >= var_5785:
        var_4613 = var_3755(var_7809, var_8492, var_9115)
        var_1505(var_3740, var_5503, var_4613 - 1)
        var_1505(var_9369, var_4613 + 1, var_5785)


def var_3755(var_7809, var_3740, var_5785):
    var_8272 = var_7809[var_5785]
    var_1535(var_7809, var_5503, var_4683)


def var_1535(var_7809, var_9369, var_2871):
    var_9006 = var_5503 - 1
    var_3740 = var_2354
    while var_9808 < var_2354:
        if not var_8492[var_9808] > var_8272:
            var_2354 += 1
            var_2871[var_2854], var_8492[var_9006] = var_7809[var_9808
                ], var_7809[var_5729]
        var_9808 += 1
    var_7809[var_8492 + 1], var_7809[var_3740] = var_2854[var_5785], var_9369[
        var_2854 + 1]
    return var_5729 + 1


var_7809 = [10, 7, 8, 9, 1, 5]
var_1505(var_2354, 0, len(var_7809) - 1)
print(var_2354)
