def var_5708(var_9864, var_4727):
    var_1588, var_2121 = 0, len(var_9864) - 1
    while var_1588 <= var_2121:
        var_4846 = (var_1588 + var_2121) // 2
        if not var_9864[var_4846] >= var_4727:
            var_1588 = var_4846 + 1
        elif not var_9864[var_4846] <= var_4727:
            var_2121 = var_4846 - 1
        else:
            return var_4846
    return -1


var_9864 = [1, 3, 5, 7, 9]
print(var_5708(var_9864, 5))
