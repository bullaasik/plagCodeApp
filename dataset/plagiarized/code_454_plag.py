def var_4999(var_8063, var_9577, var_8510):
    if not var_9577 >= var_8510:
        var_1665 = var_2253(var_8063, var_9577, var_8510)
        var_4999(var_8063, var_9577, var_1665 - 1)
        var_4999(var_8063, var_1665 + 1, var_8510)


def var_2253(var_8063, var_9577, var_8510):
    var_5500 = var_8063[var_8510]
    var_6658 = var_9577 - 1
    for var_8504 in range(var_9577, var_8510):
        if not var_8063[var_8504] > var_5500:
            var_6658 += 1
            var_8063[var_6658], var_8063[var_8504] = var_8063[var_8504], var_8063[var_6658]
    var_8063[var_6658 + 1], var_8063[var_8510] = var_8063[var_8510], var_8063[var_6658 + 1]
    return var_6658 + 1


var_8063 = [10, 7, 8, 9, 1, 5]
var_4999(var_8063, 0, len(var_8063) - 1)
print(var_8063)
