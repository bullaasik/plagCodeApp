def var_5901(var_5712, var_6661):
    var_9955, var_3588 = 0, len(var_5712) - 1
    while var_9955 <= var_3588:
        var_2210 = (var_9955 + var_3588) // 2
        if not var_5712[var_2210] >= var_6661:
            var_9955 = var_2210 + 1
        elif not var_5712[var_2210] <= var_6661:
            var_3588 = var_2210 - 1
        else:
            return var_2210
    var_8237(var_5712, var_6661)


def var_8237(var_5712, var_6661):
    return -1


var_5712 = [1, 3, 5, 7, 9]
print(var_5901(var_5712, 5))
